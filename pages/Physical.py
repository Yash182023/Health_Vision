# import streamlit as st
# from deta import Deta

# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)
# physical_wellness_db = deta.Base("Physical_health")

# def enter_workplace_wellness_data():
#     st.title("Enter Workplace Wellness Data")

#     # Collect workplace wellness details from user input
#     exercise = st.text_input("Exercise")
#     gym = st.text_input("Gym")
#     jogging = st.text_input("Jogging")
#     meditation = st.text_input("Meditation")
#     yoga = st.text_input("Yoga")

#     # Store workplace wellness details in the Deta Base when the 'Submit' button is clicked
#     if st.button('Submit Workplace Wellness Data'):
#         new_workplace_wellness_record = {
#             "key": "hi4lg7qpa0ze",
#             "Excercise": exercise,
#             "Gym": gym,
#             "Jogging": jogging,
#             "Meditation": meditation,
#             "Yoga": yoga
#         }
#         physical_wellness_db.put(new_workplace_wellness_record)
#         st.success("Workplace wellness data submitted successfully!")

# if __name__ == "__main__":
#     enter_workplace_wellness_data()

# import streamlit as st
# from deta import Deta
# import plotly.graph_objs as go
# import pandas as pd

# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)
# physical_wellness_db = deta.Base("Physical_health")

# def enter_workplace_wellness_data():
#     st.title("Enter Workplace Wellness Data")

#     # Collect workplace wellness details from user input
#     exercise = st.text_input("Exercise")
#     gym = st.text_input("Gym")
#     jogging = st.text_input("Jogging")
#     meditation = st.text_input("Meditation")
#     yoga = st.text_input("Yoga")

#     # Store workplace wellness details in the Deta Base when the 'Submit' button is clicked
#     if st.button('Submit Workplace Wellness Data'):
#         new_workplace_wellness_record = {
#             "Exercise": exercise,
#             "Gym": gym,
#             "Jogging": jogging,
#             "Meditation": meditation,
#             "Yoga": yoga
#         }
#         physical_wellness_db.put(new_workplace_wellness_record)
#         st.success("Workplace wellness data submitted successfully!")

# def plot_physical_wellness_report():
#     st.title("Workplace Wellness Report")

#     # Fetch workplace wellness data from the Deta Base
#     wellness_data = physical_wellness_db.fetch().items

#     # Create DataFrame for easier manipulation
#     df = pd.DataFrame(wellness_data)

#     st.write(df)
#     # Process data for plotting
#     wellness_columns = ["Excercise", "Gym", "Jogging", "Meditation", "Yoga"]
    

#     # Create Plotly traces for bar charts
#     traces = [go.Bar(x=["Activities"], y=df[col].astype(str), name=col) for col in wellness_columns]

#     # Create Plotly layout
#     layout = go.Layout(title='Workplace Wellness Report',
#                        xaxis=dict(title='Activities'),
#                        yaxis=dict(title='Rating'))

#     # Create Plotly figure
#     fig = go.Figure(data=traces, layout=layout)

#     # Display Plotly figure
#     st.plotly_chart(fig)

# if __name__ == "__main__":
#     enter_workplace_wellness_data()
#     plot_physical_wellness_report()
import streamlit as st
from deta import Deta
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime

DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# Initialize with a project key
deta = Deta(DETA_KEY)
physical_wellness_db = deta.Base("Physical_health")

style = """
    <style>
    
    @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
        .main{
           background: rgb(255,57,174);
           background: linear-gradient(164deg, rgba(255,57,174,1) 0%, rgba(255,0,91,1) 51%, rgba(229,255,5,1) 100%);
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

def enter_workplace_wellness_data():
    st.title("Enter Workplace Wellness Data")

    # Collect workplace wellness details from user input
    H_Id = st.text_input("H_ID")
    P_ID = st.text_input("W_ID")
    exercise = st.text_input("Exercise")
    gym = st.text_input("Gym")
    jogging = st.text_input("Jogging")
    meditation = st.text_input("Meditation")
    yoga = st.text_input("Yoga")

    # Automatically capture the current date
    date = datetime.now().strftime("%Y-%m-%d")

    # Store workplace wellness details in the Deta Base when the 'Submit' button is clicked
    if st.button('Submit Workplace Wellness Data'):
        new_workplace_wellness_record = {
            "H_ID":H_Id,
            "P_ID":P_ID,
            "Date": date,
            "Exercise": exercise,
            "Gym": gym,
            "Jogging": jogging,
            "Meditation": meditation,
            "Yoga": yoga
        }
        physical_wellness_db.put(new_workplace_wellness_record)
        st.success("Workplace wellness data submitted successfully!")

def plot_physical_wellness_report():
    st.title("Physical Wellness Report")
    
    P_ID = st.text_input("Enter the P_ID:")

    # Fetch workplace wellness data from the Deta Base
    progress_data = physical_wellness_db.fetch({"P_ID": str(P_ID)}).items

    # Create DataFrame for easier manipulation
    df = pd.DataFrame(progress_data)

    if not df.empty:
        st.write(df)
        
        # Process data for plotting
        wellness_columns = ["Exercise", "Gym", "Jogging", "Meditation", "Yoga"]

        # Create Plotly traces for bar charts
        traces = [go.Bar(x=df["Date"], y=df[col].astype(str), name=col) for col in wellness_columns]

        # Create Plotly layout
        layout = go.Layout(title='Physical Wellness Report',
                           xaxis=dict(title='Date'),
                           yaxis=dict(title='Rating'))

        # Create Plotly figure
        fig = go.Figure(data=traces, layout=layout)

        # Display Plotly figure
        st.plotly_chart(fig)
    else:
        st.warning("No data found for the entered P_ID.")

if __name__ == "__main__":
    enter_workplace_wellness_data()
    plot_physical_wellness_report()