from django.conf.urls import url
from myapp.views import HomeView
from .views import AboutView
from .views import PeopleView


urlpatterns = [

    url(r'^home', HomeView.as_view(), name = 'home'),
    url(r'^about', AboutView.as_view(), name = 'about'),
    url(r'people', PeopleView.as_view(), name = 'people'),
]
