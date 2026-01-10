class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {")":"(", "}":"{", "]":"["}

        for x in s:
            if x in hash.values():
                stack.append(x)
            elif x in hash.keys():
                if not stack or hash[x] != stack.pop():
                    return False
        return not stack