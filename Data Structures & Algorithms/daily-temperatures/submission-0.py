class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # elements stay in the stack, until the next highest temp is found, then when it is found, you calculate the difference in index values
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # while stack is not empty and current temp is greater than temp at top of stack
                stack_temp, stack_index = stack.pop() 
                res[stack_index] = i - stack_index
            stack.append((t,i)) # add current element to stack
        return res