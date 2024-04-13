# import streamlit as st
# from deta import Deta

# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)
# daily_mood_db = deta.Base("Daily_Mood")

# def enter_daily_mood():
#     st.title("Enter Daily Mood")

#     # Collect daily mood details from user input
#     cto = st.text_input("CTO")
#     meditation = st.text_input("Meditation")
#     mood = st.text_input("Mood")
#     sleep = st.text_input("Sleep")
#     stress = st.text_input("Stress")

#     # Store daily mood details in the Deta Base when the 'Submit' button is clicked
#     if st.button('Submit Mood'):
#         new_mood_record = {
#             "CTO": cto,
#             "Meditation": meditation,
#             "Mood": mood,
#             "Sleep": sleep,
#             "Stress": stress
#         }
#         daily_mood_db.put(new_mood_record)
#         st.success("Daily mood details submitted successfully!")

# if __name__ == "__main__":
#     enter_daily_mood()

# import streamlit as st
# from deta import Deta
# import plotly.graph_objs as go
# import pandas as pd

# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)
# daily_mood_db = deta.Base("Daily_Mood")

# def enter_daily_mood():
#     st.title("Enter Daily Mood")

#     # Collect daily mood details from user input
#     cto = st.text_input("CTO")
#     meditation = st.text_input("Meditation")
#     mood = st.text_input("Mood")
#     sleep = st.text_input("Sleep")
#     stress = st.text_input("Stress")

#     # Store daily mood details in the Deta Base when the 'Submit' button is clicked
#     if st.button('Submit Mood'):
#         new_mood_record = {
#             "CTO": cto,
#             "Meditation": meditation,
#             "Mood": mood,
#             "Sleep": sleep,
#             "Stress": stress
#         }
#         daily_mood_db.put(new_mood_record)
#         st.success("Daily mood details submitted successfully!")

# def plot_daily_mood():
#     st.title("Daily Mood Report")

#     # Fetch daily mood data from the Deta Base
#     mood_data = daily_mood_db.fetch().items

#     # Create DataFrame for easier manipulation
#     df = pd.DataFrame(mood_data)

#     # Process data for plotting
#     mood_columns = ["CTO", "Meditation", "Mood", "Sleep", "Stress"]

#     # Create Plotly traces for bar charts
#     traces = [go.Bar(x=mood_columns, y=df[col].astype(str), name=col) for col in mood_columns]

#     # Create Plotly layout
#     layout = go.Layout(title='Daily Mood Report',
#                        xaxis=dict(title='Factors'),
#                        yaxis=dict(title='Rating'))

#     # Create Plotly figure
#     fig = go.Figure(data=traces, layout=layout)

#     # Display Plotly figure
#     st.plotly_chart(fig)

# if __name__ == "__main__":
#     enter_daily_mood()
#     plot_daily_mood()
# import streamlit as st
# from deta import Deta
# import plotly.graph_objs as go
# import pandas as pd
# from datetime import datetime

# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)
# daily_mood_db = deta.Base("Daily_Mood")

# def enter_daily_mood():
#     st.title("Enter Daily Mood")

#     # Collect daily mood details from user input
#     cto = st.text_input("CTO")
#     meditation = st.text_input("Meditation")
#     mood = st.text_input("Mood")
#     sleep = st.text_input("Sleep")
#     stress = st.text_input("Stress")

#     # Automatically capture the current date
#     date = datetime.now().strftime("%Y-%m-%d")

#     # Store daily mood details in the Deta Base when the 'Submit' button is clicked
#     if st.button('Submit Mood'):
#         new_mood_record = {
#             "Date": date,
#             "CTO": cto,
#             "Meditation": meditation,
#             "Mood": mood,
#             "Sleep": sleep,
#             "Stress": stress
#         }
#         daily_mood_db.put(new_mood_record)
#         st.success("Daily mood details submitted successfully!")

# def plot_daily_mood():
#     st.title("Daily Mood Report")

