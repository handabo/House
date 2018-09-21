from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

urlpatterns = [
    path('districts/', views.provinces, name='provinces'),
    path('districts/<int:pid>', views.districts, name='districts'),
    path('estates/<int:distid>', views.EstateView.as_view(), name='estates'),
]

router = DefaultRouter()
router.register('housetypes', views.HouseTypeViewSet)

urlpatterns += router.urls