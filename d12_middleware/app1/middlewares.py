# Function Based Middleware
from typing import Any


def funcMiddleware(get_response):
    print('--------func:one-time configuration/initialization---------')
    def myMiddleware(request):
        print('-----func:Code execute before view-------')
        response = get_response(request)
        print('-----func:Code execute After view-------')
        return response
    return myMiddleware

# Class Based Middleware
class classMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print('--------class:one-time configuration/initialization---------')
    def __call__(self,request):
        print('-----class:Code execute before view-------')
        response = self.get_response(request)
        print('-----class:Code execute After view-------')
        return response