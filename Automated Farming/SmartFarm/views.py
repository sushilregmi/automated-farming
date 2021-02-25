from django.shortcuts import render
from .models import Sensordata
import sys
from subprocess import run,PIPE
from rest_framework.decorators import api_view
from rest_framework.response import Response
import joblib



def index(request):
	data = Sensordata.objects.all().order_by('-sample_id')[:5]

	dl = len(data)
	return render(request, "SmartFarm/show.html",{"objects":data,"length":dl})

def more(request,sample_id):
	obj = Sensordata.objects.filter(pk = sample_id).first()
	print(obj.humidity)
	return render(request, "SmartFarm/more.html",{"object":obj})

def turnonoff(request):
	onoff = request.GET.get("onoff")
	out = run([sys.executable,'//Users//kailash//Desktop//hello.py',onoff],shell = False, stdout = PIPE)

@api_view(["POST"])
def restapi(request):
    try:
        temp = request.data.get('temperature', None)
        hum = request.data.get('humidity', None)
        mois = request.data.get('moisture', None)
        inputs = [temp, hum, mois]

        if not None in inputs:
            temp = float(temp)
            hum = float(hum)
            mois = float(mois)
            result = [[temp, hum, mois]]
            classifier = joblib.load('model.pkl')
            prediction = classifier.predict(result)[0]
            predictions = {
                'error': '0',
                'message': 'successful',
                'prediction': prediction

            }
        else:
            predictions = {
                'error': '1',
                'message': 'Invalid inputs'
            }
    except Exception as e:
        predictions = {
            'error': '2',
            'message': str(e)
        }
    print(predictions)
    return Response(predictions)

@api_view(['GET'])
def restapi1(request):
	data = Sensordata.objects.all().first()
	temp1=data.temperature
	hum1=data.humidity
	mois1=data.moisture
	dataa={
		'temperature':temp1,
		'humidity':hum1,
		'moisture':mois1
	}

	return Response(dataa)