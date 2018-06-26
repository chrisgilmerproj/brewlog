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
9:45AM - Turn off heat.  Keep covered.  Ensure system is ready for chilling.
9:55AM - Begin wort chiller process into carboy
       - Measure wort between 1.061-1.062 gravity and 3.9 Gallons
       - Gallons measured as 50mm / 55mm in the 3 gallon maker range
       - add 2x 4.22floz of yeast starter, about 1 cup of fluid
       - added 4 cups of water to get 1.056 gravity
       - added 4 cups of water to get 1.051 gravity


On kegging the readings were:
- 1.031 with refractometer
- 1.014 to 1.020 with hydrometer (had a problem with CO2 bubbles lifting it)

$ abv -o 1.051 -f 1.031 -r
4.53%
$ abv -o 1.051 -f 1.014
4.86%
$ abv -o 1.051 -f 1.020
4.07%

Based on these I'll say it was 4.5% ABV
"""


if __name__ == "__main__":
    main()
