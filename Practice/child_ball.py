# Problem : You are given two positive integers n and k. There are n children numbered from 0 to n - 1 standing in a queue 
# in order from left to right.Initially, child 0 holds a ball and the direction of passing the ball is towards the right 
# direction. After each second, the child holding the ball passes it to the child next to them. Once the ball reaches either 
# end of the line, i.e. child 0 or child n - 1, the direction of passing is reversed.
# Return the number of the child who receives the ball after k seconds.

def Child_ball(n, move):
     
    n -= 1
    rounds = move // n
    rem = move % n
    
    if rounds % 2 == 0:
        return rem
    else:
        return n - rem
    
    
    return n

child = 4
moves = 15
print(Child_ball(child,moves))

# class Solution:
#     def numberOfChild(self, n: int, k: int) -> int:
#         n -= 1  # Decrement n to simplify calculation (so range is now 0 to n-1)
#         rounds = k // n  # Calculate the number of complete back-and-forth trips
#         rem = k % n  # Calculate the remaining steps after the last complete trip

#         if rounds % 2 == 0:
#             # If the number of complete back-and-forth trips is even
#             return rem  # The ball is passed forward from the start
#         else:
#             # If the number of complete back-and-forth trips is odd
#             return n - rem  # The ball is passed backward from the end