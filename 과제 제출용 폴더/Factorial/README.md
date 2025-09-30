# 팩토리얼 계산기 과제
함수 factorial_iter과 factorial_rec를 사용해 각각 반복문, 재귀 기반으로 팩토리얼 계산
start class 내부 함수
> __init__          생성자 / 전역변수로 주어진 함수 생성 입력받을 n > self.n
> print_factorial   반복문과 재귀 팩토리얼 계산 및 출력 함수 생성 / 계산이 걸리는 시간 확인
> tester            main 실행 함수

tester 내부에 무한 반복문을 이용해 메뉴 무한 반복

input_num 변수를 입력받아 사용자가 메뉴에서 선택
> input_num 1,2,3 일 경우 print_factorial에 변수값 전송
>> 전송받은 변수값이 1일때 반복문, 2일때 재귀로 팩토리얼 계산 3일때 if구문 두개 모두 통과하여 반복과 재귀 계산
>> input_num 4 일 경우 n에 준비된 배열의 값 선언 후 print_factorial에 변수 3을 전달 - 반복 재귀 모두 계산

변수를 입력 받을때 마다 try-except 구문을 사용해 오류 판별 / try-except로 안되는 오류는 if 구문으로 판별
