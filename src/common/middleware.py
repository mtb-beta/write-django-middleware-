class MyLoggingMiddleware:

    def __init__(self, get_responce):
        self.get_responce = get_responce
        print("MyLogging Middleware init")

    def __call__(self, request):
        print("pre-call:{}".format(request))
        responce = self.get_responce(request)
        print("post-call:{}".format(request))
        return responce
