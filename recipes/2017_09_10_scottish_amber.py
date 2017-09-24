#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Brew Shop

Scottish Amber

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
        u'name': u"Scottish Amber (Extract)",
        u'start_volume': 5.0,
        u'final_volume': 5.0,
        u'grains': [
            {u'name': u'Pale Liquid Extract',
             u'weight': 7.0 + (1.125 / 16) - (3.25 / 16.0),  # Remove container
             u'grain_type': u'lme'},
            {u'name': u'Caramel Crystal Malt 80l',
             u'weight': 1.04,
             u'grain_type': u'specialty'},
            {u'name': u'Smoked Malt',
             # Rausch means "Smoked"
             u'weight': 1.04,
             u'data': {
                 u'color': 6.0},
             u'grain_type': u'specialty'},
            {u'name': u'Victory Malt',
             u'weight': 1.04,
             u'grain_type': u'specialty'},
        ],
        u'hops': [
            {u'name': u'Perle',
             u'weight': 1.0,
             u'boil_time': 60.0},
            {u'name': u'Perle',
             u'weight': 1.0,
             u'boil_time': 30.0},
        ],
        u'yeast': {
            u'name': u'Wyeast 1728',
        },
        u'data': {
            u'brew_house_yield': 0.458,
            u'units': u'imperial',
        },
    }

    data_dir = os.path.abspath(os.path.join(os.getcwd(), 'data/'))
    loader = JSONDataLoader(data_dir)
    beer = parse_recipe(recipe, loader)
    print(beer.format(short=True))

    # Refractometer needed to be calibrated
    REF_ADJ = 0.005

    # BIAB Measurement
    # This is before removing grains from mash water
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    bhy = calculate_brew_house_yield(1.0,
                                     1.048 + REF_ADJ,
                                     grain_additions)
    print("\nBrew House Yield: {:0.2%} (Mash BIAB)".format(bhy))

    # BIAB Measurement
    # This after sparging mash
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    bhy = calculate_brew_house_yield(4.5,
                                     1.011 + REF_ADJ,
                                     grain_additions)
    print("\nBrew House Yield: {:0.2%} (Post Sparge)".format(bhy))

    # BIAB Measurement
    # This after second sparging
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    bhy = calculate_brew_house_yield(5.0,
                                     1.010 + REF_ADJ,
                                     grain_additions)
    print("\nBrew House Yield: {:0.2%} (Post Second Sparge)".format(bhy))

    # Post Extract Addition
    # Extract adds about 2qt to volume
    bhy = calculate_brew_house_yield(5.5,
                                     1.052 + REF_ADJ,
                                     beer.grain_additions)
    print("\nBrew House Yield: {:0.2%} (Pre-Boil, after extract addition)".format(bhy))  # noqa

    # Boil
    bhy = calculate_brew_house_yield(5.25,
                                     1.065 + REF_ADJ,
                                     beer.grain_additions)
    print("\nBrew House Yield: {:0.2%} (Boil)".format(bhy))  # noqa

    # Measured OG
    # at 1.070

    # Measured FG
    # - with refractometer at 1.043
    # - with hydrometer at 1.020R


if __name__ == "__main__":
    main()
