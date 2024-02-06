class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []
        
        for i, temper in enumerate(temperatures):

            #현재 인덱스(날짜 경과)에서 스택의 마지막 인덱스(시작날짜)를 빼준다.
            while stack and temperatures[stack[-1]] < temper:
                prev_index = stack.pop()
                days[prev_index] = i - prev_index
            
            stack.append(i)
        
        return days