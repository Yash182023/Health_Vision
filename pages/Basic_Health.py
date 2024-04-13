# # import streamlit as st
# # from deta import Deta
# # import plotly.graph_objs as go
# # import pandas as pd
# # from datetime import datetime

# # DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # # Initialize with a project key
# # deta = Deta(DETA_KEY)

# # # Create Deta Base instances
# # my_db = deta.Base("Basic_Health")
# # bs_db = deta.Base("Basic_Progress")

# # def enter_health_details():
# #     st.title("Enter Health Details")

# #     # Collect health details from user input
# #     username = st.text_input("Username")
# #     age = st.number_input("Age", min_value=0, max_value=150)
# #     dor = st.date_input("Date of Registration")
# #     health_id = st.text_input("Health ID")
# #     height = st.number_input("Height (in cm)", min_value=0)
# #     sex = st.selectbox("Sex", ["Male", "Female", "Other"])
# #     weight = st.number_input("Weight (in kg)", min_value=0)

# #     # Store health details in the Deta Base when the 'Submit' button is clicked
# #     if st.button('Submit'):
# #         new_health_record = {
# #             "Age": age,
# #             "DOR": str(dor),
# #             "Health_ID": health_id,
# #             "Height": height,
# #             "Sex": sex,
# #             "Username": username,
# #             "Weight": weight
# #         }
# #         my_db.put(new_health_record)
# #         st.success("Health details submitted successfully!")

# # def enter_basic_progress():
# #     st.title("Enter Basic Progress")

# #     # Collect basic progress details from user input
# #     discomfort = st.text_input("Any Discomfort")
# #     daily_tasks = st.text_input("Daily Tasks")
# #     health_id_progress = st.text_input("Health_ID")

# #     # Automatically capture the current date
# #     date = datetime.now().strftime("%Y-%m-%d")

# #     hydration = st.text_input("Hydration")
# #     minutes_of_exercise = st.text_input("Minutes of Exercise")
# #     nutrition_intake = st.text_input("Nutrition Intake")
# #     screen_time = st.text_input("Screen Time in Hrs")

# #     # Store basic progress details in the Deta Base when the 'Submit' button is clicked
# #     if st.button('Submit Progress'):
# #         new_progress_record = {
# #             "Any_Discomfort": discomfort,
# #             "Daily_Tasks": daily_tasks,
# #             "Health_ID": health_id_progress,
# #             "Date": date,
# #             "Hydration": hydration,
# #             "Minutes_of_Excercise": minutes_of_exercise,
# #             "Nutrition_intake": nutrition_intake,
# #             "Screen_Time": screen_time
# #         }
# #         bs_db.put(new_progress_record)
# #         st.success("Basic progress details submitted successfully!")

# # def plot_progress_data():
# #     st.title("Weekly Progress Report")

# #     # Fetch progress data from the Deta Base
# #     progress_data = bs_db.fetch().items

# #     # Create DataFrame for easier manipulation
# #     df = pd.DataFrame(progress_data)

# #     # Convert 'Date' column to datetime
# #     df['Date'] = pd.to_datetime(df['Date'])

# #     # Aggregate data weekly
# #     df_weekly = df.resample('W-Mon', on='Date').mean()

# #     # Process data for plotting
# #     hydration_data = df_weekly['Hydration'].tolist()
# #     exercise_data = df_weekly['Minutes_of_Excercise'].tolist()
# #     screen_time_data = df_weekly['Screen_Time'].tolist()

# #     # Create Plotly traces for bar charts
# #     hydration_trace = go.Bar(x=df_weekly.index, y=hydration_data, name='Hydration')
# #     exercise_trace = go.Bar(x=df_weekly.index, y=exercise_data, name='Minutes of Exercise')
# #     screen_time_trace = go.Bar(x=df_weekly.index, y=screen_time_data, name='Screen Time')

# #     # Create Plotly layout
# #     layout = go.Layout(title='Weekly Progress Report',
# #                        xaxis=dict(title='Week'),
# #                        yaxis=dict(title='Average Value'))

# #     # Create Plotly figure
# #     fig = go.Figure(data=[hydration_trace, exercise_trace, screen_time_trace], layout=layout)

# #     # Display Plotly figure
# #     st.plotly_chart(fig)

# # if __name__ == "__main__":
# #     enter_health_details()
# #     enter_basic_progress()
# #     plot_progress_data()
# import streamlit as st
# from deta import Deta
# import plotly.graph_objs as go
# import pandas as pd
# from datetime import datetime

# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)

# # Create Deta Base instances
# my_db = deta.Base("Basic_Health")
# bs_db = deta.Base("Basic_Progress")

# def enter_health_details():
#     st.title("Enter Health Details")

#     # Collect health details from user input
#     username = st.text_input("Username")
#     age = st.number_input("Age", min_value=0, max_value=150)
#     dor = st.date_input("Date of Registration")
#     health_id = st.text_input("Health ID")
#     height = st.number_input("Height (in cm)", min_value=0)
#     sex = st.selectbox("Sex", ["Male", "Female", "Other"])
#     weight = st.number_input("Weight (in kg)", min_value=0)

#     # Store health details in the Deta Base when the 'Submit' button is clicked
#     if st.button('Submit'):
#         new_health_record = {
#             "Age": age,
#             "DOR": str(dor),
#             "Health_ID": health_id,
#             "Height": height,
#             "Sex": sex,
#             "Username": username,
#             "Weight": weight
#         }
#         my_db.put(new_health_record)
#         st.success("Health details submitted successfully!")

# def enter_basic_progress():
#     st.title("Enter Basic Progress")

#     # Collect basic progress details from user input
#     discomfort = st.text_input("Any Discomfort")
#     daily_tasks = st.text_input("Daily Tasks")
#     health_id_progress = st.text_input("Health_ID")

#     # Automatically capture the current date
#     date = datetime.now().strftime("%Y-%m-%d")

#     hydration = st.text_input("Hydration")
#     minutes_of_exercise = st.text_input("Minutes of Exercise")
#     nutrition_intake = st.text_input("Nutrition Intake")
#     screen_time = st.text_input("Screen Time in Hrs")

#     # Store basic progress details in the Deta Base when the 'Submit' button is clicked
#     if st.button('Submit Progress'):
#         new_progress_record = {
#             "Any_Discomfort": discomfort,
#             "Daily_Tasks": daily_tasks,
#             "Health_ID": health_id_progress,
#             "Date": date,
#             "Hydration": hydration,
#             "Minutes_of_Excercise": minutes_of_exercise,
#             "Nutrition_intake": nutrition_intake,
#             "Screen_Time": screen_time
#         }
#         bs_db.put(new_progress_record)
#         st.success("Basic progress details submitted successfully!")

# def plot_progress_data():
#     st.title("Weekly Progress Report")

#     # Fetch progress data from the Deta Base
#     progress_data = bs_db.fetch().items

#     # Create DataFrame for easier manipulation
#     df = pd.DataFrame(progress_data)

#     # Convert 'Date' column to datetime
#     df['Date'] = pd.to_datetime(df['Date'])

#     # Only select relevant columns for plotting
#     df_selected = df[['Date', 'Hydration', 'Minutes_of_Excercise', 'Screen_Time']]

#     # Aggregate data weekly
#     df_weekly = df_selected.resample('W-Mon', on='Date').mean()

#     # Process data for plotting
#     hydration_data = df_weekly['Hydration'].tolist()
#     exercise_data = df_weekly['Minutes_of_Excercise'].tolist()
#     screen_time_data = df_weekly['Screen_Time'].tolist()

#     # Create Plotly traces for bar charts
#     hydration_trace = go.Bar(x=df_weekly.index, y=hydration_data, name='Hydration')
#     exercise_trace = go.Bar(x=df_weekly.index, y=exercise_data, name='Minutes of Exercise')
#     screen_time_trace = go.Bar(x=df_weekly.index, y=screen_time_data, name='Screen Time')

#     # Create Plotly layout
#     layout = go.Layout(title='Weekly Progress Report',
#                        xaxis=dict(title='Week'),
#                        yaxis=dict(title='Average Value'))

#     # Create Plotly figure
#     fig = go.Figure(data=[hydration_trace, exercise_trace, screen_time_trace], layout=layout)

#     # Display Plotly figure
#     st.plotly_chart(fig)

# if __name__ == "__main__":
#     enter_health_details()
#     enter_basic_progress()
#     plot_progress_data()
import streamlit as st
from deta import Deta
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime

DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# Initialize with a project key
deta = Deta(DETA_KEY)

# Create Deta Base instances
my_db = deta.Base("Basic_Health")
bs_db = deta.Base("Basic_Progress")


