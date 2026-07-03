import math
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

    if look == "help":
        print("help - command page")
        print()
        print("show - displays table data by page")
        print()
        print("search - search for customer by name or id")
        print()
        print("sentiment - sentiment data")
        print()
        print("end - end program\n")

    elif look == "show":
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
        #counts amount of each given senitment type
        ver_pos = len(df[df["Sentiment"] == "Very Positive"]) #alternativly could use:  ver_pos = (df["Sentiment"] == "Very Positive").sum()
        pos = len(df[df["Sentiment"] == "Positive"]) 
        neut = len(df[df["Sentiment"] == "Neutral"]) 
        neg = len(df[df["Sentiment"] == "Negative"]) 
        ver_neg = len(df[df["Sentiment"] == "Very Negative"]) 

        sentiments = df["Sentiment"].value_counts()

        print(sentiments)


    elif look == "search":
        customer = df[["Customer Name", "ID"]]

        for index, row in customer.iterrows(): 
            name = row["Customer Name"]
            customer_id = row["ID"] 
    
            print(name) 
            print(customer_id) 
            print()