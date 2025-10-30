class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Split the string into words and take the last one
        words = s.strip().split(" ")
        return len(words[-1])

# Example usage
s = "Hello World"
obj = Solution()
print(obj.lengthOfLastWord(s))  # Output: 5
