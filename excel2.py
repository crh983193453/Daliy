# coding=utf8
import xlrd, os, time
path = input()
xls_path = path.replace('\\', '\\\\')
path = xls_path
table = xlrd.open_workbook(path).sheet_by_index(0)
num = table.nrows
def getclassname():
    class_name = []
    for i in range(1, num):
        if str(table.row_values(i, 1, 2))[2:-2] not in class_name:
            class_name.append(str(table.row_values(i, 1, 2))[2:-2])
    return class_name
def getstudentname(a, b=3, c=7):
    list = []
    table1 = table.row_values(a, b, c)
    for i in table1:
        if i == '':
            continue
        else:
            result = str(i).split('、')
            for i in result:
                if i not in list:
                    list.append(i)
    return list
def check(class_name, dict):
    list = []
    switch = 0
    for i in range(1, num):
        every_line_classname = str(table.row_values(i, 1, 2))[2:-2]
        if class_name != every_line_classname:
            continue
        else:
            for a in range(3, 7):
                line_name = getstudentname(i, a, a + 1)
                if dict not in line_name:
                    continue
                elif switch == 0:
                    list.append(dict + ' ' + '日期' + str(table.row_values(i, 0, 1))[1:-1] + ' 上课时间' + str(table.row_values(i, 2, 3))[1:-1] + ' 原因' + str(table.row_values(0, a, a + 1))[1:-1])
                    switch = 1
                else:
                    list.append(' 日期' + str(table.row_values(i, 0, 1))[1:-1] + ' 上课时间' + str(table.row_values(i, 2, 3))[1:-1] + ' 原因' + str(table.row_values(0, a, a + 1))[1:-1])
    return list
def first():
    class_name = getclassname()
    dict = {}
    for i in class_name:
        dict.update({i: ''})
        dict[i] = []
        for b in range(1, num):
            if i == str(table.row_values(b, 1, 2))[2:-2]:
                for c in getstudentname(b):
                    if c not in dict[i]:
                        dict[i].append(c)
    return dict
def sencond(dict):
    global dirs
    class_name = getclassname()
    for i in class_name:
        total_num = len(dict[i])
        for b in range(0, total_num):
            result = check(i, dict[i][b])
            dict[i][b] = result
    for i in dict:
        for b in range(0, len(dict[i])):
            if not os.path.exists('C:\\result\\结果.txt'):
                os.mkdir('C:\\result\\')
            with open('C:\\result\\结果.txt', 'a') as (save):
                save.write('\r\n' + str(dict[i][b]))
                if b == len(dict[i]) - 1:
                    save.write('\r\n' + i + '统计结束')
if __name__ == '__main__':
    sencond(first())
    print('已在C:\\result\\结果.txt导出结果')
    input("please input any key to exit!!!")
    time.sleep(100)