class MyLoggingMiddleware:

    def __init__(self, get_responce):
        self.get_responce = get_responce
        print("MyLogging Middleware init")

    def __call__(self, request):
        print("MyLoggingMiddleware pre-call:{}".format(request))
        responce = self.get_responce(request)
        print("MyLoggingMiddleware post-call:{}".format(request))
        return responce

from django.utils.deprecation import MiddlewareMixin

class NewLoggingMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        print("NewLoggingMiddleware process_response:{}".format(request))
        return response
