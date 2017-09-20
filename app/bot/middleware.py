from django.http import JsonResponse
from namba_one.settings import APP_TOKEN


class BotAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.GET.get('token', None)

        if not token or token != APP_TOKEN:
            return JsonResponse({
                'code': 401,
                'success': False,
                'message': 'Unauthorized'
            }, status=401)

        response = self.get_response(request)

        return response
