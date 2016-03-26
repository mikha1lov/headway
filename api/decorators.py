# coding: utf-8
from django.http import JsonResponse


def required_post_params(params):
    def wrapper(f):
        def decorator(request, *args, **kwargs):
            missing_params = []
            for param in params:
                if param not in request.POST:
                    missing_params.append(param)
            if not missing_params:
                return f(request, *args, **kwargs)
            return JsonResponse({
                'status': 'error', 'message': 'Missing required params: %s' % ', '.join(missing_params)
            })
        return decorator
    return wrapper
