# Algorithm:
# 1) loop for carrying out multiple passes
    # 2) keep iterating throught the length of the array - this is just one pass
        # 3) comapre the first and second, if first element is greater than the second:
        # 4) swap the element
# finally return the sorted array


# disadvantages = sometimes the array is already sorted - then we have to loop through all the elements for n-1 passes
# to overcome this we had to declare a boolean value after intializing the pass loop
# its a stable sorting algorithm - with a duplicate value its going tomaintain the relative position
# its am inplace sorting algo = O(1) - constant space complexity

class Solution():
    def bubblesort(self, arr):

        i = 0
        while i < len(arr):
            swapped = False
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                    swapped = True

            if not swapped:
                break
            i = i+1
        return arr



if '__name__==__main__':
    # arr = [2,1,3,6,4]
    arr = [39, 12, 18, 85, 72, 10, 2, 18]
    print(Solution().bubblesort(arr))