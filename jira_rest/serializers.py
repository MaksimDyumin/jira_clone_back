from rest_framework.serializers import ModelSerializer, ImageField
from .models import User, Room

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
    picture = ImageField(read_only=True, source='profile_picture')
    class Meta:
        model = User
        fields = ['username', 'picture']


class ProfilePictureSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['picture']
    
    picture = ImageField(write_only=True, source='profile_picture')


class UserRoomSerializer(ModelSerializer):
    users = ProfileUserSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = [ 'id', 'title', 'description', 'author', 'users']
        read_only_fields = ['users', 'author']

    