from rest_framework.views import APIView
from rest_framework.response import Response


class CollectorView(APIView):
    def get(self, request):
        return Response("ok", status=200)