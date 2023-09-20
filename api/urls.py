from django.urls import path
from . import views

urlpatterns = [
    path('rawwooldata/', views.RawWoolDataListCreate.as_view(), name='rawwooldata-listcreate'),
]
