from django.db import models
#from apps.catalog.models import Author, Gengre, Publishing_house

class Product(models.Model):
	product_name = models.CharField(max_length = 200)
	product_price = models.	(default = 0)
	product_avaliable_count = models.IntegerField( default = 0)
	product_detail = models.TextField(default = "", editable = True)
	def __str__(self):
		return self.product_name
'''class Books(Product):
	author_name= models.ForeignKey(Author, on_delete=models.SET_NULL, null = True)
	gengre = models.ForeignKey(Gengre, on_delete=models.SET_NULL, null = True)
	publishing_house = models.ForeignKey(Publishing_house, on_delete=models.SET_NULL, null = True)
	Publication_date = models.DateTimeField() 
	Number_of_pages = models.IntegerField( default = 0)
	def __str__(self):
		return self.product_name'''


