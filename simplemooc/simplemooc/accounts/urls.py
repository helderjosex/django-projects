from django.conf.urls import url
from django.contrib.auth.views import login, logout
from simplemooc.accounts import views as accounts_views


urlpatterns = [
    url(r'^$', accounts_views.dashboard, name='dashboard'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', accounts_views.register, name='register'),
    url(r'^editar/$', accounts_views.edit, name='edit'),
    url(r'^editar-senha/$', accounts_views.edit_password, name='edit_password'),

]