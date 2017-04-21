'''
Question:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example:
Input: "cbbd"
Output: "bb"
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Dynamic Programming:
        n = len(s)
        sub = ''
        du = [[0]*n  for i in range(n)]
        for i in xrange(n-1,-1,-1):
            for j in xrange(i, n): 
                du[i][j] = ( (s[i]==s[j]) and  ( j-i< 3 or du[i+1][j-1] ) )
                if du[i][j] == 1 and (j-i+1) > len(sub):
                    sub = s[i:j+1]
        return sub
    
    # Another Solution:
    '''
    def longestPalindrome(self, s):
        res = ""
        for i in xrange(len(s)):
            for k in xrange(2):
            # odd case, like "aba"
                tmp = self.helper(s, i, i+k)
                if len(tmp) > len(res):
                    res = tmp
        return res
 
    # Get the longest palindrome, l, r are the middle indexes   
    # From inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
        '''
