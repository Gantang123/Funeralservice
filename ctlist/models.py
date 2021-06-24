from django.db import models
 
class Item(models.Model):
	PRODUCT_CHOICES = (
    ('Wooden Casket', 'Item1'),
    ('Metal Casket', 'Item2'),
    ('Imported Casket ', 'Item3')
	)
	product = models.CharField(max_length=100, choices=PRODUCT_CHOICES, default='Item1')
	Quantity = models.IntegerField()
	SIZE_CHOICES = (
    ('size1', 'Length: 78 inches Width: 23 inches'),
    ('size2', 'Length: 75 inches Width: 22 inches'),
    ('size3', 'Length: 83 inches Width: 28 inches'),
    ('size4', 'Length: 85 inches Width: 38 inches'),
    ('size5', 'Length: 60 inches Width: 11 inches')
	)
	size = models.CharField(max_length=100, choices=SIZE_CHOICES, default='size1')
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
	zipp = models.CharField(max_length=50)
	Number2 = models.CharField(max_length=50)
	Sex = models.CharField(max_length=50)
	Bayad = (
    ('Annual', 'Annual'),
    ('Semi-Annual', 'Semi-Annual'),
    ('Quarterly', 'Quarterly'),
    ('Monthly', 'Monthly')
    	)
	payment = models.CharField(max_length=50, choices=Bayad, default='pay1')    	
	atms = (
    ('Savings accounts', 'Savings accounts'),
    ('Checking accounts', 'Checking accounts'),
    ('Salary account', 'Salary account'),
    ('Walk-in', 'Walk in')
   		)
	atm = models.CharField(max_length=50, choices=atms, default='card1')
	mode = models.CharField(max_length=50, default='none')
	cvv = models.CharField(max_length=50)
	card = models.CharField(max_length=50, null=True)
	months = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December')
    )
	Month = models.CharField(max_length=50, choices=months, default='month1')
	years = (
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025')
    )
	Year = models.CharField(max_length=50, choices=years, default='year1')
	def __str__(self):
		return self.Name

class Suggestion(models.Model):
	Gantangproduct = models.CharField(max_length=50, default='none')
	Product_Category = models.CharField(max_length=50, default='none')
	Quantity = models.CharField(max_length=50, default='none')
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