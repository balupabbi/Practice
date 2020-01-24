from DS_and_ALG.LinkedList import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.counter = 0

    #O(1)
    def insertStart(self, data):

        self.counter += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            #always make new inserted node head node for insertion to be O(1) and change pointer accordingly
            newNode.nextNode = self.head
            self.head = newNode

    #O(1) instead of O(N)
    def size(self):
        return self.counter

    def insertEnd(self,data):
        """
        Assuming LinkedList is filled with data
        :param data:
        :return:
        """
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove(self, data):

        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)


