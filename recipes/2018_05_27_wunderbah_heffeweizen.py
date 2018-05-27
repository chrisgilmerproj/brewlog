#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Brew Shop

Wunderbah Heffeweizen

Used by permission of The Brew Shop. All rights reserved.

You can purchase this kit at their store:

- http://thebrewshopbend.com/

Original Stats:

OG:
FG:
ADF:
IBU:
Color:
Alcohol:
Boil:    60 min
Pre-Boil Volume:
Pre-Boil Gravity:
"""  # noqa

import os

from brew.parsers import JSONDataLoader
from brew.parsers import parse_recipe
from brew.styles import StyleFactory
from brew.utilities.efficiency import calculate_brew_house_yield  # noqa


def main():

    recipe = {
        u'name': u"Wunderbah Heffeweizen (Extract)",
        u'start_volume': 4.0,
        u'final_volume': 5.0,
        u'grains': [
            {u'name': u'Wheat Liquid Extract',
             u'weight': 7.0 + (7.25 - 3.5) / 16,
             u'grain_type': u'lme'},
        ],
        u'hops': [
            # bittering
            {u'name': u'Hallertau US',
             u'weight': 1.0,
             u'boil_time': 60.0,
             u'hop_type': u'whole',
             u'percent_alpha_acids': 0.054,  # from bag
             },
            # flavoring
            {u'name': u'Hallertau US',
             u'weight': 1.0,
             u'boil_time': 30.0,
             u'hop_type': u'whole',
             u'percent_alpha_acids': 0.054,  # from bag
             },
        ],
        u'yeast': {
            u'name': u'Wyeast 3068',
        },
        u'data': {
            u'units': u'imperial',
        },
    }

    data_dir = os.path.abspath(os.path.join(os.getcwd(), 'data/'))
    loader = JSONDataLoader(data_dir)
    beer = parse_recipe(recipe, loader)
    print(beer.format(short=True))

    factory = StyleFactory(os.path.join(data_dir, 'bjcp', 'styles.json'))
    style = factory.create_style(10, 'A')  # German Wheat Beer, Weizen/Weissbier
    print("")
    print(style.format())

    print('Style issues:')
    errors = style.recipe_errors(beer)
    for err in errors:
        print('- {}'.format(err))


"""
Notes:

Tub of extract:
- Before opening: 7lbs, 7.25 oz (or 3.380kg)
- After opening:  3.5oz (or 98kg)
- Total Used: 7lbs, 3.75oz (or 3.382kg)

8:00AM - Started brewing by boiling 4 gallons of water
8:10AM - Startead two yeast smack packs.
8:30AM - Water boiling, added LME
8:45AM - Measured gravity between 1.057-1.059. Added Bittering Hops.
9:15AM - Added flavoring hops.
9:45AM - 
"""


if __name__ == "__main__":
    main()
