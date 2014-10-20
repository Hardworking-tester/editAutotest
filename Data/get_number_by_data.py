# encoding:utf-8
import xlrd
class GetRowAndColNumber():
    def getRowAndColNumber(self,sheet_name,key):
        data=xlrd.open_workbook("F:\\pytest\\editAutotest\\Data\\login_data.xls")
        sheet=data.sheet_by_name(sheet_name)
        rows=sheet.nrows
        cols=sheet.ncols
        # key='id'
        row_col_list=[]
        for row_number in range(rows):
            for col_number in range(cols):
                if sheet.cell_value(row_number,col_number)==key:
                    row_col_list.append(row_number)
                    row_col_list.append(col_number)
                    return row_col_list

