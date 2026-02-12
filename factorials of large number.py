class Solution:
    def factorial(self, n):
        result = [1]
        
        for x in range(2, n + 1):
            carry = 0
            for i in range(len(result)):
                prod = result[i] * x + carry
                result[i] = prod % 10
                carry = prod // 10
            
            while carry:
                result.append(carry % 10)
                carry //= 10
        
        return result[::-1]
