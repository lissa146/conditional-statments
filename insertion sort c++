#include <iostream>
using namespace std;

int arr[5] = { 4, 2, 5, 1, 3 };

int main() {
	for (int i = 1; i < (sizeof(arr) / sizeof(int)); i++) {

		int key = arr[i];
		int j = i-1;

		while (j >= 0 && key < arr[j]) {
			arr[j + 1] = arr[j];
			j -= 1;
		}

		arr[j + 1] = key;

	}
	for (int i = 0; i < (sizeof(arr) / sizeof(int)); i++) {
		cout << arr[i] << " ";
	}
}
