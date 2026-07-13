

def longest_substring(s):
    left = 0
    seen = set()
    longest = 0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[r])
        longest = max(longest, r - left + 1)
        print(seen)
    return longest

s = "pwwkew"
res = longest_substring(s)
print(f"The length of the longest substring is {res}")