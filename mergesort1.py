from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums, L, M, R):
            left, right  = nums[L:M+1], nums[M+1: R+1]
            i, j, k = L, 0, 0
            
            while j<len(left) and k<len(right):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j+=1
                else:
                    nums[i] = right[k]
                    k+=1
                i+=1

            while j<len(left):
                nums[i] = left[j]
                j+=1
                i+=1

            while k<len(right):
                nums[i] = right[k]
                k+=1
                i+=1


        def mergesort(nums, l, r):
            if l == r:
                return nums
            
            m = (l + r)//2
            mergesort(nums, l, m)
            mergesort(nums, m+1, r)
            merge(nums, l, m, r)
            return nums
        
        return mergesort(nums, 0, len(nums)-1)

nums = [5,2,3,1]
# nums = [5,1,1,2,0,0]
print(Solution().sortArray(nums))