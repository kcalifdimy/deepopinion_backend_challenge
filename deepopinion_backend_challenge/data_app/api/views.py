import csv
import pandas as pd
import io
import openpyxl
# import magic
import pylibmagic
# import magic
from upload_validator import FileTypeValidator
from rest_framework import parsers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from deepopinion_backend_challenge.data_app.models import  Text
from .serializers import DataSerializer, FileUploadSerializer
from deepopinion_backend_challenge.utils.check_file import is_csv_file, is_excel_file

class EXCELUploadView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser]

    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file_upload']
        file_validator = serializer.validated_data['file_upload']

        # csv_validator = FileTypeValidator(allowed_types=['text/plain'], allowed_extensions=['.csv'])
        excel_validator = FileTypeValidator(allowed_types=['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'], allowed_extensions=['.xlsx', 'xls'])
        # excel_validator(file_validator)
        try:
            excel_validator(file_validator)
            df = pd.read_excel(file, engine='openpyxl')
            for _, row in df.iterrows():
                new_file = Text(text=row['Account'])
                new_file.save()        
        except Exception as e:
                return Response({"status": "only excel file is excepted"})
        return Response({"status": "success"}, status.HTTP_201_CREATED)



class CSVUploadView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser]

    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file_upload']
        file_validator = serializer.validated_data['file_upload']
        csv_validator = FileTypeValidator(allowed_types=['text/plain'], allowed_extensions=['.csv'])

        try:
            csv_validator(file_validator)
            file_data = io.StringIO(file.read().decode("utf-8"))
            csv_data = pd.read_csv(file_data)
            for _, row in csv_data.iterrows():
                new_file = Text(text=row['Text'])
                new_file.save()                
        except Exception as e:
                return Response({"status": "only csv file is excepted"})
        return Response({"status": "success"}, status.HTTP_201_CREATED)
    

    
class CSVUploadViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = DataSerializer
    lookup_field = 'id'  
    # parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser]



   