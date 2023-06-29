from django.core.exceptions import ValidationError


def validate_file_size(image_object):
    if image_object.size > 10_000:
        raise ValidationError("The maximum file size is 10 MB")
