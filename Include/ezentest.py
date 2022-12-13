year = int(input("년도를 입력하세요 : "))

if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
    print(year,"년은 윤년입니다")
else:
    print(year,"년은 평년입니다")