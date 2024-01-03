from rest_framework import serializers
from rajan.views import *

class item(serializers.ModelSerializer):
    class Meta:
        model = createpost
        fields = '__all__'