'''

'''

def hello(world):
    print("hello, ",world)

hello("NiceYear")

print()

# 함수2
def hello_return(world):
    value = "Helloe, "+str(world)
    return value

str = hello_return("Ezen!")
print(str)

def func_mul(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1,y2,y3

val1,val2,val3 = func_mul(3)
print(val1,val2,val3)

print()
tup = func_mul(4)
print(type(tup), tup, list(tup))

# 딕셔너리 리턴

def func_mul4(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return {'ret1':y1,'ret2':y2,'ret3':y3}

dic = func_mul4(8)
print(type(dic), dic, dic.get('ret3'), dic.keys(),dic.values())

print()

# 함수4 (*args, **args)
# *args
def args_func(*args):
    for i,v in  enumerate(args):
        print('{}'.format(i),v,end=' ')
        
args_func('ezen')  
print()
args_func('ezen','ezenit')  
print()
args_func('ezen','ezenit','seoul')  

print()

# **args
def args_func2(**args):
    for v in  args.keys():
        print('{}'.format(v),args[v],end=' ')

args_func2(name1 ='lee')
print()
args_func2(name1 ='lee',name2 ='kim')
print()
args_func2(name1 ='lee',name2 ='kim',name3 ='park')
print()
      
# 함수5 - 전체 혼합

def func_ezen(arg_1,arg_2,*args,**kargs):
    print(arg_1,arg_2,args,kargs)
    
func_ezen(10,20)
print()
func_ezen(10,20,'snow','snow2','snow3')
print()
func_ezen(10,20,'snow','snow2','snow3', age1=30,age2=31,age3=32)

print()

# 함수6 - 중첩 함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    
    print("In func")
    func_in_func(num+100)

nested_func(1)
print()

# 함수7 - hint
def tot_length(word: str, num: int) -> int:
    return len(word)*num

print("hint func :",tot_length("Heavy snow falls in Seoul",10))