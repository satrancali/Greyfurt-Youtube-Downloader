from pytube import YouTube
import re

videoitag=[]
videoTur=[]
videoRes=[]
#a=YouTube("https://www.youtube.com/watch?v=CaksNlNniis").streams.get_by_itag(247).download()
a=YouTube("https://www.youtube.com/watch?v=CaksNlNniis")
for b in a.streams.filter(adaptive=True).all():
   print(b)
#for b in a.streams.filter(subtype='mp4').filter(resolution='1080p').all():
for b in a.streams.filter(resolution='1080p').filter(adaptive=True).all():
  # print(b)
   cevir=str(b)
   itagim = re.search('itag="(.*)" mime', cevir)
   videoitag.append(itagim.group(1))

   turum = re.search('mime_type="(.*)" res', cevir)
   videoTur.append(turum.group(1))

   kalitem = re.search('res="(.*)" fps', cevir)
   videoRes.append(kalitem.group(1))
for b in a.streams.filter(adaptive=True).filter(resolution='720p').all():
   #print(b)
   cevir = str(b)
   itagim = re.search('itag="(.*)" mime', cevir)
   videoitag.append(itagim.group(1))

   turum = re.search('mime_type="(.*)" res', cevir)
   videoTur.append(turum.group(1))

   kalitem = re.search('res="(.*)" fps', cevir)
   videoRes.append(kalitem.group(1))
for b in a.streams.filter(adaptive=True).filter(resolution='480p').all():
   #print(b)
   cevir = str(b)
   itagim = re.search('itag="(.*)" mime', cevir)
   videoitag.append(itagim.group(1))

   turum = re.search('mime_type="(.*)" res', cevir)
   videoTur.append(turum.group(1))

   kalitem = re.search('res="(.*)" fps', cevir)
   videoRes.append(kalitem.group(1))
for b in a.streams.filter(adaptive=True).filter(resolution='360p').all():
   #print(b)
   cevir = str(b)
   itagim = re.search('itag="(.*)" mime', cevir)
   videoitag.append(itagim.group(1))

   turum = re.search('mime_type="(.*)" res', cevir)
   videoTur.append(turum.group(1))

   kalitem = re.search('res="(.*)" fps', cevir)
   videoRes.append(kalitem.group(1))


print(a.thumbnail_url)
sayi=int(len(videoitag))
i=0
while i<sayi:
     print(i,videoitag[i],videoRes[i],videoTur[i])
     i=i+1

cevap=input("Which one ?")
a.streams.get_by_itag(int(cevap)).download()
# 0 , 1 , 2, 3
print(" ")
