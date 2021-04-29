from django.http import HttpResponse

# Create your views here. python manage.py runserver

data = {

    "Name ": "Viviane Johnson",

    "Track ": "Backend(Python)",

    "Message ": "I hope this works! \U0001F91E"}



x = ""

# Iterating over values and attaching strings
for key, value in data.items():
    x = x + key + ": " + value + '<p>'


def index(request):
    return HttpResponse(x)
    #return HttpResponse("1")



