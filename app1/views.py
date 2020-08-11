from django.shortcuts import render
from django.http import HttpResponse
from .models import info
from django.contrib.auth import authenticate

def page1(request):
	if request.method=='POST':
		uname=request.POST.get('uname')
		email=request.POST.get('email')
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		pno=request.POST.get('pno')
		pd=request.POST.get('pd')
		cpd=request.POST.get('cpd')
		profile = info(uname=uname,email=email,fname=fname,lname=lname,pno=pno,pd=pd)
		profile.save()
		x=info.objects.filter(uname=uname)
		print(x)

		if pd==cpd:
			if x IS None:
				return render(request,'page2.html')
			else:
				return render(request,'page1.html',{'message':'User already exhists. Try again!'})
		else:
			return render(request,'page1.html',{'message':'Passwords do not match'})

	else:
		return render(request,'page1.html')
def page2(request):
	if request.method=='POST':
		uname1=request.POST.get('uname')
		pd1=request.POST.get('pd')
		x=auth.authenticate(uname=uname,pd=pd)
		if x is None:
			return render(request,'page2.html',{'message':'Invalid credentials'})
		else:
			return render(request,'page3.html')