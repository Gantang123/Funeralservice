from django.shortcuts import redirect,render
from .models import Item, Details, Bayad, Bagahe, Suggestion, Starling
from .forms import DeleteName
def homepage(request):

	return render(request,'homepage.html')

def home(request):

	return render(request,'homepage.html')

def Traditional(request):

	return render(request,'third.html')	

def TraditionalInput(request):

	item=Item.objects.create(
		product=request.POST['product'],
		Quantity=request.POST['Quantity'],
		size=request.POST['size']
		)
	return render(request,'sixth.html')

def Payment(request):

	bagahe=Bagahe.objects.create(
		Name=request.POST['Name'],
		Email=request.POST['Email'],
		Address2=request.POST['Address2'],
		zipp=request.POST['zipp'],
		Number2=request.POST['Number2'],
		Sex=request.POST['Sex'],
		payment=request.POST['payment'],
		mode=request.POST['mode'],
		cvv=request.POST['cvv'],
		card=request.POST['card'],
		Month=request.POST['Month'],
		Year=request.POST['Year']
		)


	Gantang = Bagahe.objects.last
	Gantang1 = Item.objects.last

	return render(request, 'eighth.html', {
		'Gantang': Gantang,
		'Gantang1': Gantang1
		}

	)
	

def Cremation(request):


	return render(request,'fourth.html')

def CremationInput(request):

	details=Details.objects.create(
		product=request.POST['product'],
		Quantity=request.POST['Quantity']
		)
	return render(request,'sixth.html')

def Flower(request):


	return render(request,'fifth.html')

def FlowerInput(request):

	details=Details.objects.create(
		product=request.POST['product'],
		Quantity=request.POST['Quantity']
		)
	return render(request,'sixth.html')

def Other(request):

	return render(request,'seventh.html')

def OtherInput(request):

	suggestion=Suggestion.objects.create(
		Gantangproduct=request.POST['Gantangproduct'],
		Product_Category=request.POST['Product_Category'],
		Quantity=request.POST['Quantity'],
		price=request.POST['price']
		)

	return render(request,'sixth.html')


def Details(request):
	

	return render(request,'third.html')


def Suggestion(request):

	

	return render(request,'sixth.html')

def Starling(request):

	return render(request,'seventh.html')

def Bura(request):

	Gantang = Bagahe.objects.last

	return render(request, 'eighth.html', {
		'Gantang': Gantang,
		}

	)

def Deletes(request,id):
	Gantang = Bagahe.objects.get(id=id)
	Gantang.delete()
	return redirect("/isip")