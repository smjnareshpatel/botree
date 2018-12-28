from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import Customer_form,Cleaner_form
from .models import Customer,Cleaner
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login/')
def customer(request,id=None):
	customer = Customer.objects.all()
	# product=User.objects.filter(groups__name='Superuser')
	# st = Student.objects.all()
	# tech = Teacher.objects.all()

	return render(request,'customer.html',{'customer':customer})

@login_required(login_url='/login/')
def login(request):
	if request=='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid() and request.method == "POST":
			username = form.cleaned_data['username']
			# request.session.set_expiry(1)
			return redirect('customer')
			# return redirect('product')
	else:
		form=AuthenticationForm()
	return render(request,'login.html',{'form':form})


@login_required(login_url='/login/')
def customer_update(request,id=None):
	
	instance = get_object_or_404(Customer, id=id)
	customer_form = Customer_form(request.POST or None, request.FILES or None,instance=instance)
	if customer_form.is_valid() and request.method == "POST":
		instance = customer_form.save(commit=False)
		instance.save()
		return redirect('customer')
	# else :
	# 	messages.error(request, "Please enter valid data...")
	return render(request, "customer_update.html",{'customer_form':customer_form}) 



@login_required(login_url='/login/')
def customer_add(request):
	
	customer_form = Customer_form(request.POST or None, request.FILES or None)
	if customer_form.is_valid() and request.method == "POST":
		instance = customer_form.save(commit=False)
		customer_form.save()
		return redirect('customer')
	# else :
	# 	messages.error(request, "Please enter valid data...")
	return render(request, "customer_add.html",{'customer_form':customer_form}) 


@login_required(login_url='/login/')
def customer_delete(request, id=None):
	instance = get_object_or_404(Customer, id=id)
	instance.delete()
	# messages.success(request, "Record deleted successfully...")
	return redirect('customer')


@login_required(login_url='/login/')
def booking(request, id=None):
	customer = Customer.objects.all()
	return render(request,'booking.html',{'customer':customer})

	
@login_required(login_url='/login/')
def booking_update(request,id=None):
	
	instance = get_object_or_404(Customer, id=id)
	customer_form = Customer_form(request.POST or None, request.FILES or None,instance=instance)
	if customer_form.is_valid() and request.method == "POST":
		instance = customer_form.save(commit=False)
		instance.save()
		return redirect('booking')
	# else :
	# 	messages.error(request, "Please enter valid data...")
	return render(request, "booking_update.html",{'customer_form':customer_form}) 

@login_required(login_url='/login/')
def booking_add(request):
	
	customer_form = Customer_form(request.POST or None, request.FILES or None)
	if customer_form.is_valid() and request.method == "POST":
		instance = customer_form.save(commit=False)
		customer_form.save()
		return redirect('booking')
	# else :
	# 	messages.error(request, "Please enter valid data...")
	return render(request, "booking_add.html",{'customer_form':customer_form}) 

@login_required(login_url='/login/')
def booking_delete(request, id=None):
	instance = get_object_or_404(Customer, id=id)
	instance.delete()
	# messages.success(request, "Record deleted successfully...")
	return redirect('booking')



@login_required(login_url='/login/')
def cleaner(request, id=None):
	cleaner = Cleaner.objects.all()
	return render(request,'cleaner.html',{'cleaner':cleaner})

@login_required(login_url='/login/')
def cleaner_add(request):
	
	cleaner_form = Cleaner_form(request.POST or None, request.FILES or None)
	if cleaner_form.is_valid() and request.method == "POST":
		instance = cleaner_form.save(commit=False)
		cleaner_form.save()
		return redirect('cleaner')
	# else :
	# 	messages.error(request, "Please enter valid data...")
	return render(request, "cleaner_add.html",{'cleaner_form':cleaner_form}) 

@login_required(login_url='/login/')
def cleaner_delete(request, id=None):
	instance = get_object_or_404(Cleaner, id=id)
	instance.delete()
	# messages.success(request, "Record deleted successfully...")
	return redirect('cleaner')


@login_required(login_url='/login/')
def cleaner_update(request,id=None):
	
	instance = get_object_or_404(Cleaner, id=id)
	cleaner_form = Cleaner_form(request.POST or None, request.FILES or None,instance=instance)
	if cleaner_form.is_valid() and request.method == "POST":
		instance = cleaner_form.save(commit=False)
		instance.save()
		return redirect('cleaner')
	# else :
	# 	messages.error(request, "Please enter valid data...")
	return render(request, "cleaner_update.html",{'cleaner_form':cleaner_form}) 
