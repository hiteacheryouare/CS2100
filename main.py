"""temperature converter"""

COLD_THRESHOLD = 0
HOT_THRESHOLD = 25

def convert_fahrenheit_to_celsius(temp_farh: float) -> float:
    """
    Converts fahrenheit to celcius
    paramters:
        temp_farh (flot) the starting temp
    returns:
        float that is the temperature in celcius
    """
    return (temp_farh - 32) * (5/9)

def main() -> None:
    """prompts for temp in farenhiet and converts to celcius"""
    temp_farh_str = input("gimme temp in F: ")
    while not temp_farh_str.isdecimal():
        temp_farh_str = input("gimme a number not something else dummy")
    temp_farh = float(temp_farh_str)
    temp_cel = convert_fahrenheit_to_celsius(temp_farh)
    print(f"yeah you dummy that temp in cel is {round(temp_cel, 2)} how could you not know that")
    if temp_cel <= COLD_THRESHOLD:
        print("have fun freezing to death")
    elif temp_cel >= HOT_THRESHOLD:
        print("have fun melting to death")
    else:
        print("have fun being mediocore")


if __name__ == "__main__":
    main()
