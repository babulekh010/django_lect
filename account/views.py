from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class RegistrationView(APIView):
    def post(self, request):
        print(dir(request))
        print(request.data)
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = 'You are done'
            return Response(message)




