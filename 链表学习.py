class Node:
    # 创建一个链表类

    def __init__(self,data):
        self.data = data # 表示对应的元素值
        self.next = None # 表示下一个链接的链点


class Link_List:

    def __init__(self,head=None): # 链表初始化函数
        self.head = head # 表示链表的头部元素

    # 添加append函数，功能是向链表添加新的结点
    def append(self,new_element):
        # 将头部结点指向临时变量 current
        current = self.head
        # 当头部结点存在时
        if self.head:
            # 循环遍历到链表的最后一个元素
            while current.next:
                current = current.next
            current.next = new_element
        # 当头部结点不存在时
        else:
            self.head = new_element

    # 添加一个is_empty函数，判断链表是否为空
    def is_empty(self):
        return not self.head
