#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, c, d, e;
    std::cin >> a >> b >> c >> d >> e;
    std::cout <<(( a > b)? 1:0) << std::endl;
    std::cout << ((a > c)? 1:0 )<< std::endl;
    std::cout << ((a > d)? 1:0) << std::endl;
    std::cout << ((a > e)? 1:0) << std::endl;
    
    return 0;
}