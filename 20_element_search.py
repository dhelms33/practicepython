from typing import List
class ElementSearch:
    def __init__(self, sorted_list: List[int]):
        self.sorted_list = sorted_list
        
    def find_element(self, target: int) -> bool:
        """
        Perform binary search to determine if target is in the list.

        Args:
            target (int): The number to search for.

        Returns:
            bool: True if target found, False otherwise.
        """
        
        left, right = 0, len(self.sorted_list) -1
        while left <= right:
            mid = (left+right) // 2
            mid_value = self.sorted_list[mid]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else: right = mid - 1
        return False
    
if __name__ == "__main__":
    try:
        raw_list = input("Please input a list of ordered numbers, separated by commas: ")
        target = int(input("Enter the number to search for: "))
        
        #convert input string to list of ints
        sorted_list = [int(x.strip()) for x in raw_list.split(",")]
        
        #initialize and search
        searcher = ElementSearch(sorted_list)
        found = searcher.binary_search(target)
        print(f"Found: {found}")
        
    except ValueError:
        print("This was not an ordered list of elements. Please try again.")