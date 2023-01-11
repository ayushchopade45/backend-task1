from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="Home-page"),
    path('result',views.result, name='result'),
    path('result1',views.result1, name='result1')

]