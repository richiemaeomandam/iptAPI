from django.urls import path
from .views import LabCreateAPIView, LabRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('Lab/', LabCreateAPIView.as_view(), name='list-create-lab'),
    path('Lab/<int:pk/'LabRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-lab')
]