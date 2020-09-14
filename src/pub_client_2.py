#simulator device 1 for mqtt message publishing
import paho.mqtt.client as mqtt
import time
import random
import time

#hostname
broker="localhost"
#port
port=1883
def on_publish(client,userdata,result):
    print("Device 2 : Data published.")
    pass
#time to live
timelive=60000
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))#st.text("Connected with result code "+str(rc))
    client.subscribe(("/data1",1))
    
def on_message(client, userdata, msg):
	msg_received = msg.payload.decode()
	print(msg_received)
	if msg_received=='true':
		for i in range(20):
 			d=random.randint(1,5)
 	    
 			#telemetry to send 
 			message="2:Data" + str(i)
 			time.sleep(d)
 	    		
 			#publish message
 			print(message)
 			ret = client.publish("/data",message)

		
        
# Create a new client for receiving messages
client = mqtt.Client('Device2')
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker,port,timelive)
client.loop_forever()
#client.loop_start()
# # if True:#msg_received=='true':
# # 	for i in range(20):
# # 		d=random.randint(1,5)
    
# # 		#telemetry to send 
# # 		message="1:Data" + str(i)
# # 		time.sleep(d)
    		
# # 		#publish message
# # 		print(message)
# # 		ret = client.publish("/data1",message)

# client.loop_stop()
print("Stopped...")


