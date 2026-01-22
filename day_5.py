'''
   CS2100
   Spring 2026
   Starter code for class on 1/21/26

   This is roughly the same as the code we finished with on Wednesday 1/14, 
   and we prompt the user for some running data for Nate & Laney,
   and then generate some stats

    On Wednesday 1/21, we want to add a function similar to gather_mileage_input,
    but it should read from a file instead of prompting the user .We'll need:
    - the files to read from, laney_stats.txt and nate_stats.txt in the same directory
    - when we read from files, just like with input(), we have strings unless
      we tell Python otherwise
    - with open as(filename, "r", encoding = "utf-8") as infile
    - infile.readlines() or infile.readline() 
    - split() turns a string into a list
'''

from typing import Optional
LANEYFILE = 'laney_stats.txt'
NATEFILE = 'nate_stats.txt'

def read_milage_input(filename: str) -> dict[str, float]:
    """read user milage data from a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        dateline = f.readline()
        mileline = f.readline()
        if not dateline or not mileline:
            raise IOError("PANIC OVERLOAD@!!!!!! give up now.")
        dates = dateline.strip().split(',')
        miles = mileline.split(',')
        stats = {}
        for date, mile in zip(dates, miles):
            stats[date] = float(mile)
        return stats



def gather_mileage_input(name: str, dates: list[str]) -> dict[str, float]:
    ''' prompt the user to enter mileage information, validating values >= 0
  
       Parameters:
           name (str): who we're collecting data for
           dates (list: str): list of dates to prompt for
      
       Returns:
           a dictionary [str, float] where key = date, value = mileage on that date
      
    '''
    miles = {}
    for date in dates:
        today_miles = float(input(f"How many miles did {name} run on {date}?\n"))
        while today_miles < 0:
            today_miles = float(input("Enter again, miles can't be negative!\n"))
        miles[date] = today_miles
    return miles


def generate_mileage_stats(miles: Optional[dict[str, float]]) -> Optional[dict[str, float]]:
    ''' compute basic stats from a mileage list: total, avg daily
        return a dictionary with stat : value pairs
  
       Parameters:
           miles (list[float]): a list containing a runner's mileage per-day, or None
      
       Returns:
           dict[str, float]: summary stats for total miles and avg daily miles for that runner, or None
                if none/empty dictionary given
        
        Raises:
            ValueError if any miles are negative
    '''
    if not miles:
        return None
    if any(mileage < 0 for mileage in miles.values()):
        raise ValueError("Miles can't be negative :(")
    stats = {}
    stats["total miles"] = sum(miles.values())
    stats["avg daily"] = sum(miles.values()) / len(miles.values())
    return stats

def print_summary(name: str, stats: dict[str, float]) -> None:
    ''' print a summary of the stats in the given dictionary 
    
        parameters:
            name (str), the name of the runner
            stats (dict of str, float), the stats for the runner's summary
        returns:
            none, just prints
    '''
    print(f"Running stats for {name}:")
    for key, value in stats.items():
        print(f"{key}...{value}")
    print()

def main() -> None:
    ''' create lists for Laney and Nate's last week of running and compute stats about them '''

    dates = ["JAN 07", "JAN 08", "JAN 09", "JAN 10", "JAN 11"]
    laney_miles = gather_mileage_input("Laney", dates)
    nate_miles = gather_mileage_input("Nate", dates)

    # Compute basic stats about the week of running for each person
    laney_stats = generate_mileage_stats(laney_miles)
    nate_stats = generate_mileage_stats(nate_miles)

    # Report the stats from their dictionaries
    if laney_stats:
        print_summary("Laney", laney_stats)
    if nate_stats:
        print_summary("Nate", nate_stats)

     # follow-up on a specific date, what does the user want to know?
    month, day = input("Which day do you want to know about? Enter as MMM DD\n").upper().split()
    while not month.isalpha() or not day.isdigit():
        month, day = input("Please enter as MMM DD\n").upper().split()

    date = " ".join([month, f"{int(day):02d}"])
    if date not in dates:
        print(f"Sorry, we don't have data for {date}\n")
        return

    print(f"Laney's mileage that day: {laney_miles[date]}")
    print(f"Nate's mileage that day: {nate_miles[date]}")

if __name__ == "__main__":
    main()
