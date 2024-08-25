# bfhl_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer
from .models import ProcessedData


# bfhl_app/views.py (add this function)
from django.shortcuts import render


def index(request):
    return render(request, 'api/index.html')

class BFHLAPIView(APIView):
    def get(self, request):
        data = ProcessedData.objects.all().values()
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]
            lowest_lowercase_alphabet = min(
                [char for char in data if char.islower()], default=""
            )

            # Save the response data in the database
            processed_data = ProcessedData.objects.create(
                user_id="21BCEXXXX",  # Replace with your roll number
                numbers=",".join(numbers),
                alphabets=",".join(alphabets),
                lowest_lowercase_alphabet=lowest_lowercase_alphabet
            )
            processed_data.save()

            response_data = {
                "is_success": True,
                "user_id": processed_data.user_id,
                "numbers": numbers,
                "alphabets": alphabets,
                "lowest_lowercase_alphabet": lowest_lowercase_alphabet,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
