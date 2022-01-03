from crawler.models import ScrapingState
from crawler.tasks import get_agent
from django.contrib import admin
from django.http import HttpResponseRedirect


@admin.register(ScrapingState)
class ScrapingStateAdmin(admin.ModelAdmin):
    change_form_template = 'scraping_state.html'

    def response_change(self, request, obj):
        if 'force-scrape' in request.POST:
            get_agent().schedule(force=True, marketplace=obj.marketplace)

            self.message_user(request, 'This Marketplace is scheduled to scrape')
            return HttpResponseRedirect('.')

        return super().response_change(request, obj)
