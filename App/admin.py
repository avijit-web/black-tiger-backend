from django.contrib import admin
from App.models import ContactForm, PageMeta, Portfolio, SiteSettings, ContactPageForm, Banner, PartnerCompanyLogo, BannerVideo

class ContactFormAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile_no')

class ContactFormPageAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile_no')

class PageMetaAdmin(admin.ModelAdmin):
    list_display=('id','page_name','meta_description')

class PortfolioAdmin(admin.ModelAdmin):
    list_display=('id','title')

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display=('id','site_name')

class BannerAdmin(admin.ModelAdmin):
    list_display=('id','page_name')


class PartnerCompanyLogoAdmin(admin.ModelAdmin):
    list_display=('id','name','logo')

class BannerVideoAdmin(admin.ModelAdmin):
    list_display=('id','video')


admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(ContactPageForm, ContactFormPageAdmin)
admin.site.register(PageMeta, PageMetaAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(PartnerCompanyLogo, PartnerCompanyLogoAdmin)
admin.site.register(BannerVideo, BannerVideoAdmin)
