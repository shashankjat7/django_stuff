from django.urls import path
from users import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup_view,name='signup_view')
]