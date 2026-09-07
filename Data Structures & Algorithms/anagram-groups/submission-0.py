class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
 
        groups = {}

        for word in strs:
            count = {}

            # Count frequency of each character
            for char in word:
                count[char] = count.get(char, 0) + 1

            # Convert frequency dictionary into a tuple
            key = tuple(sorted(count.items()))

            # Create group if key doesn't exist
            if key not in groups:
                groups[key] = []

            # Add word to its group
            groups[key].append(word)

        return list(groups.values())