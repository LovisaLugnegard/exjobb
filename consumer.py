import cv2
import numpy as np

from PIL import Image
from io import StringIO, BytesIO
from flask import Flask, Response
from kafka import KafkaConsumer

#app = Flask(__name__)

#@app.route("/")

#consumer = KafkaConsumer(group_id=b"my_group_id",
 #                        bootstrap_servers=["129.16.125.242:9092"]) #,
#                         value_deserializer = lambda m: m.decode('ascii'))

#consumer.subscribe(topics=['test'])


def main():
    consumer = KafkaConsumer(group_id=b"my_group_id",
                             bootstrap_servers=["129.16.125.242:9092"]) #,
#                             value_deserializer = lambda m: m.decode('ascii'))

    consumer.subscribe(topics=['test'])
#    print("in main")
    print('hohoho')
 #   return ('hejhej')
   # return Response(events(),
    #                mimetype='multipart/x-mixed-replace; boundary=frame')



    def events():
        print("in events")
        for message in consumer:
 #         if message is not None:
  #            result='{} {} '.format(message.value, message.offset) #.append('hello') #str(message.value).decode('utf-8'))  # <--- here (str)
   #       yield result
#           print(message.value)
#           yield (b'--frame\r\n'
 #                 b'Content-Type:image/png\r\n\r\n' + message.value + b'\r\n\r\r')
           imgfile = BytesIO(message.value)
           img = Image.open(imgfile)
#           print(img)
           imag = np.fromstring(message.value, sep ="/")
           cv2.imwrite(str(message.offset) + ".png", imag)
           print("efter imwrite")
   #      f = open("test.txt","a") #opens file with name of "test.txt"
    #     f.write("\n offset: {} ".format(message.offset))

     #    f.close()

         # print(message.value)
#    for message in consumer:
        # This will wait and print messages as they become available
       # print('Offset: %s' % message.offset)
 #       return 'Offset: %s' % message.offset
    return Response(events())

if __name__ == "__main__":
   # index()
    main()
#    app.run(debug=True)

