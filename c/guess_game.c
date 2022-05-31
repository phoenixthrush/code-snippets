#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    system("cls");
    int hidden;
    srand(time(NULL));
    hidden = rand() % 51;
    int guess = 0;
    int guesscount = 0;
    int guesslimit = 20;
    int outofguesses = 0;

    while (guess != hidden && outofguesses == 0) {
        if (guesscount < guesslimit) {
            printf("\033[31mEnter ur number (between 0 and 50)\033[00m: ");
            scanf("%d", &guess);
            guesscount++;
            if (guess < hidden && guess != hidden) {
                printf("\033[96mbigger\033[00m\n\n");
            } else if (guess > hidden && guess != hidden) {
                printf("\033[96mlower\033[00m\n\n");
            }
        } else {
            outofguesses = 1;
        }
    }
    if (outofguesses == 1) {
        system("cls");
        printf("\033[31myeah out of guesses\033[00m\n");
        printf("\033[96mpress enter to continue\033[00m");
        system("pause >nul");
    } else {
        system("cls");
        printf("\033[31myou won uh ye\033[00m\n");
        printf("\033[96mpress enter to continue\033[00m");
        system("pause >nul");
    }

    return 0;
}
