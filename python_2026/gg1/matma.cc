#include <iostream>
#include <cmath>
#include <chrono>
#include <iomanip>

/**
* Wersja C++ programu do liczenia sin (matma.py).
* Kompilacja przez g++ -O3 matma.cc
*/

double get_sin(double degree) {
    return std::sin(degree * M_PI / 180.0);
}

int main() {
    double x = 0.0;
    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < 10000000; ++i) {
        x += get_sin(i);
    }


    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;

    std::cout << "duration: " << std::fixed << std::setprecision(6)
              << duration.count() << std::endl;
    std::cout << x << std::endl;


    return 0;
}
