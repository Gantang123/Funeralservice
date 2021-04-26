from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import Homepage
from django.urls import resolve
from .models import Item

class MainTest(TestCase):

	def html_Homepage(self):
		found = resolve('/')
		self.assertEqual(found.func, homepage)

		
	def test_index_returns_correct_view(self):
		request = HttpRequest()
		response = Homepage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')

		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'homepage.html')
		self.assertIn('<html>', html)
		self.assertIn('</html>', html)
		self.assertIn('<title>Essential Order Form</title>', html)
		self.assertIn('<body bgcolor= "gray">', html)
		self.assertIn('</body>', html)
		self.assertTemplateUsed(response, 'homepage.html')
		self.assertIn('<h1 style="color:black; font-size:33px;"> <center><u>Essential Order Form</u></center> </h1>', html)
		self.assertIn('<form class ="form" action="" method="post">', html)
		self.assertIn('</form>', html)
		self.assertIn('<input bold type="text" id="name" name="name" placeholder="Enter your name"><br>', html)
		self.assertIn('<div id="Essential">', html)
		self.assertIn('</div>', html)
		self.assertIn('<p id="par"><b>Select your essential here</b></p>', html)
		self.assertIn('<input type ="radio" id="Gloves1" name="Essential" value="Gloves">Gloves<br>', html)
		self.assertIn('<input type ="radio" id="Alcohol2" name="Essential" value="Alcohol">Alcohol<br>', html)
		self.assertIn('<input type ="radio" id="Facemask3" name="Essential" value="Facemask">Facemask<br>', html)
		self.assertIn('<input type ="radio" id="Faceshield4" name="Essential" value="Faceshield">Faceshield<br>', html)
		self.assertIn('<input type ="radio" id="SetofPPE5" name="Essential" value="Set of PPE">Set of PPE<br>', html)
		self.assertIn('<input type ="radio" id="Handsanitizer6" name="Essential" value="Hand sanitizer">Hand sanitizer<br><br>', html)
		self.assertIn('<input bold type="text" id="Quantity" name="Quantity" placeholder= "Quantity"><br>', html)
		self.assertIn('<input bold type="text" id="Address" name="Address" placeholder= "Enter your Address"><br>', html)
		self.assertIn('<p id="pay"><b>Mode of Payment</b></p>', html)
		self.assertIn('<input type ="radio" id="CashonDelivery1" name="Payment" value="Cash on Delivery">Cash on Delivery<br>', html)
		self.assertIn('<input type ="radio" id="OnlinePayment2" name="Payment" value="Online Payment">Online Payment<br>', html)
		self.assertIn('<input type ="radio" id="Meetup3" name="Payment" value="Meet up">Meet up<br><br>', html)
		self.assertIn('<button type="submit" name="done" onclick="myFunction()">Place Order</button>', html)
		self.assertIn('<script>function myFunction() {alert("Your order is being processed.");}</script>', html)
		self.assertIn('<center>', html)
		self.assertIn('</center>', html)
		self.assertIn('<br>', html)
		self.assertIn('</div>', html)
		self.assertTrue(html.strip().endswith('</html>'))
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


class Antique(TestCase):
	def berniemylabs(self):
		Item.objects.create(name='name', Essential='Essential',Quantity='Quantity', 
		Address='Address', Payment='Payment')
		response = self.client.get('/app/views.homepage.html/')
