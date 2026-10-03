class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0
        for person in accounts:
            wealth = sum(person)
            if wealth > maxwealth:
                maxwealth = wealth
        return maxwealth