def search():
    x = int(input("Nhap x:"))
    L = 0
    R =


# Sử dụng để kiểm tra <a href="https://dothanhspyb.com/khai-niem-mo-ta-thuat-toan-do-phuc-tap-cua-thuat-toan/">thuật toán</a>
arr = [2, 3, 4, 10, 40]
x = 10

# Hàm gọi tìm kiếm nhị phân
result = binary_search(arr, x)

if result != -1:
    print("Phần tử được tìm thấy tại vị trí", str(result))
else:
    print("Phần tử không được tìm thấy trong mảng")