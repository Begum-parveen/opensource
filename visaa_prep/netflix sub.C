#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int A, B, C, X;
    scanf("%d %d %d %d", &A, &B, &C, &X);
    if(A + B >= X || A + C >= X || B + C >= X){
        printf("YES\n");
    } else {
        printf("NO\n");
    }
    return 0;
}
