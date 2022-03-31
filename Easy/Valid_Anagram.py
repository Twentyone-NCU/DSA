class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # base case --> different length
        if len(s) != len(t):
            return False
        
        # Create corresponding hast table
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)


        for c in countS:
            if countS[c] != countT.get(c, 0): # 避免不存在時錯誤發生
                return False
        
        return True

# Second way
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Third way: Reduce space complexity --> compare after sorted
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)