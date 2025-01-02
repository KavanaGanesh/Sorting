# Algorithm: Whole idea: Pick the pivot: the last element in the array
# partitioning the arraysuch that every value to the left of the pivot is less than or equal to the pivot and 
# every value to the right of the pivot is greater than the pivot
# then recursively run quicksort on left and right array until to reach the base case : until the length of the array is 1


# choose the pivot = which is the last element in the array
# write the base case: len(arr) should be less than or equal to 1
# Keep 2 pointers, 1st pointer iterating through the for loop and 
# 2nd pointer for storing the values to bring all the valuess less than the pivot one side and greater than the pivot to other side
# move the pivot between left and right side
# recursively run quicksort on left side
# recursively run quicksort on right side
class Solution:
    def quickSort(self, arr, start ,end):
        if end-start + 1 <=1 : #base case
            return arr

    
        pivot = arr[end]
        store = start
        # partition the elements smaller than the pivot to the left side
        for i in range(start, end):
            if arr[i] < pivot:
                temp = arr[store]
                arr[store] = arr[i]
                arr[i] = temp
                store = store + 1

        # bring the pivot inbettwen left and right sides
        arr[end] = arr[store]
        arr[store] = pivot


        # quicksort on the left and right side
        self.quickSort(arr, start, store-1)
        self.quickSort(arr, store+1, end)

        return arr

if '__name__ == __main__':
    # arr = [2,3,1,5,4]
    arr = [(3, "cat"), (2, "dog"), (3, "bird")]

    print(Solution().quickSort(arr, 0 , (len(arr)-1)))