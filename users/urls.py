from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="Home-page"),
    path('result',views.result, name='result'),
    path('result1',views.result1, name='result1'),
    path('result2',views.result2, name='result2'),
    path('result3',views.result3, name='result3'),
    path('result4',views.result4, name='result4')


]