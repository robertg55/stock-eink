from yticker import YTicker
import threading
import logging
import time

logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler("logs.txt", mode='a'),
                        logging.StreamHandler()
    ])

class StockTracker(threading.Thread):       
    def __init__(self, symbol, data, lock, reconnect_delay=5):
        threading.Thread.__init__(self)  
        self.lock = lock
        self.data = data
        self.symbol = symbol
        self.reconnect_delay = reconnect_delay

    def run(self):
        YTicker(on_ticker=self.on_message, ticker_names=list([self.symbol]), on_close=self.on_close)

    def on_message(self, _, message):
        try:
            with self.lock:
                self.data.update({message["id"]: round(message["price"], 2)})
        except Exception as e:
            logging.error(e, exc_info=True)
    
    def on_close(self, *_):
        logging.info(f"connection lost, reconnecting in {self.reconnect_delay}")
        time.sleep(self.reconnect_delay)
        self.run()