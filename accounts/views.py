from django.shortcuts import render

# Create your views here.
def signup(request):
	return render(request, 'accounts/signup.html')

def login(request):
	return render(request, 'accounts/login.html')

def logout(request):
	#TODO - need to route to home page and don't forget to log out
	return render(request, 'accounts/logout.html')