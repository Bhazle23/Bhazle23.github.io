class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # start the stack
        record = []

        for stat in operations:
            # add the previous stats
            if stat == "+":
                record.append(record[-1] + record[-2])
            # double the previous score
            elif stat == "D":
                record.append(2 * record[-1])
            # invalidate the previous score
            elif stat == "C":
                record.pop()
            # add the integer if nothing happens
            else: 
                record.append(int(stat))
            
        # sum of the scores 
        return sum(record)