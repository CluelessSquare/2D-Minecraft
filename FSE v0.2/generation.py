import numpy as np
from random import *
pieces=[]
anchor=20
length=0

for i in range(780):
    x=randint(-3,3)
    anchor+=x
    if anchor<=6:
        anchor+=3
    if anchor>=79:
        anchor-=3

    temp=np.zeros((85,1),dtype="int")
    temp[anchor:].fill(1)
    temp[anchor]=3

    if i!=0:
        if not length:

            length = randint(0, 20)
            x=choice([84,0])
            temp=np.delete(pieces[i-1],[x])
            if x:
                temp = np.insert(temp, 0, 0).reshape((85, 1))

            else:
                temp = np.append(temp, 0).reshape((85, 1))


            # temp=np.insert(temp,x,0).reshape((85,1))
        else:
            temp=pieces[i-1]
            length-=1
        # else:
        #     temp=pieces[i-1]
        #     x=randint(-1,0)
        #     if x==-1:
        #         temp=np.delete(temp,[84])
        #     else:
        #         temp=np.delete(temp,[0])
        #
        #
        #     if x:
        #         temp = np.insert(temp,0,0).reshape(85,1)
        #     else:
        #         temp=np.append(temp,0).reshape((85,1))

        # temp.reshape((85,1))

    # for j in range(randint(5,30)):
    #     try:
    #         temp[anchor+randint(10,35)]=2
    #     except IndexError:
    #         continue

    pieces.append(temp)

blocks=np.concatenate(pieces,axis=1)

blocks[60:,:]=2
print(blocks)