style = """
    <style>
    
    @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
        .main{
            background: rgb(199,57,255);
            background: linear-gradient(164deg, rgba(199,57,255,1) 0%, rgba(0,255,200,1) 51%, rgba(254,255,216,1) 100%);
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

def enter_health_details():
    st.title("Health Registration!")

    # Collect health details from user input
    username = st.text_input("Username")
    age = st.number_input("Age", min_value=0, max_value=150)
    dor = st.date_input("Date of Registration")
    health_id = st.text_input("Health ID")
    height = st.number_input("Height (in cm)", min_value=0)
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    weight = st.number_input("Weight (in kg)", min_value=0)

    # Store health details in the Deta Base when the 'Submit' button is clicked
    if st.button('Submit'):
        new_health_record = {
            "Age": age,
            "DOR": str(dor),
            "Health_ID": health_id,
            "Height": height,
            "Sex": sex,
            "Username": username,
            "Weight": weight
        }
        my_db.put(new_health_record)
        st.success("Health details submitted successfully!")

def enter_basic_progress():
    st.title("Enter Basic Progress")

    # Collect basic progress details from user input
    discomfort = st.text_input("Any Discomfort")
    daily_tasks = st.text_input("Daily Tasks")
    health_id_progress = st.text_input("Health_ID")

    # Automatically capture the current date
    date = datetime.now().strftime("%Y-%m-%d")

    hydration = st.text_input("Hydration")
    minutes_of_exercise = st.text_input("Minutes of Exercise")
    nutrition_intake = st.text_input("Nutrition Intake")
    screen_time = st.text_input("Screen Time in Hrs")

    # Store basic progress details in the Deta Base when the 'Submit' button is clicked
    if st.button('Submit Progress'):
        new_progress_record = {
            "Any_Discomfort": discomfort,
            "Daily_Tasks": daily_tasks,
            "Health_ID": health_id_progress,
            "Date": date,
            "Hydration": hydration,
            "Minutes_of_Excercise": minutes_of_exercise,
            "Nutrition_intake": nutrition_intake,
            "Screen_Time": screen_time
        }
        bs_db.put(new_progress_record)
        st.success("Basic progress details submitted successfully!")

def plot_progress_data(health_id):
    st.title(f"Weekly Progress Report for Health ID: {health_id}")

    # Fetch progress data specific to the entered Health ID from the Deta Base
    progress_data = bs_db.fetch({"Health_ID": health_id}).items

    # Create DataFrame for easier manipulation
    df = pd.DataFrame(progress_data)

    # Check if 'Date' column is present in the DataFrame
    if 'Date' in df.columns:
        # Convert relevant columns to numeric data types
        numeric_columns = ['Hydration', 'Minutes_of_Excercise', 'Screen_Time']
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

        # Convert 'Date' column to datetime
        df['Date'] = pd.to_datetime(df['Date'])

        # Only select relevant columns for plotting
        df_selected = df[['Date', 'Hydration', 'Minutes_of_Excercise', 'Screen_Time']]

        # Aggregate data weekly
        df_weekly = df_selected.resample('W-Mon', on='Date').mean()

        # Process data for plotting
        hydration_data = df_weekly['Hydration'].tolist()
        exercise_data = df_weekly['Minutes_of_Excercise'].tolist()
        screen_time_data = df_weekly['Screen_Time'].tolist()

        # Create Plotly traces for bar charts
        hydration_trace = go.Bar(x=df_weekly.index, y=hydration_data, name='Hydration')
        exercise_trace = go.Bar(x=df_weekly.index, y=exercise_data, name='Minutes of Exercise')
        screen_time_trace = go.Bar(x=df_weekly.index, y=screen_time_data, name='Screen Time')

        # Create Plotly layout
        layout = go.Layout(title='Weekly Progress Report',
                           xaxis=dict(title='Week'),
                           yaxis=dict(title='Average Value'))

        # Create Plotly figure
        fig = go.Figure(data=[hydration_trace, exercise_trace, screen_time_trace], layout=layout)

        # Display Plotly figure
        st.plotly_chart(fig)
    else:
        st.warning("No 'Date' column found in the progress data for the entered Health ID.")


if __name__ == "__main__":
    option = st.sidebar.selectbox('Select Option', ('Enter Health Details', 'Enter Basic Progress', 'View Weekly Progress Report'))

    if option == 'Enter Health Details':
        enter_health_details()
    elif option == 'Enter Basic Progress':
        enter_basic_progress()
    elif option == 'View Weekly Progress Report':
        # Ask user to enter Health ID
        health_id_input = st.text_input("Enter Health ID to view progress report:")
        if st.button('View Progress Report'):
            plot_progress_data(health_id_input)
