from django.views.generic import UpdateView
from django.urls import reverse_lazy
from account.models import Profile

class DashboardProfileView(UpdateView):
    template_name = 'dashboard/profile.html'
    model = Profile
    fields = [
        'first_name',
        'last_name',
        'address',
        'avatar',
    ]
    
    def get_success_url(self):
        return reverse_lazy('dashboard:profile', kwargs={'pk':self.get_object().pk})