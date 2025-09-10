# stack_class
# array로 구현한 stack 클래스
# is_empty(), in_full(), push(), pop(), peek(), size()

class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [None]*self.capacity
        
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1
    
    def push(self, item):
        if not self.is_full():
            self.array[++self.top] = item
            print("PUSH : {item!r} -> stack = {self.array[:self.top + 1]}")
        else:
            # print("Stack Overflow")
            # exit()
            raise OverflowError("Stack Overflow") # 위 내용을 한번에 출력하도록 도와주는 에러문
    
    def pop(self):
        if not self.is_empty():
            item = self.array[self.top]
            self.array[self.top] = None
            --self.top
            print("POP : {item!r} -> stack = {self.array[:self.top + 1]}")
            return item
        else:
            raise IndexError("Stack Underflow")
        
    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        else:
            None
            
    def size(self):
        return self.top + 1
    
# stack 클래스를 이용해 문자열을 거꾸로 뒤집어 출력
    
def Reverse_string(statement):
    print("\n[1] PUSH 단계 -----------")
    st = ArrayStack(len(statement))
    for ch in statement:
        st.pop(ch)
    
    print("\n[2] POP 단계 -----------")
    out = []
    while not st.is_empty():
        result.append(st.pop())
    
    result = ''.join(out)
    
    print(f"\n[3] 최종 결과 : {result}")
    return result


# test

def test_reverse():
    tests = ["기러기", "Hellow I'm Stack", "012345"]
    
    for i in tests:
        Reverse_string(tests[i])
    
