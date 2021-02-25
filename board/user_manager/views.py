from django.contrib import auth
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.template.context_processors import csrf
from django.template.loader import get_template
# from rest_framework.authtoken.admin import User

from user_manager.forms import LoginForm, JoinForm


def login(request):
    template = get_template('user_manager/login_form.html')

    context = {'login_form': LoginForm()}
    context.update(csrf(request))

    return HttpResponse(template.render(context))

def login_validate(request):
    login_form_data = LoginForm(request.POST)

    if login_form_data.is_valid():
        user = auth.authenticate(username = login_form_data.cleaned_data['id'], password = login_form_data.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                auth.login(request, user)

                return redirect('/board/')
        else:
            return HttpResponse('사용자가 없거나 비밀번호를 잘못 누르셧습니다.')

    else:
        return HttpResponse('로그인 폼이 비정상적입니다.')

    return HttpResponse('알 수 없는 오류 입니다.')

def join_page(request):
    if request.method == 'POST':
        form_data = JoinForm(request.POST)

        if form_data.is_valid():
            username = form_data.cleaned_data['id']
            password = form_data.cleaned_data['password']
            User.objects.create_user(username=username, password=password)

            return redirect('/board/')
    else:
        form_data = JoinForm()

    template = get_template('user_manager/join_page.html')

    context = {'join_form' : JoinForm()}
    context.update(csrf(request))

    return HttpResponse(template.render(context))