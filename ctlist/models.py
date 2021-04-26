from django.db import models

class Item(models.Model):
	name = models.CharField(max_length=30, null=True)
	Choices=(('Gloves1','Gloves'),('Alcohol2','Alcohol'),('Facemask3','Facemask'),('Faceshield4','Faceshield'),('SetofPPE5','Set of PPE'),('HandSanitizer6','Hand Sanitizer'))	
	Essential = models.CharField(max_length=20, choices=Choices, default='none')
	Quantity = models.CharField(max_length=20, null=True)
	Address = models.CharField(max_length=100, null=True)
	Pay=(('CashonDelivery1','Cash on Delivery'),('OnlinePayment2','Online Payment'),('Meetup3','Meet up'))
	Payment = models.CharField(max_length=20, choices=Pay, default='none')
	def __str__(self):
		return self.name