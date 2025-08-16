n = int(input())
first_str = list(input())
for _ in range(n-1):
    str1 = input()
    for i in range(len(str1)):
        if first_str[i] != str1[i]:
            first_str[i] = '?'
print(''.join(first_str))