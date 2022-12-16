# ezen07-2
'''
    * Defaulte parameter (기본 인자)
        - 함수의 파라미터에 기본값 지정 가능
        - 파라미터를 명시하지 않을 경우. 지정된 기본값으로 대체
        - 디폴트 파라미터 뒤에 일반 파라미터가 위치할수 없음
            - e.g) def test(a,b,c = 1)
                    def test(a,b =1, c =2)
                    def test(a=1, b=1, c= 3)

                올바르지 않은 예)
                    def test(a,b = 1, c)
                    def test(a=1,b,c)
                    def test(a=1,b=1,c)
'''
print('test')
help(print)

def plus_ver2(number_01, number_02 = 100):
    print(number_01 + number_02)

print(plus_ver2(11))
plus_ver2(number_01=0,number_02=77)

print()

'''
    *agrs : 함수를 호출할때 아규먼트의 개수를 특정지을수 없을 때 사용함
            불특정한 수의 숫자들은 'args' 라는 튜플에 추가됨
'''
def plus_unlimited(*args):
    print(type(args), args)
    sum(args)
    print(sum(args))

plus_unlimited(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)

print()
'''
    **kwargs : 함수를 호출할때 키워드 아규먼트의 개수를 특정지을 수 없을 때 사용함
                불특정한 수의 키워드 아규먼트들은 'kwargs'라는 딕셔너리에 추가됨
'''
def plus_unlimited(*args, **kwargs):
    print(type(kwargs),kwargs)
    '''
        *args 와 **kwargs라는 딕셔너리 형태로 값을 받는 함수
        전체 합의 결과를 출력합니다
    '''
    sum(kwargs.values())    ## 키워드 아규먼트의 합
    sum(args)               ## dkrbajsxmdml gkq
    print(sum(args) + sum(kwargs.values()))

plus_unlimited(1,2,3,4, num1 =100, num2 = 3000, num3 =20, num4=7)
print()

'''
    list를 함수의 파라미터로 넣어 실행하는 경우
'''
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plus_unlimited(*list_numbers)
print()
'''
    딕셔너리를 함수의 파라미터로 넣어 실행하는 경우
'''
dict_heights = {'ezen_height' : 178, 'ezenyoung_height' : 180, 'sugiezen_height' : 176, 'ezensun_height' :180}
plus_unlimited(**dict_heights)

'''
    Docstring : 함수의 설명을 작성해놓은 기술문서
                수많은 파이썬 함수의 사용법과 정보를 나타냄
'''

#help(plus_unlimited)
#help(print)
#help(input)

'''
    * Lambda 함수
        - 단일문으로 표현되는 익명함수
            - 익명함수란 이름이 없는 구현체만 존재하는 간단한 함수를 의미
        - 코드 상에서 한번만 사용되는 기능이 있을 때,
          굳이 함수로 만들지 않고 1회성으로 만들어서 쓸때 사용
'''

square = lambda x: x**2
print(square(5))

def add(x, y):
    return x + y

add = lambda x,y:x+y
print(add(10,20))

def Pythagoras(num1, num2):
    return (num1**2 + num2**2)**0.5

Pytha = lambda x,y:(x**2+y**2)**0.5
print(Pytha(3,4))

'''
    키가 180cm 이상인 사람들의 경우 "키가 정말 큽니다." 라는 메시지가 출력하고,
    그렇지 않은 경우를 " 계속 키가 클 겁니다." 라는 메시지로 출력하는 함수를 작성하시오.

    height_high(181)
    height_high(178)
'''

def height_high(height):
    if height>=180:
        print("키가 정말 큽니다.")
    else:
        print("계속 키가 클 겁니다.")
        
height_high(181)
height_high(178)

