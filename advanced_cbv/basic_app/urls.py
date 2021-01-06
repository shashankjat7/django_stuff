from . import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('list/',views.SchoolListView.as_view(),name='list'),
    path('list/<pk>/',views.SchoolDetailView.as_view(),name='detail')
]
