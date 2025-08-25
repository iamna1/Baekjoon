str1 = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = len(str1)
for i in range(len(str1)):
    if str1[i] == '=':
        if str1[i-2] == 'd' and str1[i-1] == 'z':
                n -= 2
        else :
            n -= 1
    if str1[i] == '-': n -= 1 
    if str1[i] == 'j':
        if i - 1 >= 0 and (str1[i-1] == 'l' or str1[i-1] == 'n') :
            n -= 1
print(n)