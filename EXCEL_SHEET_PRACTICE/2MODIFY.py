import openpyxl

wb = openpyxl.load_workbook('/content/SampleData.xlsx')
ws = wb.active
ws['C3'] = 'Approved'

wb.save('records.xlsx')

print("Cell C3 updated and file saved successfully!")
