from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView
    )

from rest_framework.filters import SearchFilter

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
    )
from .permissions import IsOwnerOrReadOnly

from main.models import Companies, Codes
from .serializers import (
    CompaniesSerializer,
    CompanyDetailSerializer,
    CompanyCreateSerializer,
    CodesSerializer,
    CodeCreateSerializer,
    CodesDetailSerializer
    
    )

from math import radians,degrees,cos,sqrt

class CompaniesListAPIView(ListAPIView):
    permissions_classes = [AllowAny]
    queryset = Companies.objects.filter(visible=True)
    serializer_class =  CompaniesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'tag1', 'tag2', 'tag3']
    def get_queryset(self, *args, **kwargs):
        queryset_list = Companies.objects.filter(visible=True)
        
        query_info=self.request.GET.get("l")
        if query_info:
            query = query_info.split(',')
            range = float(query[2])
            U=radians(float(query[0])),radians(float(query[1]))
            dx=range/6371.00/cos(U[0])
            dy=range/6371.00
            D=degrees(U[0]-dy),degrees(U[0]+dy),degrees(U[1]-dx),degrees(U[1]+dx)
            queryset_list=queryset_list.filter(
                    Q(latitude__gte=D[0]),
                    Q(latitude__lte=D[1]),
                    Q(longitude__gte=D[2]),
                    Q(longitude__lte=D[3])
                    ).distinct()
        return queryset_list

class CompanyCreateAPIView(CreateAPIView):
    #permissions_classes = [IsAuthenticated]
    queryset = Companies.objects.all()
    serializer_class =  CompanyCreateSerializer


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class CompanyDetailAPIView(RetrieveAPIView):
    #permissions_classes = [IsAuthenticated]
    #queryset = Companies.objects.all()
    queryset = Companies.objects.filter(visible=True)
    serializer_class =  CompanyDetailSerializer
    lookup_field = 'id'

class CompanyUpdateAPIView(RetrieveUpdateAPIView):
    permissions_classes = [IsOwnerOrReadOnly]
    #queryset = Companies.objects.all()
    queryset = Companies.objects.filter(visible=True)
    serializer_class =  CompanyDetailSerializer
    lookup_field = 'id'
    


class CodesListAPIView(ListAPIView):
    queryset = Codes.objects.filter(visible=True)
    serializer_class =  CodesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['company__id']

class CodesDetailListAPIView(ListAPIView):
    queryset = Codes.objects.filter(visible=True)
    serializer_class =  CodesDetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['company__id']

class CodeCreateAPIView(CreateAPIView):
    #permissions_classes = [IsAuthenticated]
    queryset = Codes.objects.all()
    serializer_class =  CodeCreateSerializer

    #def perform_create(self, serializer):
    #    if company__creator__id==self.request.user:
    #        serializer.save()

class CodeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Codes.objects.filter(visible=True)
    permissions_classes = [IsOwnerOrReadOnly]
    serializer_class =  CodesDetailSerializer
    lookup_field = 'id'
