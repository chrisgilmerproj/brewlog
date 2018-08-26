#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Brew Shop

White House Honey Ale
https://en.wikipedia.org/wiki/White_House_Honey_Ale

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
        u'name': u"White House Honey Ale (Extract)",
        u'start_volume': 3.0,
        u'final_volume': 5.0,
        u'grains': [
            {u'name': u'Caramel Crystal Malt 60l',
             u'weight': 0.75,
             u'grain_type': u'specialty'},
            {u'name': u'Biscuit Malt',
             u'weight': 0.5,
             u'grain_type': u'specialty'},
            {u'name': u'Pilsner Liquid Extract',
             u'weight': 3.3,
             u'data': {
                 u'color': 8.0},
             u'grain_type': u'lme'},
            {u'name': u'Light Dry Extract',
             u'weight': 1.0,
             u'grain_type': u'dme'},
            # Add honey after aroma hops, boil for 5 min
            {u'name': u'Honey',
             u'weight': 1.0,
             u'grain_type': u'lme'},
        ],
        u'hops': [
            # bittering
            {u'name': u'East Kent Golding',
             u'weight': 1.5,
             u'boil_time': 45.0,
             u'hop_type': u'pellet',
             u'percent_alpha_acids': 0.058,  # from bag
             },
            # flavoring (none)
            # aroma
            {u'name': u'Fuggle',
             u'weight': 1.5,
             u'boil_time': 1.0,
             u'hop_type': u'pellet',
             u'percent_alpha_acids': 0.049,  # from bag
             },
        ],
        u'yeast': {
            u'name': u'Danstar Lallemand Windsor Ale Yeast',
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
    style = factory.create_style(26, 'B')  # Belgian Dubbel (Wikipedia), could be 23 Specialty
    print("")
    print(style.format())

    print('Style issues:')
    errors = style.recipe_errors(beer)
    for err in errors:
        print('- {}'.format(err))


"""
Notes:

Starter made from 6oz of DME and 1.8L of water approx 30 min before brew
Intend to use two yeast packets for this brew

Did a 3gallon brew because my pot is 9gallons.  Steep grains for 30+min.



"""


if __name__ == "__main__":
    main()
