from django.db import models

class Form(models.Model):
	user = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	def __str__(self):	
		return self.user

class Item(models.Model):
	User = models.ManyToManyField(Form)

	Quantity = models.IntegerField(null=True)
	Quantity1 = models.IntegerField(null=True)
	Quantity2 = models.IntegerField(null=True)
	Quantity3 = models.IntegerField(null=True)
	Quantity4 = models.IntegerField(null=True)
	Quantity5 = models.IntegerField(null=True)
	Total = models.IntegerField(null=True)

	def __str__(self):
		return self.Quantity

class Details(models.Model):
	Contact = models.IntegerField(null=True)
	address = models.CharField(max_length=50)
	def __str__(self):	
		return self.Contact

class Bayad(models.Model):
	User = models.ManyToManyField(Form)
	pay = (('gcash1','gcash'),('paymaya2','paymaya'),('diskartech3','diskartech'),('cash4','cashondelivery'))
	Payment = models.CharField(max_length=20, choices=pay, default='none')
	def __str__(self):
		return self.pay

class Bagahe(models.Model):
	User = models.ManyToManyField(Form)

	courrier = (('lalamove1','lalamove'),('jandt2','jandt'),('jrs3','jrs'),('mrspeed4','mrspeed'))
	Payment = models.CharField(max_length=20, choices=courrier, default='none')
	def __str__(self):
		return self.courrier

class Suggestion(models.Model):
	User = models.ManyToManyField(Form)

	Message = models.TextField(max_length=100, null=True)

	def __str__(self):
		return self.Message

class Starling(models.Model):
	User = models.ManyToManyField(Form)

	Star = (('star5','5'),('star4','4'),('star3','3'),('star2','2'),('star1','1'))
	rate = models.CharField(max_length=20, choices=Star, default='none')
	def __str__(self):
		return self.Star


	# RecId = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)
	# text = models.TextField(default="")