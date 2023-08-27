from django.urls import path
from .views import generateLeasePage

urlpatterns = [
    path('', generateLeasePage),
    # path('generateContract/', generateContractPage),
]