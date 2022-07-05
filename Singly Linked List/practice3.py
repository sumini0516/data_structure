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


def findNode(findData):
    global memory, head, current, pre

    current = head
    if current.data == findData:
        return current

    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
        return Node()


# 전역변수 선언 부분
memory = []
head, current, pre = None, None, None
dataArray = ["amy", "betty", "cendy", "dori", "emile"]

# 메인코드부분
if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

    fNode = findNode("amy")
    print(fNode.data)

    fNode = findNode("betty")
    print(fNode.data)

    fNode = findNode("flora")
    print(fNode.data)