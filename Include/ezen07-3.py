'''
    리스트 내 원소 중에서 가장 큰값의 인덱스(위치)를 찾아서 반환하는 함수를 작성하시오
    data = [7,1,5,9,3,2,4]
'''

def find_big_num(data):
    max_index = 0
    for i in range(len(data)):
        if data[max_index] < data[i]:
            max_index = i
            
    return max_index

data = [7,1,5,9,16,2,4]

print(f"최대값 위치 : data[{find_big_num(data)}] , 최대값 : {data[find_big_num(data)]}")

'''
    특정한 값을 가지는 원소의 인덱스를 찾는 함수를 작성
    
    [3,5,7,9],2     => -1 (찾지못한 경우 -1반환)
    [3,5,7,9],7     =>  2
    
    enumerate()
'''
print()

print("숫자 찾기")

def find_num(data,num):
    find_numlist = [] 
    for number in enumerate(data):
        if num == number[1]:
            find_numlist.append(number[0])
        
    if len(find_numlist) == 0 :
        return -1
    else:
        return find_numlist
         
num_data = [3,5,7,9,7,1,7,5]
print(f"찾은숫자의 인덱스: {find_num(num_data,7)}")

print()
print("소수 찾기")

'''
    하나의 자연수가 주었을때 소수인지 아닌지 판별하는 함수
'''

def find_primeNum(num):
    if num <= 1:
        return str(num)+"는 소수가 아닙니다" 
    
    for i in range(2,num):
        if num % i == 0:
            return str(num)+"는 소수가 아닙니다"          
    return str(num)+"는 소수입니다"
      
    
    
print(find_primeNum(2))
