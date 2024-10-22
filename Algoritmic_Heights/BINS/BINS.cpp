#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

std::vector<int> read_data_from_file(const std::string& file_path) {
    std::ifstream file(file_path);
    std::string line;
    std::vector<int> data;

    if (file.is_open()) {
        std::getline(file, line); // Read the first line with n and m
        std::istringstream iss(line);
        int n, m;
        iss >> n >> m;

        for (int i = 0; i < n; ++i) {
            int num;
            iss >> num;
            data.push_back(num);
        }

        for (int i = 0; i < m; ++i) {
            int num;
            iss >> num;
            data.push_back(num);
        }

        file.close();
    }

    return data;
}

int binary_search(const std::vector<int>& arr, int key) {
    int left = 0, right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == key) {
            return mid + 1; // Return 1-based index
        } else if (arr[mid] < key) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int main() {
    std::string file_path = "./BINS_input.txt";
    std::vector<int> data = read_data_from_file(file_path);

    int n = data[0];
    int m = data[1];
    std::vector<int> array(data.begin() + 2, data.begin() + 2 + n);
    std::vector<int> numbers(data.begin() + 2 + n, data.end());

    std::vector<int> indexes;
    for (int i : numbers) {
        int result = binary_search(array, i);
        indexes.push_back(result);
    }

    // Print indexes
    for (int index : indexes) {
        std::cout << index << " ";
    }
    std::cout << std::endl;

    std::ofstream output_file("./BINS_output.txt");
    if (output_file.is_open()) {
        for (int index : indexes) {
            output_file << index << " ";
        }
        output_file.close();
    }

    return 0;
}
