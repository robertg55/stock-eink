# https://pypi.org/project/websocket_client/
import websocket
import threading
import logging

logging.basicConfig(level=logging.INFO)


class StockTracker(threading.Thread):
    def __init__(self, data, symbol, lock, token):
        threading.Thread.__init__(self)
        self.lock = lock
        self.data = data
        self.symbol = symbol
        self.token = token

    def run(self):
        websocket.enableTrace(False)
        ws = websocket.WebSocketApp(
            f"wss://ws.finnhub.io?token={self.token}",
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        ws.on_open = self.on_open
        ws.run_forever()

    def on_message(self, ws, message):
        try:
            price = None
            symbol = None
            for value in message.split(","):
                if '"p":' in value:
                    price = round(int(value.split(":")[1]), 2)
                if '"s":' in value:
                    symbol = value.split(":")[1][1:-1]
            if price and symbol:
                with self.lock:
                    self.data.update({symbol: price})
        except Exception as e:
            logging.error(e, exc_info=True)

    def on_error(self, ws, error):
        logging.error(error)

    def on_close(self, ws):
        logging.info("### closed ###")

    def on_open(self, ws):
        ws.send('{"type":"subscribe","symbol":"%s"}' % self.symbol)
