'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
'''
import random

class RandomizedSet:

    def __init__(self):
        self.list = []  # List to store the values
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)  # Add the value to the dictionary
        self.list.append(val)  # Add the value to the list
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        index = self.dict[val]  # Get the index of the value
        last_element = self.list[len(self.list)-1]  # Get the last element
        self.list[index] = last_element  # Replace the value with the last element
        self.list[last_element] = self.dict[val]  # Replace the value with the last element
        self.list.pop()
        del self.dict[val]  # Delete the value from the dictionary
        return 

    def getRandom(self) -> int:
        return random.choice(self.list)