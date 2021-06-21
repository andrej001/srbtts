from pydub import AudioSegment

combined = AudioSegment.from_mp3("azbuka/_.mp3")

#rad sa stringom
with open('text_goes_here.txt', 'r') as file:
    old_s = file.read().replace('\n', '')
old_s = old_s.lower()
old_s = old_s.replace(" ","_")
old_s = old_s.replace(".","_")
old_s = old_s.replace(",","_")
old_s = old_s.replace("š","0")
old_s = old_s.replace("č","1")
old_s = old_s.replace("ć","2")
old_s = old_s.replace("dj","3")
old_s = old_s.replace("đ","3")
old_s = old_s.replace("dz","4")
old_s = old_s.replace("dž","4")
old_s = old_s.replace("ž","5")
old_s = old_s.replace("nj","6")
old_s = old_s.replace("lj","7")
s = [char for char in old_s]
br = len(s)
i = 0
#glavni deo tts-a
for x in s:
    i+=1
    combined+=AudioSegment.from_mp3("azbuka/"+x+".mp3")
    print(str(round((i/br)*100))+"%")

combined.export("output.mp3", format="mp3")
print("Vaš audio fajl je spreman.")
