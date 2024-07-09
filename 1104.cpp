#include <bits/stdc++.h>

int main()
{
    int a, b;
    std::cin >> a;
    std::cin >> b;

    while (true)
    {
        if (a == 0 && b == 0)
        {
            break;
        }
        std::set<int> alice;
        std::set<int> beatriz;

        for (int i = 0; i < a; i++)
        {
            int x;
            std::cin >> x;
            alice.insert(x);
        }
        for (int i = 0; i < b; i++)
        {
            int x;
            std::cin >> x;
            beatriz.insert(x);
        }
        std::vector<int> diffA;
        std::set_difference(alice.begin(), alice.end(), beatriz.begin(), beatriz.end(), std::inserter(diffA, diffA.begin()));
        std::vector<int> diffB;
        std::set_difference(beatriz.begin(), beatriz.end(), alice.begin(), alice.end(), std::inserter(diffB, diffB.begin()));

        int result = std::min(diffA.size(), diffB.size());

        std::cout << result << '\n';

        std::cin >> a;
        std::cin >> b;
    }
}
