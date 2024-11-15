#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n,x,y;
    scanf("%d%d%d", &n,&x,&y);
    if(y%x==0 && y<=n * x) {
        printf("YES\n");
    } else{
        printf("NO\n");
    }
    return 0;
}
