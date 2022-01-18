from django_elasticsearch_dsl.management.commands.search_index import Command as DjangoElasticSearchSearchIndexCommand
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import Index


class Command(DjangoElasticSearchSearchIndexCommand):
    help = 'Prepare search index'

    def handle(self, *args, **options):
        models = self._get_models(options['models'])

        for index in registry.get_indices(models):
            self.stdout.write(f"Creating index '{index._name}'")
            index: Index = index
            if not index.exists():
                index.create()
