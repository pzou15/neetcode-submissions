class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # brute force method
        # basically we would iterate twice (O(n^2))
        # i % 2 == 0 -> one path > < > < > < ..
        # i % 2 == 1 -> second path < > < > < ...
        # continue both invalid

        maxLen = 1
        for i in range(len(arr)):
            t1_len = 1
            t2_len = 1
            t1_stop = False
            t2_stop = False
            for j in range(i + 1, len(arr)):
                if not t1_stop:
                    if j % 2 == 0 and arr[j] < arr[j-1]:
                        t1_len += 1
                    elif j % 2 == 1 and arr[j] > arr[j-1]:
                        t1_len += 1
                    else:
                        t1_stop = True

                if not t2_stop:
                    if j % 2 == 0 and arr[j] > arr[j-1]:
                        t2_len += 1
                    elif j % 2 == 1 and arr[j] < arr[j-1]:
                        t2_len += 1
                    else:
                        t2_stop = True
                maxLen = max(t1_len, t2_len, maxLen)
                if t1_stop and t2_stop:
                    continue
                
                

                

        return maxLen
                