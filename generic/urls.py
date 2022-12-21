from django.urls import path
from .views import CarListAPIView, CarDetailAPIView, CarCreateAPIView, CarUpdateAPIView

urlpatterns = [
    path('car-list/', CarListAPIView.as_view(), name='car_list'),
    path('car-detail/<int:id>/', CarDetailAPIView.as_view(), name='detail_view'),
    path('car-create/', CarCreateAPIView.as_view(), name='car_create'), 
    path('car-update/<int:id>/', CarUpdateAPIView.as_view(), name='car_update'),
]
