"""BePitchAndPutt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from iBePitchAndPutt.views import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', mainpage, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/logout/$', logout, name='logout'),
    
    url(r'^player(\.(?P<extension>(json|xml)))?$$',PlayerList.as_view(),name='Player_list'),
    url(r'^player/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',PlayerDetail.as_view(),name='Player_detail'),
    url(r'^player/create/$',PlayerCreate.as_view(),name='player_create'),
    
    url(r'^rules/',rules, name='rules'),
    
    url(r'^player/(?P<pkr>\d+)/match/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',MatchDetail.as_view(),name="Match_detail"),
    url(r'^player/(?P<pk>\d+)/match/create/$',MatchCreate.as_view(),name='match_create'),
    url(r'^player/(?P<pkr>\d+)/match/(?P<pk>\d+)/edit/$',LoginRequiredCheckIsOwnerUpdateView.as_view(
        model = Match,
        form_class = MatchForm),
        name='match_edit'
        ),
    
    url(r'player/(?P<pkrr>\d+)/match/(?P<pkr>\d+)/throw/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$', ThrowDetail.as_view(), name="Throw_detail"),

    url(r'^player/(?P<pkrr>\d+)/match/(?P<pkr>\d+)/throw/(?P<pk>\d+)/edit/$',LoginRequiredCheckIsOwnerUpdateView.as_view(
        model = Throw,
        form_class = ThrowForm),
        name='throw_edit'
        ),

    url(r'^player/(?P<pkr>\d+)/match/(?P<pk>\d+)/throw/create/$',ThrowCreate.as_view(),name='throw_create'),
    
    url(r'^field(\.(?P<extension>(json|xml)))?$',FieldList.as_view(),name="Field_list"),
    url(r'^field/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',FieldDetail.as_view(),name="Field_detail"),


    #RESTful API
    
    url(r'^api/auth/',include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^api/player/$',
        APIPlayerList.as_view(), name='player-list'),
    url(r'^api/player/(?P<pk>\d+)/$',
        APIPlayerDetail.as_view(), name='player-detail'),

    url(r'^api/field/$',
        APIPlayerList.as_view(), name='field-list'),
    url(r'^api/field/(?P<pk>\d+)/$',
        APIFieldDetail.as_view(), name='field-detail'),

    url(r'^api/match/(?P<pk>\d+)/$',
        APIMatchDetail.as_view(), name='match-detail'),

    url(r'^api/throw/(?P<pk>\d+)/$',
        APIThrowDetail.as_view(), name='throw-detail'),

    
   # url(r'^api/actualWeather/$',
    #    APIActualWeather.as_view(), name='actual_weather'),
    
]


urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])
 
   

    
    
