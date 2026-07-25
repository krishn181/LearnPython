from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import datetime

class SimpleMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print(f"[{datetime.datetime.now()}] Request URL: {request.path}")

    def process_response(self, request,response):
        print(f"[{datetime.datetime.now()}] Response status code: {response.status_code}")
        return response

class BlockIpMiddleWare(MiddlewareMixin):
    BLOCKED_IP =  ['127.0.0.1']
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.BLOCKED_IP:
            return HttpResponse('your ip is blocked ')
