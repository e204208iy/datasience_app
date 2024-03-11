from django.urls import path
from . import views

#app_nameを指定すると、テンプレートで[% app_name:〇〇 %]とした際、app_nameがこのファイルを指定していると解釈する
app_name = "dswebapp"

urlpatterns = [
  path('', views.index, name='index'),
  path("overview/",views.overview,name="overview"),
  path("compedata/",views.compedata,name="compedata"),
  path("ranking/",views.overview,name="ranking"),
  path("postresult/",views.postResult,name="postresult"),
  path("fileupload/",views.file_upload,name="file_upload")
]