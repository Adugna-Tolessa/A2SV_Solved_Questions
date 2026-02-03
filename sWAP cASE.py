def swap_case(s):
    ans = []
    for i in range(len(s)):
        if s[i].isupper():
            ans += s[i].lower()
        elif s[i].islower():
            ans += s[i].upper()
        else:
            ans += s[i]
    return "".join(ans)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
