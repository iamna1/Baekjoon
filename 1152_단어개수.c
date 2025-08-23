#include <stdio.h>
#include <string.h>
int main() {
    char str1[1000002];
    int n, cnt = 0;
    fgets(str1, 1000002, stdin);
    if (str1[0] == '\n') {
        printf("%d", 0);
        return 0;
    }
    n = strlen(str1);
    for (int i = 0; i < n; i++){
        if(str1[i] == ' ') cnt++;
    }
    cnt++;
    if (str1[0] == ' ') cnt--;
    if (str1[n-2] == ' ') cnt--;
    printf("%d\n", cnt);
}