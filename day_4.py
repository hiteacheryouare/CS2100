'''
CS2100
Spring 2026
Starter code from class -- 1/12/26
This code is also available on github for some git-command practice!
* On a browser, go to https://github.com/laneystrange/cs2100-scratch
* Click on "code", then the SSH tab, then "copy"
* In VSCode, type "git clone" and then paste what's copied
This program prompts the user for the daily mileage of two runners and compares
them.
In this starter version, we use lists to maintain and analyze the runners'
data:
* List 1 -- dates we're tracking
* List 2 -- Laney's mileage
* List 3 -- Nate's mileage
The lists are all the same length and the values at a given index correspond
with each other.
For example, if the lists contain...
dates = ["JAN 06", "JAN 07"]
laney_mileage = [4, 5]
nate_mileage = [0, 8]
... then, we know that on January 6th, Laney ran 4 miles and Nate ran 0 miles.
In class, we'll see how dictionaries can be a different (better??) way to
organize this data.
'''
TOTAL_MILES_LOC = 0
AVG_DAILY_LOC = 1
def gather_mileage_input(name: str, dates: list[str]) -> list[float]:
    ''' prompt the user to enter mileage information, validating values >= 0
    Parameters:
    name (str): who we're collecting data for
    dates (list: str): list of dates to prompt for
    Returns:
    list of mileage on each day
    '''
    miles = []
    for date in dates:
        today_miles = float(input(f"How many miles did {name} run on {date}?\n"))
    while today_miles < 0:
        today_miles = float(input("Enter again, miles can't be negative!\n"))
        miles.append(today_miles)
    return miles
def generate_mileage_stats(miles: list[float]) -> dict[str, float]:
    ''' compute basic stats from a mileage list: total, avg daily, max
    return a dictionary with stat : value pairs
    Parameters:
    miles (list[float]): a list containing a runner's mileage per-day
    Returns:
    dict[str, float]: summary stats for total miles and avg daily miles for that
    runner
    '''
    stats = {}
    stats["total miles"] = sum(miles)
    stats["avg daily"] = (sum(miles) / len(miles))
    return stats
def main() -> None:
    ''' create lists for Laney and Nate's last week of running and compute stats
    about them '''
    dates = ["JAN 7", "JAN 8", "JAN 9", "JAN 10", "JAN 11"]
    laney_miles = gather_mileage_input("Laney", dates)
    nate_miles = gather_mileage_input("Nate", dates)
    # Compute basic stats about the week of running for each person
    laney_stats = generate_mileage_stats(laney_miles)
    nate_stats = generate_mileage_stats(nate_miles)
    # report the stats
    for k,v in laney_stats.items():
        print(f"{k}...{v}")
    for k,v in nate_stats.items():
        print(f"{k}...{v}")
    # follow-up on a specific date, what does the user want to know?
    month, day = input("Which day do you want to know about? Enter as MMM DD\n").upper().split()
    while not month.isalpha() or not day.isdigit():
        month, day = input("Please enter as MMM DD\n").upper().split()
        date = " ".join([month, f"{int(day):02d}"])
    if date not in dates:
        print(f"Sorry, we don't have data for {date}\n")
        return
    index = dates.index(date)
    print(f"Laney's mileage that day: {laney_miles[index]}")
    print(f"Nate's mileage that day: {nate_miles[index]}")


main()
