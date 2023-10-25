from django.db import models
from django.contrib import admin
class football_player(models.Model):
    p_name=models.CharField(max_length=20)
    p_age=models.IntegerField()
    p_country=models.CharField(max_length=20)
    p_email=models.EmailField()
    P_Salary=models.IntegerField()

class football_playerAdmin(admin.ModelAdmin):
    list_display=('p_age','p_name','P_Salary','p_country','p_email')
