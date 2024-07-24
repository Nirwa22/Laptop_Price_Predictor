import streamlit as st
import pickle
import numpy as np
pipeline = pickle.load(open('pipeline.pkl','rb'))
Data = pickle.load(open('Data.pkl','rb'))
st.title('LAPTOP PREDICTOR')
Company = st.selectbox('BRAND',Data['Company'].unique())
Type = st.selectbox('TYPE',Data['TypeName'].unique())
Ram = st.selectbox('RAM(GB)',Data['Ram'].unique())
Weight = st.number_input('WEIGHT')
Touch_Screen = st.selectbox('TOUCHSCREEN',['Yes','No'])
IPS = st.selectbox('IPS',['Yes','No'])
Screen_size = st.number_input('SCREENSIZE')
Screen_resolution = st.selectbox('RESOLUTION',['1920X1080','1366X768','1600X900','3840X2160','3200X1800','2880X1800','2560X1600','2560X1440','2304X1440'])
CPU = st.selectbox('CPU BRAND',Data['Cpu brand'].unique())
HDD = st.selectbox('HDD',['0','128','256','512','1024','2048'])
SDD = st.selectbox('SDD',['0','128','256','512','1024'])
GPU = st.selectbox('GPU',Data['Gpu'].unique())
OpSys = st.selectbox('OPERATING SYSTEM',Data['OpSys'].unique())
if st.button('PREDICT PRICE'):
  PPI = None
  if Touch_Screen == 'Yes':
    Touch_Screen = 1
  else:
    Touch_Screen = 0
  if IPS == 'Yes':
    IPS = 1
  else:
    IPS = 0
  X_Resolution = int(Screen_resolution.split('X')[0])
  Y_Resolution = int(Screen_resolution.split('X')[1])
  if Screen_size == 0:
    st.title('Error')
  else:
    PPI = ((X_Resolution**2)+(Y_Resolution**2))**0.5/Screen_size
  Query = np.array([Company, Type, Ram, GPU, OpSys, Weight, Touch_Screen, IPS, PPI, CPU, HDD, SDD])
  Query = Query.reshape(1,12)
  st.title('Predicted Price : '+str(int(np.exp(pipeline.predict(Query)[0]))))
