from . import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('list/',views.SchoolListView.as_view(),name='list'),
    path('list/<pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<pk>',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<pk>',views.SchoolDeleteView.as_view(),name='delete')
]
