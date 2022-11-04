import streamlit as st
from PIL import Image #Image processing 
import datetime


nav = st.sidebar.radio("Navigation", ["Smart Door-Keeper", "Records", "About Us"])

        
        
if nav == "Smart Door-Keeper":
    st.title("Camera:")
    file_image = st.camera_input(label = "Doorbell View")

    if file_image:
        input_img = Image.open(file_image)
        if st.button("Download Sketch Images"):
            im_pil = Image.save(input_img)
            im_pil.save('final_image.jpeg')
            st.write('Download completed')
    

    
    


if nav == "Records":
    st.title("Records")


if nav == "About Us":
    st.title("About Us")


