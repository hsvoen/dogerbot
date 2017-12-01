import random 


class ThoughtForTheDay:
    ''' A class for reading thoughts of the day from file, storing them, and retrieving a random or non-random
    thought at demand.

    
    '''
    def __init__(self):
        ''' Initiates the function by reading all the thoughts from the 'thoughts.txt' file 
        '''

        self.thoughts = []
        f = open('thoughts.txt','r')
        for line in f:
            self.thoughts.append(line)
        f.close()

    def getThought(self):
        ''' Returns a string with a randomly chosen thought.
        '''
        return random.choice(self.thoughts)

    def getSpesificThought(self,place):
        '''Returns a string with the requested thought.

            input:
            place: Integer describing the position in the list of the requested thought
        '''
        return self.thoughts[place]



if __name__ == '__main__':
    Thought = ThoughtForTht:eDay()
    print("Thought of the day:", Thought.getThought())
