from mail_sender import SendMailResponse

class Http_client:
    def __init__(self, is_available=False):
        self.requests_history = []
        self.is_available = is_available
        
    def post(self, base_url, request):
        self.requests_history.append(request)
        if self.is_available:
            return SendMailResponse(200, "OK")
        else:
            return SendMailResponse(503, "Service unavailable")