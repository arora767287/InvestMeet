from django.contrib import admin
from .models import User_Profile , Card , Coupon , Transaction, Wallet, Document, Label, LabelValue, Question, DocumentType, DocumentTypeType
# Register your models here.


# ours
class CompanyAdmin(admin.ModelAdmin):
    list_display =  ('id', 'name', 'company_blurb', 'email', 'password', 'industry', 'investors',  'business_model', 'city_country', 'social_media', 'keycodes','tag', 'timeline', 'external', 'logo', 'revenue_approximation')

class InvestorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',  'blurb','password', 'keycodes', 'companies', 'social_media', 'profile_photo')

class SocialMediaSerializer(admin.ModelAdmin):
    list_display = ('id', 'socialType', 'link')

class CityCountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'city')

class BusinessModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'business_model') 

class TimelineAdmin(admin.ModelAdmin):
    list_display = ('id', 'descriptions', 'date_time')

class IndustryAdmin(admin.ModelAdmin):
    list_display = ('id', 'industry')

class KeycodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'keycode')

admin.register.site(Company, CompanyAdmin)
admin.register.site(Investor, InvestorAdmin)
admin.register.site(SocialMedia, SocialMediaAdmin)
admin.register.site(CityCountry, CityCountryAdmin)
admin.register.site(BusinessModel, BusinessModelAdmin)
admin.register.site(Timeline, TimelineAdmin)
admin.register.site(Industry, IndustryAdmin)
