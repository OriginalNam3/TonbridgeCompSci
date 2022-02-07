class Solution:
    def reverse(Reverse, x, self) -> int:
        x = int(input("please input number"))
        Reverse = 0
        while (x > 0):
            Reminder = x % 10
            Reverse = (Reverse * 10) + Reminder
            x = x // 10
        print(Reverse)
