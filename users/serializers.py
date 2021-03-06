from rest_framework import serializers
from users.models import User
 
# the serializers will convert the models into JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email','password','gender','role')
