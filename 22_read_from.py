#import readline, unused import
class Misc:
    """ Given a txt file that has a list of a bunch of names, count how many of each name there are in the file and print results."""
    
    def __init__(self, name, file):
        self.name = name
        self.file = file
        
    def read_to_output(self):
        count = 0
        target_name = self.name
        for word in self.file:
            if word == self.name:
                count+=1 
                return(f"{target_name} was found!")
            else:
                return(f"{target_name}" not found)
        return count
    
if __name__ == "__main__":
    user_input = input("Please input a target name to scan the file: ")