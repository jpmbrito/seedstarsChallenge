from django.conf.urls import patterns, url
from seedstars import views

urlpatterns = patterns(
                    url(r'^$', 
                        views.index,
                        name="ss_index"),
                    url(r'^list/', 
                        SeedStarsUser_List.as_view(),
                        name="ss_list"),
                    url(r'^add/', 
                        SeedStarsUser_Create.as_view(),
                        name="ss_add"),
                    )
