from django.urls import path
from . import views

#URLCol
urlpatterns = [
    path('hello/', views.say_hello),
    path('main/', views.another_page_view),
]