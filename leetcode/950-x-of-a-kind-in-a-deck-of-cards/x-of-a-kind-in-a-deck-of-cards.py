class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        rep = Counter(deck)      
        gd = gcd(*rep.values())
        if gd >=2:
            return True
        else:
            return False
        