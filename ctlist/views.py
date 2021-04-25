from django.shortcuts import render, HttpResponse

from .models import Item

# Create your views here.
def Homepage(request):

	if request.method == 'POST':
		name = request.POST['name']
		Essential = request.POST['Essential']
		Quantity = request.POST['Quantity']
		Address = request.POST['Address']
		Payment = request.POST['Payment']
		
		
		mvg = Item()
		mvg.name =name
		mvg.Essential = Essential
		mvg.Quantity = Quantity
		mvg.Address = Address
		mvg.Payment = Payment
		mvg.save()

	return render(request,'homepage.html')

def Page(request):

	mvg = Item.objects.all().order_by('name')
	return render(request,'ProjectPage.html', {'mvg': mvg})
	