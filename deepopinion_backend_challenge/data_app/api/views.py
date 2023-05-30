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
from rest_framework.decorators import action
from rest_framework.response import Response
from deepopinion_backend_challenge.data_app.models import  Text, Tag
from .serializers import DataSerializer, FileUploadSerializer, TagSerializer
from deepopinion_backend_challenge.utils.check_file import is_csv_file, is_excel_file

class EXCELUploadView(generics.CreateAPIView):
    """
    This is an Excel file upload feature.
    I use pandas to read file because pandas can read large files very fast
    """
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
                new_file = Text(text=row['Text'])
                new_file.save()        
        except Exception as e:
                return Response({"status": "only excel file is excepted"})
        return Response({"status": "success"}, status.HTTP_201_CREATED)



class CSVUploadView(generics.CreateAPIView):
    """
    This is a CSV file upload feature.
    I use pandas to read file because pandas can read large files very fast
    """
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
            csv_data = pd.read_csv(file_data, engine="python")
            for _, row in csv_data.iterrows():
                new_file = Text(text=row['Text'])
                new_file.save()                
        except Exception as e:
                return Response({"status": "only csv file is excepted"})
        return Response({"status": "success"}, status.HTTP_201_CREATED)
    

    
class CSVEXCELViewSet(viewsets.ModelViewSet):
    """
     This feature get all data. 
     This feature create single data with tags
     This feature also delete single data, add and change tag of a data.  
    """
    queryset = Text.objects.all()
    serializer_class = DataSerializer
    lookup_field = 'id'  
    #parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser]get


    # This function create endpoint that gets all available aspect.
    @action(detail=False)
    def get_aspects(self, request):
        aspect_data = Tag.objects.values('aspect')
        all_aspect = []
        for value in aspect_data:
               value = value['aspect']
               all_aspect.append(value)

        return Response(all_aspect)
   

    # This function create endpoint that gets all available sentiment.
    @action(detail=False)
    def get_sentiment(self, request):
        sentiment_data = Tag.objects.values('sentiment')
        all_sentiment = []
        for value in sentiment_data:
               value = value['sentiment']
               all_sentiment.append(value)

        return Response(all_sentiment)
   