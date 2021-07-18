"""
CSE212 
(c) BYU-Idaho
06-Prove

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

#############
# Problem 1 #
#############

class Translator:
    """
    This class provides the capability of a translator.  A
    Python Dictionary is used to keep track of the mapping 
    of words from one language to another language.  You should 
    assume that there is only one translation for every 
    word (and vice versa).
    """

    def __init__(self):
        """ 
        Initialize the Python Dictionary to store word mappings
        """
        self.words = dict() 

    def add_word(self, from_word, to_word):
        """
        Add the translation from 'from_word' to 'to_word'
        For example, in a english to german dictionary:

        my_translator.add_word("book","buch")
        """
        #add_word function being implemented
        if from_word not in self.words.keys(): 
        #the condition is used to iterate over the available dictionary words and check 
        #if the given word is available or not. Since we assume there is only one translation for every word we must check if that word is already present in the dictionary or not.
            self.words[from_word]=to_word
        #adding the given word to the dictionary words by mapping the given from_word with the to_word
        else:
        #if the word is already present we can either overwrite
        #the word's translation or return an error. Here we are returning an error.
            print("Words already in the dictionary")

    #translate function being implemented
    def translate(self, from_word):
        """
        Translate a word and return the result.  If the word 
        can not be translated then "???" is returned.  
        For example, in an english to german dictionary:

        german_word = my_translator.translate("book")
        """
        if from_word not in self.words.keys():
        #the given condition checks the keys and if the given
        #from_word id not present in the words dictionary then it prints ???.
            return "???"
        else:
        #If the from_word key is found then the mapped translation is returned.
            return self.words[from_word]


# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
english_to_german = Translator()
english_to_german.add_word("House","Haus")
english_to_german.add_word("Car","Auto")
english_to_german.add_word("Plane","Flugzeug")
print(english_to_german.translate("Car")) # Auto
print(english_to_german.translate("Plane")) # Flugzeug
print(english_to_german.translate("Train")) # ???

#############
# Problem 2 #
#############

def summarize_degrees(filename):
    """
    Read a census file and summarize the degrees (education)
    earned by those contained in the file.  The summary
    should be stored in a dictionary where the key is the
    degree earned and the value is the number of people that 
    have earned that degree.  The degree information is in
    the 4th column of the file.  There is no header row in the
    file.
    """
    degrees = dict()
    with open(filename) as file_in:
        for line in file_in:
            #Using split to disect meaningful data with a comma as a delimiter
            fields = line.split(",") 
            #Checking if the degree already exists in dict using built-in function get() for dict
            if degrees.get(fields[3], 0):
                degrees[fields[3]] += 1
            else:
                degrees[fields[3]] = 1
    return degrees

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 2 TESTS ===========")
print(summarize_degrees("census.txt")) # You might need to add a path for the file
# Results may be in a different order:
# {'Bachelors': 5355, 'HS-grad': 10501, '11th': 1175, 
# 'Masters': 1723, '9th': 514, 'Some-college': 7291, 
# 'Assoc-acdm': 1067, 'Assoc-voc': 1382, '7th-8th': 646, 
# 'Doctorate': 413, 'Prof-school': 576, '5th-6th': 333, 
# '10th': 933, '1st-4th': 168, 'Preschool': 51, 
# '12th': 433}   

#############
# Problem 3 #
#############

def is_anagram(word1, word2):
    """
    Determine if 'word1' and 'word2' are anagrams.  An anagram
    is when the same letters in a word are re-organized into a 
    new word.  A Python dictionary is used to solve the problem.

    Examples:
    is_anagram("CAT","ACT") would return True
    is_anagram("DOG","GOOD") would return False because GOOD has 2 O's

    Important Note: When determining if two words are anagrams, you
    should ignore any spaces.  You should also ignore cases.  For 
    example, 'Ab' and 'Ba' should be considered anagrams

    Reminder: You can access a letter by index in a Python string by 
    using the [] notation.
    """
    # convert both the strings into lowercase
    word1 = word1.lower()
    word2 = word2.lower()
    # check if length is same
    if(len(word1) == len(word2)):
        # sort the strings
        sorted_word1 = sorted(word1)
        sorted_word2 = sorted(word2)
        # if sorted char arrays are same
        if(sorted_word1 == sorted_word2):
            print(word1 + " and " + word2 + " are an anagram.")
        else:
            print(word1 + " and " + word2 + " are not an anagram.")
    else:
        print(word1 + " and " + word2 + " are not an anagram.")

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 3 TESTS ===========")
print(is_anagram("CAT","ACT")) # True
print(is_anagram("DOG", "GOOD")) # False
print(is_anagram("AABBCCDD", "ABCD")) # False
print(is_anagram("ABCCD","ABBCD")) # False
print(is_anagram("BC","AD")) # False
print(is_anagram("Ab","Ba")) # True
print(is_anagram("A Decimal Point", "Im a Dot in Place"))  # True
print(is_anagram("tom marvolo riddle", "i am lord voldemort")) # True
print(is_anagram("Eleven plus Two", "Twelve Plus One")) # True
print(is_anagram("Eleven plus One", "Twelve Plus One")) # False

#############
# Problem 4 #
#############

class Maze:
    """
    Defines a maze using a dictionary.  The dictionary is provided by the
    user when the Maze object is created.  The dictionary will contain the
    following mapping:

    (x,y) : (left, right, up, down)

    'x' and 'y' are integers and represents locations in the maze.
    'left', 'right', 'up', and 'down' are boolean are represent valid directions

    If a direction is False, then we can assume there is a wall in that direction.
    If a direction is True, then we can proceed.  

    If there is a wall, then display "Can't go that way!".  If there is no wall,
    then the 'curr_x' and 'curr_y' values should be changed.
    """

    def __init__(self, maze_map):
        """
        Initialize the map.  We assume that (1,1) is a valid location in
        the maze.
        """
        self.maze_map = maze_map
        self.curr_x = 1
        self.curr_y = 1

    def move_left(self):
        """
        Check to see if you can move left.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """
        #Accessing the Dictionary Values and saving in a temporary variable
        temp= self.maze_map[self.curr_x, self.curr_y]
        #Cheking the value at the position of left which is first postion.
        if temp[0]:
            #If value of left True then decreasing value of x to go left
            self.curr_x-=1
        else:
            print("Can't go that way!")
        return

    def move_right(self):
        """
        Check to see if you can move right.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """        
        #Accessing the Dictionary Values and saving in a temporary variable
        temp= self.maze_map[self.curr_x, self.curr_y]
        #Cheking the value at the position of left which is second postion.
        if temp[1]:
            #If value of right True then increasing value of x to go right
            self.curr_x+=1
        else:
            print("Can't go that way!")
        return

    def move_up(self):
        """
        Check to see if you can move up.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """
        #Accessing the Dictionary Values and saving in a temporary variable
        temp= self.maze_map[self.curr_x, self.curr_y]
        #Cheking the value at the position of left which is third postion.
        if temp[2]:
            #If value of up True then decreasing value of y to go up
            self.curr_y-=1
        else:
            print("Can't go that way!")
        return

    def move_down(self):
        """
        Check to see if you can move down.  If you can, then move.  If you
        can't move, then display "Can't go that way!"
        """
        #Accessing the Dictionary Values and saving in a temporary variable
        temp= self.maze_map[self.curr_x, self.curr_y]
        #Cheking the value at the position of left which is fourth postion.
        if temp[3]:
            #If value of down True then increasing value of y to go down
            self.curr_y+=1
        else:
            print("Can't go that way!")
        return
    
    def show_status(self):
        print("Current location (x={} , y={})".format(self.curr_x, self.curr_y))

# Sample Test Cases (may not be comprehensive) 
map =  {(1,1) : (False, True, False, True),
        (1,2) : (False, True, True, False),
        (1,3) : (False, False, False, False),
        (1,4) : (False, True, False, True),
        (1,5) : (False, False, True, True),
        (1,6) : (False, False, True, False),
        (2,1) : (True, False, False, True),
        (2,2) : (True, False, True, True),
        (2,3) : (False, False, True, True),
        (2,4) : (True, True, True, False),
        (2,5) : (False, False, False, False),
        (2,6) : (False, False, False, False),
        (3,1) : (False, False, False, False),
        (3,2) : (False, False, False, False),
        (3,3) : (False, False, False, False),
        (3,4) : (True, True, False, True), 
        (3,5) : (False, False, True, True),
        (3,6) : (False, False, True, False),
        (4,1) : (False, True, False, False),
        (4,2) : (False, False, False, False),
        (4,3) : (False, True, False, True),
        (4,4) : (True, True, True, False),
        (4,5) : (False, False, False, False),
        (4,6) : (False, False, False, False),
        (5,1) : (True, True, False, True),
        (5,2) : (False, False, True, True),
        (5,3) : (True, True, True, True),
        (5,4) : (True, False, True, True),
        (5,5) : (False, False, True, True),
        (5,6) : (False, True, True, False),
        (6,1) : (True, False, False, False),
        (6,2) : (False, False, False, False),
        (6,3) : (True, False, False, False),
        (6,4) : (False, False, False, False),
        (6,5) : (False, False, False, False),
        (6,6) : (True, False, False, False)}

print("\n=========== PROBLEM 4 TESTS ===========")
maze = Maze(map)
maze.show_status() # Should be at (1,1)
maze.move_up() # Error
maze.move_left() # Error
maze.move_right() 
maze.move_right() # Error
maze.move_down()
maze.move_down()
maze.move_down()
maze.move_right()
maze.move_right()
maze.move_up()
maze.move_right()
maze.move_down()
maze.move_left()
maze.move_down() # Error
maze.move_right()
maze.move_down()
maze.move_down()
maze.move_right()
maze.show_status() # Should be at (6,6)

#############
# Problem 5 #
#############

import requests  

def earthquake_daily_summary():
    """
    This function will read JSON (Javascript Object Notation) data from the 
    United States Geological Service (USGS) consisting of earthquake data.
    The data will include all earthquakes in the current day.
    
    JSON data is organized into a dictionary.  After reading the data using
    the 'requests' library, this function will print out a list of all
    earthquake locations ('place' attribute) and magnitudes ('mag' attribute).
    Additional information about the format of the JSON data can be found 
    at this website:  

    https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
        
    To install the requests library, run:
       If using virtual environment: pip install requests
       If using Windows: py -m pip install requests
       If using Mac: pip3 install requests
    """    
    req = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
    data = req.json() #The .json() function will convert the json data from the server to a dictionary
    #A counter for each feature in the metadata, which then prints the information with
    #given tags assigned to each earthquake location with properties of those earthquakes
    for i in data['features']:
        print(i['properties']['place']+" - Mag "+str(i['properties']['mag']))

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 5 TESTS ===========")
earthquake_daily_summary()

# Sample output from the function.  Number of earthquakes, places, and magnitudes will vary.

# 1km NE of Pahala, Hawaii - Mag 2.36
# 58km NW of Kandrian, Papua New Guinea - Mag 4.5
# 16km NNW of Truckee, California - Mag 0.7
# 9km S of Idyllwild, CA - Mag 0.25
# 14km SW of Searles Valley, CA - Mag 0.36
# 4km SW of Volcano, Hawaii - Mag 1.99






