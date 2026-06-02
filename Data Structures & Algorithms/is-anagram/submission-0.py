def stringToHash(s: str) -> dict:
    hashmap = {}
    for c in s:
        if c not in hashmap:
            hashmap[c] = 1
        elif c in hashmap:
            hashmap[c] += 1
    
    return hashmap


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_1 = stringToHash(s)
        hashmap_2 = stringToHash(t)

        if hashmap_1 == hashmap_2:
            return True
        
        return False

