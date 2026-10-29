"""Fruit, fresh juice and bedtime drink recipes (serves 4)."""

from .base import R

_CUT = "Wash under running water before cutting. Serve within 30 minutes of cutting so vitamin C is not lost."

RECIPES = {
    # ---------------- Fruit / juice (no added sugar) ----------------
    "Guava slices with a pinch of salt and pepper": R(
        "5 min",
        ["2-3 ripe guavas", "Pinch of salt and pepper (or chilli powder for adults)"],
        ["Wash and cut into wedges, removing the hard core if the children prefer.", "Sprinkle salt and pepper.", _CUT],
    ),
    "Papaya bowl with lime": R(
        "5 min",
        ["½ medium ripe papaya", "1 lime"],
        ["Peel, deseed and cube the papaya.", "Squeeze lime over it.", _CUT],
    ),
    "Rasthali / Nendran Banana": R(
        "2 min",
        ["4 bananas (1 per person)"],
        ["Serve whole, or slice into the lunchbox with a squeeze of lime so it does not darken."],
    ),
    "Pomegranate pearls": R(
        "10 min",
        ["2 pomegranates"],
        [
            "Cut off the crown and score the skin into 4 parts.",
            "Break apart in a bowl of water - the seeds sink and the white pith floats.",
            "Drain and serve in glasses with spoons.",
        ],
    ),
    "Fresh Watermelon Juice (no sugar)": R(
        "10 min",
        ["4 cups watermelon cubes, deseeded", "6 mint leaves, juice of ½ lime, pinch of black salt"],
        ["Blend watermelon with mint for 20 seconds - no water needed.", "Strain if you like, add lime and black salt.", "Serve chilled straight away."],
    ),
    "Fresh Sathukudi (Mosambi) Juice": R(
        "10 min",
        ["8 sathukudi (sweet lime)", "Pinch of salt (optional)"],
        ["Cut in half and squeeze on a citrus juicer.", "Serve fresh; do not add sugar - it is naturally sweet."],
    ),
    "Apple slices with peanut butter (home-ground)": R(
        "10 min",
        ["3 apples", "Peanut butter: ½ cup roasted peanuts + 1 tsp honey or jaggery + pinch salt"],
        [
            "Grind roasted peanuts in a mixer for 2-3 minutes, stopping to scrape, until creamy. Add honey and salt.",
            "Slice apples and serve with 1 tbsp peanut butter each as a dip.",
            "Store the extra peanut butter in a clean jar in the fridge for up to 2 weeks.",
        ],
    ),
    "Mango slices": R(
        "5 min",
        ["2 ripe mangoes (Banganapalli or Imam Pasand)"],
        ["Soak in water for 30 minutes before cutting.", "Cut the cheeks, score into cubes and serve.", _CUT],
    ),
    "Sapota (Chikoo) Milkshake (no sugar)": R(
        "10 min",
        ["6 ripe sapota (chikoo), peeled and deseeded", "3 cups cold milk", "4 soft dates (for sweetness)"],
        ["Blend sapota and dates with 1 cup milk until smooth.", "Add the remaining milk and blend 10 seconds.", "Serve chilled."],
    ),
    "Pineapple chunks with pepper": R(
        "10 min",
        ["½ ripe pineapple", "Pinch of pepper and salt"],
        ["Peel, remove the eyes and core, and cut into chunks.", "Sprinkle a pinch of pepper and salt."],
    ),
    "Muskmelon Juice": R(
        "10 min",
        ["1 muskmelon, peeled and deseeded", "6 mint leaves, 1 cup cold water or milk"],
        ["Blend the melon with mint and water (or milk for a shake).", "Serve chilled, no sugar."],
    ),
    "Jackfruit pieces": R(
        "10 min",
        ["16-20 ripe jackfruit pods", "Oil on your hands and knife (prevents stickiness)"],
        ["Remove the seeds from the pods.", "Serve 4-5 pods per person. Keep the seeds to boil or add to sambar."],
    ),
    "Mixed fruit bowl with lime and chaat spice": R(
        "10 min",
        ["1 banana, 1 apple, 1 cup papaya cubes, ½ cup pomegranate", "Juice of 1 lime, pinch chaat masala or black salt and roasted cumin"],
        ["Cube all fruits into a bowl.", "Toss with lime and chaat spice.", _CUT],
    ),
    "Orange segments": R(
        "5 min",
        ["4 oranges (1 per person)"],
        ["Peel and separate the segments. Keep the white pith - it has fibre."],
    ),
    "Grapes": R(
        "5 min (+1 h freezing for 'ice candy')",
        ["500 g black grapes"],
        [
            "Soak grapes in water with 1 tsp salt for 10 minutes, then rinse well.",
            "Serve as they are, or freeze on a plate for 1 hour for natural 'ice candy' bites.",
        ],
    ),
    # ---------------- Bedtime drinks ----------------
    "Manjal Paal - turmeric pepper milk with palm jaggery": R(
        "5 min",
        ["4 cups milk", "½ tsp turmeric, ¼ tsp pepper powder", "2-3 tsp palm jaggery (karupatti)"],
        ["Boil milk with turmeric and pepper for 2 minutes.", "Switch off and stir in jaggery (adding it while boiling can split the milk).", "Serve warm."],
    ),
    "Ragi Malt with Milk": R(
        "10 min",
        ["4 tbsp ragi flour", "1 cup water, 3 cups milk", "2-3 tsp palm jaggery, pinch cardamom"],
        [
            "Mix ragi flour in the cold water with no lumps.",
            "Cook on low flame, stirring, for 5 minutes until thick and glossy.",
            "Add milk and bring to a boil. Switch off, add jaggery and cardamom.",
        ],
    ),
    "Home-made Badam Milk": R(
        "Soak almonds 6 h; 10 min",
        ["20 almonds, soaked and peeled", "4 cups milk", "Pinch saffron, ¼ tsp cardamom, 2-3 tsp palm jaggery or 4 dates"],
        [
            "Grind the almonds with ½ cup milk to a smooth paste.",
            "Boil the rest of the milk with saffron, add the almond paste and simmer 5 minutes, stirring.",
            "Add cardamom; sweeten with jaggery after switching off.",
        ],
    ),
    "Dates Milk": R(
        "10 min",
        ["8 soft dates, deseeded", "4 cups milk"],
        ["Soak dates in ½ cup warm milk for 10 minutes.", "Blend smooth, add the rest of the warm milk and mix. No extra sugar."],
    ),
    "Warm Milk with Nutmeg and Cardamom": R(
        "5 min",
        ["4 cups milk", "Tiny pinch of nutmeg, ¼ tsp cardamom, 2 tsp jaggery (optional)"],
        ["Boil milk with cardamom.", "Add a tiny pinch of grated nutmeg - more makes it bitter.", "Serve warm before bed."],
    ),
}
