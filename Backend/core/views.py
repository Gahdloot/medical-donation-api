from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Client
from .serializer import ClientSerializer


def sign_up(request):
    pass


@api_view(['GET'])
def get_patients(request):

    if request.data.blood_group == 'O-':
        patient_filter = Client.objects.filter(needs_donation=True).all()
        serializer = ClientSerializer(patient_filter, many=True)
        return Response(serializer)
    patient_filter = Client.objects.filter(needs_donation=True, blood_group=request.data.blood_group).all()
    serializer = ClientSerializer(patient_filter, many=True)
    return Response(serializer) 


@api_view(['POST'])
def set_donation_status(request):
    client_info = dict(request.data)
    client = Client.objects.get(id=client_info.id)
    if client.eligible_donate():
        client.wants_to_donate= client_info.wants_to_donate
        client.save()
        return Response()
    else:
        return Response({"message": "Your are not eligible to donate yet"})


@api_view(['POST'])
def agree_to_donate(request):
    pass


@api_view(['POST'])
def set_patient_status(request):
    client_info = dict(request.data)
    client = Client.objects.get(id=client_info.id)
    client.wants_to_donate= client_info.wants_to_donate
    client.save()
    return Response()
    