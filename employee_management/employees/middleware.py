import logging
import json
from datetime import datetime

logger = logging.getLogger('employee_management')

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request sent
        if request.path.startswith('/api/'):
            self.log_request(request)

        response = self.get_response(request)

        # Log the response received
        if request.path.startswith('/api/'):
            self.log_response(request, response)

        return response

    def log_request(self, request):
        try:
            data = {
                'timestamp': datetime.now().isoformat(),
                'method': request.method,
                'path': request.path,
                'user': str(request.user),
                'ip': self.get_client_ip(request)
            }
            if request.method in ['POST', 'PUT', 'PATCH']:
                data['body'] = json.loads(request.body) if request.body else {}
            
            logger.info(f"Request: {json.dumps(data)}")
        except Exception as e:
            logger.error(f"Error logging request: {str(e)}")

    def log_response(self, request, response):
        try:
            data = {
                'timestamp': datetime.now().isoformat(),
                'path': request.path,
                'status_code': response.status_code,
                'user': str(request.user),
            }
            logger.info(f"Response: {json.dumps(data)}")
        except Exception as e:
            logger.error(f"Error logging response: {str(e)}")

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')