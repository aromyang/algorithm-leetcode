class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def backtrack(hours, minutes, cur_turned_on, cur_idx):
            if cur_turned_on == turnedOn:
                if hours < 12 and minutes < 60:
                    time = "{:d}:{:02d}".format(hours, minutes)
                    ans.append(time)
                return

            if cur_idx == 10:
                return
            
            if cur_idx < 4:
                next_hours = hours + (1 << cur_idx)
                backtrack(next_hours, minutes, cur_turned_on + 1, cur_idx + 1)
            else:
                next_minutes =  minutes + (1 << (cur_idx - 4))
                backtrack(hours, next_minutes, cur_turned_on + 1, cur_idx + 1)
            
            backtrack(hours, minutes, cur_turned_on, cur_idx + 1)
        
        ans = []
        backtrack(0, 0, 0, 0)
        
        return ans