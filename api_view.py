from serializers import UserSerializer, ProfileSerializer
from models import *
from rest_framework import viewsets


#Profile/User
class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.

    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    #This viewset automatically provides `list` and `detail` actions.
    queryset = User.objects.all()
    serializer_class = UserSerializer
