from collections import deque


# https://nifannn.github.io/2018/10/01/Algorithm-Notes-Leetcode-346-Moving-Average-from-Data-Stream/#python-implementation
# https://github.com/yuzhoujr/leetcode/blob/master/stack_queue/movingAverage.py

class MovingAverage:
    def __init__(self, maxsize):
        self.wsize = 0
        self.maxsize = maxsize
        self.wsum = 0
        self.average = 0
        self.clist = deque()

    def next(self,item):
        """
        Appends to clist for a given wsize
        :return:
        """
        if not self.clist or len(self.clist)<self.maxsize:
            self.clist.append(item)
            self.wsize = len(self.clist)
        else:
            self.clist.popleft()
            if len(self.clist) > self.maxsize:
                print('Something fishy with size')
            else:
                self.clist.append(item)
                self.wsize = len(self.clist)

    def get_average(self):
        """
        gets average
        :return:
        """
        if self.wsize != 0:
            self.average = self._getsum()/self.wsize
        else:
            return "Error Window size is 0"

        return self.average

    def _getsum(self):
        self.wsum = sum(self.clist)
        return self.wsum




if __name__ == '__main__':
    m = MovingAverage(3)
    m.next(2)
    m.next(2)
    m.next(4)
    # m.next(5)

    print(m.clist)
    print(m.get_average())
