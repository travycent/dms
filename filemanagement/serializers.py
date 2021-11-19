# serializers.py --This file will serialize all the data of this app
from rest_framework import serializers #import the serializer
from .models import FileCategory,DepartmentModel,FilesModel #Import all the models in the APP
#FileCategorySerializers for Create, Get,Delete
class FileCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FileCategory
        fields = ('cat_id', 'cat_name','created_on')
        cat_name = serializers.CharField(max_length=100)
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance
#FileCategorySerializers Serializers for Update and get detail
class UpdateFileCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FileCategory
        fields = ('cat_id', 'cat_name','created_on')
        cat_name = serializers.CharField(max_length=100)
#FileCategorySerializers for Create, Get,Delete
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields = ('dept_id', 'dept_name','created_on')
        dept_name = serializers.CharField(max_length=100)
    def create(self, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance
#FileCategorySerializers Serializers for Update and get detail
class UpdateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields = ('dept_id', 'dept_name','created_on')
        cat_name = serializers.CharField(max_length=100)
#Archives Serializers for Create, Get,Delete
class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesModel
        fields = ('file_id', 'cat_id','dept_id','file_name','file_media_link','created_on')
        cat_id=serializers.IntegerField()
        dept_id=serializers.IntegerField()
        file_name = serializers.CharField(max_length=100)
        file_media_link=serializers.FileField()
    def create(self,instance, validated_data):
        instance=self.Meta.model(**validated_data)
        instance.save()
        return instance
#FilesModel Serializers for Create, Get,Delete
class UpdateFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesModel
        fields = ('file_id', 'cat_id','dept_id','file_name','file_media_link','created_on')
        cat_id=serializers.IntegerField()
        dept_id=serializers.IntegerField()
        file_name = serializers.CharField(max_length=100)
        file_media_link=serializers.FileField()