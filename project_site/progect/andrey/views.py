from django.shortcuts import render

# Create your views here.
def education_andriy(request):
    return render(request, 'andrey/education.html')

def programming_andriy(request):
    return render(request, 'andrey/programming.html')

def freetime_andriy(request):
    return render(request, 'andrey/freetime.html')

def hobbies_andriy(request):
    return render(request, 'andrey/hobbies.html')