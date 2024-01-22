{
    "name": "algolia_search",
    "version": "1.0",
    "category": "Website",
    "summary": "Algolia Search Integration for Odoo eCommerce",
    "sequence": 1,
    "author": "Your Company",
    "website": "https://www.yourcompany.com",
    "description": """
    This module integrates the Algolia search engine into the Odoo eCommerce platform. 
    It provides enhanced search performance, advanced search features, and a user-friendly interface.
    """,
    "depends": ["base", "website_sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/algolia_search_view.xml",
        "views/templates.xml",
        "data/algolia_search_demo.xml"
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "external_dependencies": {
        "python": ["algoliasearch"]
    }
}