class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        output = []
        strs_sorted = []
        for i in strs:
            strs_sorted.append(''.join(sorted(i)))
        for i in range(len(strs_sorted)):
            if strs_sorted[i] in hm:
                hm[strs_sorted[i]].append(strs[i])
            else:
                hm[strs_sorted[i]] = [strs[i]]
        for i in hm:
            output.append(hm[i])
        return output