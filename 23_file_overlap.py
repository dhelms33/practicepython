import file
class Overlaps:
    
    def __init__(self, file, n1, n2):
        self.file = file
        self.n1 = n1
        self.n2 = n2
    
    def file_reader(self, file: list) -> list:
        with open('file', r) as file:
        content = file.read().split(',').strip()
        return content
    def string_to_int_(self, content: list) -> int[]:
        nums = []
        for word in content:
            nums[word] += int(word)
        return nums