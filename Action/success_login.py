# encoding:utf-8
from selenium import  webdriver
from Data import ReadExcel
from Data import get_number_by_data
from object import LocateLoginObject
import Browser,unittest
from resultlog import ResultLog
class Login(unittest.TestCase):


    def setUp(self):
        self.browser=Browser.Browser().init_browser()

    def getUsernameAndPasswordByTestcaseid(self,testcaseid):
        """根据传递过来得testcaseid去拿到用户名、密码、弹出框内容"""
        excel=ReadExcel.ReadExcel()
        testcase_excelpath="F:\\pytest\\editAutotest\\Data\\login_data.xls"
        testcase_sheet=excel.getTableBySheetName(testcase_excelpath,"username_password_data")
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber("username_password_data",testcaseid)
        data_list=[]
        user_name=testcase_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+2)
        pass_word=testcase_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+3)
        alert_message=testcase_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+4)
        data_list.append(user_name)
        data_list.append(pass_word)
        data_list.append(alert_message)

        return data_list


    def testNullUsername(self):
        u"""case_0002-用户名为空的测试用例"""
        testcaseid='case_0002'
        data_list=self.getUsernameAndPasswordByTestcaseid(testcaseid)
        username=data_list[0]
        password=data_list[1]
        alertmessage=data_list[2]
        LocateLoginObject.LocateLoginObject().getLocateObject(self.browser,username,password,alertmessage)

        self.dealAlert(alertmessage)


    def testNotExistUsername(self):
        u"""case_0001-用户名不存在的测试用例"""
        testcaseid='case_0001'
        data_list=self.getUsernameAndPasswordByTestcaseid(testcaseid)
        username=data_list[0]
        password=data_list[1]
        alertmessage=data_list[2]
        LocateLoginObject.LocateLoginObject().getLocateObject(self.browser,username,password,alertmessage)
        self.dealAlert(alertmessage)

    def testErrorPassword(self):
        u"""case_0003-密码错误的测试用例"""
        testcaseid='case_0003'
        data_list=self.getUsernameAndPasswordByTestcaseid(testcaseid)
        username=data_list[0]
        password=data_list[1]
        alertmessage=data_list[2]
        LocateLoginObject.LocateLoginObject().getLocateObject(self.browser,username,password,alertmessage)
        self.dealAlert(alertmessage)

    def testSuccessLogin(self):
        u"""case_0004-登录成功的测试用例"""
        testcaseid='case_0004'
        data_list=self.getUsernameAndPasswordByTestcaseid(testcaseid)
        username=data_list[0]
        password=data_list[1]
        alertmessage=data_list[2]
        LocateLoginObject.LocateLoginObject().getLocateObject(self.browser,username,password,alertmessage)
        self.dealAlert(alertmessage)


    def dealAlert(self,alertmessage):
        """处理弹出框"""
        self.assertEqual(alertmessage,self.browser.switch_to_alert().text)

        try:
            self.browser.switch_to_alert().accept()
        except:
            print("no alert")
    def tearDown(self):
        self.browser.close()