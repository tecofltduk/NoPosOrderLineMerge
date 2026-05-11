{
    "name": "POS No Order Lines Merge",
    "version": "17.0.1.0.0",
    "summary": "Prevent POS from merging identical order lines",
    "category": "Point of Sale",
    "author": "Tecof",
    "license": "LGPL-3",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_no_line_merge/static/src/js/pos_no_line_merge.js",
        ],
    },
    "installable": True,
    "application": False,
}
