from django.core.exceptions import ValidationError


# example of validators, can improvise
def validate_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('All letters must be alphabetic')


def validate_file_size(value):
    max_size_photo = 5242880

    filesize = value.size

    if filesize > max_size_photo:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value
