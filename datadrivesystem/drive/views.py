from django.shortcuts import render, redirect, get_object_or_404
from .models import Folder
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm, ProfileAdditionalForm

from drive.models import Folder


@login_required
def create_folder(request):
    if request.method == 'POST':
        name = request.POST['name']
        parent_id = request.POST.get('parent_id')
        if parent_id:
            parent = Folder.objects.get(pk=parent_id)
            folder = Folder(name=name, parent=parent, owner=request.user)
        else:
            folder = Folder(name=name, owner=request.user)
        folder.save()
        return redirect('home')
    return render(request, 'create_folder.html')

@login_required
def edit_folder(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id, owner=request.user)
    if request.method == 'POST':
        folder.name = request.POST['name']
        folder.save()
        return redirect('home')
    return render(request, 'edit_folder.html', {'folder': folder})

@login_required
def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id, owner=request.user)
    folder.delete()
    return redirect('home')


@login_required
def view_folder(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id, owner=request.user)
    subfolders = Folder.objects.filter(parent=folder)
    return render(request, 'view_folder.html', {'folder': folder, 'subfolders': subfolders})


@login_required
def profile(request):
    user = request.user

    context = {
        'user': user,
    }

    return render(request, 'profile.html', context)
def edit_profile(request):
    # Implement logic to edit the user's profile
    if request.method == 'POST':

        return redirect('profile')

    return render(request, 'edit_profile.html')

@login_required
def home(request):
    # Implement logic to display user's folders and files
    folders = Folder.objects.filter(owner=request.user)
    return render(request, 'home.html', {'folders': folders})
