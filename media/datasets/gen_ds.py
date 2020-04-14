import random
print("SL.No.,Subject,Rating,Marks,Rand")
subjects=["Physics","Chemistry","CS","Mathematics"]
for i in range(0,200):
    print(i+1,subjects[random.randrange(0,4)],random.randrange(1,6),random.randrange(40,101),2*(i+1)+46,sep=",")