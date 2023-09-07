import openpyxl as xl
from datetime import datetime


ls = []

ls_86 = []
ls_1 = []
ls_2 = []
ls_3 = []

n_st = int(input())
n_end = int(input())

table = xl.load_workbook('M-CHAT-R.xlsx')
sheet = table.active


for i in range(n_st, n_end+1):
    current_ls = []
    for j in range(10):
        if j != 7:
            if j == 2:
                current_ls.append(str(int(sheet[i][j].value)) + '/20')
            elif j == 0:
                dt = sheet[i][j].value
                current_ls.append(str(dt.strftime('%d.%m.%Y %H:%M:%S')))
            elif j == 4:
                dt = sheet[i][j].value
                current_ls.append(str(dt.strftime('%d.%m.%Y')))
            else:
                current_ls.append(str(sheet[i][j].value))
        else:
            continue
    ls.append(current_ls)

for i in ls:
    if i[7] == 'ДГП 86':
        ls_86.append(i)
    elif i[7] == 'ДГП 86 филиал 1':
        ls_1.append(i)
    elif i[7] == 'ДГП 86 филиал 2':
        ls_2.append(i)
    elif i[7] == 'ДГП 86 филиал 3':
        ls_3.append(i)

print(ls_1)
print(ls_2)
print(ls_3)
print(ls_86)


# для каждого здания сделать автозаполнение