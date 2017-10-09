"""
5/29/2017 Yellow Moon IPA
{
    "Beer Creator": "The Brew Shop",
    "Beer Recipe": "Yellow Moon IPA",
    "Beer Type": "IPA",
    "Letter": "Y",
    "Our Beer Name": "",
    "Original Volume (Gallons)": "4",
    "Final Volume (Gallons)": "5",
    "Brew": "5/29/2017",
    "Bottle/Keg": "6/7/2017",
    "Open": "NA",
    "Boil": "1.093 Refractometer",
    "Original Gravity": "1.041 Refractometer",
    "OG": "1041",
    "Final Gravity": "1022, 1.032 refractometer",
    "FG": "1022",
    "ABV": "2.47%",
    "Notes": "Did a calculation after the specialty grains extract and figured out I was below target.  I miscalculated though and added only 1.5 lbs dme when I probably should have added 2.5 lbs.  This was a problem because I topped up my brew to 5 gallons at the end without doing a final measurement before fermenting.",
    "Links": ""
}
{
    "Beer Creator": "The Brew Shop",
    "Beer Recipe": "Yellow Moon IPA",
    "Beer Type": "IPA",
    "Liquid Malt Extract": "7lbs Light Malt Extract",
    "Dry Malt Extract": "",
    "Steeping Grains": "1 lbs Crystal 20L\n1/2 lbs Munich\n1/2 lbs Caraipls",
    "BIAB Grains": "",
    "Add-in": "",
    "Hops": "2oz Centennial Hops (0 and 30)\n2oz Cascade Hops (50 and 60)",
    "Yeast": "Wyeast 1056 American Yeast",
    "Wirlfloc": "Irish Moss",
    "Priming Sugar": "NONE!",
    "Container": "Kegs"
}
"""

{
    "name": "Yellow Moon IPA",
    "start_volume": "4",
    "final_volume": "5",
    "grains": [
        {
            "name": "7lbs Light Malt Extract",
            "weight": 1.0,
            "grain_type": "lme"
        },
        {
            "name": "1 lbs Crystal 20L",
            "weight": 1.0,
            "grain_type": "specialty"
        },
        {
            "name": "1/2 lbs Munich",
            "weight": 1.0,
            "grain_type": "specialty"
        },
        {
            "name": "1/2 lbs Caraipls",
            "weight": 1.0,
            "grain_type": "specialty"
        }
    ],
    "hops": [
        {
            "name": "2oz Centennial Hops (0 and 30)",
            "weight": 1.0,
            "hop_type": "pellet"
        },
        {
            "name": "2oz Cascade Hops (50 and 60)",
            "weight": 1.0,
            "hop_type": "pellet"
        }
    ],
    "yeast": [
        {
            "name": "Wyeast 1056 American Yeast"
        }
    ],
    "data": {
        "brew_house_yield": 0.7,
        "units": "imperial"
    }
}