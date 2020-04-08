from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, response, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from .models import Pizza, Topping, Sub, Pasta, Salad, Platter, Cart, Order
from decimal import Decimal

import os
import stripe

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return render(request, "orders/login.html")

	context = {
		"user": request.user,
		"toppings": Topping.objects.all(),
		"subs": Sub.objects.all(),
		"pastas": Pasta.objects.all(),
		"salads": Salad.objects.all(),
		"platters": Platter.objects.all()
	}

	return render(request, "orders/index.html", context)

def login_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request, username=username, password=password)

	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		messages.error(request, 'Login failed! Incorrect username or password.')
		return render(request, "orders/login.html")

def logout_view(request):
	logout(request)
	return render(request, "orders/logout.html")

def register_view(request):

	if request.method == "POST":
		
		form = RegisterForm(request.POST)
		name = request.POST["username"]
		
		if form.is_valid():
			form.save()
			messages.success(request, 'Registration Success!')
			return HttpResponseRedirect(reverse('index'))

		else:
			try:
				user = User.objects.get(username=name)
			except User.DoesNotExist:
				form = RegisterForm()
				messages.error(request, 'Registration failed! Please try again!')
				return render(request, "orders/register.html", {"form":form})

			form = RegisterForm()
			messages.error(request, 'Too slow! Username is already taken!')
			return render(request, "orders/register.html", {"form":form})

	else:
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('index'))

		else:
			form = RegisterForm()
			return render(request, "orders/register.html", {"form":form})

def add(request):

	category = request.POST["category"]
	main = request.POST["style"]
	user = User.objects.get(pk=request.user.id)

	if category == 'Platter':
		item = Platter.objects.get(style=main)
		size = request.POST["size"]
		if size == 'small':
			price = item.price_small
		else:
			price = item.price_large
		name = f'{size} {main} ({category})'
		new_item = Cart.objects.create(item=name.title(), customer=user, price=price)

	elif category == 'Pasta':
		item = Pasta.objects.get(style=main)
		price = item.price
		name = f'{main} ({category})'
		new_item = Cart.objects.create(item=name.title(), customer=user, price=price)

	elif category == 'Salad':
		item = Salad.objects.get(style=main)
		price = item.price
		name = f'{main} ({category})'
		new_item = Cart.objects.create(item=name.title(), customer=user, price=price)

	elif category == 'Sub':
		item = Sub.objects.get(style=main)
		size = request.POST["size"]
		if size == 'small':
			price = item.price_small
		else:
			price = item.price_large

		topping = request.POST["topping"]

		if topping != 'None':
			price += Decimal(0.50)
			name = f'{main} + {topping} ({category})'
			new_item = Cart.objects.create(item=name.title(), customer=user, price=price)
		else:
			name = f'{main} ({category})'
			new_item = Cart.objects.create(item=name.title(), customer=user, price=price)

	elif category == 'Pizza':
		types = request.POST["type"]
		style = request.POST["style"]
		size = request.POST["size"]

		if types == 'cheese' and size == 'small':
			price = Decimal(12.70)
			name = f'small {style} cheese pizza (pizza)'

		elif types == 'cheese' and size == 'large':
			price = Decimal(17.95)
			name = f'large {style} cheese pizza (pizza)'


		elif types == '1' and size == 'small':
			price = Decimal(13.70)
			topping = request.POST["topping"]
			name = f'small {style} pizza + {topping} (pizza)'

		elif types == '1' and size == 'large':
			price = Decimal(19.95)
			topping = request.POST["topping"]
			name = f'large {style} pizza + {topping} (pizza)'


		elif types == '2' and size == 'small':
			price = Decimal(15.20)
			toppings = request.POST.getlist("topping")
			string = ''
			for topping in toppings[:2]:
				string += f'{topping}, '

			length = len(string)
			string = string[:length-2]

			name = f'small {style} pizza + {string} (pizza)'

		elif types == '2' and size == 'large':
			price = Decimal(21.95)
			toppings = request.POST.getlist("topping")
			string = ''
			for topping in toppings[:2]:
				string += f'{topping}, '

			length = len(string)
			string = string[:length-2]

			name = f'large {style} pizza + {string} (pizza)'


		elif types == '3' and size == 'small':
			price = Decimal(16.20)
			toppings = request.POST.getlist("topping")
			string = ''
			for topping in toppings[:3]:
				string += f'{topping}, '

			length = len(string)
			string = string[:length-2]

			name = f'small {style} pizza + {string} (pizza)'

		elif types == '3' and size == 'large':
			price = Decimal(23.95)
			toppings = request.POST.getlist("topping")
			string = ''
			for topping in toppings[:3]:
				string += f'{topping}, '

			length = len(string)
			string = string[:length-2]

			name = f'large {style} pizza + {string} (pizza)'


		elif types == 'special' and size == 'small':
			price = Decimal(17.75)
			toppings = request.POST.getlist("topping")
			string = ''
			for topping in toppings[:5]:
				string += f'{topping}, '

			length = len(string)
			string = string[:length-2]

			name = f'small {style} pizza + {string} (pizza)'

		elif types == 'special' and size == 'large':
			price = Decimal(25.95)
			toppings = request.POST.getlist("topping")
			string = ''
			for topping in toppings[:5]:
				string += f'{topping}, '

			length = len(string)
			string = string[:length-2]

			name = f'large {style} pizza + {string} (pizza)'

		new_item = Cart.objects.create(item=name.title(), customer=user, price=price)
		main = 'Pizza'

	messages.success(request, f'{main} added to Cart!')
	return HttpResponseRedirect(reverse('order'))

def cart(request):
	items = Cart.objects.filter(customer=request.user)

	total = 0

	if items:
		for item in items:
			total += item.price

	payment = round(total*100)

	context = {
		"items": items,
		"total": total,
		"key": os.environ["STRIPE_PUBLISHABLE_KEY"],
		"payment": payment
	}

	return render(request, "orders/cart.html", context)

def order(request):

	context = {
		"user": request.user,
		"toppings": Topping.objects.all(),
		"subs": Sub.objects.all(),
		"pastas": Pasta.objects.all(),
		"salads": Salad.objects.all(),
		"platters": Platter.objects.all()
	}

	return render(request, "orders/order.html", context)

def purchase(request):
	global order_id
	user = User.objects.get(pk=request.user.id)
	items = Cart.objects.filter(customer=request.user)

	if not items:
		return render(request, "orders/order.html")

	if request.method == 'POST':
		charge = stripe.Charge.create(
			amount=request.POST["payment"], 
			currency='sgd', 
			description="Jereld's Pizza", 
			source=request.POST['stripeToken']
		)

	try:
		maximum = Order.objects.latest('order_id')
		order_id = maximum.order_id + 1
	except Order.DoesNotExist:
		order_id = 1

	for item in items:
		Order.objects.create(order_id=order_id, item=item.item, customer=user, price=item.price, ordered_on=datetime.today())

	items.delete()

	items = Order.objects.filter(order_id=order_id)

	total = 0
	if items:
		for item in items:
			total += item.price

	context = {
		"user": request.user,
		"items": items,
		"total": total,
		"order_id": order_id,
		"ordered_on": datetime.today(),
	}

	return render(request, "orders/purchase.html", context)
