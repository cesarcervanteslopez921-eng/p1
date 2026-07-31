import math
import re #implemented to help me search of ID's due to their unique syntax
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

df = pd.read_excel(
    "data/Call-Center-Sentiment-Sample-Data.xlsx",
    header=5
    )
df = df.loc[:, ~df.columns.str.contains("^Unnamed")] #the "~" is removing what im searching for in this case Unnamed metadata that cluters
df = df.dropna(how="all") #to remove empty rows

page_size = 10


print("Type 'help' for list of commands.\n")

@app.route("/")
def home():
        return render_template("index.html")


# while True:
#     look = input("Enter a Valid Command: ").strip().lower()

#     if look == "help": #Displays basic help page
#         print("help - command page")
#         print()
#         print("show - displays table data by page")
#         print()
#         print("search - search for customer by name or id")
#         print()
#         print("sentiment - sentiment data")
#         print()
#         print("end - end program\n")


@app.route("/show")
def show():
        current_page = request.args.get("page", default=1, type=int)
        total_pages = math.ceil(len(df) / page_size)

        start = (current_page - 1 ) * page_size
        end = start + page_size

        rows = df.iloc[start:end].to_dict(orient="records") # used to convert the rows into a dictionary that html understands
        


        return render_template("show.html", rows=rows, current_page=current_page, total_pages=total_pages)

#     elif look == "show": #shows the first 10 entries of data set allowing you to cycle through and select specific pages
#         current_page = 0
#         total_pages = math.ceil(len(df) / page_size) #calculates the amount of pages in dataset  by 10 per page

#         while True:
#             start = current_page * page_size
#             end = start + page_size

#             print(f"\nPage {current_page + 1} of {total_pages}") # says what page of the data is currently being viewed
#             print(df.iloc[start:end].to_string(index=False))

#             page = input("[n]next, [p]previous, [s]search, or exit\n").strip().lower() #navigation between the different pages

#             if page == "n": #adds 1 to page count to display the next subsequent set of data
#                 if current_page < total_pages - 1:
#                     current_page += 1
#                 else:
#                     print("On Last Page")

#             elif page == "p": #subtracts 1 to page count to display the next subsequent set of data
#                 if current_page > 0:
#                     current_page -= 1
#                 else:
#                     print("On First Page")

#             elif page =="s": #allows the user to go to a specific page
#                 try: #stops error from occuring when user inputs non number
#                     num_page = int(input(f"enter a page number from 1 to {total_pages}\n"))
#                 except ValueError:
#                     print("please enter a VALID NUMBER.")
#                     continue

#                 if num_page <= 0: #sets the page to the 1st page when trying to set page to a negative or 0
#                     num_page = 1

#                 elif num_page > total_pages: #sets page to last page when trying to input a big number
#                     num_page = total_pages

#                 current_page = num_page - 1

#             elif page == "exit":
#                 break

#             else:
#                 print("Enter Valid Navigation\n")
#                 cont = input("Press enter to continue.")
        

@app.route("/sentiment")
def sentiment():
        return render_template("sentiment.html")
#     elif look == "sentiment":
#         while True:
#             print("\n=== Sentiment Menu ===")
#             print("1. Overall Sentiment Summary")
#             print("2. Call Center Sentiment Report")
#             print("3. Return to Main Menu\n")

#             section = input("Select an option to view: ").strip()
#             print("")


#             if section == "1":

#                 print("\nSentiment Summary")
#                 print("-----------------------")

#                 total = len(df) #gets the length of the data
#                 for sentiment, count in df["Sentiment"].value_counts().items(): #counts the amount of each type of sentiment in the data frame to use for later
#                     percent = (count / total) * 100 #uses the previous info to calculate the percent of how often a certaion sentiment appears
#                     print(f"{sentiment:<15}: {count:>3} - ({percent:.2f}%)") #formating of info to make readable 


#             elif section == "2":
#                 while True:
#                     call_center = input("Enter call center location: ").strip()
#                     print("")

#                     #This is done so when search "CA" i get only california and not chicago that has a "ca" in its spelling
#                     if len(call_center) == 2: #when its 2 letters it is only looking at the state abbreviation and not city spelling

#                         location = df[
#                             (df["Call Center"].str.split("/").str[1].str.upper() == call_center.upper())   
#                         ]
#                     else: #searches the entire city spelling
#                         location = df[
#                             df["Call Center"].str.split("/").str[0].str.contains(call_center, case=False, na=False)
#                         ]

#                     if location.empty:
#                         print("No Call Center in city/state, try again.")
#                         print("")

#                     else:
#                         total = len(location) #shows the data for the specific location based on where the user wanted to search for
#                         for sentiment, count in location["Sentiment"].value_counts().items():
#                             percent = (count / total) * 100
#                             print(f"{sentiment:<15}: {count:>3} - ({percent:.2f}%)")

#                         break

            
#             elif section == "3":
#                 break

#             else:
#                 print("Invalid Option, Try Again")

#             print("")
#             cont = input("Press enter to continue.")


@app.route("/search")
def search():
        return render_template("search.html")
#     elif look == "search":
#         cx = input("Enter customer name or ID: ").strip()

#         if re.fullmatch(r"[A-za-z]{3}-\d{8}", cx): #checks for it to contain 3 letters of any capitalization, a dash, and then exactly 8 numbers as per the syntax of the ID's
#             result = df[df["ID"].str.upper() == cx.upper()]
        
#         else: #still searches bgut by name this time not ID
#             result = df[df["Customer Name"].str.contains(cx, case=False, na=False)] #case=False ignores capitalization when searching dataframe / na=False has it ignore cases of NaN

#         if result.empty:
#             print("No Customer Found.\n")
        
#         else: #shows info of person found based on search parameters
#             print(result.to_string(index=False))

#     elif look == "end":
#         break #ends the program

#     else:
        print("")
        print("Please Enter a valid Command, type 'help' for list of commands.")


if __name__ == "__main__":
        app.run(debug=True)