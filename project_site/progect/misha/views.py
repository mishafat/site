from django.shortcuts import render

# Create your views here.

def education(request):
    return render(request, 'misha/education.html')

def leisure(request):
    return render(request, 'misha/leisure.html')

def hobbies(request):
    return render(request, 'misha/hobbies.html')

def program(request):
    return render(request, 'misha/program.html')