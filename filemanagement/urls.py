# mtnpulseapp/urls.py
from django.conf.urls import url
from django.urls import path
from .views import FileCategoryApi,FileCategoryDetailApi,DepartmentApi,DepartmentDetailApi,FilesApi,FileDetailApi

#Add Our API URLS
urlpatterns = [
    path('files/', FilesApi.as_view(),name="Files"),
    path('files/<int:id>/', FileDetailApi.as_view(),name="Files Detail"),
    path('departments/', DepartmentApi.as_view(),name="File Departments"),
    path('departments/<int:id>/', DepartmentDetailApi.as_view(),name="Departents Detail"),
    path('categories/', FileCategoryApi.as_view(),name="Categories"),
    path('categories/<int:id>/', FileCategoryDetailApi.as_view(),name="Categories Detail"),
    
]
