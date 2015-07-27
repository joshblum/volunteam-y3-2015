from django.shortcuts import render, HttpResponse, redirect
from django.utils.datastructures import MultiValueDictKeyError
from models import Account
import datetime



# Create your views here.
def home(request):
	return render(request, 'app/home.html', {})

def login(request):
	return render(request, 'app/login.html', {})

def signup(request):
	return render(request, 'app/signup.html', {})

def aboutus(request):
	return render(request, 'app/aboutus.html', {})

def volunteam(request):
	return render(request, 'app/volunteam.html', {})
def signupRequest(request):
	
	try:
		name = request.POST['name']
		password = request.POST['password']
		email = request.POST['emailAddress']
		birthdayDay = request.POST['birthdayDay']
		birthdayMonth = request.POST['birthdayMonth']
		birthdayYear = request.POST['birthdayYear']
		nationality = request.POST['nationality']
	except MultiValueDictKeyError:
		return HttpResponse("Not all of the fields were filled")
	

	if (name == "" or password == "" or email == "" or birthdayDay == "" or birthdayMonth == "" or birthdayYear == "" or nationality == ""):
		return HttpResponse("Some of the fields are empty.")

	if (nationality == "isra"):
		nationality = False
	else:
		nationality = True

	birthday = datetime.datetime(int(birthdayYear), int(birthdayMonth), int(birthdayDay))
	# birthday = datetime.datetime.now()

	account_obj = Account(name = name, emailAddress = email, password = password, isPalestinian = nationality, birthday = birthday)
	account_obj.save()

	return HttpResponse("Banana")
def loginRequest(request):
	try:
		emailAddress = request.POST['emailAddress']
		password = request.POST['password']
	except MultiValueDictKeyError:
		return HttpResponse("Not all of the fields were filled")
	filters = {"emailAddress": emailAddress, "password": password}
	loggedUser = Account.objects.filter(**filters)
	if (len(loggedUser) == 0):
		returnDict = { "Error": "wrong username or password" }
		return render(request, 'app/login.html', returnDict)
	else:
		
		return redirect("/volunteam/")
	


def showUsers(request):
	return render(request, 'app/showUsers.html', {"Accounts": Account.objects.all()})

