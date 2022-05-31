#include <stdio.h>

void checkgrade(char grade) {
    printf("Your grade is: %c\n", grade);

    if(grade == 'A') {
        printf("cool\n");
    } else if(grade == 'B') {
        printf("wtf\n");
    } else {
        printf("huhhh\n");
    }
    }

int main() {
    checkgrade('A');
    return 0;
}
