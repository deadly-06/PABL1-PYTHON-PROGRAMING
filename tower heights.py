class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()

        ans = arr[n - 1] - arr[0]

        smallest = arr[0] + k
        largest = arr[n - 1] - k

        for i in range(n - 1):
            min_height = min(smallest, arr[i + 1] - k)
            max_height = max(largest, arr[i] + k)

            if min_height < 0:
                continue

            ans = min(ans, max_height - min_height)

        return ans
