from django.contrib import admin
from django.urls import path
from  .views import home_view, URLRedirector, db_view, login_view,register_view, logout_view, delete_view
app_name = 'url'
urlpatterns = [
    path('', home_view,name='home'),
    path('<url>/',URLRedirector,name='redirector'),
    path('db',db_view, name = 'database'),
    path('login',login_view, name = 'login'),
    path('register',register_view, name='register'),
    path('logout',logout_view, name='logout'),
    path('delete/<id>',delete_view, name ='delete')
]
