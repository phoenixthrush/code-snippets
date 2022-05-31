#include <stdio.h>

int main() {
    char username[20];
    printf("please enter your username: ");
    fgets(username, 20, stdin);

    int age = 15;
    printf("hello, %s\n", username);
    printf("I heard that you're %d years old\n", age);
    printf("just %d years till you are 18\n\n", 18 - age);

    const int cat = 15;
    printf("cat is %d\n\n", cat);

    int banana;
    printf("how many bananas do you have wtf: ");
    scanf("%d", &banana);
    printf("you have %d bananas lol\n\n", banana);

    double number;
    double number2;
    printf("What do you wanna multiply with (first number): ");
    scanf("%lf", &number);
    printf("What do you wanna multiply with (second number): ");
    scanf("%lf", &number2);
    printf("%f\n\n", number * number2);

    return 0;
}
