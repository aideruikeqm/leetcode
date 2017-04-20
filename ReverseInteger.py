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
后者经过非符号位取反加1后，同样变成了0000000000000000，也就是正0和负0在补码系统中的编码是一样的。
但是，我们知道，16位二进制数可以表示2的16次方个编码，
而在补码中零的编码只有一个，也就是补码中会比原码多一个编码出来，这个编码就是1000000000000000，
因为任何一个原码都不可能在转成补码时变成1000000000000000。所以，人为规定1000000000000000这个补码编码为-32768。
所以，补码系统中，范围是-23768～32767。
因此，实际上，二进制的最小数确实是1111111111111111，只是二进制补码的最小值才是1000000000000000，而补码的1111111111111111是二进制值的-1。
在表示有符号数时，如果用最高位来表示符号，而用除了最高位之外的其他位来表示数字部分，就会出现“正零”和“负零”的问题。
如在32位的系统中，两个二进制数如下所示：
00000000 00000000 00000000 00000000=+00=0  
10000000 00000000 00000000 00000000=-0=0 
这个看似不大的问题，却会导致很多严重的问题，如判断上述两个值是否相等，如果仅仅是用相等（C语言中的运算符为“==”）判断，
同样表示0，则本来应该相等的值，判断结果却是不相等；再如，按“异或”操作的规定，两个相同的数，异或的结果应该是0，但却因为最高位不相同，
而使得两个0的异或结果不为零。
为了解决这一问题，计算机中的数据表示采用的是补码（Two’s Complement）表示法，即在表示有符号数的时候，采用的方式是：
如果该数是正数，则最高位为0，其余位为该数；如果是负数，则最高位为1，其余位为“2的位数次方+该数”。
比如，如果用1个字节表示，+73的表示方法为“01001001”，其中第1个0表示正号，后面边的“1001001表示为73的二进制表示。
而-73则表示为“10110111”，其中第1个1表示负号，后面的“10110111”是“2的8次方+（-73）”=183。
！！！所以与2的8次方的插值即为应有负值！！！
如果用4个字节表示，+73的表示方法为：“00000000 00000000 00000000 01001001”，
其中第1个0表示正号，后面边的“0000000 00000000 00000000 01001001”表示为73的二进制表示。
而-73则表示为“11111111 11111111 11111111 10110111”，其中第1个1表示负号，
后面的“1111111 11111111 11111111 10110111”是“2的32次方+（-73）”=4294967223。
与“求和”算法将所有数都当成正数不同的是，“补码求和”运算根据补码的规则判断数据的正负，但算法没有什么不同，所以代码也差异不大。
还有一种改进型的补码求和算法，又称“双补码算法”，该算法与求和算法相似的，所不同的是，对于单字节的校验，校验和是用256减去所求的和，
并作为最终的结果，从而避免了上述问题。
'''
