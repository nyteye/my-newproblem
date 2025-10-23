def checkIfExist(arr):
    # 1. Initialize an empty set to store the numbers we have seen so far.
    seen = set()

    # 2. Loop through each number in the input array one by one.
    for num in arr:
        
        # 3. CHECK FOR A MATCH:
        # We check two conditions:
        
        # Condition A: Is this 'num' the DOUBLE of a number we've already seen?
        # Example: We are at '10', and our set already has '5'.
        # We check this by seeing if (num * 2) is in the 'seen' set.
        if (num * 2) in seen:
            return True

        # Condition B: Is this 'num' the HALF of a number we've already seen?
        # Example: We are at '5', and our set already has '10'.
        # We check this by seeing if (num / 2) is in the 'seen' set.
        #
        # IMPORTANT: We only check for the half if 'num' is an even number.
        # We don't care about '5 / 2 = 2.5' because we're only dealing with integers.
        if num % 2 == 0 and (num // 2) in seen:
            return True
            
        # 4. NO MATCH FOUND:
        # If neither check was true, it means we haven't found a pair *yet*.
        # So, we add the current 'num' to the 'seen' set.
        # This makes it available for future numbers in the loop to check against.
        seen.add(num)
        
    # 5. If the loop finishes without returning True,
    # it means no match was ever found.
    return False

# --- Examples ---
arr1 = [10, 2, 5, 3]
print(f"{arr1} -> {checkIfExist(arr1)}")  # Output: [10, 2, 5, 3] -> True

arr2 = [3, 1, 7, 11]
print(f"{arr2} -> {checkIfExist(arr2)}")  # Output: [3, 1, 7, 11] -> False

arr3 = [0, 0]
print(f"{arr3} -> {checkIfExist(arr3)}")  # Output: [0, 0] -> True
