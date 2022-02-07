#Author - Sam Ou
from tkinter import *
import tkinter as tk
from tkinter import messagebox
# messagebox is for the error boxes i have used

import pandas as pd

# to import the csv file ^^^^
global window

a = int
b = int
c = int
# to ensure all the variables are integers
root = Tk()


def clearTextInput():
    firstclass.delete(0, END)
    firstclass.update()
    firstclassprice.delete(0, END)
    firstclassprice.update()
    economyprice.delete(0, END)
    economyprice.update()
    print(firstclassprice, firstclass, economyprice)


# this is the function for the clear button


def assignvar():
    global first
    first = firstclass.get()
    global second
    second = firstclassprice.get()
    global third
    third = economyprice.get()


# this assigns the string inputs to the integer variables i made before


def depart(*args):
    global departure
    departure = str(clicked.get())
    print(departure)


# this assigns the selection of departure airport to a variable


def arrive(*args):
    global arrival
    arrival = str(clickedinternational.get())
    print(arrival)


# this assigns the selection of arrival airport to a variable

def aircraft_type():
    global aircraft
    aircraft = str(v.get())
    print(aircraft)


# this assigns the selection of airplane from a checkbox to a variable


def calculations():
    # ^^^ this giant definition/function is how the enter button works and how the calculations happen.
    global x, y

    assignvar()
    # using the functions i created earlier to assign inputs to variables
    depart()
    # using the functions i created earlier to assign inputs to variables
    arrive()
    # using the functions i created earlier to assign inputs to variables
    print(first, second, third)
    print("going to", arrival, "from", departure)
    aircraft_type()
    # the text print outs here are to show that the program is functioning correctly

    if aircraft == '0':
        messagebox.showerror("No selection", "Please select aircraft type")
    if first == '':
        messagebox.showerror("Error", "Please enter the number of first class seats")
    if second == '':
        messagebox.showerror("Error", "Please enter the price of a first class seat in £")
    if third == '':
        messagebox.showerror("Error", "Please enter the price of an economy class seat in £")

    # messagebox is the error box to ensure the user enters acceptable values

    def numbers():
        d = firstclass.get()
        e = firstclassprice.get()
        f = economyprice.get()
        if d.isdigit() and e.isdigit() and f.isdigit():
            d, e, f = int(d), int(e), int(f)

            print("There will be", first, "first class seats, at a cost of £", second,
                  "and the economy price will be  £", third)
            return True
        else:
            messagebox.showerror("Invalid Entries", "Please use whole numbers")
            return False
        # this ensures only whole numbers are entered

    result = numbers()
    if not result:
        return
    assert isinstance(first, object)
    first_int = int(first)
    second_int = int(second)
    third_int = int(third)
    # these three variables ^^^ convert the strings to integers
    global distance
    global economy
    global full
    global aircraftcostperseat
    global totalcost
    global flightincome
    global profitloss
    profitloss = 0
    flightincome = 0
    totalcost = 0
    economy = 0
    full = 0
    aircraftcostperseat = 0

    # these variables are set to zero to prevent error codes

    def header(msg):
        print("-" * 50)
        print("[ " + msg + " ]")

    header("Flight Data")
    raw_data = {"Airport Name": ["John F Kennedy International", "Paris-Orly", "Adolfo Suarez Madrid-Barajas",
                                 "Amsterdam Schipol", "Cairo International"],
                "Airport Code": ["JFK", "ORY", "MAD", "AMS", "CAI"],
                "Liverpool John Lennon": [5326, 629, 1428, 526, 3779],
                "Bournemouth International": [5486, 379, 1151, 489, 3584]}
    # in this version of the program, the raw_data is used as you don't have access to the text file but in cases where you do have MY version of the csv file, you can use the other version of the program and it will read the csv file
    df = pd.DataFrame(raw_data,
                      columns=["Airport Name", "Airport Code", "Liverpool John Lennon", "Bournemouth International"])
    # labeling the columns ^^^
    print(df)
    x = 0
    y = 0

    if arrival == str("John F Kennedy Interational"):
        x = 0

    elif arrival == str("Paris-Orly"):
        x = 1

    elif arrival == str("Adolfo Suarez Madrid-Barajas"):
        x = 2

    elif arrival == str("Amsterdam Schipol"):
        x = 3

    elif arrival == str("Cairo International"):
        x = 4

    if departure == str("Bournemouth International"):
        y = 3

    elif departure == str("Liverpool John Lennon"):
        y = 2
    # assigning variables
    print(x, y)
    print(arrival, departure)
    distance = df.iloc[x, y]
    print(distance)

    if aircraft == "1":
        economy = 180 - (first_int * 2)
        full = first_int + economy
        aircraftcostperseat = ((first_int + economy) * 8 * distance / 100) / full
        totalcost = (first_int + economy) * 8 * distance / 100
        flightincome = (first_int * second_int) + (economy * third_int)
        profitloss = flightincome - totalcost

    if aircraft == "2":
        economy = 220 - (first_int * 2)
        full = first_int + economy
        aircraftcostperseat = ((first_int + economy) * 7 * distance / 100) / full
        totalcost = (first_int + economy) * 7 * distance / 100
        flightincome = (first_int * second_int) + (economy * third_int)
        profitloss = flightincome - totalcost

    if aircraft == "3":
        economy = 406 - (first_int * 2)
        full = first_int + economy
        aircraftcostperseat = ((first_int + economy) * 5 * distance / 100) / full
        totalcost = (first_int + economy) * 5 * distance / 100
        flightincome = (first_int * second_int) + (economy * third_int)
        profitloss = flightincome - totalcost

    # all of these are calculations to calculate the profit  ^^^^

    def new_window():

        window = tk.Toplevel(root)
        window.title("Results")
        window.geometry("600x900")
        tk.Label(window, text="Flight Cost per seat").grid(row=1, column=0)
        tk.Label(window, text="Total Flight Cost").grid(row=2, column=0)
        tk.Label(window, text="Flight income").grid(row=3, column=0)
        tk.Label(window, text="Flight Profit").grid(row=4, column=0)
        tk.Label(window, text=aircraftcostperseat).grid(row=1, column=1)
        tk.Label(window, text=totalcost).grid(row=2, column=1)
        tk.Label(window, text=flightincome).grid(row=3, column=1)
        if profitloss > 0:
            tk.Label(window, text=profitloss, fg="#009933").grid(row=4, column=1)
        elif profitloss < 0:
            tk.Label(window, text=profitloss, fg="#ff0000").grid(row=4, column=1)
        tk.Button(window,
                  text='Quit',
                  command=window.quit).grid(row=6,
                                            column=0,
                                            sticky=tk.W,
                                            pady=4)

    # this opens the new window that you see in the program ^^^

    if aircraft == "1" and 0 < first_int < 8:
        messagebox.showerror("Error", "Insufficient First Class Seats, please add more.")
        if window is not None:
            window.quit
    elif aircraft == "2" and 0 < first_int < 10:
        messagebox.showerror("Error", "Insufficient First Class Seats, please add more.")
        if window is not None:
            window.quit
    elif aircraft == "3" and 0 < first_int < 14:
        messagebox.showerror("Error", "Insufficient First Class Seats, please add more.")
        if window is not None:
            window.quit
    elif aircraft == "1" and first_int > 90:
        messagebox.showerror("Error", "Too many first class seats")
        if window is not None:
            window.quit
    elif not (not (aircraft == "2") or not (first_int > 110)):
        messagebox.showerror("Error", "Too many first class seats")
        if window is not None:
            window.quit
    elif aircraft == "3" and first_int > 203:
        messagebox.showerror("Error", "Too many first class seats")
        if window is not None:
            window.quit
    # just a bunch of error boxes for ease of use
    else:
        new_window

    root.quit

    if aircraft == "1":
        if distance > 2650:
            messagebox.showerror("Error",
                                 "This aircraft's range is too low for this trip, please choose another aircraft")
        else:
            new_window()
        full = first_int + economy
        aircraftcostperseat = ((first_int + economy) * 8 * distance / 100) / full
        totalcost = (first_int + economy) * 8 * distance / 100
        flightincome = (first_int * second_int) + (economy * third_int)
        profitloss = flightincome - totalcost
    if aircraft == "2":
        if distance > 5600:
            messagebox.showerror("Error",
                                 "This aircraft's range is too low for this trip, please choose another aircraft")
        else:
            new_window()
        full = first_int + economy
        aircraftcostperseat = ((first_int + economy) * 7 * distance / 100) / full
        totalcost = (first_int + economy) * 7 * distance / 100
        flightincome = (first_int * second_int) + (economy * third_int)
        profitloss = flightincome - totalcost
    if aircraft == "3":
        if distance > 4050:
            messagebox.showerror("Error",
                                 "This aircraft's range is too low for this trip, please choose another aircraft")
        else:
            new_window()
        full = first_int + economy
        aircraftcostperseat = ((first_int + economy) * 5 * distance / 100) / full
        totalcost = (first_int + economy) * 5 * distance / 100
        flightincome = (first_int * second_int) + (economy * third_int)
        profitloss = flightincome - totalcost
        # this ensures that the range of the aircraft is sufficient for the journey

    print("There will be", economy, "economy seats, with a total of", full, "people on board, at a cost of",
          aircraftcostperseat, "per passenger, the total cost is", totalcost, "The flight income will be", flightincome,
          "The airline is making a profit/loss of", profitloss)
    # to ensure the program runs smoothly


