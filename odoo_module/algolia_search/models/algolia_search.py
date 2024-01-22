```python
from odoo import models, fields, api
from algoliasearch.search_client import SearchClient

class AlgoliaSearch(models.Model):
    _name = 'algolia.search'
    _description = 'Algolia Search'

    algolia_app_id = fields.Char(string='Algolia App ID', required=True)
    algolia_api_key = fields.Char(string='Algolia API Key', required=True)
    algolia_index_name = fields.Char(string='Algolia Index Name', required=True)

    @api.model
    def create(self, vals):
        record = super(AlgoliaSearch, self).create(vals)
        client = SearchClient.create(record.algolia_app_id, record.algolia_api_key)
        index = client.init_index(record.algolia_index_name)
        products = self.env['product.template'].search([])
        for product in products:
            index.save_object({
                'objectID': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.list_price,
                'category': product.categ_id.name,
            })
        return record

    @api.model
    def search_products(self, query, filters=None):
        client = SearchClient.create(self.algolia_app_id, self.algolia_api_key)
        index = client.init_index(self.algolia_index_name)
        search_parameters = {
            'query': query,
            'filters': filters,
            'attributesToRetrieve': ['name', 'description', 'price', 'category'],
            'hitsPerPage': 10,
        }
        response = index.search(**search_parameters)
        return response['hits']
```