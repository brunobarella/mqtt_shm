
import streamlit as st
#from streamlit.report_thread import add_report_ctx
import pandas as pd
import pymongo  # package for working with MongoDB
import threading
import paho.mqtt.client as mqtt
import time

def data_from_mongo(st):
	data1_old=None
	data2_old=None
	while 1:
		data1 = [x['data'] for x in colection_dev1.find()]
		data2 = [x['data'] for x in colection_dev1.find()]
		if len(data1)>0 & data1!=data1_old:
			data1_old = data1
			chart_data1 = pd.DataFrame([float(x) for x in data1], columns=['Device 1'])
			st.line_chart(chart_data1)
		if len(data2)>0 & data2!=data2_old:
			data2_old = data2
			chart_data2 = pd.DataFrame([float(x) for x in data2], columns=['Device 2'])
			st.line_chart(chart_data2)
			

# mongodb
client_db = pymongo.MongoClient("mongodb://localhost:27017/")

device1 = client_db["device1"] # databse named device1
colection_dev1 = device1['dev1'] # colection named dev1

device2 = client_db["device2"] # databse named device1
colection_dev2 = device2['dev2'] # colection named dev1

#port
port=1883
#hostname
broker="localhost" 
#time to live
timelive=60
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))#st.text("Connected with result code "+str(rc))
    client.subscribe([("/data2",1),("/data1",1)])
    
# data_mongo = threading.Thread(target=data_from_mongo, args=(st,))
# data_mongo.start()

st.header('Device 1')

bt1 = st.button('Device 1')

if bt1:
	client = mqtt.Client('server_streamlit')
	client.connect(broker,port,timelive)
	client.on_connect = on_connect
	client.loop_start()
	client.publish("/data1","true")
	client.disconnect()
	#time.sleep(8)
	client.loop_stop()

data1 = [x['data'] for x in colection_dev1.find()]

if len(data1)>0:
	data1_old = data1
	chart_data1 = pd.DataFrame([float(x) for x in data1], columns=['Device 1'])
	st.line_chart(chart_data1)
	
st.header('Device 2')

bt2 = st.button('Device 2')

if bt2:
	client = mqtt.Client('server_streamlit')
	client.connect(broker,port,timelive)
	client.on_connect = on_connect
	client.loop_start()
	client.publish("/data2","true")
	client.disconnect()
	#time.sleep(8)
	client.loop_stop()

data2 = [x['data'] for x in colection_dev2.find()]

if len(data1)>0:
	data1_old = data2
	chart_data2 = pd.DataFrame([float(x) for x in data2], columns=['Device 2'])
	st.line_chart(chart_data2)
	
refresh = st.button("Atualizar")








