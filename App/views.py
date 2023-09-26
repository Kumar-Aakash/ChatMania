import json
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import User, Room, UserRooms, Message, JoinRequests
import pusher


# Create your views here.

# Index
@login_required(login_url="login")
def index(request):
    # get the list of rooms
    rooms = Room.objects.all()
    print(rooms)
    # Get the list of rooms that users has requested to join
    join_requests = JoinRequests.objects.filter(user=request.user)
    x = [room.room for room in join_requests]
    print(x)
    # Get the list of rooms that the user has joined
    user_rooms = UserRooms.objects.filter(user=request.user)
    y = [room.room for room in user_rooms]
    print(y)
    return render(request, 'app/index.html', {
        'rooms': rooms,
        'join_requests': join_requests,
        'x': x,
        'y': y,
    })




def login_view(request):
    if request.method == 'POST':
        # Attempt to sign user in
        print("Login attempt")
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) 
        print(user)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            print("User is logged in")
            return HttpResponseRedirect(reverse("index"))
        else:
            print("User is not logged in")
            return render(
                request,
                "app/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        # Load login form
        return render(request, "app/login.html")



# Register a new user
def register_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "app/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            print("User created")
        except IntegrityError:
            return render(
                request,
                "app/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        # Load registration form
        return render(request, 'app/register.html')



# Logout
def logout_view(request):
    logout(request)
    return render(request, "app/login.html", {"message": "Logged out."})

