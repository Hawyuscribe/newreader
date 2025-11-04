from django.http import JsonResponse, HttpResponse


def healthz(request):
    """Lightweight health check endpoint for uptime probes.
    Returns 200 OK with a small JSON payload.
    """
    # Minimal response to avoid heavy imports or DB hits
    return JsonResponse({
        "status": "ok",
        "app": "neurology_mcq",
    })

