from .models import Copy

class CopySerializers:
    class Meta:
        model = Copy
        fields = ["id", "libraryName", "created_at", "book_id"]
    
    def create(self, validated_data: dict) -> Copy:
        return Copy.objects.create(**validated_data)