from django.db import models
 
class Item(models.Model):
	PRODUCT_CHOICES = (
    ('Item1', 'Wooden Casket'),
    ('Item2', 'Metal Casket'),
    ('Item3', 'Imported Casket')
	)
	product = models.CharField(max_length=15, choices=PRODUCT_CHOICES, default='Item1')
	Quantity = models.IntegerField()
	SIZE_CHOICES = (
    ('size1', 'Length: 78 inches Width: 23 inches'),
    ('size2', 'Length: 75 inches Width: 22 inches'),
    ('size3', 'Length: 83 inches Width: 28 inches'),
    ('size4', 'Length: 85 inches Width: 38 inches'),
    ('size5', 'Length: 60 inches Width: 11 inches')
	)
	size = models.CharField(max_length=15, choices=SIZE_CHOICES, default='size1')
	def __str__(self):
		return self.product

class Details(models.Model):
	Quantity = models.CharField(max_length=50)
	Price = models.CharField(max_length=50)
	Total	= models.CharField(max_length=50)
	Product = (
    ('Urns1', 'Individual Cremation Urns'),
    ('Urns2', 'Companion Cremation Urns'),
    ('Urns3', 'Keepsake Cremation Urns'),
    ('Urns4', '3D Artisan Portrait Cremation Urns'),
    ('Urns5', 'Child and Infant Cremation Urns'),
    ('Urns6', 'Pet Cremation Urns')
	)
	urns = models.CharField(max_length=15, choices=Product, default='Urns1')
	Size = (
    ('Size1', 'Regular size'),
    ('Size2', '15 cubic inches'),
    ('Size3', '100 cubic inches'),
    ('Size4', '200 cubic inches'),
    ('Size5', '220 cubic inches'),
    ('Size6', '250 cubic inches'),
    ('Size7', '300 cubic inches')
	)
	inches = models.CharField(max_length=15, choices=Size, default='Size1')

	def __str__(self):
		return self.Quantity

class Bayad(models.Model):
	Flower = (
    ('flow1', 'All white Standing sympathy'),
    ('flow2', 'Always remember (WHITE STANDING)'),
    ('flow3', 'Angelic All White Wreath'),
    ('flow4', 'Care and Compassion Spray'),
    ('flow5', 'Classic all Whites Standing Spray'),
    ('flow6', 'From your loving family'),
    ('flow7', 'Funeral White Basket')
	)
	bulaklak = models.CharField(max_length=15, choices=Flower, default='flow1')
	Sukat = (
    ('sukat1', 'Regular'),
    ('sukat2', '10 inches'),
    ('sukat3', '15 inches'),
    ('sukat4', '20 inches'),
    ('sukat5', '25 inches'),
    ('sukat6', '30 inches')
	)
	inch = models.CharField(max_length=15, choices=Sukat, default='flow1')
	def __str__(self):
		return self.Flower

class Bagahe(models.Model):
	Name = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)
	Address2 = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=50)
	Number2 = models.CharField(max_length=50)
	CHOICESS = (('male','male1'),('female','female1'))
	select = models.CharField(choices=CHOICESS,max_length=50, default="none")
	Bayad = (
    ('pay1', 'Annual'),
    ('pay2', 'Semi-Annual'),
    ('pay3', 'Quarterly'),
    ('pay4', 'Monthly')
    	)
	payment = models.CharField(max_length=50, choices=Bayad, default='pay1')    	
	card = (
    ('card1', 'atm1'),
    ('card2', 'atm2'),
    ('card3', 'atm3'),
    ('card4', 'atm4')
   		)
	atm = models.CharField(max_length=15, choices=card, default='card1')
	CVV = models.CharField(max_length=50)
	CARD_NUMBER = models.CharField(max_length=50)
	month = (
    ('month1', 'January'),
    ('month2', 'February'),
    ('month3', 'March'),
    ('month4', 'April'),
    ('month5', 'May'),
    ('month6', 'June'),
    ('month7', 'July'),
    ('month8', 'August'),
    ('month9', 'September'),
    ('month10', 'October'),
    ('month11', 'November'),
    ('month12', 'December')
    )
	buwan = models.CharField(max_length=15, choices=month, default='month1')
	year = (
    ('year1', '2021'),
    ('year2', '2022'),
    ('year3', '2023'),
    ('year4', '2024'),
    ('year5', '2025')
    )
	taon = models.CharField(max_length=15, choices=year, default='year1')
	def __str__(self):
		return self.Name

class Suggestion(models.Model):
	Gantangproduct = models.CharField(max_length=50, default='none')
	Product_Category = models.CharField(max_length=50, default='none')
	quantity = models.CharField(max_length=50, default='none')
	price = models.CharField(max_length=50, default='none')
	def __str__(self):
		return self.Gantangproduct

class Starling(models.Model):

	Star = (('star5','5'),('star4','4'),('star3','3'),('star2','2'),('star1','1'))
	rate = models.CharField(max_length=20, choices=Star, default='none')
	def __str__(self):
		return self.Star


	# RecId = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)
	# text = models.TextField(default="")