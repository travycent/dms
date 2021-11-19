from django.contrib import admin
from .models import FilesModel,DepartmentModel,FileCategory
#Register all Models
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('cat_name',  'created_on')#Display Data in A List
    search_fields = ('cat_id','cat_name')#Add A search Field
class FilesAdmin(admin.ModelAdmin):
    list_display= ('file_id', 'file_name','file_media_link','slug', 'created_on')#Display Data in A List
    search_fields = ('file_name', 'file_media_link')#Add A search Field
class DepartmentAdmin(admin.ModelAdmin):
    list_display= ('dept_id', 'dept_name', 'created_on')#Display Data in A List
    search_fields = ('dept_id','dept_name')#Add A search Field
#Register Models
admin.site.register(FileCategory,CategoryAdmin)
admin.site.register(FilesModel,FilesAdmin)
admin.site.register(DepartmentModel,DepartmentAdmin)




# Register your models here.
