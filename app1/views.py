from django.shortcuts import render
from django.http import HttpResponse
from .models import info
from django.contrib import auth
from django.contrib.auth.models import User

def page1(request):
	if request.method=='POST':
		uname=request.POST.get('uname')
		email=request.POST.get('email')
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		pno=request.POST.get('pno')
		pd=request.POST.get('pd')
		cpd=request.POST.get('cpd')

		if pd==cpd:
			try:
				x=User.objects.get(username=uname)
				return HttpResponse('<h2>User already exists</h2>')
			except User.DoesNotExist:
				user= User.objects.create_user(username=uname,password=pd,email=email,first_name=fname,last_name=lname)
				user.save()
				info=info(user=user,pno=pno)
				info.save()
				return render(request,'page2.html')
		else:
			return render(request,'page1.html',{'message':'Passwords do not match'})

	else:
		return render(request,'page1.html')


def login(request):
	if request.method=='POST':
		uname1=request.POST.get('uname')
		pd1=request.POST.get('pd')
		user=auth.authenticate(username=uname1,password=pd1)
		if user is None:
			return render(request,'page2.html',{'message':'Invalid credentials'})
		else:
			q=auth.login(request,user)
			return render(request,'page3.html',{'message':'User logged in'})
	else:
		return render(request,'page2.html')

def logout(request):
	if request.method=='POST':
		auth.logout(request)
		return render(request,'page1.html',{'message':'Logged out successfully!'})

