
# 세 정수를 입력받아 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a=int(input('정수 a의 값을 입력하세요.:')) #input() 함수는 문자열 입력받아 반환
b=int(input('정수 b의 값을 입력하세요.:'))
c=int(input('정수 c의 값을 입력하세요.:'))

maximum=a
if b>maximum : maximum=b
if c>maximum : maximum=c

print(f'최댓값은 {maximum}입니다.') #f-string 은 문자열 안에 변수 값을 삽입하는 용도로 사용될 때 진가 발휘
