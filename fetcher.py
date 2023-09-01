from yticker import YTicker
import threading
import logging

logging.basicConfig(filename="logs.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


class StockTracker(threading.Thread):       
    def __init__(self, data, lock):
        threading.Thread.__init__(self)  
        self.lock = lock
        self.data = data

    def run(self):
        YTicker(on_ticker=self.on_message, ticker_names=list(self.data.keys()))

    def on_message(self, _, message):
        try:
            with self.lock:
                self.data.update({message["id"]: round(message["price"], 2)})
        except Exception as e:
            logging.error(e, exc_info=True)
