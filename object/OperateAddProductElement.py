# encoding:utf-8
from selenium import webdriver
from Data import  ReadExcel,get_number_by_data
import time
class OperateElement():


    def opermateAddProductElement(self,br,object_name,located_element,data_list):
        br=br
        object_name=object_name
        located_element=located_element
        # print br,object_name,located_element

        excel=ReadExcel.ReadExcel()
        operate_method_excelpath="F:\\pytest\\editAutotest\\Data\\addProduct_data.xls"
        operate_method_sheet=excel.getTableBySheetName(operate_method_excelpath,"operate_method")
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(operate_method_excelpath,"operate_method",object_name)
        operate_method=operate_method_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+1)

        # print object_name
        if operate_method=='click':
            located_element.click()
            time.sleep(4)
        elif operate_method=='sendkey' and object_name==u'产品标题':
            located_element.clear()
            located_element.send_keys(data_list[0])
        elif operate_method=='sendkey' and object_name==u'关键词':
            located_element.clear()
            located_element.send_keys(data_list[1])