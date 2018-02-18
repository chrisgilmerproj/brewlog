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

# from brew.constants import GRAIN_TYPE_SPECIALTY
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
             u'grain_type': u'specialty'},
        ],
        u'hops': [
            # bittering
            {u'name': u'Hallertau US',
             u'weight': 1.2,
             u'boil_time': 60.0,
             u'hop_type': u'pellet',
             u'percent_alpha_acids': 0.038,  # from bag
             },
            # flavoring
            {u'name': u'Hallertau US',
             u'weight': 0.5,
             u'boil_time': 20.0,
             u'hop_type': u'pellet',
             u'percent_alpha_acids': 0.038,  # from bag
             },
        ],
        u'yeast': {
            u'name': u'Wyeast 2308',
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
    style = factory.create_style(8, 'A')  # Munich Dunkel
    print("")
    print(style.format())

    print('Style issues:')
    errors = style.recipe_errors(beer)
    for err in errors:
        print('- {}'.format(err))

    # # Specialty Grains, Multi Step Mash
    # grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    # bhy = calculate_brew_house_yield(6.12 / 4.0,
    #                                  1.030,
    #                                  grain_additions)
    # print("\nBrew House Yield: {:0.2%} (Multi Step Mash)".format(bhy))  # noqa

    # # After diluting
    # grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    # bhy = calculate_brew_house_yield(6.12 / 4.0 + 3.5,  # Added into water
    #                                  1.009,
    #                                  grain_additions)
    # print("\nBrew House Yield: {:0.2%} (Dilution)".format(bhy))  # noqa


"""
Notes:

"""


if __name__ == "__main__":
    main()