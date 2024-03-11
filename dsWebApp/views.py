from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse

import sys
# Create your views here.

def index(request):
  return render(request, 'dsWebApp/overview.html')

def overview(request):
  return render(request,'dsWebApp/overview.html')

def compedata(request):
  return render(request,'dsWebApp/compeData.html')

def ranking(request):
  return render(request,'dsWebApp/ranking.html')

def postResult(request):
  return render(request,'dsWebApp/postResult.html')

# ---------------------------------ファイルアップロードに関する関数------------------------------------------------------

def file_upload(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        print("sucess")
        return HttpResponseRedirect('dsWebApp/')
    else:
        form = UploadFileForm()
    return render(request, 'dsWebApp/postResult.html', {'form': form})
# ---------------------------------ファイルアップロードに関する関数------------------------------------------------------
