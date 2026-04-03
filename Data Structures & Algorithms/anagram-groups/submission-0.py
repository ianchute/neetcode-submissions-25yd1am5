class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            k = str(sorted(s))
            if k in result:
                result[k].append(s)
            else:
                result[k] = [s]
        return list(result.values())