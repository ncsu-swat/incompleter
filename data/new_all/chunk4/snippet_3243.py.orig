#Source: https://stackoverflow.com/questions/76841111/attributeerror-openpyxlwriter-object-has-no-setter-when-setting-writer-book
book = openpyxl.load_workbook(r'D:\Anto\Daily Work\Daily Reservoir Level\August\Plotting\Excel\{}.xlsx'.format(my_list[j], data_only=True))
writer = pd.ExcelWriter(r'D:\Anto\Daily Work\Daily Reservoir Level\August\Plotting\Excel\{}.xlsx'.format(my_list[j]),engine='openpyxl', mode='a', if_sheet_exists='overlay')
writer.book = book