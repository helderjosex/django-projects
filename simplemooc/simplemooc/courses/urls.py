from django.conf.urls import url
from simplemooc.courses import views as courses_views

urlpatterns = [
    url(r'^$', courses_views.index, name='index'),
    #url(r'^(?P<pk>\d+)/$', courses_views.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', courses_views.details, name='details'),

]