
from django.db import models, forms

# Create your models here.

class Company(models.Model):
    class tagField(models.TextChoices):
        B2C = 'B2B', _('Business to Consumer')
        B2B = 'B2C', _('Business to Business')
    
    name = models.CharField(max_length=120, default="") 
    company_blurb = models.CharField(max_length = 1000, default="")
    email = models.EmailField() 
    password = forms.CharField(widget=forms.PasswordInput) 
    industry = models.ForeignKey(Industry ,on_delete=models.CASCADE)
    investors = models.ManyToManyField(Investor)
    business_model = models.ManyToManyField(BusinessModel)
    city_country = models.ForeignKey(cityCountry, on_delete=models.CASCADE)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    keycodes = models.ManyToManyField(Keycode)
    tag = models.CharField(max_length=120,  choices=tagField, default="")
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    external = models.BooleanField(default=False)
    logo = models.ImageField(upload_to="logos")
    revenue_approximation = models.IntegerField()



class Investor(models.Model):
    #ID = models.charField()
    name = models.CharField(max_length = 100, default = "")
    email = models.EmailField()
    blurb = models.CharField(max_length = 1000, default = "")
    
    password = forms.CharField(widget=forms.PasswordInput)
    keycodes = models.ManyToManyField(Keycode)
    companies = models.ManyToManyField(Company)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to="profilephotos")

class Keycode(models.Model):
    keycode = models.CharField(max_length=120, default="")



# Option 1:  
'''
class SocialMedia(models.TextChoices:
    INSTAGRAM = 'IG', _('Instagram')
    WEBSITE = 'WB', _('Website')
    LINKEDIN = 'LI', _('LinkedIn')
    FACEBOOK = 'FB', _('Facebook')
    TWITTER = 'TW', _('Twitter')
'''    
# Option 2: 
class SocialMedia(models.Model):
    INSTAGRAM = 'IG'
    WEBSITE = 'WB'
    LINKEDIN = 'LI'
    FACEBOOK = 'FB'
    TWITTER = 'TW'
    SOCIAL_MEDIA_CHOICES = [
        (INSTAGRAM, 'Instagram'),
        (WEBSITE, 'Website'),
        (LINKEDIN, 'LinkedIn'),
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
    ]
    socialType = models.CharField(
        max_length=2,
        choices=SOCIAL_MEDIA_CHOICES.choices,
        default="",
    )
    link = models.CharField(max_length = 500, default = "")

class Industry(models.Model):
    industry = models.CharField(max_length = 60, default = "")

class CityCountry(models.Model):
    country = models.CharField(max_length = 60, default = "")
    city = models.CharField(max_length = 170, default = "")

class BusinessModel(models.Model):
    class businessModelID(models.TextChoices):
        THEMANUFACTURER = 'MF', _('The Manufacturer')
        BRICKSANDCLICKS = 'BC', _('Bricks and Clicks')
        ADVERTISING = 'AD', _('Advertising')
        THEMARKETPLACE = 'MP', _('The Marketplace')
        SUBSCRIPTION = 'SC', _('Subscription')
        DIRECTSALES = 'DS', _('Direct Sales')
        ONDEMAND = 'OD', _('On-demand')

    business_model = models.CharField(
        max_length=2,
        choices=businessModelID.choices,
        default=businessModelID.THEMANUFACTURER,
    )

class Timeline(models.Model):
    descriptions = models.ListField()
    date_time = models.DateField() 

