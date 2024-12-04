from django.shortcuts import render

def error_404(request, exception):
    context = {"exeption": exception}
    response = render(request, "errors/404.html", context=context)
    response.status_code = 404
    return response