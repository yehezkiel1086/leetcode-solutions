class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def gen_next(n):
            tt = 0
            while n > 0:
                tt += (n % 10) ** 2
                n //= 10
            return tt
        
        while n not in visit:
            visit.add(n)
            n = gen_next(n)
            if n == 1:
                return True

        return False