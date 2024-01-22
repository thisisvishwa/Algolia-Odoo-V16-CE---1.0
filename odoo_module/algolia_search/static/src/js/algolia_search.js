odoo.define('algolia_search.algolia_search', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var publicWidget = require('web.public.widget');

    var _t = core._t;

    publicWidget.registry.AlgoliaSearch = publicWidget.Widget.extend({
        selector: '#search-bar',
        events: {
            'keyup': '_onKeyup',
            'change': '_onChange',
        },

        start: function () {
            this.algoliaClient = algoliasearch('YourApplicationID', 'YourSearchOnlyAPIKey');
            this.algoliaIndex = this.algoliaClient.initIndex('YourIndexName');
            return this._super.apply(this, arguments);
        },

        _onKeyup: function (ev) {
            var query = $(ev.currentTarget).val();
            this._search(query);
        },

        _onChange: function (ev) {
            var query = $(ev.currentTarget).val();
            this._search(query);
        },

        _search: function (query) {
            var self = this;
            this.algoliaIndex.search(query, function(err, content) {
                if (err) {
                    console.error(err);
                    return;
                }
                self._updateSearchResults(content.hits);
            });
        },

        _updateSearchResults: function (results) {
            var $results = $('#search-results');
            $results.empty();
            if (results.length === 0) {
                $results.append($('<p>').text(_t('No results found')));
                return;
            }
            results.forEach(function (result) {
                var $result = $('<div>').addClass('search-result');
                $result.append($('<h2>').text(result.name));
                $result.append($('<p>').text(result.description));
                $results.append($result);
            });
        },
    });

    return {
        AlgoliaSearch: publicWidget.registry.AlgoliaSearch,
    };
});