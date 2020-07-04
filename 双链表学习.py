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
        if self.is_empty():
            # 如果是空链表，将node赋值给_head
            self._head = node
        else:
            # 将node的next属性指向头结点_head
            node.next = self._head
            # 将头结点_head的prev属性指向node
            self._head.prev = node
            # 将node赋值给_head
            self._head = node

    def append(self,item):
        # 尾部插入元素
        node = Node(item)
        if self.is_empty():
            # 如果是空列表，将node赋值给_head
            self._head = node
        else:
            # 循环移动到链表尾部结点的位置
            cur = self._head
            while cur.next != None:
                cur = cur.next
            # 将尾结点cur的next属性指向node
            cur.next = node
            # 将node的prev属性指向cur
            node.prev = cur

    def insert(self,pos,item):
        # 在指定位置插入元素
        if pos <= 0:
            self.add(item)
        elif pos >=(self.get_length()):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            # 将node的prev属性指向cur
            node.prev = cur
            # 将node的next属性指向cur的下一个结点
            node.item = cur.next
            # 将node下一个结点的pre属性指向node
            cur.item.prev = node
            # 将cur的next指向node
            cur.next = node

    def remove(self,item):
        # 删除链表中的元素
        if self.is_empty():
            return 
        else:
            cur = self._head
            if cur.item == item:
                # 如果首结点是要删除的值
                if cur.next == None:
                    # 如果链表只有一个结点，删除将首结点置为None即可
                    self._head = None
                else:
                    # 将cur的下一个结点置为首结点
                    self._head = cur.next
                    # 将下一个结点的prev属性置为None
                    cur.next.prev = None
                return
            while cur:
                # 遍历链表找到item值
                if cur.item == item:
                    # 当cur的值为要删除的值时，执行删除操作
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                    break
                cur.next