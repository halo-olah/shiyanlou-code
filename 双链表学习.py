class Node(object):
    # 双向链表节点
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkedList(obeject):
    # 双向链表
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def get_length(self):
        cur =self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历链表
        cur = self.head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")

    def add(self,item):
        # 头部加入元素
        node = Node(item)