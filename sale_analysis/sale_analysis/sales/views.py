# views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import generate_insights
from .serializers import RepPerformanceDataSerializer,TeamPerformanceDataSerializer,PerformanceTrendDataSerializer
import pandas as pd



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd


class REP_PERFORMANCE(APIView):
    def post(self, request):
        serializer = RepPerformanceDataSerializer(data=request.data)
        if serializer.is_valid():
            print("I am inside")
            rep_id = self.request.data.get("rep_id")
            question = f'Tell me detailed performance analysis and feedback of rep id: {rep_id}', 
            print(question)
            
            
            file_path = 'sales/sales_performance_data.csv'  
            try:
                df = pd.read_csv(file_path)
            except FileNotFoundError:
                return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
            except pd.errors.EmptyDataError:
                return Response({"error": "File is empty"}, status=status.HTTP_400_BAD_REQUEST)
            except pd.errors.ParserError:
                return Response({"error": "File is corrupt or not a CSV"}, status=status.HTTP_400_BAD_REQUEST)

           
            print(df.head())
            answer = generate_insights(df, question)

           
            return Response({"answer": answer}, status=status.HTTP_201_CREATED)
        else:
            
            print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TEAM_PERFORMANCE(APIView):
    def post(self, request):
        serializer = TeamPerformanceDataSerializer(data=request.data)
        if serializer.is_valid():
            print("I am inside")
            question = f'Tell me detailed summary of the sales team overall performance ! ', 
            print(question)
            
           
            file_path = 'sales/sales_performance_data.csv'  
            try:
                df = pd.read_csv(file_path)
            except FileNotFoundError:
                return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
            except pd.errors.EmptyDataError:
                return Response({"error": "File is empty"}, status=status.HTTP_400_BAD_REQUEST)
            except pd.errors.ParserError:
                return Response({"error": "File is corrupt or not a CSV"}, status=status.HTTP_400_BAD_REQUEST)

            
            print(df.head())
            answer = generate_insights(df, question)

           
            return Response({"answer": answer}, status=status.HTTP_201_CREATED)
        else:
            
            print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PERFORMANCE_TRENDS(APIView):
    def post(self, request):
        serializer = PerformanceTrendDataSerializer(data=request.data)
        if serializer.is_valid():
            print("I am inside")
            time_period = self.request.data.get("time_period")
            question = f'Tell me sales data over time period over time period: {time_period} to identify trends and forecast future peroformance !', 
            print(question)
            
           
            file_path = 'sales/sales_performance_data.csv' 
            try:
                df = pd.read_csv(file_path)
            except FileNotFoundError:
                return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
            except pd.errors.EmptyDataError:
                return Response({"error": "File is empty"}, status=status.HTTP_400_BAD_REQUEST)
            except pd.errors.ParserError:
                return Response({"error": "File is corrupt or not a CSV"}, status=status.HTTP_400_BAD_REQUEST)

            
            print(df.head())
            answer = generate_insights(df, question)

           
            return Response({"answer": answer}, status=status.HTTP_201_CREATED)
        else:
            
            print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

