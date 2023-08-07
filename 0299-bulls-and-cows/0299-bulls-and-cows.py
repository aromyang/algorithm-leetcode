class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_cnt = Counter(secret)
        guess_cnt = Counter(guess)
        
        bulls = [s for s, g in zip(secret, guess) if s == g]
        cows = dict([(k, min(v, guess_cnt.get(k))) for k, v in secret_cnt.items() if k in guess_cnt])
        
        return str(len(bulls)) + 'A' + str((sum(cows.values()) - sum([1 for b in bulls if b in cows]))) + 'B'