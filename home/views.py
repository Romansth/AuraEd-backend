from django.shortcuts import render
from .models import Achievements, Blogs, Albums, Teams


def home(request):

	context = {
		'achievements' : Achievements.objects.all(),
		'blogs_home' : Blogs.objects.all().order_by('-date_posted')[:3]
	}
	return render(request,'home/index.html',context)



def about_us(request):
	about_context = {
		'teams' : Teams.objects.all(),
	}
	return render(request,'home/about_us.html',about_context)

def blog(request):
	blog_context = {
		'blogs' : Blogs.objects.all().order_by('-date_posted')
	}
	return render(request,'home/blog.html',blog_context)

def contact_us(request):
	return render(request,'home/contact_us.html')

def portfolio(request):
	portfolio_context = {
		'albums' : Albums.objects.all(),
	}
	return render(request,'home/portfolio.html',portfolio_context)


def apply(request):
	return render(request,'home/apply.html')