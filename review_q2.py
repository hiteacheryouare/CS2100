'''
    CS2100
    Spring 2026
    Starter code for class on Wednesday 2/11/26

    These are practice problems! Fill in the function stubs for as many
    or as few as you would like.

    Notice the use of the Any type. That's because these functions will work
    the same no matter what is contained in their list/set/tuple/dictionary :)

    We'll work together on a few them during class, and then run the tests
    in test_lec14.py to make sure everything works as expected.

    Pick your favorites... (starred ones are MOST relevant for quiz 2)
    1. **create_email (practice with default params and strings)
    2. normalize_lst (normalization with a list instead of a dataframe)
    3. dedupe (practice with data structures)
    4. **find_common (practice with data structures)
    5. swap_pairs (practice with tuples)
    6. has_required (practice with sets)
    7. **get_seconds (practice with lists and dictionaries)
    8. **Book class (practice with classes and objects, __str__, default params)
'''

from typing import Any

def create_email(recipient: str, subject: str = "No Subject",
                 sender: str = "noreply@northeastern.edu") -> str:
    ''' returend a string formatted for an email message
    
        parameters:
            recipient (str), the email address to send to (REQUIRED)
            subject (str), optional. the email subject line (default: "No Subject")
            sender (str), optional. the sender's email (default: "noreply@university.edu")
        
        returns:
            str, a formatted email string with items sepaerated by linebreaks
            Ex: "From: noreply@northeastern.edu
                 To: student@northeastern.edu
                 Subject: Subject
        raises:
            ValueError if recipient is empty string
     '''
    email = (
        f"From: {sender}"
        f"To: {recipient}"
        f"Subject: {subject}"
    )
    return email

def normalize_lst(lst: list[float]) -> list[float]:
    ''' normalize a list of floats using min-max scaling.

        parameters: 
            lst, a list of floats to normalize
        
        returns:
            a list of floats, the normalized values all between 0-1

        raises:
            value error if list has fewer than two elements
            value error if max and min are same value
    '''
    pass

def dedupe(lst: list[Any]) -> list[Any]:
    ''' remove duplicates from the given list

        parameters:
            lst, a list of any data type
        
        returns:
            lst, also any data type, with dupes removed
        
        raises:
            value error if list is empty
    '''
    pass

def find_common(lst1: list[Any], lst2: list[Any]) -> set[Any]:
    ''' find common elements between two lists

        parameters: 
            lst1, lst2, both of type [Any] to find common elements
        
        returns:
            set[Any], the elements that appear in both lists
        
        raises:
            value error if either list is empty
    '''
    pass

def swap_pairs(lst: list[tuple[Any, Any]]) -> list[tuple[Any, Any]]:
    ''' swap pairs of tuples in the given list (e.g., [(1, 2), (3, 4)] -> [(2,1), (4,3)]

        parameters:
            lst, a list of pairs of tuples of type Any
        
        returns:
            list of tuple of Any, the same pairs of tuples as we started with,
            but with values swapped
        
        raises:
            value error if the given list is empty
    '''
    if not lst:
        raise ValueError("no list")
    swaplist = []
    for tup in lst:
        swaplist.append((tup[1], tup[0]))


def has_required(avail: set[Any], req: set[Any]) -> bool:
    ''' determine whether all required elements are available
        ex: {'a', 'b', 'c'}, {'b'} returns True
            {'a', 'b', 'c'}, {'b', 'd'} returns False
    
        parameters:
            avail, req, both sets of type Any
        
        returns: 
            a boolean indicating whether ALL required elements appear in available set
        
        raises:
            value error if either set is empty
    '''
    pass


def get_seconds(person: str, connections: dict[str, list[str]]) -> set[str]:
    '''  finds a list of second-level connections for the given person. 
         A second-level connection is someone your connection is connected to,
         but YOU are not connected to.
         A second-level connection cannot be someone you're connected to, or yourself.

         parameters:
            person (str), the name of the person whose second-level connections
                we're looking for
            connections (dict[str, list[str]]), the person's first-level connections (keys)
                and THEIR connections (values)
        
        returns:
            a set of strings, the person's second-level connections 
            (a person cannot be their own second-level connection)
        
        raises:
            valueError if dictionary is empty
            valueError if person is the empty string
    '''
    pass

#     write a class to represent a Book. It should have attributes for
#     title, author, and number of pages read.

#     Its constructor should take in title, author, and number of pages read
#     ALL as default parameters with reasonable default values.
#     (number of pages read should default to 0; the others you can choose)

#     Write a method to increase the number of pages read by a given value.

#     Write the __str__ method to print the title, author, and pages read in the
#     following format: "Read so far: {pages} pages"

class Book:
    ''' class to represent a book '''
    pass