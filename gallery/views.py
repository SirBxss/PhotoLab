from django.shortcuts import render, redirect, get_object_or_404
from .forms import PhotoForm
from .models import Photo

def photo_list(request):
    photos = Photo.objects.order_by("-created")
    return render(request, "gallery/list.html", {"photos": photos})

def upload_photo(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return redirect("photo_detail", pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, "gallery/upload.html", {"form": form})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, "gallery/detail.html", {"photo": photo})
