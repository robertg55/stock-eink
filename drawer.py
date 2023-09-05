#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import logging
from waveshare_epd import epd2in13_V3
import time
from PIL import Image, ImageDraw, ImageFont
import threading

class ScreenPrinter(threading.Thread):
    def __init__(self, data, lock):
        threading.Thread.__init__(self)
        self.lock = lock
        self.data = data

    def run(self):
        try:
            logging.info("Start")
            epd = epd2in13_V3.EPD()
            epd.init()
            epd.Clear(0xFF)
            picdir = os.path.join(os.path.dirname(__file__), "pic")
            font24 = ImageFont.truetype(os.path.join(picdir, "Font.ttc"), 24)

            stock_image = Image.new("1", (epd.height, epd.width), 255)
            stock_draw = ImageDraw.Draw(stock_image)

            epd.displayPartBaseImage(epd.getbuffer(stock_image))
            lastran = time.time()
            while True:
                if lastran + 0.3 < time.time():
                    stock_draw.rectangle((0, 0, 250, 122), fill=255)
                    stock_draw.text(
                        (161, 99), time.strftime("%H:%M:%S"), font=font24, fill=0
                    )

                    with self.lock:
                        y_loc = 0
                        for symbol, price in self.data.items():
                            if price:
                                stock_draw.text(
                                    (0, y_loc), f"{symbol}: {format(price, '.2f')}", font=font24, fill=0
                                )
                                y_loc = y_loc + 40
                        epd.displayPartial(epd.getbuffer(stock_image))
                    lastran = time.time()

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info("ctrl + c:")
            epd2in13_V3.epdconfig.module_exit()
            exit()
