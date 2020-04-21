class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        [1,2,3,4,5]

        s1 = [1,2,3]   s2 =[3,2,1]
        Push to s1
        """
        self.s1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # s2 = [] --> push elements from s1 to s2
        # s1 = [], [1,2,3]

        if not self.s2:
            if not self.s1:
                return "Nothing to pop"
            else:
                #s1 has elements, need to push to s2
                while self.s1:
                    cn = self.s1.pop()
                    self.s2.append(cn)
            return self.s2.pop()
        else:
            #s2 already has elements
            return self.s2.pop()





    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2:
            return self.s2[-1]
        else:
            #s2 is empty
            #check if s1 isn't empty then push into s2
            if self.s1:
                #push s1 to s2
                while self.s1:
                    cn = self.s1.pop()
                    self.s2.append(cn)
                return self.s2[-1]
            else:
                #s1 and s2 is empty
                return "Queue is empty"



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not (self.s1 and self.s2):
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == '__main__':
    q = MyQueue()
    q.push(12)
    q.push(2)
    q.push(10)
    q.push(8)
    print(q.peek())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())