import math
import re #implemented to help me search of ID's due to their unique syntax
import pandas as pd 
df = pd.read_excel(
    "data/Call-Center-Sentiment-Sample-Data.xlsx",
    header=5
    )
df = df.loc[:, ~df.columns.str.contains("^Unnamed")] #the "~" is removing what im searching for in this case Unnamed metadata that cluters
df = df.dropna(how="all") #to remove empty rows

page_size = 10


print("Type 'help' for list of commands.\n")

while True:
    look = input("Enter a Valid Command: ").strip().lower()

    if look == "help": #Displays basic help page
        print("help - command page")
        print()
        print("show - displays table data by page")
        print()
        print("search - search for customer by name or id")
        print()
        print("sentiment - sentiment data")
        print()
        print("end - end program\n")


    elif look == "show": #shows the first 10 entries of data set allowing you to cycle through and select specific pages
        current_page = 0
        total_pages = math.ceil(len(df) / page_size)

        while True:
            start = current_page * page_size
            end = start + page_size

            print(f"\nPage {current_page + 1} of {total_pages}")
            print(df.iloc[start:end].to_string(index=False))

            page = input("[n]next, [p]previous, [s]search, or exit\n").strip().lower()

            if page == "n":
                if current_page < total_pages - 1:
                    current_page += 1
                else:
                    print("On Last Page")

            elif page == "p":
                if current_page > 0:
                    current_page -= 1
                else:
                    print("On First Page")

            elif page =="s":
                num_page = int(input(f"enter a page number from 1 to {total_pages}\n"))

                if num_page < 0:
                    num_page = 1

                elif num_page > total_pages:
                    num_page = 7

                current_page = num_page - 1

            elif page == "exit":
                break

            else:
                print("Enter Valid Navigation")
        

    elif look == "sentiment":
        while True:
            print("\n=== Sentiment Menu ===")
            print("1. Overall Sentiment Summary")
            print("2. Call Center Sentiment Report")
            print("3. Return to Main Menu\n")

            section = input("Select an option to view: ").strip()
            print("")


            if section == "1":

                print("\nSentiment Summary")
                print("-----------------------")

                total = len(df)
                for sentiment, count in df["Sentiment"].value_counts().items():
                    percent = (count / total) * 100
                    print(f"{sentiment:<15}: {count:>3} - ({percent:.2f}%)")


            elif section == "2":
                while True:
                    call_center = input("Enter call center location: ").strip()
                    print("")

                    if len(call_center) == 2:

                        location = df[
                            (df["Call Center"].str.split("/").str[1].str.upper() == call_center.upper())   
                        ]
                    else:
                        location = df[
                            df["Call Center"].str.split("/").str[0].str.contains(call_center, case=False, na=False)
                        ]

                    if location.empty:
                        print("No Call Center in city/state, try again.")
                        print("")

                    else:
                        total = len(location)
                        for sentiment, count in location["Sentiment"].value_counts().items():
                            percent = (count / total) * 100
                            print(f"{sentiment:<15}: {count:>3} - ({percent:.2f}%)")



                        break

            
            elif section == "3":
                break

            else:
                print("Invalid Option, Try Again")

            print("")
            cont = input("Press enter to continue.")


    elif look == "search":
        cx = input("Enter customer name or ID: ").strip()

        if re.fullmatch(r"[A-za-z]{3}-\d{8}", cx): #checks for it to contain 3 letters of any capitalization, a dash, and then exactly 8 numbers as per the syntax of the ID's
            result = df[df["ID"].str.upper() == cx.upper()]
        
        else:
            result = df[df["Customer Name"].str.contains(cx, case=False, na=False)] #case=False ignores capitalization when searching dataframe / na=False has it ignore cases of NaN

        if result.empty:
            print("No Customer Found.\n")
        
        else:
            print(result.to_string(index=False))