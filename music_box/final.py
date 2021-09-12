import random
from playsound import playsound
sec=int(input("Duration Of Song(sec):"))
sec=sec*2
a=" "
loco="sounds"
sounds=[loco+"/1.mp3",loco+"/2.mp3",loco+"/3.mp3",loco+"/4.mp3",loco+"/5.mp3",loco+"/6.mp3",loco+"/7.mp3",loco+"/8.mp3",loco+"/9.mp3",loco+"/10.mp3",loco+"/11.mp3",loco+"/12.mp3",loco+"/13.mp3",loco+"/14.mp3",loco+"/15.mp3",loco+"/16.mp3",loco+"/17.mp3",loco+"/18.mp3",loco+"/19.mp3",loco+"/20.mp3",loco+"/21.mp3",loco+"/22.mp3",loco+"/23.mp3",loco+"/24.mp3",loco+"/25.mp3",loco+"/26.mp3",loco+"/27.mp3",loco+"/28.mp3",loco+"/29.mp3",loco+"/30.mp3",loco+"/31.mp3",loco+"/32.mp3",loco+"/33.mp3",loco+"/34.mp3",loco+"/35.mp3",loco+"/36.mp3"]
k=1
mus=0
j=0
z=open("music_points.txt","w")
while j<=sec:
   m=0
   k = random.randint(0, 34)
   z.write(a+".")
   z.write("\n")
   a = ""
   while m <= k:
      a += " "
      m += 1
   j+=1
z.close()
p=open("music_points.txt","r")
for i in p.read():
    if i=="\n":
        mus=0
    elif i == " ":
        mus+=1
    elif i == ".":
        playsound(sounds[mus])
p.close()
