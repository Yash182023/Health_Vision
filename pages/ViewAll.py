# import streamlit as st 
# from deta import Deta



# st.title("This the dataset for all the records")


# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)
# work_data_db = deta.Base("Workplace_DB")
# workplace_wellness_db = deta.Base("Physical_health")
# daily_mood_db = deta.Base("Daily_Mood")
# my_db = deta.Base("Basic_Health")
# bs_db = deta.Base("Basic_Progress")


# def fetchall():
#     H_id = st.text_input("Enter the Health id: ")
    
import streamlit as st 
from deta import Deta

style = """
    <style>
    
    @import 'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap';
        .main{
            background: rgb(57,255,96);
            background: linear-gradient(90deg, rgba(57,255,96,1) 0%, rgba(0,255,200,1) 51%, rgba(161,0,241,1) 100%);
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

st.title("Dataset for All Records")

DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# Initialize with a project key
deta = Deta(DETA_KEY)
work_data_db = deta.Base("Workplace_DB")
workplace_wellness_db = deta.Base("Physical_health")
daily_mood_db = deta.Base("Daily_Mood")
my_db = deta.Base("Basic_Health")
bs_db = deta.Base("Basic_Progress")

def fetch_all_data(health_id):
    st.header("Data for Health ID: " + health_id)
    
    # Fetch data from each table based on the provided Health ID
    work_data = work_data_db.fetch({"H_ID": health_id}).items
    wellness_data = workplace_wellness_db.fetch({"H_ID": health_id}).items
    mood_data = daily_mood_db.fetch({"H_ID": health_id}).items
    basic_health_data = my_db.fetch({"Health_ID": health_id}).items
    basic_progress_data = bs_db.fetch({"Health_ID": health_id}).items
    
    # Display data for each table
    if work_data:
        st.subheader("Work Data:")
        st.dataframe(work_data)
    
    if wellness_data:
        st.subheader("Wellness Data:")
        st.dataframe(wellness_data)
    
    if mood_data:
        st.subheader("Mood Data:")
        st.dataframe(mood_data)
    
    if basic_health_data:
        st.subheader("Basic Health Data:")
        st.dataframe(basic_health_data)
    
    if basic_progress_data:
        st.subheader("Basic Progress Data:")
        st.dataframe(basic_progress_data)

def main():
    health_id = st.text_input("Enter the Health ID: ")
    if health_id:
        fetch_all_data(health_id)

if __name__ == "__main__":
    main()
