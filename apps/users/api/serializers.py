from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        data = {
            'id': instance.id,
            'email': instance.email,
            'firstName': instance.first_name,
            'lastName': instance.last_name,
            'phoneNumber': instance.phone_number,
            'password': instance.password,
        }
        return data   
    
    def validate_names(self):
        return self.context['firstName'].isalpha() and self.context['lastName'].isalpha()      

    def validate(self, data):
        print('validating names...')
        if None not in (self.context['firstName'], self.context['lastName']) and self.validate_names():
            print('names valid!')
            return data
        else:
            raise serializers.ValidationError('Invalid data')


    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
        # updated_user = super().update(instance, validated_data)
        # updated_user.set_password(validated_data['password'])
        # updated_user.save()
        # return updated_user
    

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        data = {
            'id': instance['id'],
            'email': instance['email'],
            'firstName': instance['first_name'],
            'lastName': instance['last_name'],
            'phoneNumber': instance['phone_number'],
            'password': instance['password'],
        }
        return data



# class TestUserSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=200)
#     email = serializers.EmailField()
#     unallowed = ['@', '!', '$', '%']

#     def validate_first_name(self, value):
#         for character in self.unallowed:
#             if character in value:
#                 raise serializers.ValidationError('invalid username')
#         return value
    
#     def validate_email(self, value):
#         return value
    
#     def validate(self, data):
#         return data

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance
    
#     def save(self, **kwargs):
#         print()