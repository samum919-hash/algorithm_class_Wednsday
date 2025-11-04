# 과제 2 / 도서 관리 프로그램

# 단순 연결 리스트 자료구조를 활용
# 메뉴를 통해 도서 추가(append), 삭제(delete), 조회(diplay), 전체 목록 출력, 종료 
# 1. 책 번호, 제목, 저자, 출판 연도를 입력하면 도서를 연결 리스트에 추가
# 2. 책 제목을 기준으로 도서 삭제 / 번호가 존재하지 않으면 오류 출력
# 3. 책 제목으로 도서 조회 / 번호를 기준으로 제목, 저자, 출판 연도 순으로 출력
# 4. 전체 도서 목록 출력 / 현재 등록된 도서를 조회, 도서가 없으면 메시지 출력
# 5. 프로그램 종료




# 단순연결구조를 위한 Node 클래스
class Node():
    def __init__(self, element, link=None): # link = None > default data with link
        self.data = element # 노드의 data 정보
        self.link = link    # 노드의 link 정보

    # 노드 기반 삽입 연산
    def append(self, new_node):         # 현재 노드(self) 뒤에 주어진 노드(new_node)를 연결
        if new_node is not None:        # 새로운 노드가 link 되어있지 않아야 함
            new_node.link = self.link   # new_node 의 다음 노드는 현재(self) 노드의 다음 노들 수정
            self.link = new_node        # self의 다음 노드를 new_node로 수정
    
    # 노드 기반 삭제 연산
    def popNext(self): # 현재 노드(self)의 다음 노드를 삭제하고 해당 노드를 반환
        deleted = self.link # 삭제할 노드의 다음 노드
        if deleted is not None:
            self.link = deleted.link
            deleted.link = None
        return deleted
 
class LinkedList:
    def __init__(self):
        self.head = None # 비어있는 리스트의 초기상태
    
    # 주요 기본 연산자
    def is_empty(self): # 리스트가 비어있는지 확인
        return self.head == None
    
    def getNode(self, pos): # pos 위치에 있는 노드 반환(출력)
        # pos는 리스트 index 0부터 고려
        if pos < 0: return None # pos는 0부터 시작해야하므로 음수 pos는 존재할 수 없음
        if self.is_empty(): # 리스트가 빈 상태
            return None
        else:
            ptr = self.head
            for _ in range(pos):
                if ptr == None: # pos가 리스트 크기보다 큰 경우
                    return None
                else:
                    ptr = ptr.link
            return ptr
    
    def getEntry(self, pos): # 리스트의 pos위치에 있는 노드를 찾아 데이터값을 반환
        node = self.getNode(pos) # 1. 해당 위치의 노드를 탐색
        if node == None: return None # 해당 노드가 없는 경우
        else: # 해당 노드가 있는 경우
            return node.data
            
    def insert(self, elem, pos = 0): # index 기반 연산 / pos 값 입력 없을 시 첫 번째 위치에 elm 삽입
        # pos 위치에서 새 노드 삽입
        if pos < 0: raise ValueError("잘못된 위치 값 입력")
        
        new = Node(elem) # 1. create new node
        before = self.getNode(pos - 1) # 2. pos -1 위치의 노드 탐색
        # 3. before 노드의 위치에 따라 구분
        if before is None:
            if pos == 0: # 1) insert head node
                new.link = self.head
                self.head = new
                return
            else: # 2) pos가 리스트 범위에서 벗어난 경우
                raise IndexError("삽입할 위치가 유효하지 않음")
        else: # 3) 중간 노드로 삽입
            before.append(new)

    def delete(self, pos): # index 기반 연산
        # pos 위치에서 해당 노드 삭제 연산 / 삭제 후 해당 값 반환
        if pos < 0: raise ValueError("잘못된 위치 값 입력")
        
        before = self.getNode(pos -1) # 1. 삭제할 노드 이전의 노드 탐색
        # 2. before 노드의 위치에 따라 구분 
        if before == None:
            if pos == 0: # 1) delete head node
                deleted = self.head
                self.head = deleted.link
                deleted.link = None
                return deleted
            else: # 2) pos가 리스트 범위에서 벗어난 경우
                raise IndexError("삽입할 위치가 유효하지 않음")
        else: # 3) 중간 노드 삭제
            return before.popNext()

    def size(self):
        if self.head == None: return 0 # 현재 리스트가 공백일때
        else:
            ptr = self.head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.link
            return count
    
    def display(self, msg="Linked List : "):
        # 리스트의 내용 출력
        print(msg, end=' ')
        if self.head == None: return None # 현재 리스트가 공백일때
        else:
            ptr = self.head
            count = 0
            while ptr is not None:
                print(ptr.data, end = " -> ")
                ptr = ptr.link
            print("None")
    
    def replace(self, pos, elem): # 인덱스 기반 연산
        # 리스트의 pos 위치에 있는 노드의 데이터 값 수정
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            node.data = elem
            
    def find_by_title(self, title): # 책 제목으로 리스트에서 도서 찾기
        for pos in range(self.size()):
            if self.getEntry(pos) == title:
                return True # 도서가 리스트에 있을 시 True
        return False # 없을 시 False
        
    def find_pos_by_title(self, title): # 책 제목으로 리스트에서 도서 위치 찾기
        for pos in range(self.size()):
            if self.getEntry(pos) == title:
                return pos
        return None
        
        

