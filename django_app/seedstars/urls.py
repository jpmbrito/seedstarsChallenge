from django.conf.urls import patterns, url
from seedstars.views import *

urlpatterns = patterns('',
                    url(r'^$', 
                        IndexView.as_view(),
                        name="ss_index"),
                    url(r'^list/', 
                        SeedStarsUser_List.as_view(),
                        name="ss_list"),
                    url(r'^add/', 
                        SeedStarsUser_Create.as_view(),
                        name="ss_add"),
                    )
