class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Step 1: Iterate through the array and mark numbers that appear.
        # We'll use the index (num - 1) as the marker position.
        # For each number, we make the value at that index negative
        # to show that the number (index + 1) exists in the array.

        l = len(nums)
        for i in range(l):
            # Use abs() because some values may have been negated already.
            index = abs(nums[i]) - 1

            # Only mark it negative if it's not already marked.
            # This avoids double-flipping (which would turn it positive again).
            if nums[index] > 0:
                nums[index] = -nums[index]

        # Step 2: After marking, all indices that remain positive
        # correspond to numbers that did NOT appear in the array.
        result = []
        for j in range(l):
            if nums[j] > 0:
                # Since index starts from 0, the missing number is (index + 1)
                result.append(j + 1)

        # Step 3: Return the list of missing numbers.
        return result
