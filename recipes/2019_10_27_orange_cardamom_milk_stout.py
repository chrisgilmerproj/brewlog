import os

from brew.constants import GRAIN_TYPE_SPECIALTY
from brew.parsers import JSONDataLoader
from brew.parsers import parse_recipe

# from brew.recipes import RecipeBuilder
from brew.styles import StyleFactory
from brew.utilities.efficiency import calculate_brew_house_yield  # noqa


def main():

    recipe = {
        u"name": u"Indian Orange Cardamom Milk Stout (Extract)",
        u"start_volume": 4.0,
        u"final_volume": 5.0,
        u"grains": [
            {u"name": u"Pale Liquid Extract", u"weight": 7.0, u"grain_type": u"lme"},
            {"name": "Milk Sugar Lactose", "weight": 1.0},
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
        u"add_in": [
            {"name": "Ground Cardamom", "weight": 0.5, "boil_time": 30.0},
            {"name": "Orange Zest", "boil_time": 15.0, "note": "6 oranges"},
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

    # builder = RecipeBuilder(
    #     name="Sweet Stout",
    #     grain_list=[g.grain for g in beer.grain_additions],
    #     hop_list=[h.hop for h in beer.hop_additions],
    #     target_ibu=27.0,
    #     target_og=1.056,
    #     brew_house_yield=0.425,
    #     start_volume=4.0,
    #     final_volume=5.0,
    # )

    # TODO: Unclear why this doesn't work
    # percent_list = [0.8044, 0.0869, 0.06525, 0.04345]
    # grain_additions = builder.get_grain_additions(percent_list)
    # for grain_add in grain_additions:
    #     print(grain_add.convert_to_cereal().format())
    #     print("")

    # BIAB Measurement at 6 qts water added, 1.037 OG
    # Removal of bag revealed only 4qts, so lost 2 qts to grain.
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    bhy = calculate_brew_house_yield(1.0, 1.037, grain_additions)
    print(
        "\nBrew House Yield: {:0.2%} (Specialty Grains BIAB, Enzymatic Rest)".format(
            bhy
        )
    )

    # Started with 3 gallons of hot water in pot, added 1 gallon of specialty grains
    # BIAB Measurement 1.008, volume reduced by 0.5 Gallons
    # This is before adding extract to volume and after grains were removed
    grain_additions = beer.get_grain_additions_by_type(GRAIN_TYPE_SPECIALTY)
    bhy = calculate_brew_house_yield(4.0, 1.008, grain_additions)
    print("\nBrew House Yield: {:0.2%} (Specialty Grains BIAB)".format(bhy))

    # After extract added
    # This is after adding extract and lactose to volume and after grains were removed
    bhy = calculate_brew_house_yield(4.0, 1.063, beer.grain_additions)
    print("\nBrew House Yield: {:0.2%} (After extract addition)".format(bhy))

    lbs_dme = beer.get_wort_correction(63, 4.0)
    print("\nAdd {:0.2f} lbs of DME to fix wort".format(lbs_dme))

    # At this point added 1.0 lbs of DME to bring up the gravity

    original_gravity = 1.072  # at approximately 4G
    print("\nOriginal Gravity: {:0.4} at 4G".format(original_gravity))

    original_gravity = 1.059  # at approximately 5G
    print("\nOriginal Gravity: {:0.4} at 5G".format(original_gravity))

    final_gravity_refractometer = 1.028
    print("\nFinal Gravity (r): {:0.4}".format(final_gravity_refractometer))
    final_gravity_hydrometer = 1.014
    print("\nFinal Gravity (h): {:0.4}".format(final_gravity_hydrometer))


"""
Resources:
- https://www.homebrewit.com/blog/2017/03/05/7-flavors-try-next-homebrew/

Added 1.0lbs of DME to the wort to fix gravity
"""


if __name__ == "__main__":
    main()
