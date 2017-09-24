#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Brew Shop

10 Pound Stout

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
from brew.styles import StyleFactory
from brew.utilities.efficiency import calculate_brew_house_yield  # noqa


def main():

    recipe = {
        u'name': u"10 Pound Stout (Extract)",
        u'start_volume': 4.0,
        u'final_volume': 5.0,
        u'grains': [
            {u'name': u'Amber Liquid Extract',
             u'weight': 6.0 + 15.75 / 16.0,
             u'grain_type': u'lme'},
            {u'name': u'Dark Dry Extract',
             u'weight': 3.001,
             u'grain_type': u'dme'},
            {u'name': u'Caramel Crystal Malt 120l',
             u'weight': 1.0,
             u'grain_type': u'specialty'},
            {u'name': u'Black Barley Stout',
             u'weight': 0.5,
             u'grain_type': u'specialty'},
            {u'name': u'Roasted Barley',
             u'weight': 0.5,
             u'grain_type': u'specialty'},
        ],
        u'hops': [
            {u'name': u'Columbus',
             u'weight': 2.0,
             u'boil_time': 60.0,
             u'hop_type': u'pellet'},
            {u'name': u'Cascade US',
             u'weight': 7.0,
             u'boil_time': 15.0,
             u'hop_type': u'whole wet'},
            {u'name': u'Cascade US',
             u'weight': 7.0,
             u'boil_time': 5.0,
             u'hop_type': u'whole wet'},
        ],
        u'yeast': {
            u'name': u'Wyeast 1084',
        },
        u'data': {
            u'brew_house_yield': 0.79,
            u'units': u'imperial',
        },
    }

    data_dir = os.path.abspath(os.path.join(os.getcwd(), 'data/'))
    loader = JSONDataLoader(data_dir)
    beer = parse_recipe(recipe, loader)
    print(beer.format(short=True))

    factory = StyleFactory(os.path.join(data_dir, 'bjcp', 'styles.json'))
    style = factory.create_style(20, 'C')
    print("")
    print(style.format())

    print('Style issues:')
    errors = style.recipe_errors(beer)
    for err in errors:
        print('- {}'.format(err))

    # Specialty Grains, Multi Step Mash
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    bhy = calculate_brew_house_yield(6.12 / 4.0,
                                     1.030,
                                     grain_additions)
    print("\nBrew House Yield: {:0.2%} (Multi Step Mash)".format(bhy))  # noqa

    # After diluting
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    bhy = calculate_brew_house_yield(6.12 / 4.0 + 3.5,  # Added into water
                                     1.009,
                                     grain_additions)
    print("\nBrew House Yield: {:0.2%} (Dilution)".format(bhy))  # noqa

    # Extract weights
    # LME
    # - In tub: 7lbs 1 7/8 oz
    # - tub: 3 1/8oz or 87g
    # - total: 6lbs 15 6/8oz
    #
    # DME
    # - In bag: 2lbs 9 1/2 oz (200g went to starter),
    #           also 1.178 kg or 1.378 kg = 3.03797 lbs
    # - bag: 1/2oz or 13g
    # - total: 2lbs 9oz + 200g or 1.365 kg = 3.0093099 lbs

    # 1.073  # post adding DME + LME


if __name__ == "__main__":
    main()