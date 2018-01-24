from django.http import HttpResponse
from django.shortcuts import render
from annotate.python_func.write_result2xml import write_hotwords2xml
from annotate.python_func.get_risk_data import  GetRawData
import os
import datetime
# Create your views here.
#展示初始化页面，默认选择当前前一天作为默认显示
def index(request):
    #获取当前时间
    date_str=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    #step1：从本地获取热搜词
    # date_str = '2018-01-15'
    hotword_lst = GetRawData(date_str=date_str)
    return render(request, 'annotate/index.html', {'hotword_lst': hotword_lst,'date_str':date_str})

#根据时间显示某一天的热搜词列表
def hotword_page(request,date_str):
    hotword_lst = GetRawData(date_str=date_str)
    return render(request,'annotate/index.html',{'hotword_lst': hotword_lst,'date_str':date_str})
#表单响应
def hotword_action(request):
    date_str=request.GET['date_str']
    #读取原始文件
    hotword_lst = GetRawData(date_str=date_str)
    for dict in hotword_lst:
        id=dict['id']
        risk_name='risk'+str(id)
        subrisk_name='subrisk'+str(id)
        dict['big_risk']=request.GET[risk_name]
        dict['small_risk']=request.GET[subrisk_name]
    #保存校正结果，filePath需要设置
    base_path = r'D:\PyCharm\risk_data\annotate_risk_data'
    filename = os.path.join(base_path, date_str + '.xml')
    write_hotwords2xml(filePath=filename, hotword_list=hotword_lst, date=date_str)
    return render(request,'annotate/hotword_action.html',{'hotword_lst': hotword_lst,'date_str':date_str})





#测试form
def hotword_action1(request):
    date_str = request.GET['date_str']
    if 'risk0' in request.GET:
        risk = 'You searched for: %r' % request.GET['risk0']
    if 'date_str' in request.GET:
        date_str = 'You searched for: %r' % request.GET['date_str']
    else:
        message = 'You submitted an empty form.'
        risk = 'You submitted an empty form.'
        subrisk = 'You submitted an empty form.'
        date_str ='You submitted an empty form.'
    return HttpResponse(date_str)
#标注系统首页数据获取与传递
def get_data1():
    lst=[]
    dict1 = {'id':1, 'title':"中国人们",'link':'http://home.firefoxchina.cn/','risk':'国家安全','subrisk':''}
    dict2 = {'id':2, 'title': "中国共产党", 'link':'http://home.firefoxchina.cn/','risk': '精神文明', 'subrisk': ''}
    dict3 = {'id': 3, 'title': "中国共产党", 'link': 'http://home.firefoxchina.cn/', 'risk': '金融经济', 'subrisk': ''}
    dict4 = {'id': 4, 'title': "中国共产党", 'link': 'http://home.firefoxchina.cn/', 'risk': '日常生活', 'subrisk': ''}
    dict5 = {'id': 5, 'title': "中国共产党", 'link': 'http://home.firefoxchina.cn/', 'risk': '社会稳定', 'subrisk': ''}
    dict6 = {'id': 6, 'title': "中国共产党", 'link': 'http://home.firefoxchina.cn/', 'risk': '政府执政', 'subrisk': ''}
    dict7 = {'id': 7, 'title': "中国共产党", 'link': 'http://home.firefoxchina.cn/', 'risk': '资源环境', 'subrisk': ''}
    dict8 = {'id': 8, 'title': "中国共产党", 'link': 'http://home.firefoxchina.cn/', 'risk': '无风险', 'subrisk': ''}
    lst=[dict1,dict2,dict3,dict4,dict5,dict6,dict7,dict8]
    # lst=GetRiskData()
    return lst
def index_action(request):
    pass
    if 'risk3' in request.GET:
        risk = 'You searched for: %r' % request.GET['risk3']
    else:
        risk = 'You submitted an empty form.'
    # return HttpResponse(risk)
    return render(request,'annotate/index_action.html',{"message":risk})
#js测试
def js_test(request):
    return render(request,'annotate/js_test.html',{'risk':'risk'})
#表单处理
def form_test(request):
    return render(request,'annotate/form.html',{'risk':'金融经济'})
def form_action(request):

    if 'date' in request.GET:
        message = 'You searched for: %r' % request.GET['date']
    if 'risk' in request.GET:
        risk = 'You searched for: %r' % request.GET['risk']
    if 'subrisk' in request.GET:
        subrisk = 'You searched for: %r' % request.GET['subrisk']
    else:
        message = 'You submitted an empty form.'
        risk = 'You submitted an empty form.'
        subrisk = 'You submitted an empty form.'
    # return HttpResponse(message)
    # return HttpResponse(risk)
    return HttpResponse(subrisk)

    # return render(request,'annotate/form_action.html',{"message":message})
#测试字典和列表型数据的传递
def get_data():
    Dict = {'site': '标注系统', 'author': '郗强'}
    List = ['hello','world','mysystem']
    lst=[Dict,Dict,Dict]
    return Dict,List,lst
def home(request):
    pass
    # List = ['自强学堂', '渲染Json到模板']
    # Dict = {'site': '标注系统', 'author': '郗强'}
    Dict,List,lst=get_data()
    return render(request,'annotate/home.html',{'dict':Dict,'list':List,'lst':lst})



