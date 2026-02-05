'''
    CS2100
    Spring 2026
    
    Starter code for 2/5/26.

    In class together, we will:
    - practice codewalking by answering Laney's questions about the code
    - practice codewalking by asking Laney questions about the code
    - finish up any code we still need to write!
'''


from collections.abc import Callable
from typing import Any
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import is_integer_dtype

ADMFILE = "./admission_rate.csv"
TUIFILE = "./tuition.csv"
COLS = ["admission", "tuition"]

def normalize_df(column: pd.Series) -> pd.Series:
    ''' apply min-max normalization on a DF column

        Parameters: 
            column, a Pandas Series (column of a dataframe) with numeric data
        
        Returns: 
            a Pandas Series, the same data we started with, but with min/max normalization applied
       '''
    return (column - column.min()) / (column.max() - column.min())

def convert_currency(column: pd.Series) -> pd.Series:
    ''' convert a column with $xx,xxx strings to xxxxx strings, cleaning up the currency notations.
     
        Parameters:
            column, a Pandas Series (dataframe column) with strings of the form $xx,xxx
        
        Returns:
            a Pandas Series with $xx,xxx converted to xxxxx, but still a string
    
    '''
    new_col = column.str.replace('$', '', regex = False).str.replace(',', '', regex = False)
    return new_col

def plot_cols(df: pd.DataFrame, cols: list[str], plot_func: Callable[..., Any] = plt.plot,
              **kwargs) -> None:
    ''' plot the columns given in the dataframe as separate lines on a line plot
     
        Parameters:
            df, a Pandas DataFrame, the entire dataframe for plotting
            cols, a list of strings, the column names from the dataframe to plot
            plot_func, type Callable[..., Any],
                the matplotlib function to call on each column (defaults to plt.plot)
            **kwargs, the keyword arguments that could include customizations for matplotlib

        Returns:
            None, creates and renders the plot
    '''
    colors = kwargs.pop("color", None)
    labels = kwargs.pop("labels", None)
    for index, col in enumerate(cols):
        plot_func(df[col], color = colors[index] if colors else None,
                  label = labels[index] if labels else None)
    title = kwargs.pop("title", None)
    xlabel = kwargs.pop("xlabel", None)
    ylabel = kwargs.pop("ylabel", None)
    legend = kwargs.pop("legend", False)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if legend:
        plt.legend()
    plt.show()


def main() -> None:
    ''' process and merge two dataframes of northeastern data for tuition $$ 
        and acceptance rates. Normalize the data so we can compare them.
        Compute the similarity measure between any two years. '''

    adm_df = pd.read_csv(ADMFILE)
    tui_df = pd.read_csv(TUIFILE)
    print(f"Here are the two dataframes:\n {adm_df.head()} \n {tui_df.head()}")

    # Rename columns to be concise and more readable
    adm_df.rename(columns = {"Admission Rate (Total)" : "admission"}, inplace = True)
    tui_df.rename(columns = {"Living On Campus" : "tuition"}, inplace = True)
                
    # oh no the $$ are not numeric :( 
    if is_integer_dtype(tui_df["tuition"]):
        print("Tuition is an int!")
    else:
        print("Tuition is not an int, we better convert it.")

    # improve the $$ values - turn $xx,xxx into xxxxx and make numeric
    tui_df["tuition"] = convert_currency(tui_df["tuition"])
    tui_df["tuition"] = pd.to_numeric(tui_df["tuition"])
    print(f"After conversion, what is dtype of tuition? ... {tui_df['tuition'].dtype}")

    # merge the two DFs together
    combo_df = adm_df.merge(tui_df, on = "Year")

    # Plot tuition and admission as line plots
    # It looks like tuition stayed flat while admission when up lololol
    plot_cols(combo_df, COLS)

    # Let's normalize, using the function we wrote
    # (we can pass a function to a function!!!!)
    combo_df[COLS] = combo_df[COLS].apply(normalize_df)
    print(combo_df[["admission", "tuition"]].head())

    # normalize using a lambda instead!


    # Plot the normalized data
    plot_cols(combo_df, COLS, plot_func = plt.plot, title = "NU Tuition vs Admission Rate",
              xlabel = "Year", ylabel = "Normalized Values", color = ["firebrick", "black"],
              labels = ["Admission Rate (normalized)", "Tuition (normalized)"],
              legend = True)
    
    # kwargs is super flexible. All of these options work! Un-comment one and try :)
    # plot_cols(combo_df, COLS, plot_func = plt.plot, title = "NU Tuition vs Admission Rate")
    # plot_cols(combo_df, COLS, plot_func = plt.plot, title = "NU Tuition vs Admission Rate",
    #           xlabel = "Year", ylabel = "Normalized Values")
    #        xlabel = "Year", ylabel = "Normalized Values", color = ["firebrick", "black"])

if __name__ == "__main__":
    main()
