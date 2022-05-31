#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main() {
    int secret;
    int guessed_num;
    int tries = 0;
    int finish = 0;
    int difficulty;
    string diff;

    cout << "Welcome to idk lotto or something..." << endl;
    cout << "Try to guess the random number you get 3 tries!\n" << endl;
    cout << "Hardness level: " << endl;
    cout << "easy       \(0-5\)" << endl;
    cout << "normal     \(0-10\)"<< endl;
    cout << "hard       \(0-20\)"<< endl;
    cout << "extreme    \(0-50\)" << endl;
    cout << "\nEnter the difficulty: ";
    getline(cin, diff);

    if (diff == "easy") {
        difficulty = 5;
        cout << "easy selected!" << endl;
    } else if (diff == "normal") {
        difficulty = 10;
        cout << "normal selected!" << endl;
    } else if (diff == "hard") {
        difficulty = 20;
        cout << "hard selected!" << endl;
    } else if (diff == "extreme") {
        difficulty = 50;
        cout << "extreme selected!" << endl;
    } else {
        cout << "wrong difficulty!" << endl;
    }

    srand(time(0));
    secret = rand() & difficulty + 1;

    do {
        while(secret!=guessed_num && tries != 3) {
            cout << "\nEnter your guess: ";
            cin >> guessed_num;
            system("cls");
            if (secret < guessed_num) {
                cout << "your numer is too big!" << endl;
                tries++;
            } else if (secret > guessed_num) {
                cout << "your number is too small!" << endl;
                tries++;
            }
        }
        finish = 1;
        break;

    } while(finish = 1);

    if (tries != 3) {
        cout << "you made it congratulations lmao!" << endl;
        system("echo press enter too exit!");
        system("pause >nul");
    } else {
        cout << "out off guesses!\n" << endl;
        system("echo press enter too exit!");
        system("pause >nul");
    }
    return 0;
}
