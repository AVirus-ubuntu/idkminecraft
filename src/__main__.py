from time import sleep as slp
from PIL import Image as img_, ImageDraw as imgdr_
import datetime as dt
import time as tm
import os as os

class func:
    def FNC_newImg(m:str='data/output/temp._.jpg'):
        img = img_.new('RGB', (16,16), (40,40,40,255))
        draw = imgdr_.Draw(img)

        draw.circle((7,7), radius=5, fill='white')
        draw.circle((7,8), radius=5, fill='white')
        draw.circle((8,8), radius=5, fill='white')
        
        draw.circle((8,7), radius=5, fill='gray')

        # img.show()
        img.save(m)

func.FNC_newImg()