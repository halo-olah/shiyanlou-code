"""
单链表学习内容
"""


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

    # 添加一个insert函数，可以往链表的任意位置添加一个new_element元素
    def insert(self,position,new_element):
        """
        流程：
        1. 先判断要插入的位置是否在链表的索引范围之内
        2. 当插入的结点是头结点时(position=0)，做特殊情况处理
        3. 当要插入结点的位置不在0时，找到要插入的位置，插入新结点
        """
        if position < 0 or position > self.get_length():
            raise IndexError("key 超出范围，无法insert")
        temp = self.head
        if position == 0:
            # 将插入元素的next属性指向旧的头结点，并将新的元素赋值给头结点
            new_element.next = temp
            self.head = new_element
            # new_element , self.append = temp , new_element
            return
        
        i = 0
        # 遍历找到索引值为position的结点后，在其后面插入结点
        while i < position:
            pre = temp
            temp = temp.next
            # pre , temp = temp , temp.next
            i += 1
        pre.next = new_element
        new_element.next = temp

    # 添加一个remove函数，remove()可以从链表任意一个位置删除元素
    def remove(self,position):
        """
        1. 先判断要删除的元素是否存在，不存在则抛出异常
        2. 判断存在链表元素时，才能执行删除操作
        3. 当要删除的是头结点时(position=0)，做特殊情况处理
        4. 其他情况时，通过循环找到要删除的结点，执行删除操作
        """
        if position < 0 or position > self.get_length():
            raise IndexError("元素索引超出异常")

        i = 0
        temp = self.head
        # 当存在列表元素时，才能进行删除操作
        while temp:
            # 将头结点的后一个结点赋值给新的头结点，然后将头结点指向'None'
            if position == 0:
                self.head = temp.next
                temp.next = None
                return

            pre = temp
            # 以此来遍历链表
            temp = temp.next
            i += 1
            if i == position:
                # 将pre的next属性指向temp的下一个结点
                pre.next = temp.next
                temp.next = None
                return

    # 定义一个get_length函数，用来返回链表长度
    def get_length(self):
        # 头部结点赋值给temp
        temp = self.head
        # 计算链表的长度变量
        length = 0
        while temp:
            length += 1
            temp = temp.next
        # 返回链表长度
        return length

    # 定义print_list函数，用来输出链表元素值
    def print_list(self):
        # print("linken_list:")
        # 头部结点赋值给临时变量temp
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # 定义reverse函数，用来反转链表
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            ccurrent = next_node
        self.head = prev

    # 定义initlist函数，用于将列表转化为链表
    def initlist(self,data_list):
        # 创建头结点
        self.head = Node(data_list[0])
        temp = self.head
        # 逐个为data内的数据创建结点，建立链表
        for i in data_list:
            node = Node(i)
            temp.next = node
            temp = temp.next


# 定义一个交换链表链点的方法：
def swap_nodes():
    """
    1. 生成链表
    2. 遍历链表，确认d1,d2元素在链表中，并且返回元素的链点值
    3. 插入两个元素分别插入至对方的链点位置
    """
    list1 = [1,2,3,4,5]
    link_list = Link_List.initlist(list1)
    print(link_list)
    #i = 0
    


if __name__ == "__main__":
    swap_nodes()