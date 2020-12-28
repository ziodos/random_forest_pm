import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 

pickle_in = open('random_forest_car_price_prediction_model.pkl', 'rb') 
classifier = pickle.load(pickle_in) 

def welcome(): 
    return 'welcome all'
  
# defining the function which will make the prediction using  
# the data which the user inputs 
def prediction(present_price, kms_driven, owner, year_difference, fuel_type, seller_type_individual, transmission_manual):   
   
    prediction = classifier.predict( 
        [[present_price, kms_driven, owner, year_difference, fuel_type, seller_type_individual, transmission_manual]]) 
    print(prediction) 
    return prediction 
      
  
# this is the main function in which we define our webpage  
def main(): 
      # giving the webpage a title 
    st.title("Car Price Prediction") 
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Predicting the price of a car using Random Forest Algorithm </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    present_price = st.text_input("Present Price", "Type Here") 
    kms_driven = st.text_input("KMS driven", "Type Here") 
    owner = st.text_input("Owner", "Type Here") 
    year_difference = st.text_input("Year Difference", "Type Here") 
    fuel_type = st.text_input("Fuel Type", "Type Here") 
    seller_type_individual = st.text_input("Seller Type Individual", "Type Here")
    transmission_manual = st.text_input("Transmission Manual", "Type Here")
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Predict"): 
        result = prediction(present_price, kms_driven, owner, year_difference, fuel_type, seller_type_individual, transmission_manual) 
    st.success('The output is {}'.format(result)) 
     
if __name__=='__main__': 
    main() 