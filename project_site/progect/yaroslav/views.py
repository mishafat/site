from django.shortcuts import render

# Create your views here.

def yaroslav_education(request):
    return render(request, 'yaroslav/educ.html')

def yaroslav_achievement(request):
    return render(request, 'yaroslav/achiev.html')

def yaroslav_hobby(request):
    return render(request, 'yaroslav/hobby.html')

def yaroslav_leisure(request):
    return render(request, 'yaroslav/leisure.html')