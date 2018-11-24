from django.urls import path

from .views import AboutPageView, HomePageView, NewsPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('news/', NewsPageView.as_view(), name='news'),
    path('', HomePageView.as_view(), name='home'),
]
