from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Disable CSRF for simplicity
def welcome_api(request):
    if request.method == "POST":
        try:
            # Parse JSON input
            data = json.loads(request.body)
            name = data.get("name", "Guest")

            # Prepare the response
            response_data = {
                "message": f"Welcome {name}!"
            }
            return JsonResponse(response_data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
