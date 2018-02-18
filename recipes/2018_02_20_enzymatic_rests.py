#!/usr/bin/env python
# -*- coding: utf-8 -*-


from brew.utilities.temperature import mash_infusion
from brew.utilities.temperature import strike_temp


def main():

    print("Enzymatic rests schedule")
    print("")
    print("This is a 20/40/20 min schedule for temps 110/140/158 F respectively")

    liquor_to_grist_ratio = 1.5  # qt:lbs
    grain_weight = 12.2 + 0.38  # lbs
    water_volume = grain_weight * liquor_to_grist_ratio  # qt

    print("")
    print("Starting with {:0.2f} lbs of grain".format(grain_weight))

    target_temp = 110
    initial_temp = 70  # grain temperature without water
    sk_temp = strike_temp(target_temp, initial_temp,
                          liquor_to_grist_ratio=liquor_to_grist_ratio)

    print("")
    print("Bring {:0.2f} qts of water to {} degF before adding grains".format(
        water_volume, round(sk_temp, 1)))  # noqa
    print("Your temperature should then reach {} degF".format(target_temp))
    print("Keep your temperature here for 20 minutes")

    initial_temp = 110  # should be previous target_temp, modify from real data
    target_temp = 140
    infusion_temp = 205  # boils at 3K ft

    infusion_volume = mash_infusion(target_temp, initial_temp,
                                    grain_weight, water_volume,
                                    infusion_temp=infusion_temp)

    print("")
    print("Add {:0.2f} qts of {} degF water".format(round(infusion_volume, 2), infusion_temp))  # noqa
    print("Your temperature should then reach {} degF".format(target_temp))
    print("Keep your temperature here for 40 minutes")

    initial_temp = 140  # Should be previous target_temp, modify from real data
    target_temp = 158
    infusion_temp = 205  # boils at 3K ft
    water_volume += infusion_volume

    infusion_volume = mash_infusion(target_temp, initial_temp,
                                    grain_weight, water_volume,
                                    infusion_temp=infusion_temp)

    print("")
    print("Add {:0.2f} qts of {} degF water".format(round(infusion_volume, 2), infusion_temp))  # noqa
    print("Your temperature should then reach {} degF".format(target_temp))
    print("Keep your temperature here for 20 minutes")
    print("")

    water_volume += infusion_volume
    print("You should now have {:0.2f} qts of water in the mash".format(round(water_volume, 2)))
    print("Now remove the grains and continue with brewing")

    # Rule of thumb is 1/2 quart per lbs grain (or as high as 0.8 quarts)
    # https://www.brewersfriend.com/2010/06/12/water-volume-management-in-all-grain-brewing/
    water_loss = 0.5 * grain_weight
    final_water_volume = water_volume - water_loss
    print("")
    print("Water lost to grain will be approximately {:0.2f} quarts".format(water_loss))
    print("Leaving you {:0.2f} quarts in your brew or {:0.2f} gallons".format(final_water_volume,
                                                                              final_water_volume / 4.0))


if __name__ == "__main__":
    main()
