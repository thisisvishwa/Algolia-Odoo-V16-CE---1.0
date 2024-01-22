```python
from odoo import http
from odoo.http import request
from .models.algolia_search import AlgoliaSearch

class AlgoliaSearchController(http.Controller):

    @http.route('/algolia_search', type='json', auth='user')
    def algolia_search(self, **kwargs):
        search_query = kwargs.get('search_query', '')
        algolia_search = AlgoliaSearch()
        results = algolia_search.search_products(search_query)
        return results

    @http.route('/algolia_search/config', type='json', auth='user')
    def get_algolia_config(self):
        algolia_search = AlgoliaSearch()
        config = algolia_search.get_config()
        return config

    @http.route('/algolia_search/config', type='json', auth='user', methods=['POST'])
    def set_algolia_config(self, **kwargs):
        algolia_search = AlgoliaSearch()
        config = kwargs.get('config', {})
        algolia_search.set_config(config)
        return {'status': 'success'}

    @http.route('/algolia_search/facets', type='json', auth='user')
    def get_facets(self):
        algolia_search = AlgoliaSearch()
        facets = algolia_search.get_facets()
        return facets

    @http.route('/algolia_search/facets', type='json', auth='user', methods=['POST'])
    def set_facets(self, **kwargs):
        algolia_search = AlgoliaSearch()
        facets = kwargs.get('facets', [])
        algolia_search.set_facets(facets)
        return {'status': 'success'}
```