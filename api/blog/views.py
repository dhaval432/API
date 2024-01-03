from rest_framework.decorators import api_view
from rest_framework.response import Response
from rajan.models import Blog
from .serializers import item

@api_view(['GET'])
def getData(request):
    post = Blog.objects.all()
    serializer = item(post, many=True)
    return Response(serializer.data)