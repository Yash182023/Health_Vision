# # import streamlit as st
# # from deta import Deta

# # DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # # Initialize with a project key
# # deta = Deta(DETA_KEY)
# # work_data_db = deta.Base("Workplace_DB")

# # def enter_daily_work_data():
# #     st.title("Enter Daily Work Data")

# #     # Collect daily work-related details from user input
# #     boss = st.text_input("BOSS")
# #     colleague = st.text_input("COLLEAGUE")
# #     cto = st.text_input("CTO")
# #     salary = st.text_input("SALARY")
# #     satisfaction = st.text_input("SATISFACTION")

# #     # Store daily work-related details in the Deta Base when the 'Submit' button is clicked
# #     if st.button('Submit Work Data'):
# #         new_work_data_record = {
# #             "BOSS": boss,
# #             "COLLEAGUE": colleague,
# #             "CTO": cto,
# #             "SALARY": salary,
# #             "SATISFACTION": satisfaction
# #         }
# #         work_data_db.put(new_work_data_record)
# #         st.success("Daily work data submitted successfully!")

# # if __name__ == "__main__":
# #     enter_daily_work_data()
# import streamlit as st
# from deta import Deta
# import plotly.graph_objs as go
# import pandas as pd

# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)
# work_data_db = deta.Base("Workplace_DB")

# def enter_daily_work_data():
#     st.title("Enter Daily Work Data")

#     # Collect daily work-related details from user input
#     boss = st.text_input("BOSS")
#     colleague = st.text_input("COLLEAGUE")
#     cto = st.text_input("CTO")
#     salary = st.text_input("SALARY")
#     satisfaction = st.text_input("SATISFACTION")

#     # Store daily work-related details in the Deta Base when the 'Submit' button is clicked
#     if st.button('Submit Work Data'):
#         new_work_data_record = {
#             "BOSS": boss,
#             "COLLEAGUE": colleague,
#             "CTO": cto,
#             "SALARY": salary,
#             "SATISFACTION": satisfaction
#         }
#         work_data_db.put(new_work_data_record)
#         st.success("Daily work data submitted successfully!")

# def plot_work_data():
#     st.title("Work Data Report")

#     # Fetch work data from the Deta Base
#     work_data = work_data_db.fetch().items

#     # Create DataFrame for easier manipulation
#     df = pd.DataFrame(work_data)

#     st.write(df)
#     # Process data for plotting
#     work_columns = ["SALARY", "SATISFACTION"]

#     # Create Plotly traces for bar charts
#     traces = [go.Bar(x=work_columns, y=df[col].astype(str), name=col) for col in work_columns]

#     # Create Plotly layout
#     layout = go.Layout(title='Work Data Report',
#                        xaxis=dict(title='Metrics'),
#                        yaxis=dict(title='Value'))

#     # Create Plotly figure
#     fig = go.Figure(data=traces, layout=layout)

#     # Display Plotly figure
#     st.plotly_chart(fig)

# if __name__ == "__main__":
#     enter_daily_work_data()
# #     plot_work_data()
# import streamlit as st
# from deta import Deta
# import plotly.graph_objs as go
# import pandas as pd

# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)
# work_data_db = deta.Base("Workplace_DB")

# def enter_daily_work_data():
#     st.title("Enter Daily Work Data")

#     # Collect daily work-related details from user input
#     H_id = st.text_input("H_ID")
#     boss = st.text_input("BOSS")
#     colleague = st.text_input("COLLEAGUE")
#     cto = st.text_input("CTO")
#     salary = st.text_input("SALARY")
#     satisfaction = st.text_input("SATISFACTION")

#     # Store daily work-related details in the Deta Base when the 'Submit' button is clicked
#     if st.button('Submit Work Data'):
#         new_work_data_record = {
#             "H_ID":H_id,
#             "BOSS": boss,
#             "COLLEAGUE": colleague,
#             "CTO": cto,
#             "SALARY": salary,
#             "SATISFACTION": satisfaction
#         }
#         work_data_db.put(new_work_data_record)
#         st.success("Daily work data submitted successfully!")

# def plot_salary():
#     st.title("Salary Report")

#     # Fetch salary data from the Deta Base
#     salary_data = work_data_db.fetch().items

