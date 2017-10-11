#import <stdio.h>
#import <math.h>

int x;

int main(void) {
    scanf("%i", &x);
    for (int j = 0; j < x; j++) {
        int n;
        int sum = 1;
        scanf("%i", &n);
        for (int i = 2; i <= sqrt(n); i++) {
            if (i == sqrt(n)) {
                sum += i;
            } else if (n % i == 0) sum += i + n/i;
        }
        if (sum > n) {
            printf("%i is an abundant number.\n", n);
        } else if (sum < n) {
            printf("%i is a deficient number.\n", n);
        } else {
            printf("%i is a perfect number.\n", n);
        } 
    }

}