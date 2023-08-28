#https://pypi.org/project/websocket_client/
import websocket
import threading   
import logging

logging.basicConfig(level=logging.DEBUG)

class StockTracker(threading.Thread):
    def __init__(self, data, lock, token):

        self.lock = lock
        self.data = data
        self.token = token
    def run(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={self.token}",
                                  on_message = self.on_message,
                                  on_error = self.on_error,
                                  on_close = self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()
    
    def on_message(self, ws, message):
        try:
            price = None
            symbol = None
            for value in message.split(","):
                if '"p":' in value:
                    price = value.split(":")[1]
                if '"s":' in value:
                    symbol = value.split(":")[1][1:-1]
            if price and symbol:
                with self.lock:
                    self.data.update({symbol:price})
        except Exception as e:
            logging.error(e, exc_info=True)
                
    
    def on_error(self, ws, error):
        logging.error(error)
    
    def on_close(self, ws):
        logging.info("### closed ###")
    
    def on_open(self, ws):
        for key in self.data:
            ws.send('{"type":"subscribe","symbol":"%s"}'% key)
