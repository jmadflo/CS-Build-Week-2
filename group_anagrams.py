class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_strings = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in sorted_strings:
                sorted_strings[key].append(s)
            else:
                sorted_strings[key] = [s]
        return sorted_strings.values()