from rest_framework import serializers
from django.core.files.base import ContentFile
import base64, uuid, imghdr
from .models import landprep, transplanting, fertilizer, harverst, packaging, Procurement, packing

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        # If the incoming data is a base64 string, convert it to a file.
        if isinstance(data, str):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')
            file_name = str(uuid.uuid4())[:12]  # generate a random file name
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = f"{file_name}.{file_extension}"
            data = ContentFile(decoded_file, name=complete_file_name)
        return super().to_internal_value(data)
    
    def get_file_extension(self, file_name, decoded_file):
        extension = imghdr.what(file_name, decoded_file)
        if extension is None:
            extension = "jpg"
        return extension

class LandPrepSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False)
    class Meta:
        model = landprep
        fields = '__all__'

class TransplantingSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False)
    class Meta:
        model = transplanting
        fields = '__all__'

class FertilizerSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False)
    class Meta:
        model = fertilizer
        fields = '__all__'

class HarverstSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False)
    class Meta:
        model = harverst
        fields = '__all__'

class PackagingSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False)
    class Meta:
        model = packaging
        fields = '__all__'

class ProcurementSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False)
    class Meta:
        model = Procurement
        fields = '__all__'

class PackingSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False)
    class Meta:
        model = packing
        fields = '__all__'