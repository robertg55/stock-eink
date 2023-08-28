#!/usr/bin/python
# -*- coding:utf-8 -*-
import threading
from fetcher import StockTracker
from drawer import ScreenPrinter

if __name__ == "__main__":
    lock = threading.Lock()
    data = {"SQQQ": None, "TQQQ": None, "SPY": None}

    t1 = ScreenPrinter(data, lock)
    for symbol in data.keys():
        t = StockTracker(data, lock)
        t.start()
    t1.start()

