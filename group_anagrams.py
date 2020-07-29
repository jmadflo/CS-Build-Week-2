class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_strs = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in sorted_strs:
                sorted_strs[key].append(s)
            else:
                sorted_strs[key] = [s]
        return sorted_strs.values()