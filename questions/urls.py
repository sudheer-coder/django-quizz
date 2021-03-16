from django.urls import path
from .views import questionview, checkanswer, finishquizz

app_name = "questions"
urlpatterns = [
    path('/(?P<id>[0-9]+)',questionview,name="questions"),
    path('/check/',checkanswer,name="check"),
    path('finish/',finishquizz,name="finishquizz"),


]
