from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from ctlist.views import Homepage
from django.urls import resolve
from ctlist.models import Item, User
from django.urls import reverse

class MainTest(TestCase):

	def test_displays_all_list(self):
		found = resolve('/')
		self.assertTrue(found.func, Homepage)
		
	def testing(self):
		request = HttpRequest()
		response = Homepage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'homepage.html')
		# self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'homepage.html')
		self.assertIn('<html>', html)
		self.assertIn('<title>Essential Order Form</title>', html)
		self.assertIn('<body bgcolor= "#548784">', html)
		self.assertTemplateUsed(response, 'homepage.html')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertIn('<h1 style="color:#0d2d4f; font-size:40px;"> <center><u><i>Essential Order Form</i></u></center> </h1>', html)
		self.assertIn('</body>', html)
		self.assertIn('<form class ="form" action="" method="post">', html)
		self.assertIn('</form>', html)
		self.assertIn('<input bold type="text" id="name" name="name" placeholder="Enter your name"><br>', html)
		self.assertIn('<div id="Essential">', html)
		self.assertIn('</div>', html)
		self.assertIn('<p id="par" style="font-size:20;"><b>> Select your essential here <</b></p>', html)
		self.assertIn('<input type ="radio" id="Gloves1" name="Essential" value="Gloves">Gloves<br>', html)
		self.assertIn('<input type ="radio" id="Alcohol2" name="Essential" value="Alcohol">Alcohol<br>', html)
		self.assertIn('<input type ="radio" id="Facemask3" name="Essential" value="Facemask">Facemask<br>', html)
		self.assertIn('<input type ="radio" id="Faceshield4" name="Essential" value="Faceshield">Faceshield<br>', html)
		self.assertIn('<input type ="radio" id="SetofPPE5" name="Essential" value="Set of PPE">Set of PPE<br>', html)
		self.assertIn('<input type ="radio" id="Handsanitizer6" name="Essential" value="Hand sanitizer">Hand sanitizer<br><br>', html)
		self.assertIn('<input bold type="text" id="Quantity" name="Quantity" placeholder= "Quantity"><br>', html)
		self.assertIn('<input bold type="text" id="Address" name="Address" placeholder= "Enter your Address"><br>', html)
		self.assertIn('<p id="pay"><b>> Mode of Payment <</b></p>', html)
		self.assertIn('<input type ="radio" id="CashonDelivery1" name="Payment" value="Cash on Delivery">Cash on Delivery<br>', html)
		self.assertIn('<input type ="radio" id="OnlinePayment2" name="Payment" value="Online Payment">Online Payment<br>', html)
		self.assertIn('<input type ="radio" id="Meetup3" name="Payment" value="Meet up">Meet up<br><br>', html)
		self.assertIn('<button style="font-size:15;" type="submit" name="done" onclick="myFunction()"><b>Place Order</b></button>', html)
		self.assertIn('<script>function myFunction() {alert("Your order is being processed.");}</script>', html)
		self.assertIn('<center>', html)
		self.assertIn('</center>', html)
		self.assertIn('<br>', html)
		self.assertIn('</div>', html)
		self.assertIn('</html>', html)
		self.assertTrue(html.strip().endswith('</html>'))

class ORM(TestCase):
	def testing(self):
		Item1 = Item()
		Item1.Choices = 'Mark Gantang'
		Item1.save()
		Item2 = Item()
		Item2.Essential = 'Hand sanitizer'
		Item2.save()
		Item3 = Item()
		Item3.Quantity = '3'
		Item3.save()
		Item4 = Item()
		Item4.Address = 'Dasmarinas City'
		Item4.save()
		Item5 = Item()
		Item5.Payment = 'Meet up'
		Item5.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		self.assertEqual(Item1.Choices, 'Mark Gantang')
		self.assertEqual(Item2.Essential, 'Hand sanitizer')
		self.assertEqual(Item3.Quantity, '3')
		self.assertEqual(Item4.Address, 'Dasmarinas City')
		self.assertEqual(Item5.Payment, 'Meet up')

