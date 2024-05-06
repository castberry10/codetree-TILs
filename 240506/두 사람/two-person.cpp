#include <iostream>
#include <string>

using namespace std;

int main() {
    string as, bs;
    int ai, bi;

    cin >> ai >> as;
    cin >> bi >> bs;
    if((as == "M" && ai >= 19)||( bs == "M" && bi >= 19)){
        cout << 1;
    }else{
        
    cout << 0;
    } 

    return 0;
}