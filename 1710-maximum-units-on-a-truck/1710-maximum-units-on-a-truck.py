class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sortedBoxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        totalUnits = 0

        for bn, bu in sortedBoxes:
            if bn <= truckSize:
                truckSize -= bn
                totalUnits += bn * bu
            else:
                totalUnits += truckSize * bu
                break

        return totalUnits
        