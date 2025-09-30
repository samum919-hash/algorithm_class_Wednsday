#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 박민성
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################

import time

def factorial_iter(n):  # 반복문 기반 n!
    result = 1
    for i in range(2, n+1):
        result *= i
    
    return result

def factorial_rec(n):   # 재귀 기반 n!
    if n == 1 or n == 0:
        return 1
    else: 
        return n * factorial_rec(n-1)
    # n-1값을 재귀함수로 다시 불러내어 n값과 곱하기를 n=1까지 반복
    

class start(): 
    def __init__(self):
        self.n = 0
        self.array = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]
    
    def print_factorial(self, input_num): # 선택값에 따른 반복, 재귀 계산
        n = self.n
        
        if input_num == 1 or input_num == 3:
            start_iter = time.perf_counter()
            result_iter = factorial_iter(n)
            end_iter = time.perf_counter()
            print(f"[반복] {n}! = {result_iter}")
    
        
        if input_num == 2 or input_num == 3:
            try:
                start_rec = time.perf_counter()
                result_rec = factorial_rec(n)
                end_rec = time.perf_counter()
                print(f"[재귀] {n}! = {result_rec}")
                
            except RecursionError:
                print("입력값이 너무 커서 재귀 계산은 불가능합니다.")
        if input_num == 3:
            if factorial_iter(n) == factorial_rec(n):
                x = True
            else:
                x = False
            print(f"결과 일치 여부 : {x}\n")
            print(f"[반복] : {(end_iter - start_iter):.10f} s || [재귀] : {(end_rec - start_rec):.10f} s")
    
    def tester(self):
        
        while(True):
            print('='*14, " Factorial Tester ", '='*14)
            print("1) 반복문으로 n! 계산\n"
                    "2) 재귀로 n! 계산\n"
                    "3) 두 방식 모두 계산 후 결과/시간 비교\n"
                    "4) 준비된 테스트 데이터 일괄 실행\n"
                    "q) 종료\n"
                    ,'-'*47)
            input_num = input("선택 : ")
            if input_num == 'q':
                break
            
            try: # 입력받은 선택값이 올바른 값인지 확인
                input_num = int(input_num)
                if input_num > 4:
                    raise TypeError("1~4의 정수로 입력해하세요 / 종료하시려면 q를 입력하세요\n")
            except TypeError:
                print("1~4의 정수로 입력해하세요 / 종료하시려면 q를 입력하세요\n")
                continue
            
            if input_num == 4:
                for i in range(len(self.array)):
                    self.n = self.array[i]
                    self.print_factorial(3)
                continue
            
            self.n = input("정수(0 이상의 숫자)만 입력하세요 : ")
            
            try: # 입력받은 n이 양의 정수인지 판별
                self.n = int(self.n)
                if self.n < 0:
                    raise ValueError("정수 (0 이상의 숫자)만 입력하세요.")
            except ValueError:
                continue
            # raise 사용시 반복문 강제 종료되기 때문에 try-except 구문으로 강제 종료 무시 후 continue
            
            if input_num < 4: # 
                self.print_factorial(input_num)
                continue

            
                

if __name__ == "__main__":
    a = start()
    a.tester()
    # main()
 