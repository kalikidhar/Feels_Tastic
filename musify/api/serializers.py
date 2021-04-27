#convert to json like response

from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=('id','id_u','the_host','the_guest_pause','votes_skip','created_at')