from rest_framework.serializers import ModelSerializer
from .models import User

class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
                'password': {
                    'style':{
                        'input_type': 'password'
                    },
                    'write_only': True
                }
            }

    def create(self, validated_data):
        ModelClass = self.Meta.model
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'])
        return user
    

class ProfileUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']