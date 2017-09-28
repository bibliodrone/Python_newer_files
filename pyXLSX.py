import openpyxl

wb=openpyxl.load_workbook("2018Budgets.xlsx")
for item in wb.get_sheet_names():
    print (item)

sheet = wb.get_sheet_by_name('Table 1')
cellRange = sheet ['A1':'P1']
for cell in cellRange:
    print(cell.coordinate, cell.value)
    print("END")
        



