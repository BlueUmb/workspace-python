sum1 = 0
cnt1 = 1

while cnt1<=100:
    sum1+=cnt1
    cnt1+=1

print('1 ~ 100 합 :',sum1)
print('1 ~ 100 합 :',sum(range(1,101)))
print('1 ~ 100 안 3의 배수의 합 :',sum(range(3,101,3)))





print()
names = ["Ezen1","Ezen2","Ezen3","Ezen4","Ezen5","Ezen6"]

for name in names:
    print("You are",name)
    
    
name = "EzenIT"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())