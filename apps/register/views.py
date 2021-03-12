from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User, UserInfo
import pandas as pd
from .Factor import FactorAnalysisFunction
from .PredictMonthlySalary import SalaryPredict
from .PredictWealth import wealthPredict
import numpy as np


def index(request):
    return render(request, 'register/index.html')


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    passwd = request.POST['password'].encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(passwd, salt)

    if (User.objects.filter(email=request.POST['email']).exists()):
        print('user exist')
        return render(request, 'register/index.html',
                      {'RegisterMassage': "User exist, please login or register new account"})

    else:
        print("hashed_password:", hashed_password)
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                                   password=hashed_password, email=request.POST['email'])
        user.save()
        request.session['id'] = user.id
        print('new user')
        return render(request, 'register/index.html', {'RegisterMassage': "Account create successful, please login"})


def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        passwd = request.POST['login_password'].encode()
        print("1111:,", passwd)
        n = len(user.password.encode()) - 1
        print("2222:,", user.password.encode()[2:n])

        if bcrypt.checkpw(passwd, user.password.encode()[2:n]):

            print("login success")
            request.session['id'] = user.id
           # return redirect('/success')

           # return render(request, 'register/success.html')
            return redirect('register/success.html')
        else:
            print("login fail")
           # return redirect('/')
            return render(request, 'register/index.html',
                      {'LoginMassage': "UserID or password wrong"})
           # return render(request, 'register/index.html')


def success(request):
    user = User.objects.get(id=request.session['id'])
    #if (UserInfo.objects.filter(email=user).exists()):
    #    print("user exit email")

    #   print(UserInfo.objects.filter(email=user))
     #   UserInfo.objects.filter(email=user).delete()

    context = {
        "user": user,
        "pleasekeyininformation":"please key in information"
        #  "hidden":"hidden"

    }

    # return render(request, 'name_of_page.html', {'form': form})
    return render(request, 'register/success.html', context)


def userinfocollect(request):
    print("UserInfoCollect")
    # user = User.objects.get(id=request.session['id'])
    user = User.objects.get(id=request.session['id'])

    # clean old data
    if (UserInfo.objects.filter(email=user).exists()):
        print("user exit email")
   #
        print( UserInfo.objects.filter(email=user))
        UserInfo.objects.filter(email=user).delete()


    userInformation = UserInfo.objects.create(email=user,
                                              age=request.POST.get('age'),
                                              education=request.POST.get("education"),
                                              location=request.POST.get("location"),
                                              houseInfo=request.POST.get("houseInfo"),
                                              Maritalstatus=request.POST.get("Maritalstatus"),
                                              Occupation=request.POST.get("Occupation"),
                                              sex=request.POST.get("sex"),
                                              hours_per_week=request.POST.get("hours_per_week"),
                                              native_country=request.POST.get("native_country"),
                                              monthySalary=request.POST['monthySalary'],
                                              OtherMonthlyIncome=request.POST['OtherMonthlyIncome'],
                                              SavingBalance=request.POST['SavingBalance'],
                                              Investment=request.POST['Investment'], Property=request.POST['Property'],
                                              CreditCardLiabilities=request.POST['CreditCardLiabilities'],
                                              HomeMortgage=request.POST['HomeMortgage'],
                                              OtherLoan=request.POST['OtherLoan'], Foodspend=request.POST['Foodspend'],
                                              clothingspend=request.POST['clothingspend'],
                                              shopping=request.POST['shopping'],
                                              accommodation=request.POST['accommodation'],
                                              Transport=request.POST['Transport'],
                                              othersMonthlyspend=request.POST['othersMonthlyspend'])
    userInformation.save()
    request.session['id'] = userInformation.id

    monthly_Income = float(request.POST['monthySalary']) + float(request.POST['OtherMonthlyIncome'])
    monthly_Expense = float(request.POST['Foodspend']) + float(request.POST['clothingspend']) + float(
        request.POST['shopping']) + float(request.POST['accommodation']) + float(
        request.POST['Transport']) + float(request.POST['othersMonthlyspend'])

    monthly_Balance = monthly_Income - monthly_Expense

    Asset = float(request.POST['SavingBalance']) + float(request.POST['Investment']) + float(request.POST['Property'])
    liabilities = float(request.POST['CreditCardLiabilities']) + float(request.POST['HomeMortgage']) + float(
        request.POST['OtherLoan'])

    Networth = Asset - liabilities

    print(float(monthly_Income))
    print(float(monthly_Expense))
    print(float(monthly_Balance))
    print(float(Asset))
    print(float(Networth))

    if (monthly_Balance < 0.4 * monthly_Income):
        Summary1 = "reduce monthly expense,check which part excess budget"
    elif (monthly_Balance >= 0.4 * monthly_Income):
        Summary1 = "Add 30% Monthly balance to saving account or investment, 10% Monthly balance used to cash reserve "
    if (liabilities > 0.5 * Asset):
        Summary2 = "reduce long term liabilities smaller than 50% Asset, short term liabilities smaller than 20% of asset"
    elif (Networth < 0):
        Summary2 = "Assess your ability to service your debts"

    context = {
        "user":user,
        "pleasekeyininformation": "This is your financial report",
        "InfoSaveMassage": "Infomation updated",

        "MonthlyState": "Monthly Statement",
        "MonthlyIncome": "Monthly Income:",
        "Num_monthly_Income": monthly_Income,
        "MonthlyExpense": "MonthlyExpense:",
        "Num_MonthlyExpense": monthly_Expense,
        "MonthlyBalance": "Monthly Balance:",
        "Num_MonthlyBalance": monthly_Balance,

        "Personal_balance_statement": "Personal balance statement",
        "Asset": "Asset:",
        "Num_Asset": Asset,
        "liabilities": "liabilities:",
        "Num_liabilities": liabilities,
        "Networth": "Networth:",
        "Num_Networth": Networth,
        "Suggestion": "Suggestion:",
        "Summary1": Summary1,
        "Summary2": Summary2,
        "GoFactorAnalysis": "Factor effect Financial Statement Analysis"

    }


    return render(request, 'register/success.html', context)


