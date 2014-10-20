#encoding:utf-8
import os
import sys,xlrd
from selenium.webdriver.common.by import By
from Data import ReadExcel
from Action import Browser
from Data import get_number_by_data
import time
class LocateLoginObject():

    def getLocateObject(self,browser,username,password,alertmessage):
        """循环需要定位的元素，拿到一个元素之后去调用getLocatMethodAndData方法，取得元素的定位方式以及定位所需数据"""
        browser=browser
        excel=ReadExcel.ReadExcel()
        object_excelpath="F:\\pytest\\editAutotest\\Data\\login_data.xls"
        object_sheet=excel.getTableBySheetName(object_excelpath,"objname_locatemethod_locatedata")
        object_sheet_rows=object_sheet.nrows
        object_name_list=[]#得到需要定位的元素的名称的列表
        for i in range(object_sheet_rows):#拿到登录功能中需要定位的对象名称列表
            object_name_list.append(object_sheet.cell(i,0).value)
        object_name_list.pop(0)#去掉对象名excel中的第一行的标签项名称
        #循环需要定位的元素，拿到一个元素之后去调用getLocatMethodAndData方法，取得元素的定位方式以及定位所需数据
        for object_name in object_name_list:
            self.getLocateMethodAndData(browser,object_name,username,password,alertmessage)


    def getLocateMethodAndData(self,browser,objname,username,password,alertmessage):
        """根据需要定位的元素的名称得到需要定位的元素的定位方式以及定位数据"""
        obj_name=objname
        br=browser
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber("objname_locatemethod_locatedata",obj_name)
        print row_col_number_list
        excel=ReadExcel.ReadExcel()
        locate_method_data_excelpath="F:\\pytest\\editAutotest\\Data\\login_data.xls"
        locate_method_data_sheet=excel.getTableBySheetName(locate_method_data_excelpath,"objname_locatemethod_locatedata")

        old_how=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+1)
        what=locate_method_data_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+2)

        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        if old_how=='linktext':
            new_how=locate_method_dict["linktext"]
        elif old_how=='id':
            new_how=locate_method_dict['id']
        elif old_how=='css':
            new_how=locate_method_dict["css"]
        elif old_how=='xpath':
            new_how=locate_method_dict["xpath"]
        print obj_name,new_how,what
        self.locateElement(br,new_how,what,obj_name,username,password,alertmessage)

    def locateElement(self,browser,how,what,obj_name,username,password,alertmessage):
        br=browser
        object_name=obj_name
        located_element=br.find_element(by=how,value=what)
        self.getOperateMethod(br,object_name,located_element,username,password,alertmessage)



    def getOperateMethod(self,br,object_name,located_element,username,password,alertmessage):
        br=br
        object_name=object_name
        located_element=located_element

        excel=ReadExcel.ReadExcel()
        operate_method_excelpath="F:\\pytest\\editAutotest\\Data\\login_data.xls"
        operate_method_sheet=excel.getTableBySheetName(operate_method_excelpath,"operate_method")
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber("operate_method",object_name)
        operate_method=operate_method_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+1)

        if operate_method=='click':
            located_element.click()
            time.sleep(5)
        elif operate_method=='sendkey' and object_name=='username':
            located_element.clear()
            located_element.send_keys(username)
            time.sleep(5)
        elif operate_method=='sendkey' and object_name=='password':
            located_element.clear()
            located_element.send_keys(password)
            time.sleep(5)
