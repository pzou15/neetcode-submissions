class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        curSum = 0
        count = 0

        # initial window
        for i in range(k):
            curSum += arr[i]
        
        average = curSum / k
        if average >= threshold:
            count += 1

        for right in range(k, len(arr)):
            curSum -= arr[left]
            left += 1
            curSum += arr[right]
            average = curSum / k
            if average >= threshold:
                count += 1

        return count
