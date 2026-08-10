class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n , m = len(s) , len(p)
        if m> n:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:m])

        result = []
        if s_count == p_count:
            result.append(0)

        for i in range(m, n):
            left_char = s[i - m]
            right_char = s[i]

            s_count[right_char] +=1
            s_count[left_char] -=1
            if s_count[left_char] ==0:
                del s_count[left_char]

            if s_count == p_count:
                result.append(i - m+1)

        return result