# đọc file dạng read, có dùng encoding utf8 để có thể đọc đc dấu
f = open("Dữ liệu.txt",mode = 'r',encoding = 'utf-8')
# in nội dung biến f ra kiểm tra
#print(f.read())
#tìm và in những dòng có cụm đầu của dòng là số v.
data_v = []
with open('Dữ liệu.txt', mode='r',encoding='utf-8') as f :
    line = f.readline()
    index = 0
    while line:
        # tách dừng dòng để thành array nhiều từ trong mỗi dòng
        words = line.split(' ')
        # kiểm tra cụm đầu trong array xem có khác V hay không
        if words[0] == 'v':
            # thêm dòng đó vào biến data ở trên mới tạo
             data_v.append(line)
             print(line)
            # tăng biến đếm lên 1 để chỉ số vòng v đã thêm
        index=index+1
        #in ra biến đếm:
        print(str(index))
        #tiếp tục
        line = f.readline()

import math
#Lấy thử tạo độ điểm 120
toadodiem = data_v[120].split(" ")
x = toadodiem[1]
y = toadodiem[2]
z = toadodiem[3]
#cho sang dạng float
x = float(x)
y = float(y)
z = float(z)
#Tính khoảng cách
khoangcach = math.sqrt(x**2+y**2+z**2)
#print(khoangcach)






