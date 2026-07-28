from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateAPI(generics.GenericAPIView, 
                            mixins.ListModelMixin, # used to get api
                            mixins.CreateModelMixin): # used for post api
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # get api
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #post api
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentUpdateRetrieveDeleteAPI( generics.GenericAPIView,
                                     mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

     # get api
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        #put api
    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    