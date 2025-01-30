from django.http import JsonResponse
from django.views import View

class MinhaAPI(View):
    def get(self, request):
        return JsonResponse({ 'message': 'Olá Mundo!' })

if __name__ == '__main__':
    View()