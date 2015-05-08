# encoding:utf-8
import PublicLogin,unittest
from Data import get_number_by_data,ReadExcel
from object import LocateAddProductObject
class AddProduct(unittest.TestCase):

    def setUp(self):
        self.browser=PublicLogin.PublicLogin().publicLogin()

    def getAddProductDataByTestcaseid(self,testcaseid):
        """根据传递过来得testcaseid去拿到发布产品所需要填写的内容"""
        excel=ReadExcel.ReadExcel()
        testcase_excelpath="F:\\pytest\\editAutotest\\Data\\addProduct_data.xls"
        testcase_sheet=excel.getTableBySheetName(testcase_excelpath,"addproduct_data")
        row_col_number_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(testcase_excelpath,"addproduct_data",testcaseid)
        data_list=[]
        # product_title:产品标题,key_word:关键词,standard:规格,producter:生产厂家,quality_date:保质期,storage_conditions:存储条件
        # product_allow_id:生产许可证号,product_standard_id:产品标准号,shop_price:批发价,retail_price:零售价
        # supply_amount:供货量,min_amount:最小起订量,sendproduct_limit:发货期限,picture_path:图片地址,product_summary:产品简介,check_code:验证码
        element_list=['product_title','key_word','standard','producter','quality_date',
                      'storage_conditions','product_allow_id','product_standard_id',
                      'shop_price','retail_price','supply_amount','min_amount','sendproduct_limit',
                      'picture_path','product_summary','check_code']
        col_index=2
        for i in range(element_list.__len__()):
            element_list[i]=testcase_sheet.cell_value(row_col_number_list[0],row_col_number_list[1]+col_index)
            col_index += 1
        for index in range(element_list.__len__()):
            data_list.append(element_list[index])

        return data_list

    def testAddProduct(self):
        u"""测试发布产品功能"""
        testcaseid='case_0005'
        data_list=self.getAddProductDataByTestcaseid(testcaseid)
        LocateAddProductObject.LocateLoginObject().getLocateObject(self.browser,data_list)
        print testcaseid
        self.browser.get_screenshot_as_file("F:\\testresult\\image_SUCCESSaddProduct.png")
        print("image_SUCCESSaddProduct.png ")

    # def tearDown(self):
    #     self.browser.close()