#     # Create DataFrame for easier manipulation
#     df_salary = pd.DataFrame(salary_data)

#     st.write(df_salary)
#     # Process data for plotting
#     salary_columns = ["SALARY"]

#     # Create Plotly traces for bar chart
#     trace_salary = go.Bar(x=salary_columns, y=df_salary["SALARY"].astype(str), name='Salary')

#     # Create Plotly layout
#     layout_salary = go.Layout(title='Salary Report',
#                               xaxis=dict(title='Metrics'),
#                               yaxis=dict(title='Value'))

#     # Create Plotly figure for salary
#     fig_salary = go.Figure(data=[trace_salary], layout=layout_salary)

#     # Display Plotly figure for salary
#     st.plotly_chart(fig_salary)

# def plot_satisfaction():
#     st.title("Satisfaction Report")

#     # Fetch satisfaction data from the Deta Base
#     satisfaction_data = work_data_db.fetch().items

#     # Create DataFrame for easier manipulation
#     df_satisfaction = pd.DataFrame(satisfaction_data)

#     st.write(df_satisfaction)
#     # Process data for plotting
#     satisfaction_columns = ["SATISFACTION"]

#     # Create Plotly traces for bar chart
#     trace_satisfaction = go.Bar(x=satisfaction_columns, y=df_satisfaction["SATISFACTION"].astype(str), name='Satisfaction')

#     # Create Plotly layout
#     layout_satisfaction = go.Layout(title='Satisfaction Report',
#                                     xaxis=dict(title='Metrics'),
#                                     yaxis=dict(title='Value'))

#     # Create Plotly figure for satisfaction
#     fig_satisfaction = go.Figure(data=[trace_satisfaction], layout=layout_satisfaction)

#     # Display Plotly figure for satisfaction
#     st.plotly_chart(fig_satisfaction)

# if __name__ == "__main__":
#     enter_daily_work_data()
#     plot_salary()
# #     plot_satisfaction()
# import streamlit as st
# from deta import Deta
# import plotly.graph_objs as go
# import pandas as pd

# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)
# work_data_db = deta.Base("Workplace_DB")

# def enter_daily_work_data():
#     st.title("Enter Daily Work Data")

#     # Collect daily work-related details from user input
#     H_id = st.text_input("H_ID")
#     boss = st.text_input("BOSS")
#     colleague = st.text_input("COLLEAGUE")
#     cto = st.text_input("CTO")
#     salary = st.text_input("SALARY")
#     satisfaction = st.text_input("SATISFACTION")

#     # Store daily work-related details in the Deta Base when the 'Submit' button is clicked
#     if st.button('Submit Work Data'):
#         new_work_data_record = {
#             "H_ID": H_id,
#             "BOSS": boss,
#             "COLLEAGUE": colleague,
#             "CTO": cto,
#             "SALARY": salary,
#             "SATISFACTION": satisfaction
#         }
#         work_data_db.put(new_work_data_record)
#         st.success("Daily work data submitted successfully!")

# def plot_salary():
#     st.title("Salary Report")

#     # Fetch salary data from the Deta Base for the entered H_ID
#     H_id = st.text_input("Enter H_ID for Salary Report")
#     salary_data = work_data_db.fetch({"H_ID": H_id}).items

#     # Create DataFrame for easier manipulation
#     df_salary = pd.DataFrame(salary_data)

#     # Check if data is available for the entered H_ID
#     if not df_salary.empty:
#         st.write(df_salary)
        
#         # Process data for plotting
#         salary_columns = ["SALARY"]

#         # Create Plotly traces for bar chart
#         trace_salary = go.Bar(x=salary_columns, y=df_salary["SALARY"].astype(str), name='Salary')

#         # Create Plotly layout
#         layout_salary = go.Layout(title=f'Salary Report for H_ID: {H_id}',
#                                   xaxis=dict(title='Metrics'),
#                                   yaxis=dict(title='Value'))

#         # Create Plotly figure for salary
#         fig_salary = go.Figure(data=[trace_salary], layout=layout_salary)

#         # Display Plotly figure for salary
#         st.plotly_chart(fig_salary)
#     else:
#         st.warning("No data found for the entered H_ID.")

# def plot_satisfaction():
#     st.title("Satisfaction Report")

