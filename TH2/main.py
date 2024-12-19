arr =  [2, 5, 8, 9, 11]
x= 10
def linear_search(arr, x):
    # Duyệt qua từng phần tử của danh sách arr
    for i in range(len(arr)):
        # So sánh phần tử đang xét với giá trị cần tìm kiếm x
        if arr[i] == x:
            # Trả về vị trí của phần tử tìm thấy
            return i
    # Nếu đã duyệt qua toàn bộ danh sách mà không tìm thấy giá trị cần tìm kiếm, trả về giá trị không tìm thấy (-1)
    return -1
res = linear_search(arr,x)
if res == -1:
    print("Không tìm thấy giá trị", x)
else:
    print("Giá trị", x, "được tìm thấy tại vị trí", res)
