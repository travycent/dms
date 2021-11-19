from django.shortcuts import render

from rest_framework import viewsets
from .serializers import FileCategorySerializer,UpdateFileCategorySerializer,DepartmentSerializer,UpdateDepartmentSerializer,FilesSerializer,UpdateFilesSerializer
from .models import FileCategory,DepartmentModel,FilesModel #Import all the models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

#Get all the Data of the FileCategorySerializer
class FileCategoryViewSet(viewsets.ModelViewSet):
    queryset = FileCategory.objects.all().order_by('created_on')
    serializer_class = FileCategorySerializer

#Class to Manage FileCategories
class FileCategoryApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        item=FileCategorySerializer(data=request.data)
        if item.is_valid():
            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'message': 'File Category Created successfully',
                }
                return Response(response,status=status_code)
        return Response(item.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = FileCategory.objects.all().order_by('created_on')
        serializer_class = FileCategorySerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific FileCategory
class FileCategoryDetailApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = FileCategory.objects.filter(cat_id=id)
            serializer_class = UpdateFileCategorySerializer(queryset, many=True)
            
            status_code = status.HTTP_200_OK
            response = {
                'success' : 'True',
                'status code' : status_code,
                'data': serializer_class.data,
            }
            return Response(response,status=status_code)
        except queryset.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                    'success' : 'False',
                    'status code' : status_code,
                    'Message': "Data Not Found",
                    
            }
            return Response(response,status=status_code)
    #Update the Data
    def put(self,request,id):
        queryset = FileCategory.objects.filter(cat_id=id).first()
        serializer_class = UpdateFileCategorySerializer(queryset, data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            update=serializer_class.save()
            if update:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'Message': "Data Updated",
                    'data': serializer_class.data,
                }
            return Response(response,status=status_code)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
#Get all the Data of the FileCategorySerializer
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = DepartmentModel.objects.all().order_by('created_on')
    serializer_class = DepartmentSerializer

#Class to Manage FileCategories
class DepartmentApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        item=DepartmentSerializer(data=request.data)
        if item.is_valid():
            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'message': 'File Department Created successfully',
                }
                return Response(response,status=status_code)
        return Response(item.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = DepartmentModel.objects.all().order_by('created_on')
        serializer_class = DepartmentSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific FileCategory
class DepartmentDetailApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = DepartmentModel.objects.filter(dept_id=id)
            serializer_class = UpdateDepartmentSerializer(queryset, many=True)
            
            status_code = status.HTTP_200_OK
            response = {
                'success' : 'True',
                'status code' : status_code,
                'data': serializer_class.data,
            }
            return Response(response,status=status_code)
        except queryset.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                    'success' : 'False',
                    'status code' : status_code,
                    'Message': "Data Not Found",
                    
            }
            return Response(response,status=status_code)
    #Update the Data
    def put(self,request,id):
        queryset = DepartmentModel.objects.filter(dept_id=id).first()
        serializer_class = UpdateDepartmentSerializer(queryset, data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            update=serializer_class.save()
            if update:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'Message': "Data Updated",
                    'data': serializer_class.data,
                }
            return Response(response,status=status_code)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
#Class to Manage Files
class FilesApi(APIView):
    # permission_classes = (IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        item=FilesSerializer(data=request.data)
        if item.is_valid():
            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'message': 'Item Created successfully',
                }
                return Response(response,status=status_code)
        return Response(item.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        queryset = FilesModel.objects.all().order_by('created_on')
        serializer_class = FilesSerializer(queryset, many=True)
        
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)
#Class List Specific File
class FileDetailApi(APIView):
    # #permission_classes = (IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication
    def get(self,request,id):
        try:
            queryset = FilesModel.objects.filter(file_id=id)
            serializer_class = UpdateFilesSerializer(queryset, many=True)
            
            status_code = status.HTTP_200_OK
            response = {
                'success' : 'True',
                'status code' : status_code,
                'data': serializer_class.data,
            }
            return Response(response,status=status_code)
        except queryset.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                    'success' : 'False',
                    'status code' : status_code,
                    'Message': "Data Not Found",
                    
            }
            return Response(response,status=status_code)
    #Update the Data
    def put(self,request,id):
        queryset = FilesModel.objects.filter(archive_id=id).first()
        serializer_class = UpdateFilesSerializer(queryset, data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            update=serializer_class.save()
            if update:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'Message': "Data Updated",
                    'data': serializer_class.data,
                }
            return Response(response,status=status_code)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)