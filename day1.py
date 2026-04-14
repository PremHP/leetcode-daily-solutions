class Solution(object):
    def uniqueOccurrences(self, arr):
        dict = {}
        for num in arr:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        
        f_set = set()
        for count in dict.values():
            if count in f_set:
                return False
            f_set.add(count)
        
        return True

arr = [1,2,2,1,1,3]

obj = Solution()
res = obj.uniqueOccurrences(arr)

print(res)