class Solution(object):
    def isPalindrome_appraoch_1(self, x:int):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)[::-1]
        if str_x == str(x):
            return True 
        else:
            return False

    def isPalindrome_appraoch_2(self, x:int):
        """
        better in time complexity
        :type x: int
        :rtype: bool
        """
        x_orig = x
        reversed_num = 0
        while x >0:
            digit = x%10
            reversed_num = reversed_num*10 + digit
            x = x//10
        return reversed_num == x_orig

if __name__ == "__main__":
    case_1 = Solution().isPalindrome_appraoch_2(x=121)
    print(f"Case 1: {case_1}")
    case_2 = Solution().isPalindrome_appraoch_2(x=-121)
    print(f"Case 2: {case_2}")
    case_3 = Solution().isPalindrome_appraoch_2(x=10)
    print(f"Case 3: {case_3}")