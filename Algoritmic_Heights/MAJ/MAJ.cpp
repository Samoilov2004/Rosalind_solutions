#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>

int find_majority_element(const std::vector<int>& arr) {
    int candidate = nullptr;
    int count = 0;

    for (int num : arr) {
        if (count == 0) {
            candidate = num;
            count = 1;
        } else if (num == candidate) {
            count += 1;
        } else {
            count -= 1;
        }
    }

    count = 0;
    for (int num : arr) {
        if (num == candidate) {
            count += 1;
        }
    }

    if (count > arr.size() / 2) {
        return candidate;
    } else {
        return -1;
    }
}

int main() {
    std::ifstream input_file("./MAJ_input.txt");

    int a, b;
    input_file >> a >> b;

    std::vector<std::vector<int>> arrays;
    for (int i = 0; i < a; ++i) {
        std::string line;
        std::getline(input_file, line);
        std::istringstream iss(line);
        std::vector<int> new_arr;
        int num;
        while (iss >> num) {
            new_arr.push_back(num);
        }
        arrays.push_back(new_arr);
    }

    input_file.close();

    std::vector<int> results;
    for (const auto& arr : arrays) {
        results.push_back(find_majority_element(arr));
    }

    for (int result : results) {
        std::cout << result << " ";
    }
    std::cout << std::endl;

    std::ofstream output_file("./MAJ_output.txt");
    for (int result : results) {
        output_file << result << " ";
    }
    output_file.close();

    return 0;
}
