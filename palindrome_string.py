"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome."""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # STEP 1: Initialize pointers
        left = 0
        right = len(s) - 1
        
        # STEP 2: Loop while pointers haven't crossed
        while left < right:
            
            # STEP 3: Skip trash from left side
            while left < right and not s[left].isalnum(): #skip space, comma, symbole. and move pointer, move it man."""
                left += 1
                
            # STEP 4: Skip trash from right side
            while left < right and not s[right].isalnum():
                right -= 1
            
            # STEP 5: Compare the characters
            if s[left].lower() != s[right].lower():
                return False
            
            # STEP 6: Move both pointers inward
            left += 1
            right -= 1
            
        # STEP 7: If we got here, it's a palindrome!
        return True