def FactorAnalysis(request):
    #  Dataset_list = {"AdultDateset"}
    context = {
        'hidden2': "hidden",
        'list': "AdultDateset",
        'hiden':"hidden"
    }
    return render(request, 'register/FactorAnalysis.html', context)


def DatesetInfo(request):
    #  Dataset_list = {"AdultDateset"}


    context = {
        'hidden2': "hidden",
        'list': "AdultDateset",
        'datasetinfo11': "Extraction was done by Barry Becker from the 1994 Census database.",
        'datasetinfo12': "Attribute Information:",
        'datasetinfo13': "Listing of attributes: >50K, <=50K.",
        'datasetinfo14': "age: continuous.",
        'datasetinfo15': "workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.",
        'datasetinfo16': "education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.",
        'datasetinfo17': "education-num: continuous.",
        'datasetinfo18': "marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.",
        'datasetinfo19': "occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.",
        'datasetinfo110': "relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.",
        'datasetinfo111': "race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.",
        'datasetinfo112': "sex: Female, Male.",
        'datasetinfo113': "capital-gain: continuous. capital-loss: continuous.",
        'datasetinfo114': "fnlwgt: continuous.",
        'datasetinfo115': "hours-per-week: continuous.",
        'datasetinfo116': "native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands."


    }
    return render(request, 'register/FactorAnalysis.html', context)

def AnalysisScore(request):

    context = {
        'hidden2':"hidden",
        'list': "AdultDateset",
        'datasetinfo11': "Extraction was done by Barry Becker from the 1994 Census database.",
        'datasetinfo12': "Attribute Information:",
        'datasetinfo13': "Listing of attributes: >50K, <=50K.",
        'datasetinfo14': "age: continuous.",
        'datasetinfo15': "workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.",
        'datasetinfo16': "education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.",
        'datasetinfo17': "education-num: continuous.",
        'datasetinfo18': "marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.",
        'datasetinfo19': "occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.",
        'datasetinfo110': "relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.",
        'datasetinfo111': "race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.",
        'datasetinfo112': "sex: Female, Male.",
        'datasetinfo113': "capital-gain: continuous. capital-loss: continuous.",
        'datasetinfo114': "fnlwgt: continuous.",
        'datasetinfo115': "hours-per-week: continuous.",
        'datasetinfo116': "native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.",
        'ScoreList': str(FactorAnalysisFunction.final_result_score),
        'Conclusion1':"From the analysis result we can find the top effact financial status will be\n"+"[capital_gain], [capital_loss],[age], [hours_per_week], [marital_status], [native_country], [education_num]\nExclude non-changeable factor,as we can see: investment, working hours and education are important"

    }

    return render(request, 'register/FactorAnalysis.html', context)

