class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        counter = 0

        x = 0
        for x in range(n):
            c = a + b
            counter+=1
            a = b
            b = c

        print("Output: ",x)
        print("There are total ",counter," Ways to climb to top")
        
        x = 0
        for x in range(n):
            