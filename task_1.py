from queue import Queue
from uuid import uuid4


class Request:
    def __init__(self, request_data):
        self.request_data = request_data
        self.request_id = uuid4()


class RequestQueue:
    def __init__(self):
        self.queue = Queue()

    def generate_request(self, request_data=None):
        print("Generating request...")
        request = Request(request_data)
        print("Request generated: %s" % request.request_id)
        self.queue.put(request)

    def process_request(self):
        request = self.queue.get()
        if request:
            print("Processing request: %s" % request.request_id)
        else:
            print("No requests to process.")


if __name__ == "__main__":
    request_queue = RequestQueue()
    while True:
        try:
            request_queue.generate_request()
            request_queue.process_request()
        except KeyboardInterrupt:
            break

