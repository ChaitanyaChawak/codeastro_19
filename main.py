# this is the main file where the functions exist

class Chicagoify:
    """
    This converts a given address into the number of blocks it is away from the center of Chicago, and vice versa!


    """

    def __init__(self):

        self.question = input("Type \'blocks\' if you want to get the number of blocks from the center of Chicago, else type \'address\' to get the address given the number of blocks : ")
        if self.question == 'address':
            self.north = input('Number of blocks away to north : ')
            try:
                float(self.north)
            except ValueError:
                raise Exception("Please enter a valid positive number !!")
            self.south = input('Number of blocks away to south : ')
            try:
                float(self.south)
            except ValueError:
                raise Exception("Please enter a valid positive number !!")
            self.east = input('Number of blocks away to east : ')
            try:
                float(self.east)
            except ValueError:
                raise Exception("Please enter a valid positive number !!")
            self.west = input('Number of blocks away to west : ')
            try:
                float(self.west)
            except ValueError:
                raise Exception("Please enter a valid positive number !!")

            if self.north and self.south != '0' :
                raise Exception("The place cannot be both North and South at the same time !")
            
            if self.east and self.west != '0' :
                raise Exception("The place cannot be both East and West at the same time !")

        else:
            self.address = self.question

Chicagoify()
