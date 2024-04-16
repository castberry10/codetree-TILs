#include <iostream>

int main() {
    int a;
    std::cin >> a;
    std::cout << a * a;
    if (a < 5){
        std::cout << std::endl << "tiny";
    }
    return 0;
}