from django.urls import path
from file import views
app_name='file'


urlpatterns = [
	path('upload/', views.choose_object, name='choose'),
	path('inside/', views.container_upload, name="cont_info"),
	path('inside/<container>', views.object_upload, name="object_info"),
]