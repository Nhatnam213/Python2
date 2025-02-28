from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Sử dụng hàm
birth_date = date(2016, 5, 2)
age = calculate_age(birth_date)

print("Tuổi của bạn là: ", age)
