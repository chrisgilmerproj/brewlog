#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Deschutes Brewing Sagefight Imperial IPA
India Pale Ale brewed with Sage and Juniper Berries

Citrusy hops go head to head with resinous sage and juniper in a flavor battle royale.

A main hoppy event: In the right corner we have lively botanicals hailing from the high desert; in the left,
heavyweight citrus hops are looking for a knockout. Get ready to take a punch and keep on swinging with this bold
Imperial IPA brewed with sage and juniper berries that is best shared with those in your corner.

- https://www.deschutesbrewery.com/sagefight-ipa/
- https://www.deschutesbrewery.com/beer/sagefight/#homebrew

Recipe Type:       All Grain
Batch Size:        5 gallons
Original Gravity:  1.075
Final Gravity:     1.013 – 1.019
Boil Time:         90 minutes
Fermentation Temp: 65° F
Yeast Type:        English Ale
IBUs:              75
Expected ABV:      8%

Malt
- Pale
- Crystal
- Munich

Hops:
- Millennium
- Bravo
- Amarillo
- Centennial

Additions:
- Sage
- Juniper Berries

Yeast:
- Wyeast 1098 British Ale (0.73-0.75 attenuation)
- WLP002 English Ale (0.67-0.70 attenuation)

Description:

Back in 2012, we participated in a program called Beers Made By Walking. The basic idea of the program was to invite brewers to make beer inspired by nature hikes and urban walks. Here in the high desert of Central Oregon, we have a diverse landscape, but mainly, we have a LOT of sage and juniper. Actually, Oregon has ~6.5 million acres of juniper forest (one of the largest in the WORLD), so, it was a no-brainer to experiment with a combination of sage and juniper in a batch of beer to discover if these ingredients would work symbiotically with hops and malted barley.

The result was incredibly delicious, and won us two medals at the Great American Beer Festival (Silver in 2013 and Bronze in 2014). We have offered this beer on tap several times at our pubs in an experimental manner, but after hearing over and over how much you all love this beer, we decided to bottle it for the first time last year!

Now it’s back for a second year and available late November for a limited time. Grab yourself a 6-pack or pint directly from the tap. At 8% ABV and 75 IBUs Sagefight Imperial IPA packs a punch not only in flavor, but in aroma as well. Citrusy hops go head to head with resinous sage and juniper in a battle royale on your taste buds. It will be one of the most unique beers you’ve ever tried.

CHEERS, and as always, we love to hear what you think of this beer…feel free to comment below.

""" # noqa

from brew.grains import Grain
from brew.hops import Hop
from brew.recipes import Recipe
from brew.recipes import RecipeBuilder
from brew.yeasts import Yeast


def main():

    # Constants
    name = u"Sagefight Imperial IPA"
    brew_house_yield = 0.70
    start_volume = 4.0
    final_volume = 5.0

    # Grains
    pale = Grain(u"pale 2-row", color=2.0, ppg=36.0)
    crystal = Grain(u"crystal 20", color=2.0, ppg=35.0)
    munich = Grain(u"munich", color=9.0, ppg=37.0)
    grain_list = [pale, crystal, munich]

    # Hops
    millennium = Hop(name=u"millennium", percent_alpha_acids=0.14)  # Mild, herbaceous, elements of resin
    bravo = Hop(name=u"bravo", percent_alpha_acids=0.15)  # Spicy, earthy, and lightly floral
    amarillo = Hop(name=u"amarillo", percent_alpha_acids=0.09)  # Orange Citrus Flavor
    centennial = Hop(name=u"centennial", percent_alpha_acids=0.10)  # Floral, with elements of citrus and notes of grapefruit  # noqa
    hop_list = [millennium, bravo, amarillo, centennial]

    # Define Recipe Builder
    builder = RecipeBuilder(
        name=name,
        grain_list=grain_list,
        hop_list=hop_list,
        target_ibu=75.0,
        target_og=1.075,
        brew_house_yield=brew_house_yield,
        start_volume=start_volume,
        final_volume=final_volume,
    )

    # Get grain additions
    grain_percentages = [0.80, 0.10, 0.10]
    grain_additions = builder.get_grain_additions(grain_percentages)

    # Get hop additions
    hop_percentages = [0.25, 0.25, 0.25, 0.25]
    hop_boil_times = [90, 60, 30, 15]
    hop_additions = builder.get_hop_additions(hop_percentages, hop_boil_times)

    # Determine desired attenuation
    desired_attenuation = builder.get_yeast_attenuation(0.08)
    yeast = Yeast("English Ale", percent_attenuation=desired_attenuation)

    # Create the recipe
    recipe = Recipe(
        name=name,
        grain_additions=grain_additions,
        hop_additions=hop_additions,
        yeast=yeast,
        brew_house_yield=brew_house_yield,
        start_volume=start_volume,
        final_volume=final_volume,
    )
    print(recipe.format())

    print("\nAdjuncts")
    print("===================================")
    print("- 0.66 oz Juniper Berries (crushed), 1/3 to boil at 10 min, 2/3 at knockout")
    print("- 0.25 oz Sage, 2/3 to boil at 10 min, 1/3 at knockout")


if __name__ == "__main__":
    main()
