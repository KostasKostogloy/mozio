from django.conf.urls import url

from service_area import views

urlpatterns = [
    url(r'create', views.create),
    url(r'search', views.search),
    url(r'', views.interactive_map),
]