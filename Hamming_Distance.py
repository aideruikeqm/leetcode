class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #one line code:
        return bin(x^y).count('1')
        
        #another solution:
        '''
        res = 0
        for c in str(bin(x ^ y)):
            if c == '1':
                res += 1

        return res
        '''
