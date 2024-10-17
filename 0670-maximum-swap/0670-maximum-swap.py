class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num = [int(digit) for digit in str(num)]
        
        
        def solve(num):
            if not num:
                return num
            max_num = max(num)
            if max_num == num[0]:
                return [num[0]] + solve(num[1:])
            else:
                # get the last occurance index of max element - use index() on reversed list
                index = num[::-1].index(max_num) 
				
				# add 1 to the index so that we can use the index for negetive indexing on non reversed list while swapping
                index = index+1
				
                num[0], num[-index] = num[-index], num[0]
                return num
				
        return int(''.join(str(digit) for digit in solve(num)))