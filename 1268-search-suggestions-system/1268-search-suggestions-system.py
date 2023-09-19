class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = [[] for _ in range(len(searchWord))]
        products = [p for p in products if p[:1] == searchWord[:1]]        
        products.sort()
        
        cur = ''
        for i, word in enumerate(searchWord):
            cur += word
            left, right = 0, len(products) - 1
            while left <= right:
                mid = (left + right) // 2
                if products[mid].startswith(cur):
                    if mid > 0 and not products[mid - 1].startswith(cur):
                        ans[i] = [p for p in products[mid:mid+3] if p.startswith(cur)]
                        break
                    elif mid == 0:
                        ans[i] = [p for p in products[:3] if p.startswith(cur)]
                        break
                    else:
                        right = mid - 1
                elif products[mid] < cur:
                    left = mid + 1
                else:
                    right = mid - 1
    
        return ans
        