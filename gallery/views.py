from django.shortcuts import render, redirect

from gallery.models import Image
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('image_list')
    
    else:
        form = ImageUploadForm()
    
    return render(request, 'gallery/image_upload.html', {'form': form})

@login_required
def image_list(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'gallery/image_list.html', {'images': images})