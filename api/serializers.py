from rensoftapi.api.members.models import Principal
from rest_framework import serializers
from .models import Principal,Dependants


class PrincipalSerializer(serializers.HyperlinkedModelSerialized):
    class Meta:
        model= Principal
        fields= ('first_name', 'last_name', 'member_type','member_number')

class DependantsSerializer(serializers.HyperlinkedModelSerialized):
    class Meta:
        model= Dependants
        fields= ('first_name', 'last_name', 'member_type','principal_no')