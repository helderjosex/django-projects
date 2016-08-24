from django.conf.urls import url
from simplemooc.courses import views as courses_views

urlpatterns = [
    url(r'^$', courses_views.index, name='index'),

]