#     # Fetch daily mood data from the Deta Base
#     mood_data = daily_mood_db.fetch().items

#     # Create DataFrame for easier manipulation
#     df = pd.DataFrame(mood_data)

#     # Process data for plotting
#     mood_columns = ["CTO", "Meditation", "Mood", "Sleep", "Stress"]

#     # Create Plotly traces for bar charts
#     traces = [go.Bar(x=df["Date"], y=df[col].astype(str), name=col) for col in mood_columns]

#     # Create Plotly layout
#     layout = go.Layout(title='Daily Mood Report',
#                        xaxis=dict(title='Date'),
#                        yaxis=dict(title='Rating'))

#     # Create Plotly figure
#     fig = go.Figure(data=traces, layout=layout)

#     # Display Plotly figure
#     st.plotly_chart(fig)

# if __name__ == "__main__":
#     enter_daily_mood()
#     plot_daily_mood()
import streamlit as st
from deta import Deta
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime

DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# Initialize with a project key
deta = Deta(DETA_KEY)
daily_mood_db = deta.Base("Daily_Mood")

style = """
    <style>
    
    @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
        .main{
            background: rgb(255,57,174);
            background: linear-gradient(164deg, rgba(255,57,174,1) 0%, rgba(76,0,255,1) 51%, rgba(254,255,216,1) 100%);
        }
        
        h1{
            font-family: "Poppins", sans-serif;
            font-weight: 700;
            font-style: normal;
            color:#2f0644;
        }
        
        p{
            font-family: "Poppins", sans-serif;
            font-weight: 500;
            font-style: normal;
            color:#2f0644;
        } 
        
        .st-emotion-cache-19rxjzo{
            background-color: white;
        }
    </style>

"""

st.markdown(style, unsafe_allow_html=True)

def enter_daily_mood():
    st.title("Enter Daily Mood")

    # Collect daily mood details from user input
    H_ID = st.text_input("H_ID")
    M_ID = st.text_input("M_ID")
    cto = st.text_input("CTO")
    meditation = st.text_input("Meditation")
    mood = st.text_input("Mood")
    sleep = st.text_input("Sleep")
    stress = st.text_input("Stress")

    # Automatically capture the current date
    date = datetime.now().strftime("%Y-%m-%d")

    # Store daily mood details in the Deta Base when the 'Submit' button is clicked
    if st.button('Submit Mood'):
        new_mood_record = {
            "H_ID":H_ID,
            "M_ID":M_ID,
            "Date": date,
            "CTO": cto,
            "Meditation": meditation,
            "Mood": mood,
            "Sleep": sleep,
            "Stress": stress
        }
        daily_mood_db.put(new_mood_record)
        st.success("Daily mood details submitted successfully!")

def plot_daily_mood():
    st.title("Daily Mood Report")

    # Fetch daily mood data from the Deta Base
    mood_data = daily_mood_db.fetch().items

    if not mood_data:
        st.warning("No data available. Please enter daily mood data.")
        return

    # Create DataFrame for easier manipulation
    df = pd.DataFrame(mood_data)

    # Check if 'Date' column is present
    if 'Date' not in df.columns:
        st.warning("No 'Date' column found in the daily mood data.")
        return

    # Process data for plotting
    mood_columns = ["CTO", "Meditation", "Mood", "Sleep", "Stress"]

    # Create Plotly traces for bar charts
    traces = [go.Bar(x=df["Date"], y=df[col].astype(str), name=col) for col in mood_columns]

    # Create Plotly layout
    layout = go.Layout(title='Daily Mood Report',
                       xaxis=dict(title='Date'),
                       yaxis=dict(title='Rating'))

    # Create Plotly figure
    fig = go.Figure(data=traces, layout=layout)

    # Display Plotly figure
    st.plotly_chart(fig)

if __name__ == "__main__":
    enter_daily_mood()
    plot_daily_mood()
