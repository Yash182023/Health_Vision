# # import streamlit as st
# # from deta import Deta

# # DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # # Initialize with a project key
# # deta = Deta(DETA_KEY)

# # # Create Deta Base instance
# # my_db = deta.Base("Data_Tracking")

# # if 'logged_in' not in st.session_state:
# #     st.session_state.logged_in = False
    
# # def verify_credentials(username, password):
# #     # Fetch user record from Deta Base
# #     user = my_db.get(username)
    
# #     if user and user['Password'] == password:
# #         st.session_state.username = username
# #         return True
# #     else:
# #         st.write("Yes")
# #         return False

# # def login():
# #     st.title("Login Page")
    
# #     # Collect username and password from user input
# #     username = st.text_input("Username")
# #     password = st.text_input("Password", type="password")
    
# #     # Verify credentials against Deta Base
# #     if st.button('Submit Sign In'):
# #         if verify_credentials(username, password):
# #             st.session_state.logged_in = True
# #             st.write(f'Welcome, {username}!')
# #         else:
# #             st.error('Invalid username or password. Please try again.')

# # if __name__ == "__main__":
# #     login()

# import streamlit as st
# from deta import Deta

# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# # Initialize with a project key
# deta = Deta(DETA_KEY)

# # Create Deta Base instance
# my_db = deta.Base("Data_Tracking")

# def register_user(username, password):
#     # Check if the username already exists in the database
#     if my_db.get(username):
#         st.error("Username already exists. Please choose a different one.")
#         return False

#     # Add new user to the database
#     new_user = {
#         "Username": username,
#         "Password": password,
#     }
#     my_db.put(new_user)

#     return True

# def registration():
#     st.title("Registration Page")

#     # Collect username and password from user input
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     # Register user when the 'Register' button is clicked
#     if st.button('Register'):
#         if register_user(username, password):
#             st.success(f'Registration successful for {username}!')
#         else:
#             st.error('Registration failed. Please check the provided information.')

# if __name__ == "__main__":
#     registration()
import streamlit as st
from deta import Deta

DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"

# Initialize with a project key
deta = Deta(DETA_KEY)

# Create Deta Base instance
my_db = deta.Base("Data_Tracking")
my_db_1 = deta.Base("Basic_Health")



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
            color:#ffffff;
        } 
        
        .st-emotion-cache-19rxjzo{
            background-color: white;
        }
    </style>

"""

st.markdown(style, unsafe_allow_html=True)

def register_user(username, password):
    # Check if the username already exists in the database
    if my_db.get(username):
        st.error("Username already exists. Please choose a different one.")
        return False

    # Add new user to the database
    new_user = {
        "Username": username,
        "Password": password,
    }
    my_db.put(new_user)

    return True

def verify_credentials(username, password):
    # Fetch user record from Deta Base using the key
    users = my_db.fetch({"Username": username}).items
    
   
    if users:
        for user in users:
            if user['Password'] == password:
                return True
    return False

def display_user_data(username):
    # Fetch user data from the Deta Base
    user_data = my_db_1.fetch({"Username": username}).items

    # Display user data
    if user_data:
        st.title("User Data")
        for user in user_data:
            st.text(f"Username: {user['Username']}")
            st.text(f"Age: {user['Age']} years")
            st.text(f"Height: {user['Height']} cm")
            st.text(f"Sex: {user['Sex']}")
            st.text(f"Weight: {user['Weight']} kg")

def registration():
    st.title("Registration Page")

    # Collect username and password from user input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Register user when the 'Register' button is clicked
    if st.button('Register'):
        if register_user(username, password):
            st.success(f'Registration successful for {username}!')
        else:
            st.error('Registration failed. Please check the provided information.')

def login():
    st.title("Login Page")

    # Collect username and password from user input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Verify credentials against Deta Base
    if st.button('Submit Sign In'):
        if verify_credentials(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f'Welcome, {username}!')
            # Display user data upon successful sign-in
            display_user_data(username)
        else:
            st.error('Invalid username or password. Please try again.')
            
            
def unregister_user(username, password):
    # Verify credentials before deleting the account
    if verify_credentials(username, password):
        # Fetch the user record to get its key
        user_record = my_db.fetch({"Username": username}).items
        if user_record:
            # Delete user record from the database
            my_db.delete(user_record[0]["key"])
            st.success("Your account has been successfully deleted.")
            return True
    else:
        st.error("Incorrect password. Account deletion failed.")
        return False


def unregister():
    st.title("Unregister Page")

    # Collect username and password from user input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Delete user account when the 'Unregister' button is clicked
    if st.button('Unregister'):
        unregister_user(username, password)

if __name__ == "__main__":
    option = st.sidebar.selectbox('Select Option', ('Registration', 'Sign In', 'Unregister'))

    if option == 'Registration':
        registration()
    elif option == 'Sign In':
        login()
    elif option == 'Unregister':
        unregister()