root.title("Flight Profitability")
# title of the program

clicked = StringVar()
clicked.set("Bournemouth International")
# set the defaults for the drop down menus

clickedinternational = StringVar()
clickedinternational.set("John F Kennedy International")
# set the defaults for the drop down menus

ukairport = OptionMenu(root, clicked, "Bournemouth International", "Liverpool John Lennon").grid(row=1, column=1)
overseaairport = OptionMenu(root, clickedinternational, "John F Kennedy International", "Paris-Orly",
                            "Adolfo Suarez Madrid-Barajas", "Amsterdam Schipol", "Cairo International").grid(row=2,
                                                                                                             column=1)
# the options for the foreign and domestic airports ^^

tk.Label(root, text="UK Airport").grid(row=1)
tk.Label(root, text="Overseas Airport").grid(row=2)
tk.Label(root, text="Number of First Class Seats").grid(row=3)
tk.Label(root, text="Price of a First Class seat (Whole Numbers only)").grid(row=4)
tk.Label(root, text="Price of a Standard-Class seat (Whole Numbers only").grid(row=5)
tk.Label(root, text="Aircraft Type (Whole Numbers only").grid(row=6)
v = IntVar()
Radiobutton(root, text="Medium Narrow Body", variable=v, value=1).grid(row=6, column=1)
Radiobutton(root, text="Large Narrow Body", variable=v, value=2).grid(row=6, column=2)
Radiobutton(root, text="Medium Wide Body", variable=v, value=3).grid(row=6, column=3)
# a bunch of buttons for the interface
firstclass = tk.Entry(root)
firstclassprice = tk.Entry(root)
economyprice = tk.Entry(root)

firstclass.grid(row=3, column=1)
firstclassprice.grid(row=4, column=1)
economyprice.grid(row=5, column=1)


def combined_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func()


tk.Button(root,
          text='Quit',
          command=root.quit).grid(row=8,
                                  column=0,
                                  sticky=tk.W,
                                  pady=4)

tk.Button(root,
          text='Calculate',
          command=calculations).grid(row=8, column=1)

tk.Button(root,
          text='Clear',
          command=clearTextInput).grid(row=8, column=2)

root.mainloop()
