class Solution:
    def addDigits(self, num: int) -> int:
        num=str(num)
        sum_of=0
        while len(num)>1:
            for i in num:
                sum_of=sum_of+int(i)
            num=str(sum_of)
            sum_of=0
        return num

s=Solution()
int1=38
print(s.addDigits(int1))        