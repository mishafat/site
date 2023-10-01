from django.shortcuts import render

# Create your views here.
def education_anton(request):
    return render(request, 'anton/education.html')

def programming_anton(request):
    return render(request, 'anton/programming.html')

def hobbies_anton(request):
    return render(request, 'anton/hobbies.html')

def freetime_anton(request):
    return render(request, 'anton/freetime.html')