from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Exempt from CSRF validation (ensure this is safe for your use case)
def classification_results(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse the JSON body
            label = data.get('label', '')
            confidence = data.get('confidence', 0)
            
            # You can process the data here and store it or perform actions
            
            return JsonResponse({'status': 'success', 'message': 'Data received successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=400)
