from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topping(models.Model):
	topping = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.topping}"

class Pizza(models.Model):
	style = models.CharField(max_length=10)
	size = models.CharField(max_length=5)
	toppings = models.ManyToManyField(Topping)
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return f"{self.size} {self.style} Pizza"

class Sub(models.Model):
	style = models.CharField(max_length=30)
	extras = models.ManyToManyField(Topping, blank=True)
	price_small = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	price_large = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return f"{self.style} Sub"

class Pasta(models.Model):
	style = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return f"{self.style} Pasta"

class Salad(models.Model):
	style = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return f"{self.style}"

class Platter(models.Model):
	style = models.CharField(max_length=30)
	price_small = models.DecimalField(max_digits=6, decimal_places=2)
	price_large = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return f"{self.style} Platter"

class Cart(models.Model):
	item = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	customer = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.item}'

class Order(models.Model):
	order_id = models.IntegerField()
	item = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	customer = models.ForeignKey(User, on_delete=models.CASCADE)
	ordered_on = models.DateField()

	def __str__(self):
		return f'{self.item}'