#     # Fetch satisfaction data from the Deta Base
#     satisfaction_data = work_data_db.fetch().items

#     # Create DataFrame for easier manipulation
#     df_satisfaction = pd.DataFrame(satisfaction_data)

#     st.write(df_satisfaction)
#     # Process data for plotting
#     satisfaction_columns = ["SATISFACTION"]

#     # Create Plotly traces for bar chart
#     trace_satisfaction = go.Bar(x=satisfaction_columns, y=df_satisfaction["SATISFACTION"].astype(str), name='Satisfaction')

#     # Create Plotly layout
#     layout_satisfaction = go.Layout(title='Satisfaction Report',
#                                     xaxis=dict(title='Metrics'),
#                                     yaxis=dict(title='Value'))

#     # Create Plotly figure for satisfaction
#     fig_satisfaction = go.Figure(data=[trace_satisfaction], layout=layout_satisfaction)

#     # Display Plotly figure for satisfaction
#     st.plotly_chart(fig_satisfaction)

# if __name__ == "__main__":
#     enter_daily_work_data()
#     plot_salary()
#     plot_satisfaction()
import streamlit as st
from deta import Deta
import plotly.graph_objs as go
import pandas as pd

DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# Initialize with a project key
deta = Deta(DETA_KEY)
work_data_db = deta.Base("Workplace_DB")

style = """
    <style>
    
    @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
        .main{
            background: rgb(57,78,255); 
            background: linear-gradient(164deg, rgba(57,78,255,1) 0%, rgba(255,0,215,1) 51%, rgba(229,255,5,1) 100%);
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

def enter_daily_work_data():
    st.title("Enter Daily Work Data")

    # Collect daily work-related details from user input
    H_id = st.text_input("H_ID")
    W_ID = st.text_input("W_ID")
    boss = st.text_input("BOSS")
    colleague = st.text_input("COLLEAGUE")
    cto = st.text_input("CTO")
    salary = st.text_input("SALARY")
    satisfaction = st.text_input("SATISFACTION")
    date = st.date_input("Date")

    # Store daily work-related details in the Deta Base when the 'Submit' button is clicked
    if st.button('Submit Work Data'):
        new_work_data_record = {
            "H_ID": H_id,
            "W_ID": W_ID,
            "BOSS": boss,
            "COLLEAGUE": colleague,
            "CTO": cto,
            "SALARY": salary,
            "SATISFACTION": satisfaction,
            "Date": date.strftime("%Y-%m-%d")
        }
        work_data_db.put(new_work_data_record)
        st.success("Daily work data submitted successfully!")

def plot_salary_and_satisfaction(W_id):
    st.title("Salary and Satisfaction Report")

    # Fetch data from the Deta Base
    data = work_data_db.fetch({"W_ID": W_id}).items

    # Create DataFrame for easier manipulation
    df = pd.DataFrame(data)

    if not df.empty:
        # Get the latest date for the provided health ID
        latest_date = df['Date'].max()

        # Filter data for the latest date
        df_latest_date = df[df['Date'] == latest_date]

        salary = float(df_latest_date['SALARY'].iloc[0])
        satisfaction = float(df_latest_date['SATISFACTION'].iloc[0])

        # Create Plotly traces for salary and satisfaction
        trace_salary = go.Bar(x=['Salary'], y=[salary], name='Salary')
        trace_satisfaction = go.Bar(x=['Satisfaction'], y=[satisfaction], name='Satisfaction')

        # Create Plotly layout
        layout = go.Layout(title='Salary Report',
                           xaxis=dict(title='Metrics'),
                           yaxis=dict(title='Value'))
        
        layout_1 = go.Layout(title='Satisfaction Report',
                           xaxis=dict(title='Metrics'),
                           yaxis=dict(title='Value'))

        # Create Plotly figure
        fig = go.Figure(data=[trace_salary], layout=layout)
        fig1 = go.Figure(data=[trace_satisfaction], layout=layout_1)

        # Display Plotly figure
        st.plotly_chart(fig)
        st.plotly_chart(fig1)
    else:
        st.warning("No data found for the provided Health ID.")

if __name__ == "__main__":
    enter_daily_work_data()
    W_id_input = st.text_input("Enter Work ID:")
    if st.button('Display Data'):
        plot_salary_and_satisfaction(W_id_input)
