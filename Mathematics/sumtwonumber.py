# the_array = [1,2,3,4,5,6,7,8,9]
# the_array = [3,3]
# sum_number = 6

def twoSum(nums, target):
        result = []
        for indexi, i in enumerate(nums):
            for indexj, j in enumerate(nums):
                if(indexi == indexj):
                    continue
                elif i+j == target:
                    result.append(indexi)
                    result.append(indexj)
                    return result
                else:
                    continue

        return []

# print(twoSum(the_array, sum_number))


class Solution:
    def twoSum(self, nums, target):
        # Create a hash map to store numbers and their indices
        num_map = {}

        # Iterate through the array
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # Check if the complement is already in the hash map
            if complement in num_map:
                return [num_map[complement], index]

            # Add the current number and its index to the hash map
            num_map[num] = index

        # Return an empty list if no solution is found
        return []




