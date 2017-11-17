import xlsxwriter

workbook = xlsxwriter.Workbook('Expension1.xlsx')   # 先创建一个workbook(相当于是一个excel文件吧)

worksheet = workbook.add_worksheet('Data')                # 在创建的excel文件中添加一个sheet(默认是名字是Sheet1，Sheet2等)

worksheet.write(row, col, some_data)
worksheet.write(row, col, '=SUM(B1:B4)')            # 结果中添加公式

worksheet.set_column('A:A', 20)                     # 扩展第一列（列宽）

bold = worksheet.add_format({'blod' : True})        # 添加格式
worksheet.write('A2', 'World', bold)                # 使用格式

worksheet.insert_image('B5', 'logo.png')            # 添加图片

workbook.close()                                    # 一定要记得关闭workbook（跟文件操作类似，其实就是文件操作...）