def HowFactorImpact(request):
#"hidden":"hidden",
    context = {

        "Analysisgraph1": "/media/AdultDataset/Age_income.png",
        "Analysisgraph2": "/media/AdultDataset/education_income.png",
        "Analysisgraph3": "/media/AdultDataset/educationNum_income.png",
        "Analysisgraph4": "/media/AdultDataset/marital_income.png",
        "Analysisgraph5": "/media/AdultDataset/occupation_income.png",
        "Analysisgraph6": "/media/AdultDataset/relationship_income.png",
        "Analysisgraph7": "/media/AdultDataset/sex_income.png",
             #  "Analysisgraph8": "/media/AdultDataset/workclass_income.png"
        'list': "AdultDateset",
        'datasetinfo11': "Extraction was done by Barry Becker from the 1994 Census database.",
        'datasetinfo12': "Attribute Information:",
        'datasetinfo13': "Listing of attributes: >50K, <=50K.",
        'datasetinfo14': "age: continuous.",
        'datasetinfo15': "workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.",
        'datasetinfo16': "education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.",
        'datasetinfo17': "education-num: continuous.",
        'datasetinfo18': "marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.",
        'datasetinfo19': "occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.",
        'datasetinfo110': "relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.",
        'datasetinfo111': "race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.",
        'datasetinfo112': "sex: Female, Male.",
        'datasetinfo113': "capital-gain: continuous. capital-loss: continuous.",
        'datasetinfo114': "fnlwgt: continuous.",
        'datasetinfo115': "hours-per-week: continuous.",
        'datasetinfo116': "native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.",
        'ScoreList': str(FactorAnalysisFunction.final_result_score),
        'Conclusion1': "From the analysis result we can find the top effact financial status will be\n" + "[capital_gain], [capital_loss],[age], [hours_per_week], [marital_status], [native_country], [education_num]\nExclude non-changeable factor,as we can see: investment, working hours and education are important"

    }



    return render(request, 'register/FactorAnalysis.html', context)

def PredictPage(request):


 print("id=request.session['id']",request.session['id'])
 user = User.objects.get(id=request.session['id'])

 workclass="Private"
# clean old data
 if (UserInfo.objects.filter(email=user).exists()):
   print("user predict exist")

   UserInfomation=np.array(UserInfo.objects.filter(email=user).values())
   print("UserInfomation",UserInfomation.flatten())
   UserInfolist=UserInfomation[0]

 else:
     print("user predict not exist")


 context = {
    "user": user,
     "age":UserInfolist["age"],
     "location":UserInfolist["location"],
     "education":UserInfolist["education"],
     "Maritalstatus":UserInfolist["Maritalstatus"],
     "Occupation":UserInfolist["Occupation"],
     "sex":UserInfolist["sex"],
     "hours_per_week":UserInfolist["hours_per_week"],
     "native_country":UserInfolist["native_country"],


    #  "hidden":"hidden"

 }



 return render(request, 'register/Predict.html', context)


