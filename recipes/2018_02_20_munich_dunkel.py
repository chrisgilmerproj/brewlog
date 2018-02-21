#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Brewing Classic Styles

Munich Dunkel

Original Stats:

OG:      1.048 - 1.056
FG:      1.010 - 1.016
ADF:
IBU:     18 - 28
Color:   14 - 28 SRM
Alcohol: 4.5% - 5.6% ABV
Boil:    60 min
Pre-Boil Volume:
Pre-Boil Gravity:
"""  # noqa

import os

from brew.constants import GRAIN_TYPE_CEREAL
from brew.parsers import JSONDataLoader
from brew.parsers import parse_recipe
from brew.styles import StyleFactory
from brew.utilities.efficiency import calculate_brew_house_yield  # noqa


def main():

    recipe = {
        u'name': u"Munich Dunkel (All Grain)",
        u'start_volume': 7.0,
        u'final_volume': 6.0,
        u'grains': [
            {u'name': u'Munich Malt',
             u'weight': 12.2,
             u'grain_type': u'cereal'},
            {u'name': u'Chocolate Malt',
             u'weight': 0.38,
             u'data': {
                 u'color': 420.0},
             u'grain_type': u'cereal'},
            {u'name': u'Light Dry Extract',
             u'weight': 0.375,
             u'grain_type': u'dme',
             u'notes': u'Added from yeast starter'},
            {u'name': u'Light Dry Extract',
             u'weight': 2.7125,
             u'grain_type': u'dme',
             u'notes': u'Added to correct gravity'},
        ],
        u'hops': [
            # bittering
            {u'name': u'Hallertau US',
             u'weight': 1.25,
             u'boil_time': 60.0,
             u'hop_type': u'pellet',
             u'percent_alpha_acids': 0.038,  # from bag
             },
            # flavoring
            {u'name': u'Hallertau US',
             u'weight': 0.75,
             u'boil_time': 20.0,
             u'hop_type': u'pellet',
             u'percent_alpha_acids': 0.038,  # from bag
             },
        ],
        u'yeast': {
            u'name': u'Wyeast 2308',
        },
        u'data': {
            u'brew_house_yield': 0.5684,
            u'units': u'imperial',
        },
    }

    data_dir = os.path.abspath(os.path.join(os.getcwd(), 'data/'))
    loader = JSONDataLoader(data_dir)
    beer = parse_recipe(recipe, loader)
    print(beer.format(short=True))

    factory = StyleFactory(os.path.join(data_dir, 'bjcp', 'styles.json'))
    style = factory.create_style(8, 'A')  # Munich Dunkel
    print("")
    print(style.format())

    print('Style issues:')
    errors = style.recipe_errors(beer)
    for err in errors:
        print('- {}'.format(err))

    # Multi Step Mash
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_CEREAL)
    bhy = calculate_brew_house_yield(5.36,
                                     1.049,  # measure after lautering
                                     grain_additions)
    print("\nBrew House Yield: {:0.2%} (Multi Step Mash)".format(bhy))  # noqa


"""
Notes:

After lautering we have a gravity of 1.049.

Measured pot to be 14.5 inches across and the wort to be 7.5 inches deep.  That gives
1238.47 cubic inches or 5.36 gallons.

Added just over 4qts and the new height was 8.75 inches, giving 1444.89 cubic
inches or 6.25 gallons.  The new gravity is 1.041.

The gravity we want is 1.056 meaning we need to add 2.13 lbs of dme:

In [10]: get_wort_correction(41, 6.25, 56, 6.25, efficiency=44.0)
Out[10]: 2.1306818181818183

Decided to add another quart of water and thus redid this:

In [3]: get_wort_correction(41, 6.25, 56, 6.5, efficiency=44.0)
Out[3]: 2.4488636363636362

Which is 2lbs 7.2oz.

But turns out I want to account in advance for water I'll be adding from the yeast starter:

In [5]: get_wort_correction(41, 6.25, 56, 7.0, efficiency=44.0)
Out[5]: 3.085227272727273

Which is 3lbs 1.4 oz.  But I already had 6oz in the yeast starter, so we could go with
2lbs 11.4 oz.

After adding 1 lbs of light DME this is the gravity: 1.045
After adding 2 lbs of light DME this is the gravity: 1.051
After adding 11.4oz of light DME this is the gravity: 1.055

Decided to use all 2 oz of the hops.  Rounded from:

boil 1.2oz to 1.25 oz
flavoring 0.5oz to 0.75oz


"""


if __name__ == "__main__":
    main()
