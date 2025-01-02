from typing import List


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
#         nums1 = list(filter(lambda x : x!=0, nums1))
#         nums2 = list(filter(lambda x : x!=0, nums2))

#         sorted_list = sorted(nums1+nums2)
#         return sorted_list





# nums1 = [1,2,3,0,0,0]
# m = 3 
# nums2 = [2,5,6]
# n = 3
# # Output: [1,2,2,3,5,6]
# # nums1 = [1], m = 1, nums2 = [], n = 0, Output: [1]
# # nums1 = [0], m = 0, nums2 = [1], n = 1, Output: [1]
# print(Solution().merge(nums1, m, nums2, n))


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        # Do not return anything, modify nums1 in-place instead.
        # """
        nums1 = list(filter(lambda x : x!=0, nums1)) # this lambda didnt pass other test cases

        for i in range(len(nums1)-m):
            nums1.remove(0)
        print(nums1)

        for i in nums2:
            nums1.append(i)
            print(nums1,'result')
        nums1.sort() # remember list.sort() doesnot return the list insetad it sorts inplace




# nums1 = [1,2,3,0,0,0]
# m = 3 
# nums2 = [2,5,6]
# n = 3
# Output: [1,2,2,3,5,6]
# nums1 = [1], m = 1, nums2 = [], n = 0, Output: [1]
nums1 = [0]
m = 0 
nums2 = [1]
n = 1
# Output: [1]
print(Solution().merge(nums1, m, nums2, n))
