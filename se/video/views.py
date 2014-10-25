from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext 
from video.form import UploadFileForm
from video.models import VideoModel

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            video = VideoModel()
            video.file = request.FILES['file']
            video.description = form.cleaned_data["description"]
            video.save()
            return HttpResponseRedirect('success/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form},context_instance=RequestContext(request))



# Create your views here.

def uploadSuccess(request):
    return render_to_response('upload_Success.html',context_instance=RequestContext(request))

