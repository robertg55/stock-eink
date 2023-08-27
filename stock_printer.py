#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
from waveshare_epd import epd2in13_V3
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)




def main():
    try:
        logging.info("Start")
        epd = epd2in13_V3.EPD()
        epd.init()
        epd.Clear(0xFF)
        picdir = os.path.join(os.path.dirname(__file__), 'pic')
        # Drawing on the image
        font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        
        # # partial update
        logging.info("4.show time...")
        time_image = Image.new('1', (epd.height, epd.width), 255)
        time_draw = ImageDraw.Draw(time_image)
        
        epd.displayPartBaseImage(epd.getbuffer(time_image))
        num = 0
        while (True):
            time_draw.rectangle((120, 80, 220, 105), fill = 255)
            time_draw.text((120, 80), time.strftime('%H:%M:%S'), font = font24, fill = 0)
            epd.displayPartial(epd.getbuffer(time_image))
            num = num + 1
            if(num == 10):
                break
        
        logging.info("Clear...")
        epd.init()
        epd.Clear(0xFF)
        
        logging.info("Goto Sleep...")
        epd.sleep()
            
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd2in13_V3.epdconfig.module_exit()
        exit()
    

if __name__ == "__main__":
    main()
