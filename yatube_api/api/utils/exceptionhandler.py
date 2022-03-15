from rest_framework.views import exception_handler

HANDLERS = {
    'NotAuthenticated': 'Учетные данные не были предоставлены',
    'Http404': 'Страница не найдена.',
    'PermissionDenied': (
        'У вас недостаточно прав для выполнения данного действия.'
    ),
}


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__

    if exception_class in HANDLERS:
        response.data = {'detail': HANDLERS[exception_class]}
        return response

    return response