class ORM2(TestCase):
	def testing(self):
		Item1 = Item()
		Item1.Choices = 'Mark Gantang'
		Item1.save()
		Item2 = Item()
		Item2.Essential = 'Hand sanitizer'
		Item2.save()
		Item3 = Item()
		Item3.Quantity = '3'
		Item3.save()
		Item4 = Item()
		Item4.Address = 'Dasmarinas City'
		Item4.save()
		Item5 = Item()
		Item5.Payment = 'Meet up'
		Item5.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		self.assertEqual(Item1.Choices, 'Mark Gantang')
		self.assertEqual(Item2.Essential, 'Hand sanitizer')
		self.assertEqual(Item3.Quantity, '3')
		self.assertEqual(Item4.Address, 'Dasmarinas City')
		self.assertEqual(Item5.Payment, 'Meet up')


class ORM3(TestCase):
	def testing(self):
		Item.objects.create(name='name', Essential='Essential',Quantity='Quantity', Address='Address', Payment='Payment')
		response = self.client.get('/app/views.homepage.html/')

class ListViewTest(TestCase):

	def test_displays_all_list(self):
		form = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')

	def testing(self):
		response = self.client.get('/ProjectPage/')
		self.assertTemplateUsed(response, 'ProjectPage.html')

	def test_displays_all_list_items(self):
		form = User.objects.create()
		name = Item.objects.create(name='name')
		Essential = Item.objects.create(Essential='Essential')
		Quantity = Item.objects.create(Quantity='Quantity')
		Address = Item.objects.create(Address='Address')
		Payment = Item.objects.create(Payment='Payment')
		response = self.client.get('/')
		self.assertIn('name', response.content.decode())
		self.assertIn('Quantity', response.content.decode())
		self.assertIn('Essential', response.content.decode())
		self.assertIn('Address', response.content.decode())
		self.assertIn('Payment', response.content.decode())
		name = Item.objects.get(name="name")
		Essential = Item.objects.get(Essential="Essential")
		Quantity = Item.objects.get(Quantity="Quantity")
		Address = Item.objects.get(Address="Address")
		Payment = Item.objects.get(Payment="Payment")
		self.assertEqual(Item.objects.count(), 5)

		
class Views(TestCase):
	def setUp(self):
		name = Item.objects.create()
		Essential = Item.objects.create()
		Quantity = Item.objects.create()
		Address = Item.objects.create()
		Payment = Item.objects.create()
		
		Item.objects.create(
			name = 'Mark Gantang',
			Essential = 'Hand Sanitizer',
			Quantity = '3',
			Address = 'Dasmarinas City',
			Payment = 'Meet Up',
			)
		self.client.post('/ProjectPage/', name='Mark Gantang')
		
		#response = 
		self.client.post('/ProjectPage/')

		self.assertEqual(Item.objects.count(), 6)
		#self.assertRedirects(response, '/next/')

	def test_displays_all_list(self):
		name = Item.objects.get(name="Mark Gantang")
		Essential = Item.objects.get(Essential="Hand Sanitizer")
		Quantity = Item.objects.get(Quantity="3")
		Address = Item.objects.get(Address="Dasmarinas City")
		Payment = Item.objects.get(Payment="Meet Up")

		response = self.client.post('/ProjectPage/')



class URL(TestCase):

	def url_ko_ito_hehe(self):
		found = resolve()
		self.assertEqual(found.func, homepage)
		self.assertEqual(found.func, ProjectPage)

		url = reverse('homepage')
		self.assertEqual(resolve(url).func, homepage)

		url = reverse('ProjectPage')
		self.assertEqual(resolve(url).func, ProjectPage)



