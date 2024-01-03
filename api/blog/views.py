from rest_framework.decorators import api_view
from rest_framework.response import Response
from ranjan.models import userData
from .serializers import item

@api_view(['GET'])
def getData(request):
    post = userData.objects.all()
    serializer = item(post, many=True)
    return Response(serializer.data)