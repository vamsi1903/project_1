# import libraries
import requests
import json
from tkinter import *

#create an object
root = Tk()

# creating the Box 
root.title("Covid-19")

# Determining the size of the Box 
root.geometry('220x70')

# Including labels 
lbl = Label(root, text="Total active cases:-......")
lbl.grid(column=1, row=0)

lbl1 = Label(root, text="Total confirmed cases:-...")
lbl1.grid(column=1, row=1)

lbl2 = Label(root, text="")
lbl2.grid(column=1, row=3)

# Function to open url and get the data from api
def clicked():
    url = "https://api.covid19india.org/data.json"
    page = requests.get(url)
    data = json.loads(page.text)

    lbl.configure(text="Total active cases:-" + data["statewise"][0]["active"])

    lbl1.configure(text="Total Confirmed cases:-" + data["statewise"][0]["confirmed"])

    lbl2.configure(text="Data refreshed")

# Create a refresh button
btn = Button(root, text="Refresh", command=clicked)
btn.grid(column=2, row=0)

# infinite loop
root.mainloop() 