# Imporiting Necessary Libraries
import streamlit as st
from PIL import Image
import io
import numpy as np
import tensorflow as tf
import efficientnet.tfkeras
import requests
from io import BytesIO



# Removing Menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Loading the Model
#model = tf.keras.models.load_model('complete_data_model.h5', compile=False)

# Title and Description
st.title('Melanoma Classification ??')
st.write("This project is for identifying melanoma in lesion images")
st.markdown('''## What's the Project ?
The Project has been made by Shubhamai and the Website is a part of the SIIM-ISIC Melanoma Classification Kaggle Competition Project.\
> You can find the blogs and documentaties related to this project from here.''')       
st.markdown(''' ## How does it works ? 
You have to just upload the image and a Machine Learning Model will predict is the image is malignant or benign''')
st.image(Image.open(BytesIO(requests.get("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/199da6ad-a1ed-425e-a7c1-b39d38f2365c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200613T080836Z&X-Amz-Expires=86400&X-Amz-Signature=d84dc2fb34be481d5034d91e2f088a5ab1d235873cfc4fe8a1e9c6ed59896caa&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22").content)), caption="Example of model being run on a Benign Image.", use_column_width=True)

# Uploading Files
st.markdown('## Upload Your Own')
uploaded_file = st.file_uploader("Choose a Image file", type=["png", "jpg"])


st.write('Currently, there\'s no prediction made because of saving computation power')


# If there is a uploaded file, start making prediction
if uploaded_file != None:  
    
    
      st.image(uploaded_file)
      
#     # Display progress and text
#     progress = st.text("Crunching Image")
#     my_bar = st.progress(0)
#     i = 0

#     # Reading the uploaded image
#     image = Image.open(io.BytesIO(uploaded_file.read()))
#     st.image(image)
#     my_bar.progress(i + 40)

#     image = image.resize((1024, 1024), PIL.Image.ANTIALIAS)
#     image = np.array(image)
#     image = image/255.0
#     image = image[np.newaxis, ...]

#     # Making the predictions
#     predictions = model.predict(image)
#     my_bar.progress(i + 30)

#     st.write(predictions)

#     # Removing progress bar and text after prediction done
#     my_bar.progress(i + 30)
#     progress.empty()
#     i = 0
#     my_bar.empty()
