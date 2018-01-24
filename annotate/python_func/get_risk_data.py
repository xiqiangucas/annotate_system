#coding=utf-8
from xml.etree import ElementTree as ET
import os

"""
#功能：
    根据日期解析每日热搜词xml文件
#输入：
    日期字符串：date_str，形如“2018-01-15”
#输出：
    每日热搜词列表：
"""
# def GetRiskData(date_str='2018-01-15'):
def GetRiskData(date_str):

    filename=os.path.join('annotate/python_func',date_str+'.xml')
    # filename=date_str+'.xml'
    hotword_lst = parse_xml2dict1(filename=filename)
    return hotword_lst
#解析xml文件
def parse_xml2dict1(filename):
    xml_text = open(filename,encoding= 'utf-8').read()
    root = ET.fromstring(xml_text)
    hotword_lst = []
    # 获取element的方法
    lst_node = root.getiterator("item")
    for node in lst_node:
        dict = {}
        for child in node.getchildren():
            if child.tag=='big_risk':
                dict[child.tag]=child.text
            if child.tag=='hotword':
                dict[child.tag]=child.text
            if child.tag=='link':
                dict[child.tag] = child.text
            if child.tag=='id':
                dict[child.tag] = int(child.text)
        hotword_lst.append(dict)
    return hotword_lst


#读取xml中的数据，以列表的形式返回，每个元素为一个字典
def GetRawData(date_str):
    #路径需要设置
    # filename = os.path.join('annotate/python_func', date_str + '.xml')
    base_path=r'D:\PyCharm\risk_data\ml_risk_data'
    filename = os.path.join(base_path, date_str + '.xml')
    # filename=date_str+'.xml'
    hotword_lst = parse_xml2dict(filename=filename)
    return hotword_lst
#解析xml文件
def parse_xml2dict(filename):
    xml_text = open(filename,encoding= 'utf-8').read()
    root = ET.fromstring(xml_text)
    hotword_lst = []
    # 获取element的方法
    lst_node = root.getiterator("item")
    for node in lst_node:
        dict = {}
        for child in node.getchildren():
            dict[child.tag] = child.text
        hotword_lst.append(dict)
    return hotword_lst

if __name__=="__main__":
    pass
    hotword_lst=parse_xml2dict1(filename=r'./2018-01-15.xml')
    # hotword_lst=GetRiskData(date_str='2018-01-15')
    hotword_lst = GetRawData(date_str='2018-01-15')
    for h in hotword_lst:
        print(h)
