# Ex02 Django ORM Web Application
## Date: 12.10.2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
models.py

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

admin.py

from django.contrib import admin
from .models import football_player,football_playerAdmin
admin.site.register(football_player,football_playerAdmin)
```

## OUTPUT
![Alt text](<Screenshot (1).png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
