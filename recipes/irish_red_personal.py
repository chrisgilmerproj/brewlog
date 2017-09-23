#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Brew Shop

Lunar Eclipse Red

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

from brew.constants import GRAIN_TYPE_SPECIALTY
from brew.parsers import JSONDataLoader
from brew.parsers import parse_recipe
from brew.utilities.efficiency import calculate_brew_house_yield  # noqa


def main():

    recipe = {
        u'name': u"Lunar Eclipse Red (Extract)",
        u'start_volume': 4.0,
        u'final_volume': 5.0,
        u'grains': [
            {u'name': u'Pale Liquid Extract',
             u'weight': 6.0 + (15.0 + 3.0 / 8.0) / 16 - (3.0 + 1.0 / 8.0) / 16,
             u'grain_type': u'lme'},
            {u'name': u'Munich Malt',
             u'weight': 1.0,
             u'grain_type': u'specialty'},
            {u'name': u'Caramel Crystal Malt 10l',
             u'weight': 1.0,
             u'grain_type': u'specialty'},
            {u'name': u'Caramel Crystal Malt 60l',
             u'weight': 1.0,
             u'grain_type': u'specialty'},
            {u'name': u'Caramel Crystal Malt 80l',
             u'weight': 1.0,
             u'grain_type': u'specialty'},
        ],
        u'hops': [
            {u'name': u'Chinook',
             u'weight': 1.0,
             u'boil_time': 60.0},
            {u'name': u'Chinook',
             u'weight': 1.0,
             u'boil_time': 15.0},
        ],
        u'yeast': {
            u'name': u'Wyeast 1084',
        },
        u'data': {
            u'brew_house_yield': 0.4396,
            u'units': u'imperial',
        },
    }

    data_dir = os.path.abspath(os.path.join(os.getcwd(), 'data/'))
    loader = JSONDataLoader(data_dir)
    beer = parse_recipe(recipe, loader)
    print(beer.format(short=True))

    # BIAB Measurement 1.017, volume reduced by 0.4 Gallons
    # This is before adding extract to volume but after grains were removed
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    bhy = calculate_brew_house_yield(3.62,
                                     1.017,
                                     grain_additions)
    print("\nBrew House Yield: {:0.2%} (Specialty Grains BIAB)".format(bhy))

    # Measurement 1.078, measured right after addition of extract
    bhy = calculate_brew_house_yield(3.62,
                                     1.078,
                                     beer.grain_additions)
    print("\nBrew House Yield: {:0.2%} (Pre-Boil, after extract addition)".format(bhy))  # noqa

    # Measurement 1.082, volume reduced by 0.6
    # # 1.082 Refractometer
    # # 22, 11.2%, 1088.0 @ 69deg
    bhy = calculate_brew_house_yield(3.41,
                                     1.082,
                                     beer.grain_additions)
    print("\nBrew House Yield: {:0.2%} (After Boil, before water addition)".format(bhy))  # noqa

    # Final Measurement 1.053, add water up to 5.0 Gallons
    bhy = calculate_brew_house_yield(5.0,
                                     1.053,
                                     beer.grain_additions)
    print("\nBrew House Yield: {:0.2%} (Total Beer)".format(bhy))


if __name__ == "__main__":
    main()
