from django.shortcuts import render,HttpResponse

# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def request_exception(request):
    a,b=5,0
    print(a," ",b)
    ip = get_client_ip(request)
    print('IP Address',ip)
    # c = a/b
    return HttpResponse(f'IP address: {ip}')
