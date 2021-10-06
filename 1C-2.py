
# 세 정수를 입력받아 중앙값 구하기 1

def med3(a,b,c):
    if a>=b :
        if b>=c : return b
        elif c>=a : return a
        else : return c
    elif a<b : # 코드 효율 생각하면 빼는 게 좋으려나
        if c<=a : return a
        elif b<=c : return b
        else : return c

# 세 정수를 입력받아 중앙값 구하기 2

def med33(a,b,c):
    if (b>=a and c<=a) or (b<=a and c>=a): return a
    elif (a>b and c<b) or (a<b and c>b): return b
    return c


print('세 정수의 중앙값을 구합니다')
a = int(input('정수 a의 값을 입력학세요.:'))
b = int(input('정수 b의 값을 입력하세요.:'))
c = int(input('정수 c의 값을 입력하세요.:'))

print(f'중앙값은 {med3(a,b,c)}입니다.')
print(f'중앙값은 {med33(a,b,c)}입니다.')