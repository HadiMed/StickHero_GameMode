from ppadb.client import Client 

from numpy import asarray
from PIL import Image
from time import sleep

client= Client(host="127.0.0.1",port=5037)

device=client.device("26db8f72")

while True:

    image = device.screencap()

    f=open('screen.png',"wb")

    f.write(image)

    f.close()

    my_img=Image.open("screen.png")

    data=asarray(my_img)
    End_of_black_bridge1=0

   

    while data[1097][End_of_black_bridge1][0]!=0 :
        End_of_black_bridge1+=1
    if End_of_black_bridge1:
         End_of_black_bridge1+=1
    while data[1097][End_of_black_bridge1][0]==0 :
        End_of_black_bridge1+=1

    Start_of_black_bridge2=End_of_black_bridge1+1
    while data[1097][Start_of_black_bridge2][0]!=0:
        Start_of_black_bridge2+=1


    End_of_black_bridge2=Start_of_black_bridge2+1

    while data[1097][End_of_black_bridge2][0]==0 and End_of_black_bridge2<719:
        End_of_black_bridge2+=1

        
    center=(End_of_black_bridge2-Start_of_black_bridge2)/2

    
  
    length_to_ms=int((center+Start_of_black_bridge2-End_of_black_bridge1)*1.465)
    device.shell(f"input swipe  500 500 500 500 {length_to_ms+2}")

    sleep(2.5)