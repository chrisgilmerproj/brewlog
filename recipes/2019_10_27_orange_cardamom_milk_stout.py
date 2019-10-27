"""
10/5/2013 Triple-X
{
    "Beer Creator": "Brewing Classic Styles",
    "Beer Recipe": "Triple-X",
    "Beer Type": "Sweet Stout",
    "Letter": "X",
    "Our Beer Name": "Orange Coriander Stout",
    "Original Volume (Gallons)": "",
    "Final Volume (Gallons)": "5",
    "Brew": "10/5/2013",
    "Bottle/Keg": "10/15/2013",
    "Open": "11/16/2013",
    "Boil": "",
    "Original Gravity": "6% potential ABV,\n12.5balling,\n1046.0\nat 75F",
    "OG": "1046",
    "Final Gravity": "3%, 6, 1022 at 70F",
    "FG": "1022",
    "ABV": "3.12%",
    "Notes": "Add in zest of 6 oranges and 5-10 cardamom pods -- 11/16/13 yummm",
    "Links": "http://sciencebrewer.com/2010/12/28/strange-brew-orange-cardamom-chocolate-porter/"
}
{
    "Beer Creator": "Brewing Classic Styles",
    "Beer Recipe": "Triple-X",
    "Beer Type": "Sweet Stout",
    "Liquid Malt Extract": "7.2lbs English Pale Ale LME",
    "Dry Malt Extract": "",
    "Steeping Grains": "1.0 lbs Patent Malt (525L)\n0.75 lbs Crystal (80L)\n0.5 lbs Pale Chocolage Malt (200L)",
    "BIAB Grains": "",
    "Add-in": "1lb Lactose Powder (Milk Sugar) (0L)\nzest of 6 oranges\n5-10 cardamom pods",
    "Hops": "1.5 oz E. Kent Goldings 5%AA 60 min.",
    "Yeast": "Wyeast 1099 Whitbread Ale",
    "Wirlfloc": "Irish Moss",
    "Priming Sugar": "",
    "Container": ""
}
"""

import os

from brew.constants import GRAIN_TYPE_SPECIALTY
from brew.parsers import JSONDataLoader
from brew.parsers import parse_recipe
from brew.recipes import RecipeBuilder
from brew.styles import StyleFactory
from brew.utilities.efficiency import calculate_brew_house_yield  # noqa


def main():

    recipe = {
        u"name": u"Yellow Moon IPA (Extract)",
        u"start_volume": 5.0,
        u"final_volume": 5.0,
        u"grains": [
            {u"name": u"Pale Liquid Extract", u"weight": 7.0, u"grain_type": u"lme"},
            {
                "name": "Black Patent Malt",
                "weight": 1.0,
                "grain_type": "specialty",
                "color": 525,
            },
            {
                "name": "Caramel Crystal Malt 80l",
                "weight": 0.75,
                "grain_type": "specialty",
                "color": 80,
            },
            {
                "name": "Chocolate Malt",
                "weight": 0.5,
                "grain_type": "specialty",
                "color": 200,  # 180 - 250
            },
        ],
        u"hops": [
            {
                "name": "East Kent Golding",
                "weight": 1.5,
                "hop_type": "pellet",
                u"boil_time": 60.0,
                "percent_alpha_acids": 0.047,
            }
        ],
        u"yeast": {u"name": u"Wyeast 1099"},
        u"data": {u"brew_house_yield": 0.425, u"units": u"imperial"},
    }

    data_dir = os.path.abspath(os.path.join(os.getcwd(), "data/"))
    loader = JSONDataLoader(data_dir)
    beer = parse_recipe(recipe, loader)
    print(beer.format(short=True))

    factory = StyleFactory(os.path.join(data_dir, "bjcp", "styles.json"))
    style = factory.create_style("16", "A")
    print("")
    print(style.format())

    print("Style issues:")
    errors = style.recipe_errors(beer)
    for err in errors:
        print("- {}".format(err))

    print("")

    builder = RecipeBuilder(
        name="Sweet Stout",
        grain_list=[g.grain for g in beer.grain_additions],
        hop_list=[h.hop for h in beer.hop_additions],
        target_ibu=27.0,
        target_og=1.056,
        brew_house_yield=0.425,
        start_volume=4.0,
        final_volume=5.0,
    )

    # TODO: Unclear why this doesn't work
    percent_list = [0.8044, 0.0869, 0.06525, 0.04345]
    grain_additions = builder.get_grain_additions(percent_list)
    for grain_add in grain_additions:
        print(grain_add.convert_to_cereal().format())
        print("")

    # BIAB Measurement 1.0085, volume reduced by 0.5 Gallons
    # This is before adding extract to volume but after grains were removed
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    bhy = calculate_brew_house_yield(4.8, 1.005, grain_additions)
    print("\nBrew House Yield: {:0.2%} (Specialty Grains BIAB)".format(bhy))

    # After extract added
    # This is before adding extract to volume but after grains were removed
    bhy = calculate_brew_house_yield(4.8, 1.054, beer.grain_additions)
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
"""


if __name__ == "__main__":
    main()
