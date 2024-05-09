#include <iostream>

int main() {
    int i;
    std::cin >> i;
    int n = 0;
    while(n < i){
        std::cout << "*" << std::endl;
        n++;
    }
    return 0;
}