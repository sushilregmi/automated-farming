import paho.mqtt.client as mqtt
import sqlite3
import

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("fromEsp8266")
def on_message(client, userdata, msg):
	data_str = msg.payload.decode("utf-8")
	data_list = data_str.split(",")
	print(data_list)
	x=predict(data_list)
	conn = sqlite3.connect('data.db')
	c = conn.cursor()
	c.execute("SELECT sample_id FROM SENSORDATA ORDER BY sample_id DESC LIMIT 1")
	a = c.fetchone()
	id_num = a[0] + 1
	c.execute("INSERT into SENSORDATA VALUES(?,?,?,?)",(id_num,data_list[1], data_list[0]))
	conn.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
	
client.connect("192.168.1.70", 1883, 60)
client.loop_forever()
