#include <iostream>
#include <queue>

int main() {
    // Create a queue of integers
    std::queue<int> q;

    // Enqueue some elements
    q.push(10);
    q.push(20);
    q.push(30);

    // Display the front element
    std::cout << "Front element: " << q.front() << std::endl;

    // Display the back element
    std::cout << "Back element: " << q.back() << std::endl;

    // Dequeue elements
    std::cout << "Dequeuing elements: ";
    while (!q.empty()) {
        std::cout << q.front() << " ";
        q.pop();
    }
    std::cout << std::endl;

    return 0;
}