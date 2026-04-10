class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        q = collections.deque()
        q.append((amount, 0))
        best_at = {amount: 0}  # amount -> fewest coins to reach it
        best = float('inf')
        
        while q:
            _amount, _n = q.popleft()  # BFS, not DFS
            
            for coin in coins:
                new_amount = _amount - coin
                if new_amount > 0:
                    new_n = _n + 1
                    if new_n < best_at.get(new_amount, float('inf')):
                        best_at[new_amount] = new_n  # only enqueue if strictly better
                        q.append((new_amount, new_n))
                elif new_amount == 0:
                    best = min(best, _n + 1)
        
        return best if best != float('inf') else -1