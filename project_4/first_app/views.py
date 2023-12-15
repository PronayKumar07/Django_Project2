from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'name' : 'Pronay', 'age' : '23', 'lst': [10,20,30]}
    return render(request, "home.html", d)