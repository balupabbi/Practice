





#
# l+(r-l)/2 = 0+1.5 = 1
# [0,1,2,3,4] = 0+2
#
#
# [0,1,2,3]  l=4 even--> mid=4/2=2

def findMedian(nums):

    nums.sort()

    l = 0
    r = len(nums)-1
    mid = l+(r-l)//2

    if len(nums) % 2 == 0:
        med = (nums[mid]+nums[mid+1])/2
    elif len(nums) % 2 ==1:
        med = nums[mid]

    return med




if __name__ == '__main__':
    nums = [3,2,4,5,6,11]

    print(findMedian(nums))
