'''
    CS2100
    Spring 2026

    Starter code for class on 2/4/26

    Make sure you install matplotlib in your virtual env!

    So far, this code...
    - reads from the all_games.csv file into a dataframe
    - creates a DF view that's all the BOS vs. NY games
    - makes a bar plot that needs to be improved!
    - is ready to call three versions of a function that we'll write

    In class, we'll...
    - improve the bar plot (customizations, xticks, legend)
    - write the three versions of the plot function we're calling

'''

from typing import Optional, Any
from collections.abc import Callable
import pandas as bamboo
import numpy as numbers
import matplotlib.pyplot as graph


GAMEFILE = "all_games.csv"

def plot_hockey_v1(y_values: bamboo.Series, plot_func: Callable[..., Any] = graph.plot) -> None:
    '''
            V1 of plotting some hockey data. In this version, our function
            takes in just y_values as a parameter, a pd.Series, 
            plus the particular plotting function to use. This version's constraints:
                1. can only do plot functions that take y_values only, with no 
                x_values (plt.plot() and plt.hist())
                2. no customizations are included here, it just plots the line
                
            Params:
                y_values (pd.Series), the y values to plot
                plot_func (Callable[..., Any]), the matplotlib function to use for plotting,
                    defaults to plt.plot
            
            Returns: 
                none, just plots
        '''
    plot_func(y_values)
    graph.show
    


def plot_hockey_v2(y_values: bamboo.Series, x_values: Optional[bamboo.Series], plot_func: Callable[..., Any] = graph.plot) -> None:
    '''
            Call the given plotting function and plot the values. 
            In this version, our function takes in both x_values (opt) and y_values (req)
            plus the particular plotting function to use. This version's constraints:
                1. no customizations are included here, it just plots the line
                
            Params:
                y_values (pd.Series), the y values to plot
                x_values (pd.Series), the x values to plot - Optional.  
                plot_func (Callable[..., Any]), the matplotlib function to use for plotting.
                    defaults to plt.plot
        
            Returns: 
                none, just plots. If x values are not included, then we plot just the
                y values.
        '''
    if x_values is not None:
        plot_func(x_values, y_values)
        graph.show()
    else:
        plot_func(y_values)
        graph.show()


def plot_hockey_v3(y_values: bamboo.Series, x_values: Optional[bamboo.Series] = None, plot_func: Callable[..., Any] = graph.plot, **kwargs) -> None:
    '''
            Call the given plotting function and plot the values. 
            In this version, our function takes in both x_values (opt) and y_values (req)
            plus the particular plotting function to use. 
            This version's improvements... can pass in additional arguments to perfect the plot!
                
            Params:
                y_values (pd.Series), the y values to plot
                x_values (pd.Series), the x values to plot - Optional.  
                plot_func (Callable[..., Any]), the matplotlib function to use for plotting,
                    defaults to plt.plot
                kwargs - additional arguments to pass to the plotting function for customization
        
            Returns: 
                none, just plots. If x values are not included, then we plot just the
                y values.
        '''
    if x_values is not None:
        plot_func(x_values, y_values)   
    else:
        plot_func(y_values)
    title = kwargs.pop("title", None)
    xlabel = kwargs.pop("xlabel", None)
    ylabel = kwargs.pop("ylable", None)
    graph.show()
 
    
def main() -> None:
    ''' Read in the CSV file and make some plots! '''
    df = bamboo.read_csv(GAMEFILE)
    df["total_goals"] = df["home_goal_count"] + df["visiting_goal_count"]

    # Games that were Boston vs. NY (either could be home or away)
    # Bos is team #1, NY is team #4
    teams = [1, 4]
    bos_vs_ny = df[
        df["home_team"].isin(teams) &
        df["visiting_team"].isin(teams)
    ]

    # make a bar plot, just on its own
    # Goals scored by the home team in those Bos vs NY games
    bos_home = bos_vs_ny[bos_vs_ny["home_team"] == 1].sort_values(by = "game_number")
    x_pos = numbers.arange(len(bos_home))
    width = 0.35
    graph.bar(x_pos - width / 2, bos_home["home_goal_count"], width = width, label="BOS")
    graph.bar(x_pos + width / 2, bos_home["visiting_goal_count"], width=width, label="NY")
    graph.xlabel("Game Number")
    graph.ylabel("Number of Goals")
    graph.title("NY @ BOS Number of Goals per Team")
    graph.legend()
    graph.xticks(x_pos, bos_home["game_number"].astype(str).tolist())
    graph.show()

    # call the first version of our plotting function
    # we can call this twice -- once to make a histogram and once to make
    # a line plot (we leave out the plot_func argument when plt.plot is
    # our goal, because plt.plot is the default!)
    plot_hockey_v1(df["attendance"], plot_func = graph.hist)
    plot_hockey_v1(bos_vs_ny["total_goals"])

    # call the second version of our plotting function
    # we call this three times -- a histogram, a line plot, a scatterplot
    # (when we want the line plot using plt.plot, we don't pass an argument
    # for plot_func, b/c plt.plot is the default!)
    plot_hockey_v2(df["attendance"], plot_func = graph.hist)
    plot_hockey_v2(bos_vs_ny["total_goals"])
    plot_hockey_v2(df["home_goal_count"], x_values = df["attendance"],
                    plot_func = graph.scatter)

    # call the third version of our plotting function
    # we call this three times -- a histogram, a line plot, a scatterplot
    # (when we want the line plot using plt.plot, we don't pass an argument
    # for plot_func, b/c plt.plot is the default!)
    # plot_hockey_v3(df["attendance"], plot_func = plt.hist, 
    #                title = "PWHL Attendance over Time (2023-2025)",
    #                xlabel = "Attendance Range",
    #                ylabel = "Number of Games")

    # plot_hockey_v3(bos_vs_ny["total_goals"], title = "PWHL Boston vs. NY",
    #                xlabel = "Game Number",
    #                ylabel = "Total Goals")

    # plot_hockey_v3(df["home_goal_count"], x_values = df["attendance"], 
    #                plot_func = plt.scatter, title = "PWHL Attendance v. Home Goals",
    #                xlabel = "Attendance",
    #                ylabel = "Goals by Home Team")


if __name__ == "__main__":
    main()
