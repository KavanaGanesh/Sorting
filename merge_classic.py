# Algorithm:Divide and then conquer
# Divide the given array into 2 subparts by finding the mid recursively untill the length of the array becomes 1
    #  For dividing: we solve it by recursion
# For merging: we use below technique
    # 1) Divide the array into 2 parts: left subarray and right subarray
    # 2) Keep 3 pointer, pti for left subarray, ptr j for right subarray, ptr k for entire array to merge
        # 3) if ith element is less than jth element, add the ith element to array at kth position: increment i and increment k
        # 4) if jth element is less than the ith element, add the jth element to array at the kth psoition: icrement j and increment k
        # 5) what in case if left subarray is empty : then just add the right subarray at the kth position
        # 6) what incase if right subarray is empty :  then just add the left subarray at the kth position

# Finally return ther merged array



class Solution:
    def mergesort(self, arr, start, end):
        if end - start + 1 <= 1:
            return arr
        
        mid = (start + end)//2
        self.mergesort(arr, start, mid)
        self.mergesort(arr, mid+1, end)

        self.merge(arr, start, mid, end)

        return arr
    
    def merge(self, arr, start, mid, end):
        i=0
        j=0
        k=start

        left_array = arr[start:mid+1]
        right_array = arr[mid+1:end+1]

        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                arr[k] = left_array[i]
                i=i+1
            else:
                arr[k] = right_array[j]
                j = j+1
            k = k+1

        while i < len(left_array):
            arr[k] = left_array[i]
            i = i+1
            k = k+1

        while j < len(right_array) :
            arr[k] = right_array[j]
            j = j+1
            k = k+1


if '__name__ == __main__':
    # arr = [3,2,4,1,6]
    arr = [(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]
    print(Solution().mergesort(arr, 0, len(arr)-1))



# We have a base case where if the length of the array is less than or equal to 1 we return the array because it is already sorted.
# Otherwise we calculate the middle index of the array.
# We recursively call mergeSort() on the left half of the array. We do this by passing pointers s and m to the function, which in this case represent the start and end of the left half of the array.
# We recursively call mergeSort() on the right half of the array. We do this by passing pointers m + 1 and e to the function, which in this case represent the start and end of the right half of the array.
# We merge the two sorted halves by calling the merge() function, which is discussed more below.
