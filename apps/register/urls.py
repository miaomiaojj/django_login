from django.conf.urls import url
from .views import index,register,login,success,userinfocollect,FactorAnalysis,DatesetInfo,AnalysisScore,HowFactorImpact,PredictPage,PredictResult,PredictWealth#,t
urlpatterns = [

    url(r'^$', index),
    url(r'^userinfocollect$', userinfocollect),
    url(r'^financialanalysisystem.herokuapp.com/register$', register),
    url(r'^financialanalysisystem.herokuapp.com/success$', success),
    url(r'^financialanalysisystem.herokuapp.com/login$', login),
    url(r'^FactorAnalysis$', FactorAnalysis),
    url(r'^HowFactorImpact$', HowFactorImpact),
    url(r'^DatesetInfo$', DatesetInfo),
    url(r'^AnalysisScore$', AnalysisScore),
    url(r'^PredictPage$', PredictPage),
    url(r'^PredictResult$', PredictResult),
    url(r'^PredictWealth$', PredictWealth),
   #

]

from login_registration import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)