# Libraries
import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import time

# Load bus route data from CSV files
lists_k = []
df_k = pd.read_csv("Kerala.csv")
for i, r in df_k.iterrows():
    lists_k.append(r["Route_name"])

lists_A = []
df_A = pd.read_csv("AP.csv")
for i, r in df_A.iterrows():
    lists_A.append(r["Route_name"])

lists_T = []
df_T = pd.read_csv("Telungana.csv")
for i, r in df_T.iterrows():
    lists_T.append(r["Route_name"])

lists_g = []
df_G = pd.read_csv("Goa.csv")
for i, r in df_G.iterrows():
    lists_g.append(r["Route_name"])

lists_R = []
df_R = pd.read_csv("Rajasthan.csv")
for i, r in df_R.iterrows():
    lists_R.append(r["Route_name"])

lists_SB = []
df_SB = pd.read_csv("SouthBengal.csv")
for i, r in df_SB.iterrows():
    lists_SB.append(r["Route_name"])

lists_H = []
df_H = pd.read_csv("Haryana.csv")
for i, r in df_H.iterrows():
    lists_H.append(r["Route_name"])

lists_AS = []
df_AS = pd.read_csv("Assam.csv")
for i, r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

lists_UP = []
df_UP = pd.read_csv("UttraPradhesh.csv")
for i, r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

lists_WB = []
df_WB = pd.read_csv("WestBengal.csv")
for i, r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])

slt.set_page_config(layout="wide")

# Load the image
image = "E:\Screenshot 2024-10-07 084155.png"
slt.image(image, use_column_width=True)

# Streamlit navigation menu
web = option_menu(menu_title="Welcome to 𝒓𝒆𝒅𝑩𝒖𝒔.𝒊𝒏",
                  options=["Home", "States and Routes", "About"],
                  icons=["house", "map", "info-circle"],
                  orientation="horizontal")

# Home page setting
if web == "Home":
    slt.title("BOOK BUS TICKETS ONLINE")
    slt.markdown("redBus is India's largest brand for online bus ticket booking and offers an easy-to-use online bus and train ticket booking; with over 36 million satisfied customers, 3500+ bus operators to choose from, and plenty of offers on bus ticket booking, redBus makes road journeys super convenient for travellers. A leading platform for booking bus tickets, redBus has been the leader in online bus booking over the past 17 years across thousands of cities and lakhs of routes in India.")
    slt.markdown("Booking a bus ticket online on the redBus app or website is very simple. You can download the redBus app or visit redbus.in and enter your source, destination & travel date to check the top-rated bus services available. You can then compare bus prices, user ratings & amenities, select your preferred seat, boarding & dropping points and pay using multiple payment options like UPI, debit or credit card, net banking and more. With redBus, get assured safe & secure payment methods and guaranteed travel with the best seat and bus operator of your choice. Once the bus booking payment is confirmed, all you have to do is pack your bags and get ready to travel with the m-ticket, which you can show to the bus operator on your mobile before boarding the bus. Online bus ticket booking with redBus is that simple!")
    slt.markdown("redBus also offers other exclusive benefits on online bus tickets like flexible ticket rescheduling options, easy & friendly cancellation policies, and instant payment refunds. With a live bus tracking feature, you can plan travel and never miss the bus. You can get the cheapest bus tickets by availing the best discounts for new & existing customers. With redDeals, you can also get exclusive & additional discounts on your online bus ticket booking. You will get 24/7 customer support on call, chat & help to resolve all your queries in English & local languages.")
    slt.markdown("redBus offers Primo bus services, specially curated by redBus, which have highly rated buses and best-in-class service. With Primo by redBus, you can be assured of safe, comfortable, and on-time bus service at no additional cost. With multiple boarding and dropping points available across all major cities in India, you can select at your convenience and enjoy a smooth travel experience.")
    slt.markdown("redBus operates in six countries, including India, Malaysia, Singapore, Indonesia, Peru, and Colombia. Through its website and app, it has sold over 220 million bus tickets worldwide. With over 36 million satisfied customers, redBus is committed to providing its users with a world-class online bus booking experience.")
    slt.markdown("redBus offers bus tickets from some of the top private bus operators, such as Orange Travels, VRL Travels, SRS Travels, Chartered Bus, and Praveen Travels, and state government bus operators, such as APSRTC, TSRTC, GSRTC, Kerala RTC, TNSTC, RSRTC, UPSRTC, and more. With redBus, customers can easily book bus tickets for different bus types, such as AC/non-AC, Sleeper, Seater, Volvo, Multi-axle, AC Sleeper, Electric buses, and more.")
    slt.video("https://youtu.be/yPaODwsLpf4?si=q9ILzHz5FxvsYsOb")
    

