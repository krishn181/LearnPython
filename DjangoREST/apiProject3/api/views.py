from  rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

#CRUD operation APIView

class StudentApi(APIView):
    # Read all or single data
    def get(self, request, pk=None):
        if pk:
            try:
                student = Student.objects.get(id=pk)
                serializer = StudentSerializer(student)
                return Response( serializer.data, status=status.HTTP_200_OK )
            except Student.DoesNotExist:
                return Response({"Error":"Student not found"},status=status.HTTP_204_NO_CONTENT)
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response( serializer.data, status=status.HTTP_200_OK )


    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errorsr,status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({"Error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errorsr,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"Error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
            





            
