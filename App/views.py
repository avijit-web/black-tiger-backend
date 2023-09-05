from __future__ import print_function

from django.shortcuts import render, redirect
from .models import ContactForm, PageMeta, Portfolio,  ContactPageForm, SiteSettings, Banner, PartnerCompanyLogo, BannerVideo
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.template.loader import render_to_string


import clicksend_client
from clicksend_client.rest import ApiException
from clicksend_client import EmailRecipient
from clicksend_client import EmailFrom
from clicksend_client import Attachment

def home(request):
    items_per_page = 6
    portfolio_items = Portfolio.objects.all() 
    
    paginator = Paginator(portfolio_items, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    site_settings = SiteSettings.objects.get()
    banner = Banner.objects.get(page_name='Home')
    partner_logo = PartnerCompanyLogo.objects.all()
    banner_video = BannerVideo.objects.get()
    meta_data = PageMeta.objects.get(page_name='Home')
    print(banner_video)
    context = {
        'meta_data': meta_data,
        'banner': banner,
        'site_settings': site_settings,
        'page_obj' : page_obj,
        'partner_logo': partner_logo,
        'banner_video': banner_video
    }
    return render(request, 'index.html', context)


def load_portfolio_page(request, page_number):
    items_per_page = 6
    portfolio_items = Portfolio.objects.all()
    
    paginator = Paginator(portfolio_items, items_per_page)
    page_obj = paginator.get_page(page_number)
    
    html = render_to_string('portfolio_items_partial.html', {'page_obj': page_obj})
    
    return JsonResponse({'html': html})



def load_portfolio_page2(request, page_number):
    items_per_page = 9
    portfolio_items = Portfolio.objects.all()
    
    paginator = Paginator(portfolio_items, items_per_page)
    page_obj = paginator.get_page(page_number)
    
    html = render_to_string('portfolio_items_partial.html', {'page_obj': page_obj})
    
    return JsonResponse({'html': html})




def about(request):

    site_settings = SiteSettings.objects.get()
    meta_data = PageMeta.objects.get(page_name='About BBTAA Team')
    banner = Banner.objects.get(page_name='About BBTAA Team')
    banner_video = BannerVideo.objects.get()
    context = {
        "meta_data": meta_data,
        "site_settings": site_settings,
        "banner": banner,
        "banner_video": banner_video
    }
    return render(request, 'about.html', context)




def service(request):
    site_settings = SiteSettings.objects.get()
    meta_data = PageMeta.objects.get(page_name='Our Services')
    banner = Banner.objects.get(page_name='Our Services')
    banner_video = BannerVideo.objects.get()
    context = {
        "meta_data" : meta_data,
        "site_settings": site_settings,
        "banner": banner,
        "banner_video": banner_video
    }
    return render(request, 'service.html', context)




def portfolio(request):
    items_per_page = 9
    portfolio_items = Portfolio.objects.all() 
    
    paginator = Paginator(portfolio_items, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    site_settings = SiteSettings.objects.get()
    meta_data = PageMeta.objects.get(page_name='Portfolio')
    banner = Banner.objects.get(page_name='Portfolio')
    banner_video = BannerVideo.objects.get()
    context = {  
        'meta_data': meta_data,
        'page_obj' : page_obj,
        'site_settings' : site_settings,
        'banner': banner,
        'banner_video': banner_video
    } 
    return render(request, 'portfolio.html', context)




def contact(request):
    site_settings = SiteSettings.objects.get()
    meta_data = PageMeta.objects.get(page_name='Contact Us')
    banner = Banner.objects.get(page_name='Contact Us')
    banner_video = BannerVideo.objects.get()
    context={
        "meta_data": meta_data,
        "site_settings": site_settings,
        "banner": banner,
        "banner_video": banner_video
    }
    return render(request, 'contact.html', context)




def form(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    website = request.POST.get('url')
    budget = request.POST.get('budget')
    message = request.POST.get('message')
    enquiry =  ContactForm(name = name, email= email, mobile_no=mobile, website_url =website, projected_monthly_budget= budget, message= message)
    enquiry.save()



    #code to send email--------------------------------------------------------------------------------------
    
    # Configure HTTP basic authorization: BasicAuth
    configuration = clicksend_client.Configuration()
    configuration.username = 'claudius'
    configuration.password = '185BFECF-21A8-57B8-40C4-55A9DE137C14'

    # create an instance of the API class
    api_instance = clicksend_client.TransactionalEmailApi(clicksend_client.ApiClient(configuration))
    email_from=EmailFrom(email_address_id='27230',name='BLACK TIGER ADVERTISING.')


    # email sent to admin.------------------------------------------------------------------------------------
    email_receipient=EmailRecipient(email='sam@black-tiger-advertising.co.uk',name='black tiger admin')
    email_receipient_cc = EmailRecipient(email='office@black-tiger-advertising.co.uk',name='BLACK TIGER')
    email_receipient_bcc = EmailRecipient(email='debayan@semicolonites.com',name='BLACK TIGER')
    
    email_body = f"<table border='1'>"\
                 f"<tr><td>Name</td><td>{name}</td></tr>"\
                 f"<tr><td>Email</td><td>{email}</td></tr>"\
                 f"<tr><td>Mobile</td><td>{mobile}</td></tr>"\
                 f"<tr><td>Website</td><td>{website}</td></tr>"\
                 f"<tr><td>Budget</td><td>{budget}</td></tr>"\
                 f"<tr><td>Message</td><td>{message}</td></tr>"\
                 f"</table>"
    
    # Email | Email model
    email_message = clicksend_client.Email(to=[email_receipient],
                                cc=[email_receipient_cc],
                                bcc=[email_receipient_bcc],
                                _from=email_from,
                                subject="New Contact Request has been submitted",
                                body=email_body,
                                ) 

    try:
        # Send transactional email
        api_response = api_instance.email_send_post(email_message)
        #print(api_response)
    except ApiException as e:
        print("Exception when calling TransactionalEmailApi->email_send_post: %s\n" % e)


    #email sent to user.------------------------------------------------------------------------------------------
    email_receipient_user=EmailRecipient(email=email,name='user')
    email_message_for_user = clicksend_client.Email(to=[email_receipient_user],
                                #cc=[email_receipient],
                                #bcc=[email_receipient_bcc],
                                _from=email_from,
                                subject="Your Contact Request with Black Tiger Advertising has been submitted",
                                body="Thank you for reaching out to us. We will get back to you shortly.",
                                ) 
    try:
        # Send transactional email
        api_response_user = api_instance.email_send_post(email_message_for_user)
        #print(api_response_user)
    except ApiException as e:
        print("Exception when calling TransactionalEmailApi->email_send_post: %s\n" % e)

    return JsonResponse({'message': 'Form submitted successfully55'})   
    





def contactPageForm(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    message = request.POST.get('message')
    enquiry =  ContactPageForm(name = name, email= email, mobile_no=mobile, message= message)
    enquiry.save()


    #code to sent email-------------------------------------------------------------------------------------

    # Configure HTTP basic authorization: BasicAuth
    configuration = clicksend_client.Configuration()
    configuration.username = 'claudius'
    configuration.password = '185BFECF-21A8-57B8-40C4-55A9DE137C14'

    # create an instance of the API class
    api_instance = clicksend_client.TransactionalEmailApi(clicksend_client.ApiClient(configuration))
    email_from=EmailFrom(email_address_id='27230',name='BLACK TIGER ADVERTISING.')


    #email to the admin---------------------------------------------------------------------------------------
    email_receipient=EmailRecipient(email='sam@black-tiger-advertising.co.uk',name='black tiger admin')
    email_receipient_cc = EmailRecipient(email='office@black-tiger-advertising.co.uk',name='BLACK TIGER')
    email_receipient_bcc = EmailRecipient(email='debayan@semicolonites.com',name='BLACK TIGER')
    
    email_body = f"<table border='1'>"\
                 f"<tr><td>Name</td><td>{name}</td></tr>"\
                 f"<tr><td>Email</td><td>{email}</td></tr>"\
                 f"<tr><td>Mobile</td><td>{mobile}</td></tr>"\
                 f"<tr><td>Message</td><td>{message}</td></tr>"\
                 f"</table>"
    
    # Email | Email model
    email_message = clicksend_client.Email(to=[email_receipient],
                                cc=[email_receipient_cc],
                                bcc=[email_receipient_bcc],
                                _from=email_from,
                                subject="New Contact Request has been submitted",
                                body=email_body,
                               ) 

    try:
        # Send transactional email
        api_response = api_instance.email_send_post(email_message)
       # print(api_response)
    except ApiException as e:
        print("Exception when calling TransactionalEmailApi->email_send_post: %s\n" % e)

    

    #email sent to user.--------------------------------------------------------------------------------------
    email_receipient_user=EmailRecipient(email=email,name='user')
    email_message_for_user = clicksend_client.Email(to=[email_receipient_user],
                                #cc=[email_receipient],
                                #bcc=[email_receipient_bcc],
                                _from=email_from,
                                subject="Your Contact Request with Black Tiger Advertising has been submitted",
                                body="Thank you for reaching out to us. We will get back to you shortly.",
                                ) 
    try:
        # Send transactional email
        api_response_user = api_instance.email_send_post(email_message_for_user)
       # print(api_response_user)
    except ApiException as e:
        print("Exception when calling TransactionalEmailApi->email_send_post: %s\n" % e)


    return JsonResponse({'message': 'Form submitted successfully'})