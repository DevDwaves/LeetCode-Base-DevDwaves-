class Solution:
    def lexPalindromicPermutation(self, s, target):
        from collections import Counter

        cnt = Counter(s)

        # A palindrome can have at most one character
        # with an odd frequency.
        odd = [c for c in cnt if cnt[c] % 2 == 1]

        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""

        # Characters available in the left half
        half_cnt = [0] * 26

        for c in cnt:
            half_cnt[ord(c) - ord('a')] = cnt[c] // 2

        m = len(s) // 2
        target_half = target[:m]

        # --------------------------------------------------
        # First try to make target_half exactly.
        # --------------------------------------------------
        remaining = half_cnt[:]
        possible = True

        for c in target_half:
            x = ord(c) - ord('a')

            if remaining[x] == 0:
                possible = False
                break

            remaining[x] -= 1

        if possible:
            left = target_half
            palindrome = left + middle + left[::-1]

            # If the palindrome itself is already greater,
            # it is the smallest possible answer.
            if palindrome > target:
                return palindrome

        # --------------------------------------------------
        # We need the smallest half strictly greater than
        # target_half.
        #
        # Find the rightmost position where we can increase
        # target_half, then put the smallest possible
        # character there and sort the rest.
        # --------------------------------------------------

        prefix_cnt = [0] * 26

        for i in range(m - 1, -1, -1):

            # We need target_half[:i] to be constructible.
            # Build its remaining character counts.
            if i == 0:
                remaining = half_cnt[:]
            else:
                # Check prefix incrementally below.
                pass

            # Instead of rebuilding from scratch, calculate
            # remaining characters for this prefix.
            remaining = half_cnt[:]

            valid = True

            for j in range(i):
                x = ord(target_half[j]) - ord('a')

                if remaining[x] == 0:
                    valid = False
                    break

                remaining[x] -= 1

            if not valid:
                continue

            # At position i, choose the smallest character
            # strictly greater than target_half[i].
            current = ord(target_half[i]) - ord('a')

            for x in range(current + 1, 26):
                if remaining[x] == 0:
                    continue

                remaining[x] -= 1

                # Put all remaining characters in sorted order.
                suffix = []

                for c in range(26):
                    suffix.extend(
                        [chr(c + ord('a'))] * remaining[c]
                    )

                left = target_half[:i] + chr(x + ord('a')) + ''.join(suffix)

                return left + middle + left[::-1]

        return ""