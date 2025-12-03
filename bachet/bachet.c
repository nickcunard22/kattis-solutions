#include <stdio.h>

#define MAX_N 1000000
#define MAX_M 10

int main(void) {
    int n, k;
    int moves[MAX_M];
    static char dp[MAX_N + 1];

    while (scanf("%d %d", &n, &k) == 2) {
        for (int i = 0; i < k; i++) {
            scanf("%d", &moves[i]);
        }

        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            char win = 0;  // assume losing
            for (int j = 0; j < k; j++) {
                int m = moves[j];
                if (m <= i && dp[i - m] == 0) {
                    win = 1;
                    break;
                }
            }
            dp[i] = win;
        }

        if (dp[n]) {
            printf("Stan wins\n");
        } else {
            printf("Ollie wins\n");
        }
    }

    return 0;
}
