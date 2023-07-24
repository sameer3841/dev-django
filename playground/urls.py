from django.urls import path
from . import views

#URLCol
urlpatterns = [
    path('', views.say_hello),
    path('', views.another_page_view),
    path('say_hello', views.say_hello)
]