class Book(): # 도서 객체의 정보를 저장
    def __init__(self , book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        
    def Print_Book(self):
        print(f"[책 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]")

class BookManagement(): # 도서 객체의 정보를 저장하는 클래스 / 순서대로 도서 번호, 제목, 저자, 출판 연도
    def __init__(self):
        self.total_list = LinkedList()
    
    def Error_print(self): print("해당 도서의 정보가 존재 하지 않습니다.")
    
    def add_book(self, book_id, title, author, year):  # 리스트에 도서 추가
        title_key = title+"_total"
        book_obj = Book(book_id, title, author, year) # Book 리스트를 따로 생성해 도서정보추가
        self.total_list.insert(title_key)             # total_list에 책 제목 추가   pos = 1
        self.total_list.insert(book_obj)              # 도서 정보(Book()객체) 추가  pos = 0

        
    def remove_book(self, title): # 주어진 책 제목에 해당하는 도서 리스트에서 삭제
        title_key = title+"_total"
        if self.total_list.find_by_title(title_key): # total 리스트에 주어진 title이 있는지 확인
            pos = self.total_list.find_pos_by_title(title_key) - 1
            # total_list에 저장된 객체 모두 삭제
            for _ in range(2):
                self.total_list.delete(pos)
        else:   self.Error_print()
            
    def search_book(self, title): # 주어진 도서의 정보를 리스트에서 찾아 출력
        title_key = title+"_total"
        if self.total_list.find_by_title(title_key):
            pos = self.total_list.find_pos_by_title(title_key) # 입력받은 정보의 id가 삽입된 pos
            if pos == None:
                self.Error_print()
            else :
                book_node = self.total_list.getNode(pos-1) # Book으로 생성된 리스트 정보 출력
                if book_node == None: self.Error_print()
                else:
                    book_obj = book_node.data
                    book_obj.Print_Book()
                             
        else:   self.Error_print()
            
        
    def display_books(self): # 리스트에 등록된 모든 도서 출력
        if self.total_list.head == None:
            print("리스트가 비어있습니다.")
        else:
            size = int(max(1, self.total_list.size() / 2)) # 책 제목의 개수
            for i in range(size):
                pos = i * 2 # book의 정보가 담긴 pos
                book_obj = self.total_list.getEntry(pos)
                book_obj.Print_Book()
        
        
    def run(self): # 메뉴에서 선택한 작업 수행
        book_list = BookManagement()
        while 1:
            print('='*3, " 도서 관리 프로그램 ", '='*3)
            print(" 1. 도서 추가\n",
                  "2. 도서 삭제 (책 제목으로 삭제)\n",
                  "3. 도서 조회 (책 제목으로 조회)\n",
                  "4. 전자 도서 목록 출력\n",
                  "5. 종료")            
            try:
                input_menu = input("메뉴를 선택 하세요 : ")
                input_menu = int(input_menu)
                if input_menu > 5 or input_menu <= 0:
                    raise ValueError("1~5 의 정수로 입력하세요.")
            except ValueError:
                print("1~5 의 정수로 입력하세요.")
                continue
            
            if input_menu == 5:
                print("종료하겠습니다")
                break
            
            if input_menu == 1:
                try:
                    input_book_id = input("책 번호 입력 : ")
                    input_book_title = input("책 제목 입력 : ")
                    input_book_author = input("저자 입력 : ")
                    input_book_year = input("출판 연도 입력 : ")
                    
                    input_book_year = int(input_book_year)
                    input_book_id = int(input_book_id)
                except ValueError:
                    print("책 번호나 연도를 정수로 입력하세요")
                    continue
                book_list.add_book(input_book_id, input_book_title, input_book_author, input_book_year)
                print(f"도서 '{input_book_title}'가 추가되었습니다.")
                continue
            
            if input_menu == 2:
                del_title = input("삭제할 책 제목 입력 : ")
                book_list.remove_book(del_title)
                print(f"책 제목 '{del_title}'의 도서가 삭제되었습니다.")
                continue
            
            if input_menu == 3:
                res_title = input("조회할 책 제목 입력 : ")
                book_list.search_book(res_title)
                continue
            
            if input_menu == 4:
                print("현재 등록된 도서 목록:")
                book_list.display_books()
                continue

if __name__ == "__main__":
    a = BookManagement()
    a.run()