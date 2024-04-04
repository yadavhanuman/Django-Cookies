from django.shortcuts import render
from datetime import datetime,timedelta

def setcookie(request):
    a= render(request, 'setcookie.html')
    a.set_cookie('name','Hanuman')
    a.set_cookie('age','25' )
    a.set_cookie('location','Allahabad',max_age=3600)
    a.set_cookie('course','adit',max_age=3600)
    return a

def getcookie(request):
    b= request.COOKIES['name']
    c= request.COOKIES['age']
    d= request.COOKIES['location']
    return render(request,'getcookie.html',{'name':b,'age':c,
    'location':d})

def deletecookie(request):
    c= render(request, 'deletecookie.html')
    c.delete_cookie('age')
    return c