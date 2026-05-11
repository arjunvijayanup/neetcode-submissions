class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for item in operations:
            if item == "+":
                record.append(record[-1]+record[-2])
            elif item == "D":
                record.append(2 * record[-1])
            elif item == "C":
                record.pop()
            else:
                record.append(int(item))
            
        return sum(record)


        