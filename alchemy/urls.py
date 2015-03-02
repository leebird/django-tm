from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from alchemy.views import *

urlpatterns = patterns(
    '',
    url(r'^user/(?P<username>.+)$',
        csrf_exempt(UserAPI.as_view()),
        name=UserAPI.view_name),
    
    url(r'^user$',
        csrf_exempt(UserAPI.as_view()),
        name=UserAPI.view_name),

    url(r'^version/(?P<username>.+)/(?P<version>.+)$',
        csrf_exempt(VersionAPI.as_view()),
        name=VersionAPI.view_name),

    url(r'^version$',
        csrf_exempt(VersionAPI.as_view()),
        name=VersionAPI.view_name),

    url(r'^document/(?P<pmid>.+)$',
        csrf_exempt(DocumentAPI.as_view()),
        name=DocumentAPI.view_name),

    url(r'^document$',
        csrf_exempt(DocumentAPI.as_view()),
        name=DocumentAPI.view_name),

    url(r'^annotation$',
        csrf_exempt(AnnotationAPI.as_view()),
        name=AnnotationAPI.view_name),

    url(r'^annotation/(?P<pmid>.+)$',
        csrf_exempt(AnnotationAPI.as_view()),
        name=AnnotationAPI.view_name),
    )
