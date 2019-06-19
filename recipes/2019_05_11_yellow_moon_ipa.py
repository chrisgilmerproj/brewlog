#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Brew Shop

Yellow Moon IPA

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
from brew.recipes import RecipeBuilder
from brew.styles import StyleFactory
from brew.utilities.efficiency import calculate_brew_house_yield  # noqa


def main():

    recipe = {
        u'name': u"Yellow Moon IPA (Extract)",
        u'start_volume': 4.0 + (3.0 / 4.0),
        u'final_volume': 5.0,
        u'grains': [
            {u'name': u'Pale Liquid Extract',
             u'weight': 7.0,
             u'grain_type': u'lme'},
            {u'name': u'Caramel Crystal Malt 20l',
             u'weight': 1.0,
             u'grain_type': u'specialty'},
            {u'name': u'Munich Malt',
             u'weight': 0.5,
             u'grain_type': u'specialty'},
            {u'name': u'Cara Pils Dextrine',
             u'weight': 0.5,
             u'grain_type': u'specialty'},
        ],
        u'hops': [
            {u'name': u'Centennial',
             u'weight': 1.0,
             u'boil_time': 60.0},
            {u'name': u'Centennial',
             u'weight': 1.0,
             u'boil_time': 30.0},
            {u'name': u'Cascade US',
             u'weight': 1.0,
             u'boil_time': 10.0},
            {u'name': u'Cascade US',
             u'weight': 1.0,
             u'boil_time': 0.0},
        ],
        u'yeast': {
            u'name': u'Wyeast 1056',
        },
        u'data': {
            u'brew_house_yield': 0.425,
            u'units': u'imperial',
        },
    }

    data_dir = os.path.abspath(os.path.join(os.getcwd(), 'data/'))
    loader = JSONDataLoader(data_dir)
    beer = parse_recipe(recipe, loader)
    print(beer.format(short=True))

    factory = StyleFactory(os.path.join(data_dir, 'bjcp', 'styles.json'))
    style = factory.create_style('21', 'A')
    print("")
    print(style.format())

    print('Style issues:')
    errors = style.recipe_errors(beer)
    for err in errors:
        print('- {}'.format(err))

    print('')

    builder = RecipeBuilder(name='Pale Ale',
                            grain_list=[g.grain for g in beer.grain_additions],
                            hop_list=[h.hop for h in beer.hop_additions],
                            target_ibu=54.6,
                            target_og=1.060,
                            brew_house_yield=0.50,
                            start_volume=4.0,
                            final_volume=5.0,
                            )

    percent_list = [0.9, 0.05, 0.025, 0.025]
    grain_additions = builder.get_grain_additions(percent_list)
    for grain_add in grain_additions:
        print(grain_add.convert_to_lme(0.50).format())
        print('')

    # BIAB Measurement 1.0085, volume reduced by 0.5 Gallons
    # This is before adding extract to volume but after grains were removed
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    bhy = calculate_brew_house_yield(4.8,
                                     1.005,
                                     grain_additions)
    print("\nBrew House Yield: {:0.2%} (Specialty Grains BIAB)".format(bhy))

    # After extract added
    # This is before adding extract to volume but after grains were removed
    bhy = calculate_brew_house_yield(4.8,
                                     1.054,
                                     beer.grain_additions)
    print("\nBrew House Yield: {:0.2%} (After extract addition)".format(bhy))

    lbs_dme = beer.get_wort_correction(54, 4.8)
    print("\nAdd {:0.2f} lbs of DME to fix wort".format(lbs_dme))

    original_gravity = 1.073  # at approximately 4G
    original_gravity = 1.059  # at approximately 5G
    print("\nOriginal Gravity: {:0.4} at 5G".format(original_gravity))

    final_gravity_refractometer = 1.028
    final_gravity_hydrometer = 1.014
    print("\nFinal Gravity: {:0.4}".format(final_gravity_hydrometer))

"""
Transferred to a secondary after 3 weeks on 2019/06/03. Gravity was 1.028.  Added one package of Windsor British-style beer yeast from Danstar.  It was 11g dry.
"""


if __name__ == "__main__":
    main()
