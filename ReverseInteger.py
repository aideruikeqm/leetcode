'''
Question:
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. 
How should you handle such cases?
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution(object):
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strx = str(int(x))
        if x >= sys.maxint or x<-sys.maxint:
            return 0
        elif strx[0] == '-':
            if int('-'+(strx[1:])[::-1]) > -2147483647:
                return int('-'+(strx[1:])[::-1])
            else:
                return 0
        else:
            if int(strx[::-1]) < 2147483647:
                return int(strx[::-1])
            else:
                return 0    
'''
如果以最高位为符号位，二进制原码最大为0111111111111111=2的15次方减1=32767
最小为1111111111111111=-2的15次方减1=-32767
此时0有两种表示方法，即正0和负0：0000000000000000=1000000000000000=0
所以，二进制原码表示时，范围是-32767～-0和0～32767，因为有两个零的存在，所以不同的数值个数一共只有2的16次方减1个，
比16位二进制能够提供的2的16次方个编码少1个。
但是计算机中采用二进制补码存储数据，即正数编码不变，从0000000000000000到0111111111111111依旧表示0到32767，而负数需要把除符号位以后的部分取反加1，
即-32767的补码为1000000000000001。
到此，再来看原码的正0和负0：0000000000000000和1000000000000000，补码表示中，前者的补码还是0000000000000000，
后者经过非符号位取反加1后，同样变成了0000000000000000，也就是正0和负0在补码系统中的编码是一样的。但是，我们知道，16位二进制数可以表示2的16次方个编码，
而在补码中零的编码只有一个，也就是补码中会比原码多一个编码出来，这个编码就是1000000000000000，
因为任何一个原码都不可能在转成补码时变成1000000000000000。所以，人为规定1000000000000000这个补码编码为-32768。
所以，补码系统中，范围是-23768～32767。
因此，实际上，二进制的最小数确实是1111111111111111，只是二进制补码的最小值才是1000000000000000，而补码的1111111111111111是二进制值的-1。
'''
