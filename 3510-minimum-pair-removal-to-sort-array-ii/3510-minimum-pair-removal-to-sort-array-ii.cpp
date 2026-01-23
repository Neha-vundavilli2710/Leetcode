#include <vector>
#include <set>
#include <numeric>

using namespace std;

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;

        // Use long long for sums to avoid overflow (-10^9 to 10^9)
        vector<long long> arr(nums.begin(), nums.end());
        vector<int> left(n), right(n);
        iota(left.begin(), left.end(), -1);
        iota(right.begin(), right.end(), 1);
        right[n - 1] = -1;

        // bst stores {sum, index} to find the leftmost minimum sum
        set<pair<long long, int>> bst;
        int inversion_count = 0;

        // Lambda to check if a pair starting at index i is an inversion
        auto is_inversion = [&](int i) {
            return (right[i] != -1 && arr[i] > arr[right[i]]);
        };

        // Initial population
        for (int i = 0; i < n - 1; ++i) {
            bst.insert({arr[i] + arr[i + 1], i});
            if (is_inversion(i)) inversion_count++;
        }

        int operations = 0;
        while (inversion_count > 0 && !bst.empty()) {
            // Rule: Smallest sum, then leftmost index
            auto it = bst.begin();
            int i = it->second;
            int j = right[i];
            bst.erase(it);

            operations++;

            // 1. Remove old pairs and inversions from BST/count before merging
            if (is_inversion(i)) inversion_count--;
            
            int p = left[i];
            if (p != -1) {
                if (is_inversion(p)) inversion_count--;
                bst.erase({arr[p] + arr[i], p});
            }
            
            if (right[j] != -1) {
                // j is being merged into i, so pair (j, right[j]) disappears
                if (is_inversion(j)) inversion_count--;
                bst.erase({arr[j] + arr[right[j]], j});
            }

            // 2. Perform merge: replace nums[i] with the sum
            arr[i] += arr[j];

            // 3. Update Doubly Linked List (delete node j)
            int next_to_j = right[j];
            right[i] = next_to_j;
            if (next_to_j != -1) {
                left[next_to_j] = i;
            }

            // 4. Re-calculate neighbors and inversions for the updated element i
            if (is_inversion(i)) inversion_count++;
            if (right[i] != -1) {
                bst.insert({arr[i] + arr[right[i]], i});
            }
            
            if (p != -1) {
                if (is_inversion(p)) inversion_count++;
                bst.insert({arr[p] + arr[i], p});
            }
        }

        return operations;
    }
};
