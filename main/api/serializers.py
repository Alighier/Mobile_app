from rest_framework.serializers import (
    ModelSerializer, 
    SerializerMethodField
    )

from main.models import Companies, Codes

class CodesSerializer(ModelSerializer):
    d_photo= SerializerMethodField()
    class Meta:
        model = Codes
        fields = [
            'name',
            'company',
            'valid_date',
            'expire_date',
            'description',
            'd_photo',
        ]

    def get_d_photo(self, obj):
        try:
            d_photo = obj.d_photo.url
        except:
            d_photo = None
        return d_photo

class CodeCreateSerializer(ModelSerializer):
    class Meta:
        model = Codes
        fields = [
            'id',
            'name',
            'company',
            'valid_date',
            'expire_date',
            'description',
            'd_photo',
            'code',
            'c_photo',
        ]

class CodesDetailSerializer(ModelSerializer):
    d_photo= SerializerMethodField()
    c_photo= SerializerMethodField()
    class Meta:
        model = Codes
        fields = [
            'id',
            'name',
            'company',
            'valid_date',
            'expire_date',
            'description',
            'd_photo',
            'code',
            'c_photo',
        ]

    def get_d_photo(self, obj):
        try:
            d_photo = obj.d_photo.url
        except:
            d_photo = None
        return d_photo

    def get_c_photo(self, obj):
        try:
            c_photo = obj.c_photo.url
        except:
            c_photo = None
        return c_photo

class CompanyCreateSerializer(ModelSerializer):
    class Meta:
        model = Companies
        fields = [
            #'id',
            'name',
            'tag1',
            'tag2',
            'tag3',
            #'codes_amount',
            'logo',
            'photo',
            'latitude',
            'longitude',
            #'creator',
            #'visible',
        ]

class CompanyDetailSerializer(ModelSerializer):
    logo = SerializerMethodField()
    photo = SerializerMethodField()
    class Meta:
        model = Companies
        fields = [
            'id',
            'name',
            'tag1',
            'tag2',
            'tag3',
            'codes_amount',
            'logo',
            'photo',
            'latitude',
            'longitude',
            'creator',
            'visible',
        ]

        lookup_field = 'id'

    def get_logo(self, obj):
        try:
            logo = obj.logo.url
        except:
            logo = None
        return logo

    def get_photo(self, obj):
        try:
            photo = obj.photo.url
        except:
            photo = None
        return photo

class CompaniesSerializer(ModelSerializer):
    logo = SerializerMethodField()
    photo = SerializerMethodField()
    class Meta:
        model = Companies
        fields = [
            'id',
            'name',
            'tag1',
            'tag2',
            'tag3',
            'codes_amount',
            'logo',
            'photo',
            'latitude',
            'longitude',
        ]

    def get_logo(self, obj):
        try:
            logo = obj.logo.url
        except:
            logo = None
        return logo

    def get_photo(self, obj):
        try:
            photo = obj.photo.url
        except:
            photo = None
        return photo


