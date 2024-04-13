import streamlit as st
import pandas as pd

# Load the CSV file
@st.cache
def load_data():
    return pd.read_excel('C:/Users/sharm/OneDrive/Desktop/Daily_Health_Tracking/Nutrition_data.xlsx')

df = load_data()

# Sidebar with selectbox for food item selection
selected_food = st.sidebar.selectbox('Select a food item:', df['Shrt_Desc'])

# Display nutritional values for selected food item
st.write(f"Nutritional values for {selected_food}:")
selected_row = df[df['Shrt_Desc'] == selected_food]
selected_row = selected_row.drop(columns=['Shrt_Desc'])
st.write(selected_row)

# Check if sugar content is greater than a threshold
sugar_threshold = 10  
cholesterol_threshold = 100  
sugar_value = selected_row['Sugar_Tot_(g)'].values[0]
if sugar_value > sugar_threshold:
    st.write("Warning: This food item has high sugar content.")
else:
    st.write("This food item has moderate or low sugar content.")
    
cholesterol_value = selected_row['Cholestrl_(mg)'].values[0]
if cholesterol_value > cholesterol_threshold:
    st.write("Warning: This food item has high cholesterol content.")
else:
    st.write("This food item has moderate or low cholesterol content.")