# About page
if web == "About":
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":blue[Domain:]  Transportation")
    slt.subheader(":blue[Ojective:] ")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    slt.subheader(":blue[Overview:]") 
    slt.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data...")
    slt.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
    slt.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                    and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    slt.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    slt.subheader(":blue[Skill-take:]")
    slt.markdown("Selenium, Python, Pandas, MySQL,mysql-connector-python, Streamlit.")
    slt.subheader(":blue[Developed-by:]  Karan Kumar M")

# States and Routes page setting
if web == "States and Routes":
    S = slt.selectbox("Lists of States", ["Kerala", "Andhra Pradesh", "Telungana", "Goa", "Rajasthan",
                                          "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"])

    # Define the common function to filter and display results
    def type_and_fare(state, bus_type, fare_range, rating, departure_time):
        conn = mysql.connector.connect(host="localhost", user="root", password="@Karan549", database="redbus_project")
        my_cursor = conn.cursor()

        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:  # 2000 and above
            fare_min, fare_max = 2000, 10000  

        # Define time range based on departure_time
        if departure_time == "Before 6 am":
            time_condition = "HOUR(Start_time) < 6"
        elif departure_time == "6 am to 12 pm":
            time_condition = "HOUR(Start_time) >= 6 AND HOUR(Start_time) < 12"
        elif departure_time == "12 pm to 6 pm":
            time_condition = "HOUR(Start_time) >= 12 AND HOUR(Start_time) < 18"
        else:  # After 6 pm
            time_condition = "HOUR(Start_time) >= 18"

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT Route_name, Bus_name, Bus_type, Start_time, Total_duration, End_time,
            Ratings, Seats_Available, Price FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{state}"
            AND {bus_type_condition} 
            AND Ratings >= {rating}  -- Filter by the selected rating
            AND {time_condition}
            ORDER BY Price
        '''
        my_cursor.execute(query)
        out = my_cursor.fetchall()
        conn.close()

        df = pd.DataFrame(out, columns=[
            "Route_name", "Bus_name", "Bus_type", "Start_time", "Total_duration", "End_time",
            "Ratings", "Seats_Available", "Price"
        ])
        return df

    # Select route based on state
    if S == "Kerala":
        K = slt.selectbox("List of routes", lists_k)
    elif S == "Andhra Pradesh":
        A = slt.selectbox("List of routes", lists_A)
    elif S == "Telungana":
        T = slt.selectbox("List of routes", lists_T)
    elif S == "Goa":
        G = slt.selectbox("List of routes", lists_g)
    elif S == "Rajasthan":
        R = slt.selectbox("List of routes", lists_R)
    elif S == "South Bengal":
        SB = slt.selectbox("List of routes", lists_SB)
    elif S == "Haryana":
        H = slt.selectbox("List of routes", lists_H)
    elif S == "Assam":
        AS = slt.selectbox("List of routes", lists_AS)
    elif S == "Uttar Pradesh":
        UP = slt.selectbox("List of routes", lists_UP)
    elif S == "West Bengal":
        WB = slt.selectbox("List of routes", lists_WB)

    # Creating the 4 columns for bus type, fare range, ratings, and departure time
    col1, col2, col3, col4 = slt.columns(4)

    with col1:
        select_type = slt.selectbox("Choose Bus Type", ("sleeper", "semi-sleeper", "others"))

    with col2:
        select_fare = slt.selectbox("Choose Bus Fare Range", ("50-1000", "1000-2000", "2000 and above"))

    with col3:
        select_departure_time = slt.selectbox("Departure Time", ("Before 6 am", "6 am to 12 pm", "12 pm to 6 pm", "After 6 pm"))
        
    with col4:
        select_rating = slt.slider("Choose Ratings", 1, 5, 4)

   

    # Using the common function to filter results based on the selected state
    if S in ["Kerala", "Andhra Pradesh", "Telungana", "Goa", "Rajasthan", "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"]:
        selected_route = K if S == "Kerala" else A if S == "Andhra Pradesh" else T if S == "Telungana" else G if S == "Goa" else R if S == "Rajasthan" else SB      if S == "South Bengal" else H if S == "Haryana" else AS if S == "Assam" else UP if S == "Uttar Pradesh" else WB
        
        df_result = type_and_fare(selected_route, select_type, select_fare, select_rating, select_departure_time)
        slt.dataframe(df_result)

