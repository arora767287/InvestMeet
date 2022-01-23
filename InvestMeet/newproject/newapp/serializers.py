from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

class CompanySerializer(serializer.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'company_blurb', 'email', 'password', 'industry', 'investors',  'business_model', 'city_country', 'social_media', 'keycodes','tag', 'timeline', 'external', 'logo', 'revenue_approximation')
        extra_kwargs = {'password': {'min_length': 8}}
        widgets = {
            'password': PasswordInput(),
        }
    def create(self, validated_data)
        company = Company.objects.create(**validated_data)
        company.save()
        return company

class InvestorSerializer(serializer.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('id', 'name', 'email',  'blurb','password', 'keycodes', 'companies', 'social_media', 'profile_photo')
        extra_kwargs = {'password': {'min_length': 8}}
        widgets = {
            'password': PasswordInput(),
        }
    def create(self, validated_data):
        investor = Investor.objects.create(**validated_data)
        investor.save()
        return investor

class SocialMediaSerializer(serialize.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('id', 'socialType', 'link')
    def create(self, validated_data):
        socialmedia = SocialMedia.objects.create(**validated_data)
        socialmedia.save()
        return investor
        
class CityCountrySerializer(serialize.ModelSerializer):
    class Meta:
        model = CityCountry
        fields = ('id', 'country', 'city')
    def create(self, validated_data):
        cityCountry = CityCountry.objects.create(**validated_data)
        cityCountry.save()
        return cityCountry

class IndustrySerializer(serialize.ModelSerializer):
    class Meta: 
        model = Industry;
        fields = ('id', 'industry')
    def create(self, validated_data):
        industry = Industry.objects.create(**validated_data)
        industry.save()
        return industry

class KeyCodes(serialize.ModelSerializer):
    class Meta: 
        model = Keycode;
        fields = ('id', 'keycode')
    def create(self, validated_data):
        keycode = Keycode.objects.create(**validated_data)
        keycode.save()
        return keycode

    
class BusinessModelSerializer(serialize.ModelSerializer):
    class Meta: 
        model = BusinessModel
        fields = ('id', 'business_model')    
    def create(self, validated_data):
        businessModel = BusinessModel.objects.create(**validated_data)
        businessModel.save()
        return businessModel

class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ('id', 'descriptions', 'date_time')
    def create(self, validated_data):
        timeline = Timeline.objects.create(**validated_data)
        timeline.save()
        return timeline

    