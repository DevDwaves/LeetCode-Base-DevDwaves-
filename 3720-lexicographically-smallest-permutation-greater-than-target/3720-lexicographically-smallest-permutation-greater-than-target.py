class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        # Count characters in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        n = len(target)
        matched = 0

        # Match target as far as possible
        while matched < n:
            x = ord(target[matched]) - ord('a')

            if count[x] == 0:
                break

            count[x] -= 1
            matched += 1

        # Try to increase the first unmatched position
        if matched < n:
            x = ord(target[matched]) - ord('a')

            for c in range(x + 1, 26):
                if count[c] > 0:
                    count[c] -= 1

                    suffix = ''.join(
                        chr(j + ord('a')) * count[j]
                        for j in range(26)
                    )

                    return (
                        target[:matched]
                        + chr(c + ord('a'))
                        + suffix
                    )

        # Backtrack through the matched prefix
        for i in range(matched - 1, -1, -1):
            x = ord(target[i]) - ord('a')

            # Restore target[i]
            count[x] += 1

            # Find the smallest character greater than target[i]
            for c in range(x + 1, 26):
                if count[c] > 0:
                    count[c] -= 1

                    suffix = ''.join(
                        chr(j + ord('a')) * count[j]
                        for j in range(26)
                    )

                    return (
                        target[:i]
                        + chr(c + ord('a'))
                        + suffix
                    )

        return ""