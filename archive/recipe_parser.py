#! /usr/bin/env python3

import csv
import datetime
import json
import os


def main():
    logs = []
    with open('2017_09_22_beer_log.csv', 'r') as f:
        reader = csv.DictReader(f)
        logs = list(reader)

    recipes = []
    with open('2017_09_22_beer_recipe.csv', 'r') as f:
        reader = csv.DictReader(f)
        recipes = list(reader)

    for index, recipe in enumerate(recipes):
        log = logs[index]
        date = log['Brew']
        try:
            timestamp = datetime.datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            try:
                timestamp = datetime.datetime.strptime(date, '%Y')
            except ValueError:
                timestamp = datetime.datetime(2012, 1, 1)

        final_volume = log['Final Volume (Gallons)']
        original_volume = log['Original Volume (Gallons)']
        if not original_volume:
            original_volume = final_volume

        name = recipe['Beer Recipe']
        lme = recipe['Liquid Malt Extract'].strip().split('\n')
        dme = recipe['Dry Malt Extract'].strip().split('\n')
        steeping_grains = recipe['Steeping Grains'].strip().split('\n')
        biab_grains = recipe['BIAB Grains'].strip().split('\n')
        # add_in = recipe['Add-in'].strip().split('\n')
        hops = recipe['Hops'].strip().split('\n')
        yeasts = recipe['Yeast'].strip().split('\n')
        # wirfloc = recipe['Wirlfloc'].strip()

        # Format grains
        new_grains = []
        for grain in lme:
            if not grain:
                continue
            new_grains.append({'name': grain,
                               'weight': 1.0,
                               'grain_type': 'lme'})
        for grain in dme:
            if not grain:
                continue
            new_grains.append({'name': grain,
                               'weight': 1.0,
                               'grain_type': 'dme'})
        for grain in steeping_grains:
            if not grain:
                continue
            new_grains.append({'name': grain,
                               'weight': 1.0,
                               'grain_type': 'specialty'})
        for grain in biab_grains:
            if not grain:
                continue
            new_grains.append({'name': grain,
                               'weight': 1.0,
                               'grain_type': 'specialty'})

        # Format hops
        new_hops = []
        for hop in hops:
            if not hop:
                continue
            new_hops.append({'name': hop,
                             'weight': 1.0,
                             'hop_type': 'pellet'})

        # Format yeast
        new_yeast = []
        for yeast in yeasts:
            if not yeast:
                continue
            new_yeast.append({'name': yeast})

        # Format new recipe
        new_recipe = {
            'name': name,
            'start_volume': original_volume,
            'final_volume': final_volume,
            'grains': new_grains,
            'hops': new_hops,
            'yeast': new_yeast,
            'data': {
                'brew_house_yield': 0.70,
                'units': 'imperial',
            },
        }
        data = json.dumps(new_recipe, indent=4)

        filename = '{}_{}.py'.format(timestamp.strftime('%Y_%m_%d'),
                                     name.replace(' ', '_'))
        with open(os.path.join('recipes', filename), 'w') as f:
            f.write("\"\"\"\n")
            f.write("{} {}".format(date, name))
            f.write("\n")
            f.write(json.dumps(log, indent=4))
            f.write("\n")
            f.write(json.dumps(recipe, indent=4))
            f.write("\n")
            f.write("\"\"\"\n\n")
            f.write(data)


if __name__ == "__main__":
    main()