class Models(TestCase):

	def models(self, 
		form="test1", 
		name="test2", 
		Essential="test3", 
		Quantity="test4", 
		Address="test5", 
		Payment="test6"):
		
		return User.objects.create()
		return Item.objects.create(
			form="form", 
			name="name", 
			Essential="Essential", 
			Quantity="Quantity", 
			Address="Address", 
			Payment="Payment", )

	def test_displays_all_list(self):
		byns = self.models()
		self.assertTrue(isinstance(byns, User))
		self.assertFalse(isinstance(byns, Item))















# class ListViewTest(TestCase):

# 	def html_Homepage(self):
# 		form = User.objects.create()
# 		response = self.client.get('/')
# 		self.assertTemplateUsed(response, 'homepage.html')

# 	def html_Homepage(self):
# 		response = self.client.get('/ProjectPage/')
# 		self.assertTemplateUsed(response, 'ProjectPage.html')

# 	def test_displays_all_list(self):
# 		form = Item.objects.create()
# 		name = Item.objects.create(name='name')
# 		Essential = Item.objects.create(Essential='Essential')
# 		Quantity = Item.objects.create(Quantity='Quantity')
# 		Address = Item.objects.create(Address='Address')
# 		Payment = Item.objects.create(Payment='Payment')
# 		response = self.client.get('/')
# 		self.assertIn('name', response.content.decode())
# 		self.assertIn('Essential', response.content.decode())
# 		self.assertIn('Quantity', response.content.decode())
# 		self.assertIn('Address', response.content.decode())
# 		self.assertIn('Payment', response.content.decode())

# 		name = Item.objects.get(name="name")
# 		Essential = Item.objects.get(Essential="Essential")
# 		Quantity = Item.objects.get(Quantity="Quantity")
# 		Address = Item.objects.get(Address="Address")
# 		Payment = Item.objects.get(Payment="Payment")
# 		self.assertEqual(Item.objects.count(), 6)

		
# class User(TestCase):
# 	def testing(self):
# 		name = Item.objects.create()
# 		Essential = Item.objects.create()
# 		Quantity = Item.objects.create()
# 		Address = Item.objects.create()
# 		Payment = Item.objects.create()
		
# 		Item.objects.create(
# 			name = 'Mark Gantang',
# 			Essential = 'Hand Sanitizer',
# 			Quantity = '3',
# 			Address = 'Dasmarinas City',
# 			Payment = 'Meet up',
# 			)
# 		self.client.post('/ProjectPage/', name='Mark Gantang')
		
# 		#response = 
# 		self.client.post('/ProjectPage/')

# 		self.assertEqual(Item.objects.count(), 6)


# 	def html_Homepage(self):
# 		name = Item.objects.get(name="Mark Gantang")
# 		Essential = Item.objects.get(Essential="Hand Sanitizer")
# 		Quantity = Item.objects.get(Quantity="3")
# 		Address = Item.objects.get(Address="Dasmarinas City")
# 		Payment = Item.objects.get(Payment="Meet Up")

# 		response = self.client.post('/ProjectPage/')



# class Homepage(TestCase):

# 	def html_Homepage(self):
# 		found = resolve()
# 		self.assertEqual(found.func, homepage)
# 		self.assertEqual(found.func, ProjectPage)

# 		url = reverse('homepage')
# 		self.assertEqual(resolve(url).func, homepage)

# 		url = reverse('ProjectPage')
# 		self.assertEqual(resolve(url).func, ProjectPage)



# class Models(TestCase):

# 	def models(self, 
# 		form="test1", 
# 		name="test2", 
# 		Essential="test3", 
# 		Quantity="test4", 
# 		Address="test5", 
# 		Payment="test6"):
		
# 		return Item.objects.create()
# 		return User.objects.create(
# 			form="form", 
# 			name="name", 
# 			Essential="Essential", 
# 			Quantity="Quantity", 
# 			Address="Address", 
# 			Payment="Payment", )

# 	def testing(self):
# 		a = self.models()
# 		self.assertTrue(isinstance(a, Item))
# 		self.assertFalse(isinstance(a, User))