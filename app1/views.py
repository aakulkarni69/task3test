from django.shortcuts import render
from django.http import HttpResponse
from .models import Info                   #imported our model
from django.contrib import auth            #imported auth to use authenticate login and logout function
from django.contrib.auth.models import User#imported user class

def page1(request):
	if request.method=='POST': 
		uname=request.POST.get('uname')                      #received all the data entered by user on sign in page
		email=request.POST.get('email')
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		pno=request.POST.get('pno')
		pd=request.POST.get('pd')
		cpd=request.POST.get('cpd')

		if pd==cpd:
			try:
				x=User.objects.get(username=uname)           #to check if the user already exists
				return HttpResponse('<h2>User already exists</h2>')
			except User.DoesNotExist:
				user= User.objects.create_user(username=uname,password=pd,email=email,first_name=fname,last_name=lname)    #filled data in db
				user.save()
				info=Info(user=user,pno=pno)                 #added phone number in info model table
				info.save()                                  #saved profile in db
				return render(request,'page2.html')
		else:
			return render(request,'page1.html',{'message':'Passwords do not match'})

	else:
		return render(request,'page1.html')


def login(request):
	if request.method=='POST':
		uname1=request.POST.get('uname')                      #received data from user from login page
		pd1=request.POST.get('pd')
		user=auth.authenticate(username=uname1,password=pd1)  #checked if the data matched with any data in data base
		if user is None:                                      #if no user is found then returned invalid credentials
			return render(request,'page2.html',{'message':'Invalid credentials'}) 
		else:
			auth.login(request,user)                          #if correct data is entered then logged in with login function
			return render(request,'page3.html',{'message':'User ' + request.user.username + ' logged in'})
	else:
		return render(request,'page2.html')

def logout(request):
	auth.logout(request)                                   #user logged out
	return render(request,'page1.html',{'message':'Logged out successfully!'})

