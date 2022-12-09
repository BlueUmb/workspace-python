# ezen05-1
# 파이썬 흐름제어 (제어문)
# 조건문, 반복문 

# 1. 두 개의 숫자 a, b에 원하는 숫자를 넣고 a가 b의 배수인지 확인하는 코드를 작성하시오.
# 배수라면 "a는 b의 배수입니다."를 출력하고, 그렇지 않다면 "a는 b의 배수가 아닙니다."를 출력하시오

a = 100
b = 6
if a % b == 0:
    print(f'{a}는 {b}의 배수입니다.')
else:
    print(f'{a}는 {b}의 배수가 아닙니다')


if a % b == 0:
    print('%d는 %d의 배수입니다.'%(a,b))
else:
    print('%d는 %d의 배수가 아닙니다'%(a,b))

'''
    머신러닝에서는 모델이 학습을 하게 되면, 학습에 주어진 인자들을 가지고 어떤 결과가 나왔는지 출력을 하게 됩니다.
    주어진 인자를 해당하는 자리에 위치하는 출력문을 작성하시오.
    아래는 출력문의 예시입니다.

    - Ezen777 모델로 10 epoch을 반복 학습 시킨 결과는 학습 정확도 : 0.85, 검증 정확도 : 0.83, 테스트 정확도 : 0.76으로 나왔습니다.

'''
# 다음 주어진 변수를 활용하여 코드를 작성하시오.
epoch = 10
train_accuracy = 0.85 
val_accuracy = 0.83
test_accuracy = 0.76
model_name = "Ezen777"

# case1
print(f'{model_name} 모델로 {epoch} epoch을 반복 학습 시킨 결과는 학습 정확도 : {train_accuracy}, 검증 정확도 : {val_accuracy}, 테스트 정확도 : {test_accuracy}으로 나왔습니다.')

# case2
print("{} 모델로 {} epoch을 반복 학습 시킨 결과는 학습 정확도 : {}, 검증 정확도 : {}, 테스트 정확도 : {}으로 나왔습니다.".format("Ezen777",10,0.85,0.83,0.76))

# case3
print("%s 모델로 %d epoch을 반복 학습 시킨 결과는 학습 정확도 : %.2f, 검증 정확도 : %.2f, 테스트 정확도 : %.2f으로 나왔습니다." %("Ezen777",10,0.85,0.83,0.76))



'''
    어떤 반의 학생 5명의 키에 대한 정보가 주어집니다.
    이를 리스트로 만들고 heights라는 변수에 저장하시오.
    167, 160, 175.5, 184, 170
'''

heights = [167,160,175.5,184,170]
print(heights)

heights.sort()
print(heights)

print(type(heights))

print(len(heights))

heights.remove(heights[-1])
print(heights)
print(len(heights))

heights.pop(-1)
print(heights)

heights.append(200)
print(heights)
print(len(heights))


heights_tup = tuple(heights)
print(heights_tup) 

name = ['최선혜', '전수정', '이규황', '반태희', '이경빈']
height = [160,167,170,175.5,200]

class_A = {}

for i in range(len(name)):
    class_A[name[i]] = height[i]

print(class_A)


grade = [65,70,100,43,50]

avg = sum(grade)/ len(grade)
print(avg)


#사용자가 입력을 받는 두자리 이상의 숫자 N에대해서 십의 자리숫자를 출력하는 코드를 작성하시오

# a = int(input("두자리 이상의 숫자를 입력하시오 : "))
# print(a%100//10)


'''
   주민등록번호들의 뒤에 6자리를 가려주는 코드를 작성하시오.
   911209-1234567 => 911209-1** 
'''
ezen_man = "911209-1234567"
ezen_women = "201210-2519860"
ezen_man2 = "991209-3234567"
ezen_women2 = "021210-4519860"

print(ezen_man[:8]+'******')
print(ezen_women[:8]+'******')
print(ezen_man2[:8]+'******')
print(ezen_women2[:8]+'******')

print()
ezen = [1,['a',2],3.14,"누구세요?"] 
print(ezen)

# ezen의 index2부터 끝까지 잘라내기를하시오
print(ezen[-2:])

print(ezen[1][0])

print(type(ezen))
print(dir(ezen))