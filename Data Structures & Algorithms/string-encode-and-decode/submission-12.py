class Solution:

    def encode(self, strs: List[str]) -> str:
        output =""
        for s in strs:
            output += str(len(s)) + '#' + s # encodes with string length and some character e.g. 5#hello
        return output


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#': # moves j pointer
                j +=1
            length = int(s[i:j]) # uses slice to get length of string
            i = j + 1 # moves i pointer to start of string
            j = i + length # moves j pointer to end of string
            output.append(s[i:j]) # append string
            i = j # move i pointer to new string

        return output