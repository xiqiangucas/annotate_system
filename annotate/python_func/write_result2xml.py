#coding=utf-8
from xml.dom import minidom
from annotate.python_func.get_risk_data import parse_xml2dict, GetRawData

#将结果写入xml中
def write_hotwords2xml(filePath, hotword_list,date,date_flag=True, date_string='%Y-%m-%d',
                       num_flag=True, total_flag=True):
    '''
    将hotword_list中的信息保存到本地xml文件中
    :param filePath:xml文件路径
    :param hotword_list:需要保存的列表信息，列表中元素为字典格式
    :param date:汇总日期 类型为字符串类型
    :param date_flag:是否在xml文件中保存日期信息
    :param date_string:如果需要保存日期信息，日期的具体信息
    :param num_flag:是否需要保存信息总数
    :param total_flag:字典中的信息直接保存在根节点下，还是保存在Total节点下
    :return:
    '''
    doc = minidom.Document()
    root = doc.createElement('Rankings')
    doc.appendChild(root)
    ###如果写入时间信息
    if date_flag:
        # nowtime = datetime.datetime.now()
        # nowtime = nowtime.strftime(date_string)
        time_info_list = date.split('-')
        time_tag_info = date_string.split('-')
        time_tag_dict = {'%Y': 'Year', '%m': 'Month', '%d': 'Day'}
        for i in range(len(time_info_list)):
            time_info = doc.createElement(time_tag_dict[time_tag_info[i]])
            time_info_text = doc.createTextNode(time_info_list[i])
            time_info.appendChild(time_info_text)
            root.appendChild(time_info)
    ###如果写入热搜词数量信息
    if num_flag:
        num_info = doc.createElement('number')
        num_info_text = doc.createTextNode(str(len(hotword_list)))
        num_info.appendChild(num_info_text)
        root.appendChild(num_info)

    if total_flag:
        total = doc.createElement('Total')
        root.appendChild(total)
    for one_hotword in hotword_list:
        item = doc.createElement('item')
        for info in one_hotword:  ###one_hotword为字典格式
            info_child = doc.createElement(info)
            # print one_hotword[info]
            # info_child_text = doc.createTextNode(str(one_hotword[info]))
            info_child_text = doc.createTextNode((one_hotword[info]))
            info_child.appendChild(info_child_text)
            item.appendChild(info_child)
        if total_flag:
            total.appendChild(item)
        else:
            root.appendChild(item)
    # f = file(filePath, 'w')
    f = open(filePath, 'w')
    doc.writexml(f, '', '   ', '\n', 'utf-8')
    f.close()

if __name__=="__main__":
    date_str="2018-01-15"
    hotword_lst = parse_xml2dict(filename='2018-01-15.xml')
    write_hotwords2xml(filePath='2018-01-15_r.xml',hotword_list=hotword_lst,date=date_str)
