from crawler.agent import get_agent
from crawler.models import CrawlerState
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe


@admin.register(CrawlerState)
class CrawlerStateAdmin(admin.ModelAdmin):
    change_form_template = 'scraping_state.html'

    def response_change(self, request, obj):
        if 'force-scrape' in request.POST:
            job_ids = get_agent().schedule(force=True, marketplace=obj.marketplace)
            url = f'/admin/django-rq/queues/0/{job_ids[0]}/'

            msg = mark_safe(f"This marketplace is scheduled to scrape - <a href='{url}'>Look at Job</a>")
            self.message_user(request, msg)
            return HttpResponseRedirect('.')

        return super().response_change(request, obj)
