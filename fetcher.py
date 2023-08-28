import yliveticker
import threading
import logging

logging.basicConfig(level=logging.INFO)


class StockTracker(threading.Thread):       
    def __init__(self, data, lock):
        threading.Thread.__init__(self)  
        self.lock = lock
        self.data = data

    def run(self):
        yliveticker.YLiveTicker(on_ticker=self.on_message, ticker_names=[self.data.keys()])

    def on_message(self, message):
        try:
            with self.lock:
                self.data.update({message["id"]: round(message["price"], 2)})
        except Exception as e:
            logging.error(e, exc_info=True)


