from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

from .models import User, StudyGroup, Subject, Membership
from .forms import StudyGroupForm

def index(request):
    return render(request, "studypeer/index.html")

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "studypeer/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "studypeer/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "studypeer/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
             
        except IntegrityError:
            return render(request, "studypeer/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "studypeer/register.html")


# List all groups (homepage)
def group_list(request):
    groups = StudyGroup.objects.all().order_by('-created_at')
    return render(request, 'studypeer/group_list.html', {
        'groups': groups
        })


# View a single group
def group_detail(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    return render(request, 'studypeer/group_detail.html', {
        'group': group
        })


# Create a new group
@login_required
def create_group(request):
    if request.method == 'POST':
        form = StudyGroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.creator = request.user
            group.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = StudyGroupForm()
    return render(request, 'studypeer/group_form.html', {
        'form': form, 'action': 'Create'
        })


# Update a group (only by the creator)
@login_required
def update_group(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id, creator=request.user)
    if request.method == 'POST':
        form = StudyGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = StudyGroupForm(instance=group)
    return render(request, 'studypeer/group_form.html', {
        'form': form, 'action': 'Update'
        })


# Delete a group (only by the creator)
@login_required
def delete_group(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id, creator=request.user)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    return render(request, 'studypeer/group_confirm_delete.html', {
        'group': group
        })