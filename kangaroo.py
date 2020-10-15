"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 17: Classes and Methods in Think Python 2
    
    Note: Using Python 3.9.0
"""
class Kangaroo:
    """
        A Kangaroo is a marsupial.
    """
    def __init__(self, name, contents=None):
        """
            Initialize the pouch contents.
            
            name: string
            contents: initial pouch contents.
        """
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """
            Return a string representaion of this Kangaroo.
        """
        t = [ self.name + " has pouch contents:" ]
        for obj in self.pouch_contents:
            s = "    " + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """
            Adds a new item to the pouch contents.
            
            item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
roo.put_in_pouch("toy car")
kanga.put_in_pouch(roo)

print(kanga)
print(roo)
