#Reference: https://www.youtube.com/watch?v=D_svLpIzczY
#Heap Reference: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

import heapq

def max_meetingrooms(arr):
    #Base case
    if arr is None or len(arr)==0:
        return 0

    #Sort based on first element
    arr.sort(key=lambda x: x[0])

    #Create rooms min heap
    rooms = [arr[0][1]]

    #Skip first meeting since it is already added to the rooms
    for meeting in arr[1:]:
        current_starttime = meeting[0] #start time of current meeting
        current_endtime = meeting[1]

        if rooms[0] <= current_starttime:
            heapq.heappop(rooms)

        heapq.heappush(rooms,current_endtime)


    return len(rooms)



    print('hello')


if __name__ == "__main__":

    arr=[[0,30],[5,10],[15,20]]

    print(max_meetingrooms(arr))

