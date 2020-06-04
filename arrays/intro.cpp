#include "animal.hpp"

using std::cin;

int main()
{
    auto fred = std::make_unique<Animal>("Fred", 12, 34);

    fred->ToString();

    cin.get();

    return 0;
}