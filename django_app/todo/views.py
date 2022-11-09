from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

SIGNUP_TEMPLATE = 'todo/signupuser.html'
LOGIN_TEMPLATE = 'todo/loginuser.html'
USERNAME_INPUT = 'username'
FIRST_PASS_INPUT = 'password1'
SECOND_PASS_INPUT = 'password2'
MISMATCHED_PASS_ERROR = 'Passwords did not match'
USER_EXISTS_ERROR = 'The specified user, already exists'
MISMATCH_USER_PASS = 'User and Password did not match'
# Create your views here.


def hometodos(request):
    return render(request, 'todo/home.html')


@require_http_methods(["GET", "POST"])
def signupuser(request):
    if request.method == 'GET':
        return render(request,
                      SIGNUP_TEMPLATE,
                      dict(form=UserCreationForm())
                      )

    post = request.POST
    if post.get(FIRST_PASS_INPUT) != post.get(SECOND_PASS_INPUT):
        return render(request,
                      SIGNUP_TEMPLATE,
                      dict(form=UserCreationForm(),
                           error=MISMATCHED_PASS_ERROR)
                      )

    try:
        # NOTE: The Django Raises an IntegrityError in the attempt at user
        # creation
        user = User.objects.create_user(
                    post.get(USERNAME_INPUT, 'NoOne'),
                    password=post.get(FIRST_PASS_INPUT, 'NotAValidPass'),
                    )
        user.save()
        print('### WATCH ####')
        login(request, user)
        return redirect('currenttodos')

    except IntegrityError:
        return render(request,
                      SIGNUP_TEMPLATE,
                      dict(form=UserCreationForm(),
                           error=USER_EXISTS_ERROR)
                      )


@require_http_methods(["GET", "POST"])
def loginuser(request):
    if request.method == 'GET':
        return render(request,
                      LOGIN_TEMPLATE,
                      dict(form=AuthenticationForm())
                      )

    post = request.POST
    user = authenticate(
                request,
                username=post.get('username'),
                password=post.get('password')
                )

    if user is None:
        return render(request,
                      LOGIN_TEMPLATE,
                      dict(form=AuthenticationForm(), error=MISMATCH_USER_PASS)
                      )

    login(request, user)
    return redirect('currenttodos')


@require_http_methods(['POST'])
def logoutuser(request):
    logout(request)
    return redirect('hometodos')


def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
