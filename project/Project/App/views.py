from django.shortcuts import render, redirect
from .models import MsUser, TempMsUser, Post, Comment, Like
from django.contrib.auth.models import User
from Project.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json, csv, os
import boto3
from boto3.session import Session
from datetime import datetime, timedelta



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_DIR = os.path.join(BASE_DIR, "app", "DataBase", "MemberDataBase.csv")

# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = '아이디 또는 비밀번호가 틀렸습니다.'
            return render(request, 'registartion/login.html')
        
        auth.authenticate(
            request, 
            found_user,
            backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next', '/'))

    return render(request, 'registration/login.html')


def signup(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username = request.POST['username'])
        if(len(found_user)>0):
            error = '해당 계정은 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error': error})

        new_user = User.objects.create(
            username = request.POST['username'],
            password = request.POST['password']
        )

        MsUser.objects.create(
            user = new_user.username,
            name = request.POST['name'],
            kisoo = request.POST['kisoo'],
            email = request.POST['email'],
            major = request.POST['major'],
            idNumber = request.POST['idNumber']
        )

        auth.login(request,new_user)
        return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')

    return render (request, 'registration/signup.html')


@login_required(login_url='/registration/login')
def myPage(request):
    
    return render(request, 'myPage.html')

def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.MsUser,
            category = request.POST['category']
        )
        return redirect('detail', new_post.pk)

    return render(request, 'board.html')

@login_required(login_url = '/registration.login')
def edit(request):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(

            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('board_detail', post_pk)
    
    return render(request, 'board_detail_edit.html', {'post':post })



def board(request):
    board_post = Post.objects.all()
    return render(request, 'board.html', {'board_posts' : board_posts})



def board_detail (request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Comment.objects.create (
            post = post,
            content = request.POST ['post'],
            author = request.user
        )
        return redirect('board_detail', post_pk)
    return render(request,'board_detail.html', {'post':post})

@csrf_exempt
def memberCheck(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMP_DIR = os.path.join(BASE_DIR, "App", "DataBase", "MemberDataBase.csv")
    TempMsUser.objects.all().delete()

    with open(TEMP_DIR, newline='', encoding = "euc-kr") as csvfile:
        csv_data = list(csv.reader(csvfile))
        
    if request.method != 'POST':
        Gisoo = set()
        for i in range(1,len(csv_data)):
            Gisoo.add(csv_data[i][1])
            if csv_data[i][1] == '8':
                TempMsUser.objects.create(
                    name = csv_data[i][0],
                    kisoo = int(csv_data[i][1]),
                    email = csv_data[i][2],
                    major = csv_data[i][3],
                    idNumber = csv_data[i][4]
                )

        SendTempMsUser = TempMsUser.objects.all()
        print(SendTempMsUser) 
        return render(request, 'memberCheck.html', {'members': SendTempMsUser, "Gisoo" : Gisoo})
    
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        js_gisoo = request_body["js_gisoo"]

        TempMsUser.objects.all().delete()
        sendName = []
        sendKisoo = []
        sendEmail = []
        sendMajor = []
        sendIdNumber = []

        for i in range(1,len(csv_data)):
            if csv_data[i][1] == js_gisoo:
                    sendName.append(csv_data[i][0])
                    sendKisoo.append(int(csv_data[i][1]))
                    sendEmail.append(csv_data[i][2])
                    sendMajor.append(csv_data[i][3])
                    sendIdNumber.append(csv_data[i][4])
                

        response = {
            'name': sendName,
            'kisoo': sendKisoo,
            'email': sendEmail,
            'major': sendMajor,
            'IdNumber': sendIdNumber
        }
        
        return HttpResponse(json.dumps(response)) 
        # response = {
        #     "members" : SendTempMsUser
        # }

        # return HttpResponse(json.dumps(response))


    # return render(request.memberCheck.html)


@login_required(login_url='/registration/login')
def joinUs(request):
    if request.method == 'POST':
        file_to_upload = request.FILES.get('file')
        session = Session(
            aws_access_key_id = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
            region_name = AWS_S3_REGION_NAME
        )
        s3 = session.resource('s3')
        now = datetime.now().strftime("%Y%H%M%S")

        lfile_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = now + file_to_upload.name,
            Body = file_to_upload
        )
        # s3_url = 'https://sanggyeong-bucket.s3.ap-northeast-2.amazonaws.com/'
        return redirect('home')

    return render(request, 'joinUs.html')

