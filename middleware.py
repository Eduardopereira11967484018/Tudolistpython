# todo_app/middleware.py
import jwt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.conf import settings

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        excluded_paths = ['/api/login/', '/api/docs/', '/admin/']
        if any(request.path.startswith(path) for path in excluded_paths):
            return self.get_response(request)

        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            request.user = user
        except (jwt.InvalidTokenError, User.DoesNotExist):
            return JsonResponse({'error': 'Unauthorized'}, status=401)
        
        return self.get_response(request)