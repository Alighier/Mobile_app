from django.conf.urls import url
from django.contrib import admin

from .views import (
    CompanyCreateAPIView,
    CompanyDetailAPIView,
    CompanyUpdateAPIView,
    CompaniesListAPIView,
    CodesListAPIView,
    CodesDetailListAPIView,
    CodeCreateAPIView,
    CodeUpdateAPIView
    )

urlpatterns = [
    url(r'^companies/$', CompaniesListAPIView.as_view(), name='companies'),
    url(r'^company/create/$', CompanyCreateAPIView.as_view(), name='company create'),
    url(r'^company/(?P<id>\d+)/$', CompanyDetailAPIView.as_view(), name='company detail'),
    url(r'^company/(?P<id>\d+)/edit/$', CompanyUpdateAPIView.as_view(), name='company edit'),
    url(r'^codes/$', CodesListAPIView.as_view(), name='codes'),
    url(r'^codes/detail/$', CodesDetailListAPIView.as_view(), name='codes detail'),
    url(r'^code/create/$', CodeCreateAPIView.as_view(), name='code create'),
    url(r'^code/(?P<id>\d+)/edit/$', CodeUpdateAPIView.as_view(), name='code update'),

]
