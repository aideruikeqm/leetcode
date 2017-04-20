'''
Question:
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    
  def lengthOfLongestSubstring(self, s):
        longest = ''
        substring = ''
        for i in range(len(s)):
            if s[i] in substring:
                substring = substring[substring.index(s[i])+1:]+s[i]
            else:
                substring += s[i]
                if len(substring)>len(longest):
                    longest = substring
        return len(longest)
   
   # Another Solution:
   '''
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
   '''
