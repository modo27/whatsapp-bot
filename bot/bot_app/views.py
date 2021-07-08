import requests
import random
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def index(request):
    if request.method == 'POST':
        incoming_msg = request.POST['Body'].lower()
        resp = MessagingResponse()
        msg = resp.message()
        if incoming_msg == 'hello':
            response = """Hey, I'm a bot. \nFeeling Depressed ? Don't worry
            \nWe have a something to brighten up your mood
            \nChoose 
            \n1. If you're a dog lover
            \n2. If you're a cat person
            \n3. If you like both """
            msg.body(response)
        elif incoming_msg == '1':
            r = requests.get('https://dog.ceo/api/breeds/image/random')
            data = r.json()
            msg.media(data['message'])
        elif incoming_msg == '2':
            msg.media('https://cataas.com/cat')
        elif incoming_msg == '3':
            choice = random.choice([1, 2])
            if choice == 1:
                r = requests.get('https://dog.ceo/api/breeds/image/random')
                data = r.json()
                msg.media(data['message'])
            else:
                msg.media('https://cataas.com/cat')
        else:
            msg.body('Send hello to see the options')
        return HttpResponse(str(resp))
# Create your views here.
