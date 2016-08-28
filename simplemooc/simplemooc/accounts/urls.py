from django.conf.urls import url
from django.contrib.auth.views import login, logout
from simplemooc.accounts import views as accounts_views


urlpatterns = [
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', accounts_views.register, name='register'),

]