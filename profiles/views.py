from django.shortcuts import render
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets
from profile.serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return self.request.user.profile