def PredictResult(request):

    user = User.objects.get(id=request.session['id'])

    workclass = "Private"
    # clean old data
    if (UserInfo.objects.filter(email=user).exists()):
        print("user predict exist")

        UserInfomation = np.array(UserInfo.objects.filter(email=user).values())
        print("UserInfomation", UserInfomation.flatten())
        UserInfolist = UserInfomation[0]
        print(UserInfolist["age"])
        PreparePredictlist = np.array(
            [int(UserInfolist["age"]), UserInfolist["location"], workclass, UserInfolist["education"],
             UserInfolist["Maritalstatus"], UserInfolist["Occupation"], UserInfolist["sex"],
             int(UserInfolist["hours_per_week"]), UserInfolist["native_country"]], dtype=object).reshape(1, -1)
        print(PreparePredictlist)
        predictResult= float(SalaryPredict(PreparePredictlist).Predict())
        print('%.2f' % predictResult)
        # list.predict()


    else:
        print("user predict not exist")

    context = {
        "user": user,
        "age": UserInfolist["age"],
        "location": UserInfolist["location"],
        "education": UserInfolist["education"],
        "Maritalstatus": UserInfolist["Maritalstatus"],
        "Occupation": UserInfolist["Occupation"],
        "sex": UserInfolist["sex"],
        "hours_per_week": UserInfolist["hours_per_week"],
        "native_country": UserInfolist["native_country"],
        "yourpredict":"Base on your personal information, your monthly income will be: ",
        "predict_result":'%.2f' % predictResult

        #  "hidden":"hidden"

    }

    return render(request, 'register/Predict.html', context)

def PredictWealth(request):
    user = User.objects.get(id=request.session['id'])


    workclass = "Private"
    # clean old data
    if (UserInfo.objects.filter(email=user).exists()):
        print("user predict exist")

        UserInfomation = np.array(UserInfo.objects.filter(email=user).values())
        print("UserInfomation", UserInfomation.flatten())
        UserInfolist = UserInfomation[0]
        print(UserInfolist["age"])
        PreparePredictlist = np.array(
            [int(UserInfolist["age"]), UserInfolist["location"], workclass, UserInfolist["education"],
             UserInfolist["Maritalstatus"], UserInfolist["Occupation"], UserInfolist["sex"],
             int(UserInfolist["hours_per_week"]), UserInfolist["native_country"]], dtype=object).reshape(1, -1)
        print(PreparePredictlist)
        predictResult = float(SalaryPredict(PreparePredictlist).Predict())
        print('%.2f' % predictResult)
        # list.predict()


    else:
        print("user predict not exist")

        # clean old data

    Networth_2007 = float(request.POST['Networth_2007'])
    Networth_2008 = float(request.POST['Networth_2008'])
    Networth_2009 = float(request.POST['Networth_2009'])
    Networth_2010 = float(request.POST['Networth_2010'])
    Networth_2011 = float(request.POST['Networth_2011'])
    Networth_2012 = float(request.POST['Networth_2012'])
    Networth_2013 = float(request.POST['Networth_2013'])
    Networth_2014 = float(request.POST['Networth_2014'])
    Networth_2015 = float(request.POST['Networth_2015'])
    Networth_2016 = float(request.POST['Networth_2016'])
    Networth_2017 = float(request.POST['Networth_2017'])
    Networth_2018 = float(request.POST['Networth_2018'])
    Networth_2019 = float(request.POST['Networth_2019'])
    Networth_2020 = float(request.POST['Networth_2019'])

    PreparePredictWealthlist = np.array(
        [Networth_2007, Networth_2008,Networth_2009, Networth_2010, Networth_2011, Networth_2012, Networth_2013, Networth_2014, Networth_2015, Networth_2016, Networth_2017, Networth_2018,Networth_2019], dtype=object).reshape(1, -1)


    predictWealthResult = float(wealthPredict(PreparePredictWealthlist).predict())
    print('wealth predict %.2f' % predictWealthResult)
    print(PreparePredictWealthlist)

    context = {
        "user": user,
        "age": UserInfolist["age"],
        "location": UserInfolist["location"],
        "education": UserInfolist["education"],
        "Maritalstatus": UserInfolist["Maritalstatus"],
        "Occupation": UserInfolist["Occupation"],
        "sex": UserInfolist["sex"],
        "hours_per_week": UserInfolist["hours_per_week"],
        "native_country": UserInfolist["native_country"],
        "yourpredict":"Base on your personal information, your monthly income will be: ",
        "predict_result":'%.2f' % predictResult,
        "yourWealthpredict":"Base on your Past year Networth information, your next year networth will be: ",

        "predictwealth_result": '%.2f' % predictWealthResult


        #  "hidden":"hidden"

    }

    return render(request, 'register/Predict.html', context)