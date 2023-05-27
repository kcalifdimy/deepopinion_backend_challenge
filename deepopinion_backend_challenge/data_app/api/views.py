import csv
import pandas as pd
import io
from rest_framework import parsers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from deepopinion_backend_challenge.data_app.models import  Data
from .serializers import DataSerializer, FileUploadSerializer


class CSVUploadView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser]

    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file_upload']
        file_data = io.StringIO(file.read().decode("utf-8"))
        csv_data = pd.read_csv(file_data)
        for _, row in csv_data.iterrows():
            new_file = Data(text=row['Text'])
            new_file.save()
        return Response({"status": "success"}, status.HTTP_201_CREATED)



class CSVUploadViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    lookup_field = 'id'  
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser]
    

