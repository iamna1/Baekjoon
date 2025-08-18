import sys
s = sys.stdin.readline().strip().upper()
counts = {}
if not s :
    print("?")
else :
    for char in s:
        if char in counts:
            counts[char] += 1
        else: counts[char] = 1
    max_count = 0
    result = ''
    is_multiple = False
    for char, count in counts.items():
        if count > max_count:
            max_count = count
            result = char
            is_multiple = False
        elif count == max_count :
            is_multiple = True
    if is_multiple :
        print("?")
    else: print(result)