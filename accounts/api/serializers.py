from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model #nie wazane ze mam customowego usera!!!

from rest_framework.serializers import (
	CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer, 
    SerializerMethodField,
    ValidationError
    )

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    #email2 = EmailField(label='Potwierdz Email')
    class Meta:
        model = User
        fields = [
            'email',
            #'email2',
            'password',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    # def validate_email(self, value):
    #     data = self.get_initial()
    #     email1 = data.get("email")
    #     email2 = value
    #     if email1 != email2:
    #         raise ValidationError("Rozne emaile")
    #     return value

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            email = email,
            password = password,
            active = True, #tak dla pewnosci ze nie mozna stworzyc admina
            admin = False, #prawdopodobnie niepotrzebne
            staff = False, #ale dla spokoju glowy...
            prouser = False, #security zawsze na propsie
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField()
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }

    def validate(self, data):
    	user_obj = None
        email=data.get("email")
        password = data["password"]
        user = User.objects.filter(email=email).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Ten uzytkownik nie istnieje.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Niepoprawne dane, sprobuj ponownie.")

        data["token"]="DEFINITELY NOT A TOKEN"
        return data