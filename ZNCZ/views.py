from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from ZNCZ.Functional_function import Web_Title, auto_abstract_short, auto_abstract_norm, auto_abstract_long, \
    keywords_draw, text_wrong

from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse, HttpResponseRedirect
import json, random
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User


class auto_title(View):
    def get(self, request):
        return render(request, 'auto_title.html')

    def post(self, request):
        data = request.POST
        text = data['textArea']
        text2 = "".join(text)
        text3 = str(auto_abstract_norm.auto_abstract_norm(text2))
        title1 = Web_Title.autotitle(text)
        title2 = Web_Title.autotitle(text3)

        str1 = "".join(title1)
        str2 = "".join(title2)
        str11 = str1.replace('[UNK]', "")
        str22 = str2.replace('[UNK]', "")
        str23 = str22.replace(' ', "")
        str24 = str11.replace(' ', "")
        title1 = str24.replace('新局面新局面', "新局面")
        title2 = str23.replace('新局面新局面', "新局面")

        response = JsonResponse({'title1': title1, 'title2': title2})
        return response


class ab_long(View):
    def get(self, request):
        return render(request, 'Abstract_long.html')

    def post(self, request):
        data = request.POST
        text = data['textArea']
        text2 = "".join(text)
        # print(text)
        abstract3 = auto_abstract_long.auto_abstract_long(text)
        # print(abstract3)
        str1 = "".join(abstract3)
        str2 = str1.replace('[\'', "")
        str3 = str2.replace('\']', "")
        abstract3 = str3.replace('\', \'', "")

        response = JsonResponse({'abstract3': abstract3})
        return response


class ab_norm(View):
    def get(self, request):
        return render(request, 'Abstract_norm.html')

    def post(self, request):
        data = request.POST
        text = data['textArea']
        # print(text)
        text2 = "".join(text)
        abstract1 = auto_abstract_norm.auto_abstract_norm(text)

        str1 = "".join(abstract1)
        str2 = str1.replace('[\'', "")
        str3 = str2.replace('\']', "")
        abstract1 = str3.replace('\', \'', "")

        response = JsonResponse({'abstract1': abstract1})
        return response


class ab_short(View):
    def get(self, request):
        return render(request, 'Abstract_short.html')

    def post(self, request):
        data = request.POST
        text = data['textArea']
        # print(text)
        text2 = "".join(text)
        abstract5 = auto_abstract_short.auto_abstract_short(text)

        str1 = "".join(abstract5)
        str2 = str1.replace('[\'', "")
        str3 = str2.replace('\']', "")
        abstract5 = str3.replace('\', \'', "")

        response = JsonResponse({'abstract5': abstract5})
        return response


class historical_record(View):
    def get(self, request):
        return render(request, 'historical record.html')


class file_upload(View):
    def post(self, request):
        File = request.FILES.get("file", None)
        text = ''
        for chunk in File.chunks():
            text = text + chunk.decode('utf-8')
        title3 = Web_Title.autotitle(text)
        text2 = "".join(text)
        text3 = str(auto_abstract_norm.auto_abstract_norm(text2))
        title4 = Web_Title.autotitle(text3)

        str1 = "".join(title3)
        str2 = "".join(title4)
        str11 = str1.replace('[UNK]', "")
        str22 = str2.replace('[UNK]', "")
        title3 = str11.replace(' ', "")
        title4 = str22.replace(' ', "")
        # print(title)

        response = JsonResponse({'title3': title3, 'title4': title4})
        return response


class short_file_upload(View):
    def post(self, request):
        File = request.FILES.get("file", None)
        text = ''
        for chunk in File.chunks():
            text = text + chunk.decode('utf-8')
        abstract6 = auto_abstract_short.auto_abstract_short(text)
        # print(abstract6)

        text2 = "".join(text)
        str1 = "".join(abstract6)
        str2 = str1.replace('[\'', "")
        str3 = str2.replace('\']', "")
        abstract6 = str3.replace('\', \'', "")

        response = JsonResponse({'abstract6': abstract6})
        return response


class long_file_upload(View):
    def post(self, request):
        File = request.FILES.get("file", None)
        text = ''
        for chunk in File.chunks():
            text = text + chunk.decode('utf-8')
        abstract4 = auto_abstract_long.auto_abstract_long(text)
        # print(abstract4)
        text2 = "".join(text)
        str1 = "".join(abstract4)
        str2 = str1.replace('[\'', "")
        str3 = str2.replace('\']', "")
        abstract4 = str3.replace('\', \'', "")

        response = JsonResponse({'abstract4': abstract4})
        return response


class norm_file_upload(View):
    def post(self, request):
        File = request.FILES.get("file", None)
        text = ''
        for chunk in File.chunks():
            text = text + chunk.decode('utf-8')
        abstract2 = auto_abstract_norm.auto_abstract_norm(text)

        text2 = "".join(text)
        str1 = "".join(abstract2)
        str2 = str1.replace('[\'', "")
        str3 = str2.replace('\']', "")
        abstract2 = str3.replace('\', \'', "")
        # 将数据上传至数据库

        response = JsonResponse({'abstract2': abstract2})
        return response


class keywords(View):
    def get(self, request):
        return render(request, 'keywords.html')

    def post(self, request):
        data = request.POST
        text = data['textArea']
        # print(text)
        text2 = "".join(text)
        keywords = keywords_draw.keywords_draw(text)

        response = JsonResponse({'keywords': keywords})
        return response


class wrong(View):
    def get(self, request):
        return render(request, 'text_wrong.html')

    def post(self, request):
        data = request.POST
        text = data['textArea']
        text2 = "".join(text)
        wrong = text_wrong.text_wrong(text2)

        response = JsonResponse({'wrong': wrong})
        return response


def login_action(request):
    if request.method == 'POST':  # 判断采用的是何种请求
        username = request.POST['username']  # request.POST[]或request.POST.get()获取数据
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # 保存登录会话,将登陆的信息封装到request.user,包括session
            return redirect('/')
        else:
            return render(request, './login.html', {'error': '用户名密码错误！'})
    else:
        return render(request, './login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']  # request.POST[]或request.POST.get()获取数据
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('/')
    else:
        return render(request, './register.html')


def my_login(request):
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('login')


# class index(View):
#     @login_required
#     def get(self, request):
#         username = request.user
#         return render(request, './index.html', {'username': username})

@login_required
def index(request):
    username = request.user
    return render(request, './index.html', {'username': username})


# def index(request):
#     username = request.user
#     return render(request, './auto_title.html', {'username': username})


class introduce(View):
    def get(self,request):
        return render(request, 'introduce.html')
