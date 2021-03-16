from django.contrib import admin

# Register your models here.
from questions.models import Test, Results, Time

admin.site.register(Test)
admin.site.register(Results)
admin.site.register(Time)
