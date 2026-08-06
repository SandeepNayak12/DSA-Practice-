class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(n):
            pr = 1
            while n > 0:
                rem = n%10
                pr*=rem
                n=n//10
            return pr
        i = n
        while True:
            pr = prod(i)
            if pr%t ==0:
                return i
            else:
                i+=1
            