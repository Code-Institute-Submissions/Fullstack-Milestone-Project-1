from django.conf.urls import url, include
from .views import all_artifacts

urlpatterns = [
    url(r'^$', all_artifacts, name='artifacts'),

]