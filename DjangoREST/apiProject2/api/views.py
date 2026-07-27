from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_student(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response (serializer.data)

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','PATCH'])
def update_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"Error":"Student doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = StudentSerializer(data = request.data)
    if request.method == 'PATCH':
        serializer = StudentSerializer(student,data = request.data, partial=True)
    else:
        serializer = StudentSerializer(student,data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"Error":"Student doesn't exists"}, status=status.HTTP_404_BAD_REQUEST)
    student.delete()
    return Response({"message":"student deleted successfully"},status=status.HTTP_204_NO_CONTENT)