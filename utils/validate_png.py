from django.core.exceptions import ValidationError

def validade_icon(image):

    if not image.name.lower().endswith('.png'):
        raise ValidationError('Imagem inválida')