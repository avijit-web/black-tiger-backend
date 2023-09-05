from django.urls import path
from App import views
from App.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
     path('', views.home, name="home"),
     path('about', views.about, name="about"),
     path('services', views.service, name="services"),
     path('portfolio', views.portfolio, name="portfolio"),
     path('contact', views.contact, name="contact"),
     path('form', views.form, name="form"),
     path('ContactPageForm', views.contactPageForm, name="contactPageForm"),
     path('portfolio1/<int:page_number>/', views.load_portfolio_page, name="portfolio1"),
     path('portfolio2/<int:page_number>/', views.load_portfolio_page2, name="portfolio2"),

]


