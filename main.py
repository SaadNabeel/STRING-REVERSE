class StringReverse:
    
    def __init__(self, text):
        self.text = text

    def reversewords(self):
       
        reversedtext = ' '.join(self.text.split()[::-1])
        return reversedtext


string = StringReverse("I AM SAAD")
print(string.reversewords())
