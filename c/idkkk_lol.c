#include <stdio.h>

void checkgrade(char grade) {
    printf("Your grade is: %c\n", grade);

    switch(grade) {
    case 'A' :
        printf("nice\n");
        break;
    case 'B' :
        printf("cool\n");
        break;
    default :
        printf("huh bruh wot\n");
        break;
    }
}

int main() {
    checkgrade('A');
    return 0;
}
