from rest_framework import serializers
from home.views import *

class item(serializers.ModelSerializer):
    class Meta:
        model = createpost
        fields = '__all__'