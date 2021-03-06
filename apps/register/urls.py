from django.conf.urls import url
from .views import index,register,login,success,userinfocollect,FactorAnalysis,DatesetInfo,AnalysisScore,HowFactorImpact,PredictPage,PredictResult,PredictWealth,SimulatePredictSalary#,t
urlpatterns = [

    url(r'^$', index),
    url(r'^userinfocollect$', userinfocollect),
    url(r'^register$', register),
    url(r'^success$', success),
    url(r'^login$', login),
    url(r'^FactorAnalysis$', FactorAnalysis),
    url(r'^HowFactorImpact$', HowFactorImpact),
    url(r'^DatesetInfo$', DatesetInfo),
    url(r'^AnalysisScore$', AnalysisScore),
    url(r'^PredictPage$', PredictPage),
    url(r'^PredictResult$', PredictResult),
    url(r'^PredictWealth$', PredictWealth),
    url(r'^SimulatePredictSalary$', SimulatePredictSalary)
   #

]

from login_registration import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)