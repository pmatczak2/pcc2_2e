class AsciiArt:
    def __init__(self, characters):
        self._characters = characters

    @classmethod
    def fromFile(cls, filename):
        with open(filename) as fileObj:
            characters = fileObj.read()
            return cls(characters)

    def display(self):
        print(self._characters)

    # Other AsciiArt methods would go here...

face1 = AsciiArt('      \n' +
                 ' _______\n' +
                 '|  . .  |\n' +
                 '| \\___/ |\n' +
                 '|_______|')

face1.display()
face2 = AsciiArt.fromFile('file.txt')
face2.display()
