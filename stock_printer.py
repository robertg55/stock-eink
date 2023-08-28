#!/usr/bin/python
# -*- coding:utf-8 -*-
import threading
from finnhub_fetcher import StockTracker
from screen_draw import ScreenPrinter

if __name__ == "__main__":
    lock = threading.Lock()
    data = {"SQQQ": None, "TQQQ": None, "SPY": None}
    t1 = ScreenPrinter(data, lock)
    t2 = StockTracker(data, lock, "cjjmie9r01qorp962ctgcjjmie9r01qorp962cu0")
    t1.start()
    t2.start()
