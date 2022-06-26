from users.models import IsActivated


class ActivatedMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.activated = IsActivated.load().is_activated
        return self.get_response(request)
