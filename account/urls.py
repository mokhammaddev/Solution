from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # path('login/', views.login_page, name='login'),
    # path('logout/', views.logout_page, name='logout'),
    path('sign/', views.sign, name='sign'),
]
