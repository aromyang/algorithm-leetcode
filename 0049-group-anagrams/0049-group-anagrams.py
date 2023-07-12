class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in strs_dict:
                strs_dict[sorted_s] = [s]
            else:
                strs_dict[sorted_s].append(s)
                        
        return list(strs_dict.values())