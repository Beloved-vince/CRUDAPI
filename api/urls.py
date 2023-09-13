from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', CreatePersonView,)

urlpatterns = [
    path('api', CreatePersonView.as_view(), name='create-obj'),
    # path('api', ReadAllView.as_view(), name='obj-view'),
    path('api/<uuid:pk>', UpdatePersonView.as_view(), name='update-obj'),    
]