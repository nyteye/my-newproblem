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
    """Symbols / Spaces dikhen (Trash) ➔ Skip karo (while loop use karke aage badho).
Letters / Numbers dikhen (Valid) ➔ Compare karo (if condition se check karo).
Code se Relation:
Skip: Ye line wahi kar rahi hai 👇
while ... not s[left].isalnum(): left += 1
(Jab tak symbol hai, skip karte raho)
Compare: Ye line checking kar rahi hai 👇
if s[left].lower() != s[right].lower():<<<<----
(Agar letter match nahi hua, toh False)
Simple logic: Kachra hatao, kaam ki cheez compare karo. ✅"""
