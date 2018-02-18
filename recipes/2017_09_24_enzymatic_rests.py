#!/usr/bin/env python
# -*- coding: utf-8 -*-


from brew.utilities.temperature import mash_infusion
from brew.utilities.temperature import strike_temp


def main():

    print("Enzymatic rests schedule")

    liquor_to_grist_ratio = 1.5  # qt:lbs
    grain_weight = 2.0  # lbs
    water_volume = grain_weight * liquor_to_grist_ratio  # qt

    print("")
    print("Starting with {} lbs of grain".format(grain_weight))

    target_temp = 110
    initial_temp = 70  # grain temperature without water
    sk_temp = strike_temp(target_temp, initial_temp,
                          liquor_to_grist_ratio=liquor_to_grist_ratio)

    print("")
    print("Bring {} qts of water to {} degF before adding grains".format(
        water_volume, round(sk_temp, 1)))  # noqa
    print("Your temperature should then reach {} degF".format(target_temp))
    print("Keep your temperature here for 20 minutes")

    # Settled at 112 degF.  My guess is that I didn't stir the
    # water as it was heating and the thermometer read the sk_temp
    # when it was actuall hotter. It's also possible the heat from
    # the mash tun (my pot) transfers in over time.
    initial_temp = 113
    target_temp = 140
    infusion_temp = 205  # boils at 3K ft

    infusion_volume = mash_infusion(target_temp, initial_temp,
                                    grain_weight, water_volume,
                                    infusion_temp=infusion_temp)

    print("")
    print("Add {} qts of {} degF water".format(round(infusion_volume, 2), infusion_temp))  # noqa
    print("Your temperature should then reach {} degF".format(target_temp))
    print("Keep your temperature here for 40 minutes")

    # Settles at 125deg F, which was an issue since I was using 212 instead of
    # 205 for the temp.  I had to add heat slowly to get it fixed to 140.

    initial_temp = target_temp
    target_temp = 158
    infusion_temp = 205  # boils at 3K ft
    # water volume is usually the addition of the infusion volume
    # It recommended 1.3qt, which I rounded up to 5.25 cups
    water_volume += 5.25 / 4.0  # += infusion_volume

    infusion_volume = mash_infusion(target_temp, initial_temp,
                                    grain_weight, water_volume,
                                    infusion_temp=infusion_temp)

    print("")
    print("Add {} qts of {} degF water".format(round(infusion_volume, 2), infusion_temp))  # noqa
    print("Your temperature should then reach {} degF".format(target_temp))
    print("Keep your temperature here for 20 minutes")
    print("")

    water_volume += infusion_volume
    print("You should now have {} qts of water".format(round(water_volume, 2)))
    print("Now remove the grains and continue with brewing")


if __name__ == "__main__":
    main()
