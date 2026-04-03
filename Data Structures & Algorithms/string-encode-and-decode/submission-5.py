class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
        

    def decode(self, s: str) -> List[str]:
        pos = 0
        n = len(s)
        chunks = []
        while pos < n:
            length = ""
            while True:
                c = s[pos]
                pos += 1
                if c == "#":
                    length = int(length)
                    break
                length += c
            chunk = s[pos: pos + length]
            chunks.append(chunk)
            pos = pos + length
        return chunks
            
