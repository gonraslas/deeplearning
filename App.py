from importlib_metadata import pathlib
import streamlit as st
import tensorflow as tf
from tensorflow import keras
import pathlib
import datetime
import os
from os import listdir
st.write("Hola Mundo")

uploadead_file = st.sidebar.file_uploader("Adjuntar imagen", type=["png","jpg","svg"])
if uploadead_file is not None:
    ts = datetime.datetime.now().timestamp()
    file_name=str(ts)+'.png'
    image_location_and_name='tempDir/'+str(ts)+'.png'
    image_file=pathlib.Path(image_location_and_name)
   #with open(os.path.join("tempDir/", file_name),"wb") as f:
   #    f.write(uploaded_file.getbuffer())


   #img = keras.preprocessing.image.load_img(image_location_and_name, target_size=(256,256))

   #img_array = keras.preprocessing.image.img_to_array(img)
    #st.write(img_array)
    st.image(uploadead_file,channels="RGB")
else:
    #data_dir = pathlib.Path('modelo/')
    st.image('modelo/prueba.jpg',channels="RGB")
