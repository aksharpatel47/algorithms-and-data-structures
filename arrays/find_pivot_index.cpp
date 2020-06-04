#include <iostream>
#include <vector>
#include <numeric>
#include "temp.hpp"

int find_pivot_index(std::vector<int> nums)
{
    int sum = std::accumulate(nums.begin(), nums.end(), 0);
    int left_sum = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        int num = nums[i];
        if (left_sum == (sum - left_sum - num))
        {
            return i;
        }

        left_sum += num;
    }

    return -1;
}

int main()
{
    std::vector<int> input = {1, 7, 3, 6, 5, 6};

    std::cout << find_pivot_index(input) << std::endl;

    std::cout << get_temp() << std::endl;

    return 0;
}