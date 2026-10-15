class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return None

        maps = {}
        
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))

            if key not in maps:
                maps[key] = []

            maps[key].append(strs[i]) 

        
        return list(maps.values())


