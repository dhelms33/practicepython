from 17_decode_web import Decoder

class WriteFile(Decoder):
    def __init__(self, ui):
        self.ui = ui
    def file_write(self):
        file_used = open('File_to_be_written')
        results_decoder = Decoder.decode_webpage_text()
        written_to_file = write(results_decoder)
        return written_to_file
if __name__ == "__main__":
    user_input = input("Do you want your file to write to file?")
    
        