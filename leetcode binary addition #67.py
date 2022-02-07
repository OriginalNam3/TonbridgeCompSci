

class Solution():
    def addBinary(object, a: str, b: str) -> str:
        return str(bin(sum(int(a, 2), int(b, 2))))
