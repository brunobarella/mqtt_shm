
import streamlit as st
#from streamlit.report_thread import add_report_ctx

import pymongo  # package for working with MongoDB
import threading
import paho.mqtt.client as mqtt
# This is the Subscriber

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
    client.subscribe([("/data",1),("/data1",1)])
    
def on_message(client, userdata, msg):
	msg_received = msg.payload.decode()
	print(msg_received)
	st.text(msg_received)
	
	if len(msg_received.split(':'))>1:
		collection_data = msg_received.split(':')[0]
		if collection_data=='1':
		 	dev1 = { 
		        #"_id":  msg_received.split(':')[0], 
				"data": msg_received.split(':')[1], } 
		 	try:        
		 	    colection_dev1.insert_one(dev1)
		 	except:
		 	    colection_dev1.replace_one(dev1)   
		if collection_data=='2':
		 	dev1 = { 
		        #"_id":  msg_received.split(':')[0], 
				"data": msg_received.split(':')[1], } 
		 	try:        
		 	    colection_dev2.insert_one(dev1)
		 	except:
		 	    colection_dev2.replace_one(dev1)   
			
client = mqtt.Client('server')
client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message

st.title("Streamlit teste")


client.publish("/data1","true")
client.publish("/data2","true")

client.loop_forever()

# client.loop_start()
# btn1 = st.button('Device 1')
# if btn1:
# 	st.write('Send data to start device 1')
# 	btn1=False


# thread_client = threading.Thread(target=client.loop_forever)
# thread_client.start()







