class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = []

        for pos, spe in zip(position,speed):
            pos_speed.append((pos,spe))
        pos_speed.sort(reverse = True)

        for start_pos, start_speed in pos_speed:
            time = ( target-start_pos) / start_speed
            stack.append(time)
            while len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)