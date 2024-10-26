class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''
        [5,6,7]
        5&6&7=(5)
        '''
        while right>left:
            right=right & (right-1)
        return right