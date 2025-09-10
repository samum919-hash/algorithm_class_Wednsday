# 괄호 검사 프로그램
from stack_class import ArrayStack # 같은 파일 내부에 있는 프로그램의 클래스 사용

# 조건 1 : 열린 괄호의 개수와 닫힌 괄호의 개수가 같아야 한다.
# 조건 2 : 같은 종류인 열린괄호가 닫힌괄호보다 먼저 나와야한다.
# 조건 3 : 다른 종류의 괄호 쌍이 서로 교차하면 안된다.

def checkBrackets(statement):
    # 열린괄호 - push / 닫힌괄호 - 스택의 top의 괄호와 짝이 맞는지 확인후 짝이 맞다면 pop >> LIFO 응용
    
    pairs = { ')':'(', ']':'[', '}':'{' }
    openings = set(pairs.values()) # paris의 value 값 ('(', '[', '{' ) 을 변수에 할당
    stack = ArrayStack(len(statement))
    
    for ch in statement: # 입력 문자열 순회
        if ch in openings:
            stack.push(ch)
            
        elif ch in pairs: # 닫힌괄호
            if stack.is_empty(): #조건 2 위반
                print("조건 2위반")
                return False
            if stack.peek() != pairs[ch]: # peek한 데이터가 괄호가 아니라면 실행 x / 조건 3 위반
                print("조건 3위반")
                return False
            stack.pop()
            
        else: # 괄호가 아니라면 무시
            pass
    
    return stack.is_empty() # True - 검사 성공 / False - 조건 1 위반
                
def test_Brackets():
    tests = [
        "{A[(i+1)]=0;}", # True
        "if ((x<0) && (y<3)", # False
        "while (n < 8)) {n++;}",    # False
        "arr[(i+1])=0;", # False 
    ]
    
    for i in tests:
        print(i, "->" , checkBrackets(i))

if __name__ == "__main__":
    test_Brackets()