
# 세 정수의 최댓값 구하기

def max3(a,b,c):
    maximum=a
    if b>maximum : maximum=b
    if c>maximum : maximum=c
    return maximum # 최댓값 반환

print(f'max3(3,2,2)={max3(3,2,2)}')
print(f'max3(3,1,2)={max3(3,1,2)}')