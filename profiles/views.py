from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from profiles.serializers import ProfileSerializer

@api_view(['GET',])
@permission_classes((permissions.IsAuthenticated,))
def profile_view(request):
    profile = request.user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

