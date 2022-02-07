

class Solution():
    def addBinary(object, a: str, b: str) -> str:
        x = 1
        y = 1
        while x==1:

            a = a.replace('"', '')
            b = b.replace('"', '')
            a1 = int(a, 2)
            b1 = int(b, 2)
            sum = a1 + b1

            sum1 = format(sum, "b")

            return(sum1)
            y = y+1
            if y == 3:
                x = 2
