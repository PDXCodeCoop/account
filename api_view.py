from serializers import UserSerializer, ProfileSerializer
from models import *
from rest_framework import viewsets


#Profile/User
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    #This viewset automatically provides `list` and `detail` actions.
    queryset = User.objects.all()
    serializer_class = UserSerializer
