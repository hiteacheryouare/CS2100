'''
    CS2100
    Spring 2026
    Starter code for lecture on Jan 22nd
    
    So far, this code...
    * has a function to read from a file and return a 2d list of strings
    * has stubs to convert that 2d list into a list of tuples, or a dictionary of sets
    * has a main that reads in two files and converts them to the appropriate type

    In class, we'll....
    * write the rest of those function stubs
    * write test code for the file I/O function
'''

from typing import Optional

RACE_RESULTS_FILE = "race_results_2025.txt"
GROUPS_FILE = "groups.txt"

def read_file_to_list(filename: str) -> Optional[list[list[str]]]:
    ''' reads any comma-separated file and returns
        its content, as a 2d list of strings, or None if file is empty

        parameters: fielname, a string

        returns: a 2d list of strings, the contents of the file
                 or None, if the file is empty

        raises:
            FileNotFoundError if file doesn't exist
    '''
    lst = []
    with open(filename, "r", encoding = "utf-8") as infile:   
        for row in infile:
            lst.append(row.strip().split(","))
    if not lst:
        return None
    return lst

def list_to_tuples(lst: Optional[list[list[str]]]) -> Optional[list[tuple[str, ...]]]:
    ''' convert a 2d list of strings to a list of tuples of strings
        ex: [['a', 'b'], ['c', 'd']] ==> [('a', 'b'), ('c', 'd')]
        returns None, if input is None or contains 
                any empty sublists.
        Parameters lst (list[list[str]]): optional 2d list of strings, or None

        Returns list[tuple[str,...]]: optional list of tuples of strings, or None, 
            if input is None or contains any empty sublists.

    '''
    pass

def list_to_sets(lst: Optional[list[list[str]]]) -> Optional[dict[str, set[str]]]:
    ''' convert a 2d list of strings to a dictionary of sets of strings
        ex: [['a', 'b'], ['c', 'd']] ==> {'a' : {'b'}, 'c' : {'d'}}
        returns None if input is None or contains any empty sublists

        Parameters lst (list[list[str]]): optional 2d list of strings, or None

        Returns dict[str, set[str]]]: optional dictionariy with key = str
                and value = set of strings. Or None, if input is None or contains 
                any empty sublists.
        '''
    pass


def main() -> None:
    ''' main reads from both data files and prints out results '''

    results = read_file_to_list(RACE_RESULTS_FILE)
    results_tuples = list_to_tuples(results)
    print(results_tuples)

    groups = read_file_to_list(GROUPS_FILE)
    group_sets = list_to_sets(groups)
    print(group_sets)

if __name__ == "__main__":
    main()

