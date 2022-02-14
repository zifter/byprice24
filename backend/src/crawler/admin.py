from crawler.models import ScrapingState
from crawler.tasks import get_agent
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe


@admin.register(ScrapingState)
class ScrapingStateAdmin(admin.ModelAdmin):
    change_form_template = 'scraping_state.html'

    def response_change(self, request, obj):
        if 'force-scrape' in request.POST:
            job_ids = get_agent().schedule(force=True, marketplace=obj.marketplace)
            url = f'/admin/django-rq/queues/0/{job_ids[0]}/'

            self.message_user(request, mark_safe(f"This <a href='{url}'>Marketplace</a> is scheduled to scrape"))
            return HttpResponseRedirect('.')

        return super().response_change(request, obj)
