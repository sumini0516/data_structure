# 사용자가 입력한 정보 관리
# 사용자가 이름과 이메일을 입력하면 이메일 순서대로 단순 연결 리스트를 생성하는 프로그램을 작성한다. 이름에서 그냥 ENTER를 누르면 입력을 종료한다.

# 클래스와 함수 선언 부분
class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=" ")
    while current.link != None:
        current = current.link
        print(current.data, end=" ")
    print()


def makeSimplyLinkedList(nameEmail):
    global memory, head, current, pre

    node = Node()
    node.data = nameEmail
    memory.append(node)
    if head == None:
        head = node
        return

    if head.data[1] > nameEmail[1]:
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > nameEmail[1]:
            pre.link = node
            node.link = current
            return

    current.link = node


# 전역변수 선언 부분
memory = []
head, current, pre = None, None, None
dataArray = ["amy", "betty", "cendy", "dori", "emile"]

# 메인코드부분
if __name__ == "__main__":
    while True:
        name = input("이름-->")
        if name == "" or name == None:
            printNodes(head)
            break
        email = input("이메일-->")
        makeSimplyLinkedList([name, email])
