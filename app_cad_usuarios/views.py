from django.shortcuts import render

def home(resquest):
    return render(resquest,'usuarios/home.html')

def usuarios(resquest):
    pass