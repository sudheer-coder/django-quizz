from django.urls import path

from user.views import loginview, signupview, startview

app_name="login"
urlpatterns = [


    path('',loginview,name="login"),
    path('user/',signupview,name="signup"),
    path('start/',startview,name="start"),


]
