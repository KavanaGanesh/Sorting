# Algorithm: Insertion sort is stable sorting algorithm.
# Time complexity : O(n2) in worst case - thats when sorting is asked to done in reverse order
# For a already sorted array: complexity is O(n)

# Keep 2 pointers i,j but i starts from 1 till the length of the array. j starts one step behind i
    # now comapre j+1 and j value, if j+1 value is less than j swap the value.
    # decrement the value of j
# keep repeating the swap operation untill to maintain the sorting nature.



# Implemetation part:
# Input array = [2,3,1,5,4]

# case1: i=1, j=0, arr[j+1] < arr[j], no swap
# case2, i=2, j=1, arra[j+1] < arr[j],swap(3,1): so after swap [2,1,3,5,4]
#        i=2, j=0, arra[j+1] < arr[j],swap(2,1) : so after swap [1,2,3,5,4]
# case3: i=3, j=2, arra[j+1] < arr[j],no swap : [1,2,3,5,4]
# case4: i=4, j=3, arra[j+1] < arr[j], swap(5,4): so after swap [1,2,3,4,5]



class Solution:
    def insertionsort(self, arr):
        for i in range(1,len(arr)):
            j=i-1
            while (j>=0 and arr[j+1]<arr[j]):
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                j-=1
        return arr
    
arr = [2,3,1,5,4]
print(Solution().insertionsort(arr))
