class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [] # Question: why does this have to be empty?  
        #Answer:it is empty because the results are bign built pice by peice from the .append() {tbh i would not have known that, i only understood .append properly today.} so it is meant to be empty because of that, empty so there is something to add to it. if this result=[] starts with items, then those items will be displayd in the final result as well.

        max_candies = max(candies) # in max_candies <-- we are trying to find the greatest candies that are in the arry list. using "max" is the function in python that lets us find the greatest of something when used, hence the max()<-- parentheses
        for i in range(len(candies)): # Question: for in in range <-- what does this mean? why for i and why i in range? 
        # Answer: why for i? becasue python reads like english. so when we say "i" we mean as a variable. wonder if it's like x or n in maths
            result.append(candies[i] + extraCandies >= max_candies) # Question: <-- why do we need result.append() <-- what does append does, and why are we having having the whole block of candies[i] + extraCandies >= max_candies placed inside the append()? What i understand that, it returns the boolean array, but what does this mean?  
            # Answer: so append(x) will add x to the END of the lsit. so after each loop passes, one True/False is added to the list. otherwise it would replace the True/False from the previous loop.
            # Answer 2: why whole expression is inside the .append() -> python evalueates everything insdide the parentheses FIRST, then hands the results to .append.... i see, so the | candies[i] + extraCandies >= max_candies| gets computed first, then it proceeds to True/False.
        return result # Question: <-- why is the return result here? From what I understand the return needs to return the result, but what does return do? and why is it important that we have it indented outside of the loop and not inside the loop?
        # Answer: so reutrn handles the values back to whoever called the function. -- this time leetcode called this function. and it returns back the values to leetcodes functions. WITHOUT RETURN the function does the work but does not provide any value back to leetcode. so then leetcode sees nothing.
        #answer 2: why outside, becuase return will exit the function, so if i have it in the loop, it will exit the function after executing one iteration. when it's outside, it only exits the function after it runs all of the iteration.


"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [] # Question: why does this have to be empty?  
        #Answer:it is empty because the results are bign built pice by peice from the .append() {tbh i would not have known that, i only understood .append properly today.} so it is meant to be empty because of that, empty so there is something to add to it. if this result=[] starts with items, then those items will be displayd in the final result as well.

        max_candies = max(candies) # in max_candies <-- we are trying to find the greatest candies that are in the arry list. using "max" is the function in python that lets us find the greatest of something when used, hence the max()<-- parentheses
        for i in range(len(candies)): # Question: for in in range <-- what does this mean? why for i and why i in range? 
        # Answer: why for i? becasue python reads like english. so when we say "i" we mean as a variable. wonder if it's like x or n in maths
            result.append(candies[i] + extraCandies >= max_candies) # Question: <-- why do we need result.append() <-- what does append does, and why are we having having the whole block of candies[i] + extraCandies >= max_candies placed inside the append()? What i understand that, it returns the boolean array, but what does this mean?  
            # Answer: so append(x) will add x to the END of the lsit. so after each loop passes, one True/False is added to the list. otherwise it would replace the True/False from the previous loop.
            # Answer 2: why whole expression is inside the .append() -> python evalueates everything insdide the parentheses FIRST, then hands the results to .append.... i see, so the | candies[i] + extraCandies >= max_candies| gets computed first, then it proceeds to True/False.
        return result # Question: <-- why is the return result here? From what I understand the return needs to return the result, but what does return do? and why is it important that we have it indented outside of the loop and not inside the loop?
        # Answer: so reutrn handles the values back to whoever called the function. -- this time leetcode called this function. and it returns back the values to leetcodes functions. WITHOUT RETURN the function does the work but does not provide any value back to leetcode. so then leetcode sees nothing.
        #answer 2: why outside, becuase return will exit the function, so if i have it in the loop, it will exit the function after executing one iteration. when it's outside, it only exits the function after it runs all of the iteration.
"""