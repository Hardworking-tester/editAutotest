# encoding:utf-8
import cx_Oracle
class SelectFromOracle():

    def selectFromOracle(self,key):
        con=cx_Oracle.connect("yydscs01", "cs_123","192.168.2.102/chinapay")
        cr=con.cursor()
        data=key.decode('utf-8').encode('gbk')
        sql="select dd.* from yydscs.IMS_NEWS dd where dd.title="+"'"+data+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        count_data=cr.rowcount
        if count_data>=1:
            print ("产品：%s 存储到数据库成功,一共发布了：%s 条" %(key,count_data))



pp=SelectFromOracle()
pp.selectFromOracle("是打发")