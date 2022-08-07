class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        starthour=int(current[0:2])*60
        endhour=int(correct[0:2])*60
        startmin=int(current[3:5])
        endmin=int(correct[3:5])
        
        starttime=starthour+startmin
        endtime=endhour+endmin
        diff=endtime-starttime
        res = 0
        for sub in [60, 15, 5, 1]:
            res += diff // sub
            diff = diff % sub
        return res
        
        