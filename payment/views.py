from django.views.generic import TemplateView

class PaymentCompleteView(TemplateView):
    template_name = 'payment/complete.html'