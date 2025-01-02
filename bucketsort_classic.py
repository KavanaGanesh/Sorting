# Algorithm: Even in worst case = O(n)
# All the values fit within the finite range


# 1)count the value of the array and dump to the bucket based on the inp[ut numbers
# 2) once the count bucket is ready : iterate throught the bucket as many times as the value in the dump bucket
    # Take the value from the bucket and put it to the array


class Solution:
    def bucketSort(self, arr):
        # Assuiming array conatins only coount 0 , 1 , 2
        counts = [0,0,0]

        # count the value of the array and dump to the bucket
        for i in arr:
            counts[i] = counts[i] + 1
        # counts looks like this [2,1,3]

        n = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                arr[n] = i
                n = n+1
        return arr


if '__name__ == __main__':
    arr = [2,1,2,0,0,2]
    print(Solution().bucketSort(arr))