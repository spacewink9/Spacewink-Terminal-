import websocket
import json

class WebSocket:
    def __init__(self, url):
        self.url = url
        self.socket = websocket.WebSocketApp(url,
                                             on_message=self.on_message,
                                             on_error=self.on_error,
                                             on_close=self.on_close)

    def on_message(self, message):
        data = json.loads(message)
        # process incoming message data
        print(f"Received message: {data}")

    def on_error(self, error):
        # handle error
        print(f"WebSocket error: {error}")

    def on_close(self):
        # handle connection closed
        print("WebSocket connection closed")

    def run(self):
        self.socket.run_forever()
