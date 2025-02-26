'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
 and return an array of the non-overlapping intervals that cover all the intervals in the input.'''


'''Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6]'''


# Algorithm:
# 1. Sort the intervals on the first parameter : output of this will be: [[1,3], [2,6], [8,10], [15,18]]
# 2. create an empty result with the first list of elements already present in it : result = intervals[0] --> ([[1,3]])
# 3. iterate through the loop, since it is the list of list: keep 2 variable for list unpacking
    # 4. now compare the start > last element in the result list
        # 5. if yes append the start and end to the resuult list
        # 6. if not, end element of result should be updated with the max(end and end element of the result list)
# 7. finally return the result list.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]


        for start, end in intervals[1:]:
            if start > result[-1][1]:
                result.append([start, end])
            else:
                result[-1][1] = max(end, result[-1][1])
        return result


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))