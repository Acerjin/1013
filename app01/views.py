# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,Http404
from models import Category,BBS
from django import forms
from django.contrib import auth
from django_comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from app01.models import BBS_user,User
from django.http.response import HttpResponseNotFound, HttpResponse
from django.http.request import HttpRequest
import json
import cx_Oracle
from django.template.defaulttags import comment



# Create your views here.

def index_category(request,category_id):
    if request.user.id == 1:
        bbs = BBS.objects.all().filter(category=category_id)
    else:
        bbs = BBS.objects.filter(author=request.user.id,category=category_id)
    category = Category.objects.filter(administrator=request.user.id)
    #bbs = BBS.objects.filter(author=request.user.id,category=category_id)
    print '___>',category_id
    return render_to_response('index.html',{'category':category,'bbs_list':bbs,'user':request.user})



def index(request):
    if request.user.id == 1:
        
        category = Category.objects.all().order_by('administrator_id')
        bbs = BBS.objects.all()
    else:
        
        category = Category.objects.filter(administrator=request.user.id).order_by('administrator_id')
        bbs = BBS.objects.filter(author_id=request.user.id)
    
    print '___>',category
    return render_to_response('index.html',{'category':category,'bbs_list':bbs,'user':request.user})
def bbs(request,bbsid):
    bbs = BBS.objects.get(id=bbsid)
    
  
    return render_to_response('bbs.html',{'bbs_detail':bbs,'user':request.user})


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
def login(request):
    if request.method == "POST":
        uf = UserForm(request.POST)        
        if uf.is_valid():
            username = uf.cleaned_data['username']  
            password = uf.cleaned_data['password'] 
            user = auth.authenticate(username=username,password=password)  
            print '---->',username,password         
            if user is not None:  
                auth.login(request, user)         
                re = HttpResponseRedirect('/index', {'user':user})
                re.set_cookie('username', username, 60)
                return re
                 
            else:
                
                return render_to_response('login.html',{'Error':'error','uf':uf})
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})



def logout(request):
    auth.logout(request)
    re = HttpResponseRedirect('/index')
    re.delete_cookie('username')
    return re
    
         
def sub_comment(request):
    bbs_id = request.POST.get('bbs_id')
    comment1 = request.POST.get('comment')
    author = request.user.id
    print author,comment1
    Comment.objects.get_or_create(
          object_pk = bbs_id,                              
          content_type_id = 7,
          site_id = 1,
          user_id = author,
          comment = comment1
    )
    
    return HttpResponseRedirect('/bbs/%s' %bbs_id)
def pub_bbs(request):
    if request.user.id == 1:
        category = Category.objects.all()
    else:
        category = Category.objects.filter(administrator=request.user.id)
    return render_to_response('pub_bbs.html',{'user':request.user,'category':category})
def new_bbs(request):
    category1 = request.POST.get('category')
    bbs_content = request.POST.get('bbs_content')
    bbs_title = request.POST.get('bbs_title')
    author = request.user.id
    print category1  
    BBS.objects.create(
        title = bbs_title,
        
        summary = 'hjklll;',
        content = bbs_content,
        author_id = author,
        view_count = 1,
        ranking = 1,
        category = category1,
    )  
    return HttpResponseRedirect('/index')
def httpview(request): 
#     return HttpResponseNotFound('<h1>Not Found</h1>')
#     raise Http404('not exist')
#     return HttpResponse(status=201)
    meta = request.META.items()
    co = request.COOKIES.items()
    se = request.session.items()
    return render_to_response('httpview.html',{'meta':meta,'co':co,'se':se})
def bbsview(request):  
    model = BBS
def index1(request):
    return render_to_response('index1.html')
def readexcel(request):
    return render_to_response('readexcel.html')
def subexcel(request):
    econtent = request.POST.get('demo')
    e = json.loads(econtent)   ##list
    db1 = cx_Oracle.Connect('acerjin','acerjin','127.0.0.1:1521/ACERJIN')
    cursor = db1.cursor()
    list = ['dwbm','dwmc','sbh','xm','sfzh','xtrq','sczt','rztj','rzfs','rzjg','rzsj']    
    for ec in e:
        print ec[list[1]]
        cursor.execute('insert into dqdy(dwbm, dwmc, sbh, xm, sfzh, xtrq, sczt, rztj, rzfs, rzjg, rzsj) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)',[ec[list[0]],ec[list[1]],ec[list[2]],ec[list[3]],ec[list[4]],ec[list[5]],ec[list[6]],ec[list[7]],ec[list[8]],ec[list[9]],ec[list[10]]])
    db1.commit()
    cursor.close()
    db1.close()
    return HttpResponseRedirect('/info_search')
    
    #return render_to_response('test.html',{'dic_e':e,'dwmc':dwmc,'k':m})
def info_search(request):
    db1= cx_Oracle.connect('acerjin','acerjin','127.0.0.1:1521/ACERJIN')
    cursor = db1.cursor()
    sql = 'select sfzh,mt from FIRSTTABLE t'
    cursor.execute(sql)
    sqldata  = cursor.fetchall()
    cursor.close()
    #print sqldata
    return render_to_response('info_search.html',{'sqldata':sqldata})
def info_wr(request):
    db1=cx_Oracle.connect('acerjin','acerjin','127.0.0.1:1521/ACERJIN')
    cursor = db1.cursor()
    value1 = '454656'
    value2 = '测试'
    sql = 'insert into FIRSTTABLE (sfzh,mt) values (value1,value2)'
    cursor.execute('insert into FirSTTABLE(SFZH,mt) values(:1,:2)',[value1,value2])
    db1.commit()
    cursor.close()
    db1.close()
    return HttpResponse('ok')
