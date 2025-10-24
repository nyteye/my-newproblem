class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Initialize a new list to store missing numbers
        new = []

        # Convert the list to a set to remove duplicates and allow fast lookups
        seen = set(nums)  # e.g., nums = [4,3,2,7,8,2,3,1] → seen = {1,2,3,4,7,8}

        # Get the length of nums (n) to know the expected range of numbers [1, n]
        n = len(nums)

        # Loop through all numbers from 1 to n
        # We use n+1 because range(a, b) goes up to b-1
        for i in range(1, n + 1):
            # If the current number is not in the seen set, it's missing
            if i not in seen:
                # Add the missing number to the result list
                new.append(i)

        # Return the list of missing numbers
        return new
   # 4️⃣ Loop through all numbers from 1 to n
        for i in range(1, n + 1):
            # Dry run checks:
            # i = 1 → 1 in seen? ✅ Yes → skip
            # i = 2 → 2 in seen? ✅ Yes → skip
            # i = 3 → 3 in seen? ✅ Yes → skip
            # i = 4 → 4 in seen? ✅ Yes → skip
            # i = 5 → 5 in seen? ❌ No  → new.append(5) → new = [5]
            # i = 6 → 6 in seen? ❌ No  → new.append(6) → new = [5, 6]
            # i = 7 → 7 in seen? ✅ Yes → skip
            # i = 8 → 8 in seen? ✅ Yes → skip
