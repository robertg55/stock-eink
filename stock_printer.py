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
        font36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)
        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        
        # # partial update
        logging.info("4.show time...")
        time_image = Image.new('1', (epd.height, epd.width), 255)
        time_draw = ImageDraw.Draw(time_image)
        
        epd.displayPartBaseImage(epd.getbuffer(time_image))
        num = 0
        while (True):
            time_draw.rectangle((0, 0, 250, 122), fill = 255)
            time_draw.text((161, 99), time.strftime('%H:%M:%S'), font = font24, fill = 0)
            time_draw.text((0, 0), "TQQQ: 38.04", font = font24, fill = 0)
            time_draw.text((0, 40), "SQQQ: 19.82", font = font24, fill = 0)
            time_draw.text((0, 80), "SPY: 439.97", font = font24, fill = 0)
            epd.displayPartial(epd.getbuffer(time_image))
            num = num + 1
            if(num == 10):
                break

        epd.sleep()
            
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd2in13_V3.epdconfig.module_exit()
        exit()
    

if __name__ == "__main__":
    main()
