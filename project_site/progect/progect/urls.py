"""
URL configuration for progect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import andrey.views as andrey_views
import main.views as main_views
import yaroslav.views as yaroslav_views
import anton.views as anton_views
import misha.views as misha_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main, name= 'main'),

    #Yaroslav
    path('yaroslav/education/', yaroslav_views.yaroslav_education, name= 'yaroslav_education'),
    path('yaroslav/achievement/', yaroslav_views.yaroslav_achievement, name= 'yaroslav_achievement'),
    path('yaroslav/hobby/', yaroslav_views.yaroslav_hobby, name= 'yaroslav_hobby'),
    path('yaroslav/leisure/', yaroslav_views.yaroslav_leisure, name= 'yaroslav_leisure'),
    
    #Anton
    path('anton/education/', anton_views.education_anton, name= 'anton_education'),
    path('anton/programming/', anton_views.programming_anton, name= 'anton_programming'),
    path('anton/hobbies/', anton_views.hobbies_anton, name= 'anton_hobbies'),
    path('anton/freetime/', anton_views.freetime_anton, name='anton_freetime'),
    
    #Andrey
    path('andrey/education/', andrey_views.education_andriy, name= 'andrey_education'),
    path('andrey/programming/', andrey_views.programming_andriy, name= 'andrey_programming'),
    path('andrey/hobbies/', andrey_views.hobbies_andriy, name= 'andrey_hobbies'),
    path('andrey/freetime/', andrey_views.freetime_andriy, name='andrey_freetime'),
    
    #Misha
    path('misha/education/', misha_views.education, name = 'misha_education'),
    path('misha/leisure/', misha_views.leisure, name = 'misha_leisure'),
    path('misha/hobbies/', misha_views.hobbies, name = 'misha_hobbies'),
    path('misha/program/', misha_views.program, name = 'misha_program')
]


