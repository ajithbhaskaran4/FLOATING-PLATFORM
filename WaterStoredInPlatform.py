from imutils import contours
from skimage import measure
import numpy as np
import cv2 as cv

def WaterStoredInPlatform(platform):
    a=platform
    test=np.array(a)
    depo=np.zeros(a.shape)
    fit=np.ones(a.shape)
    fit=-1*fit
    maxval=np.max(np.max(a))
    status_z=0
    for k in range(maxval):
        minval=np.min(np.min(test))
        water_1=np.zeros(a.shape)  
        if minval==0:
            status_z=1
            pos=np.where(test==minval)
            test[pos]=test[pos]+1
            
        else:
            status_z=0
            pos=np.where(test==minval)
            water_1[pos]=1
            test[pos]=test[pos]+1
            
        if status_z==0:
            labels = measure.label(water_1, neighbors=4, background=0)
            maxl=np.max(np.max(labels))
            for z_1 in range(maxl):
                z=z_1+1
                val=np.where(labels==z)
                content=a[val]
                zero=np.where(content==0)
                top=labels[0,0:a.shape[1]]
                down=labels[a.shape[0]-1,0:a.shape[1]]
                left=labels[0:a.shape[0],0]
                right=labels[0:a.shape[0],a.shape[1]-1]
                border=np.concatenate((top,down,left,right))
                bod=np.where(border==z)
                if len(zero[0])>0 or len(bod[0])>0:
                    water_1[val]=0
            
        depo=depo+water_1
    water=np.sum(np.sum(depo))
    return water
                        
