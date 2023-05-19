class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')
        
        for ppath in paths:
            if ppath == '.' or ppath == '':
                continue
            elif ppath == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ppath)
        
        return '/' + '/'.join(stack)