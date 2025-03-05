import streamlit as st
import random
import string #provide specific letter which is find in diffrent values of string like uppercase and lowercase etc.

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters # provide uppercase and lowercase letter(a-z,A-Z)

    if use_digits:
        characters += string.digits # provide digits (0-9) if user selected digits

    if use_special_chars:
        characters += string.punctuation # provide special characters (!@#$%^&*()_+) if user selected special characters

    return ''.join(random.choice(characters) for _ in range(length)) # provide random characters from characters and join all characters in a string   
# _ is mean python ko btata k is loop ki koi specific length nh hai 

st.title("Password Generator 🔐")

length = st.slider("Select Password Length📏", min_value=6, max_value=30, value=12) # slider for password length
use_digits = st.checkbox("Use Digits🔢", value=True) # checkbox for digits
use_special_character = st.checkbox("Use Special Character🔣", value=True) # checkbox for special     
if st.button("Generate Password🛠️"):
   password = generate_password(length, use_digits, use_special_character) # generate password

   st.write(f"Generated Password: {password})") # show password

   st.write("-------------------------")

   st.write("Build by ❤️ [Ayesha Faisal] (https://github.com/ayesha-offical)")