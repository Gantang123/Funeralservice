from django.shortcuts import redirect,render
from .models import Item, Details, Bayad, Bagahe, Suggestion, Starling

def homepage(request):

	return render(request,'homepage.html')

def Traditional(request):

	return render(request,'third.html')	

def TraditionalInput(request):

	item=Item.objects.create(
		product=request.POST['product'],
		Quantity=request.POST['Quantity']
		)
	return render(request,'sixth.html')

def Details(request):
	
	# Subtotal = ['{{quantity * price}}','{{quantity1 * price1}}','{{quantity2 * price2}}',
	# '{{quantity3 * price3}}','{{quantity4 * price4}}','{{quantity5 * price5}}']
	# GrandTotal = ['{{quantity * price + quantity1 * price1 + quantity2 * price2 + quantity3 * price3 + quantity4 * price4 + quantity5 * price5 - 50}}']

	return render(request,'third.html')

def Bayad(request):

	

	return render(request,'fourth.html')

def Bagahe(request):

	

	return render(request,'fifth.html')

def Suggestion(request):

	

	return render(request,'sixth.html')

def Starling(request):

	return render(request,'seventh.html')