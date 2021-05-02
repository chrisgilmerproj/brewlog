import os

from brew.constants import GRAIN_TYPE_SPECIALTY
from brew.parsers import JSONDataLoader
from brew.parsers import parse_recipe

from brew.recipes import RecipeBuilder
from brew.styles import StyleFactory
from brew.utilities.efficiency import calculate_brew_house_yield  # noqa


def main():
    """
    From Northern Brewer Kit
    """
    brew_house_yield = 0.425

    recipe = {
        u"name": u"Kama Citra Session IPA (Extract)",
        u"start_volume": 2.5,
        u"final_volume": 5.0,
        u"grains": [
            {
                "name": "Golden Light Liquid Extract",
                "weight": 6.0,
                "grain_type": "lme"
            },
            {
                "name": "Golden Light Dry Extract",
                "weight": 1.0,
                "grain_type": "dme"
            },
            {
                "name": "Caramel Crystal Malt 40l", # Valencia Grains Caramel 40
                "weight": 0.75,
                "grain_type": "specialty",
            }
        ],
        u"hops": [
            {
                "name": "Centennial",
                "weight": 0.5,
                "hop_type": "pellet",
                "boil_time": 60.0,
                "percent_alpha_acids": 0.082,
            },
            {
                "name": "Cascade US",
                "weight": 1.0,
                "hop_type": "pellet",
                "boil_time": 20.0,
                "percent_alpha_acids": 0.06,
            },
            {
                "name": "Cascade US",
                "weight": 1.0,
                "hop_type": "pellet",
                "boil_time": 10.0,
                "percent_alpha_acids": 0.06,
            },
            {
                "name": "Citra",
                "weight": 2.0,
                "hop_type": "pellet",
                "boil_time": 0.0,
                "percent_alpha_acids": 0.133,
            }
            # { # Dry Hop
            #     "name": "Cascade",
            #     "weight": 1.0,
            #     "hop_type": "pellet",
            #     u"boil_time": 10.0,
            #     "percent_alpha_acids": 0.06,
            # },
            # { # Dry Hop
            #     "name": "Citra",
            #     "weight": 2.0,
            #     "hop_type": "pellet",
            #     u"boil_time": 0.0,
            #     "percent_alpha_acids": 0.133,
            # },
        ],
        u"yeast": {
            "name": "Omega Yeast 009",
        },
        u"data": {u"brew_house_yield": brew_house_yield, u"units": u"imperial"},
    }

    data_dir = os.path.abspath(os.path.join(os.getcwd(), "data/"))
    loader = JSONDataLoader(data_dir)
    beer = parse_recipe(recipe, loader)
    print(beer.format(short=True))

    factory = StyleFactory(os.path.join(data_dir, "bjcp", "styles.json"))
    style = factory.create_style("21", "B")
    print("")
    print(style.format())

    print("Style issues:")
    errors = style.recipe_errors(beer)
    for err in errors:
        print("- {}".format(err))

    print("")

    builder = RecipeBuilder(
        name="Specialty IPA",
        grain_list=[g.grain for g in beer.grain_additions],
        hop_list=[h.hop for h in beer.hop_additions],
        target_ibu=27.0,
        target_og=1.50,
        brew_house_yield=brew_house_yield,
        start_volume=2.5,
        final_volume=5.0,
    )

    # TODO: Unclear why this doesn't work
    # percent_list = [0.8044, 0.0869, 0.06525, 0.04345]
    # grain_additions = builder.get_grain_additions(percent_list)
    # for grain_add in grain_additions:
    #     print(grain_add.convert_to_cereal().format())
    #     print("")


"""

Kama Citra Session IPA (Extract)
===================================

Brew House Yield:   42.5%
Start Volume:       2.5
Final Volume:       5.0

Boil Gravity:       1.108 (Evaporation @ 0.0%)
Original Gravity:   1.054
Final Gravity:      1.014

ABV / ABW Standard: 5.26% / 4.18%
ABV / ABW Alt:      5.40% / 4.29%

IBU:                20.5 ibu
BU/GU:              0.2

Morey   (SRM/EBC):  9.0 degL / 17.7
Daniels (SRM/EBC):  11.1 degL / 22.0
Mosher  (SRM/EBC):  8.8 degL / 17.4


21B Specialty IPA: White IPA
===================================

Original Gravity:   1.056 - 1.065
Final Gravity:      1.010 - 1.016
ABV:                5.50% - 7.00%
IBU:                40.0 - 70.0
Color (SRM):        5.0 - 8.0

Style issues:
- OG is below style
- ABV is below style
- IBU is below style
- Color is above style

Resources:
- https://www.northernbrewer.com/products/kama-citra-session-ipa-recipe-kit
- https://dev.bjcp.org/style/2015/21/21B/specialty-ipa/
- https://omegayeast.com/yeast/ales/west-coast-ale-ii

For adding water make sure to measure gravity after yeast starter added:

gv -o 2.5 -f 5.0 -g 1.70
1.350


TBD:

abv -o 1.061 -f 1.041 -r
4.90%
abv -o 1.061 -f 1.041 -ra
5.12%

"""


if __name__ == "__main__":
    main()
