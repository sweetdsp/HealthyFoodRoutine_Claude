"""Children's soup and after-school snack recipes (serves 4)."""

from . import common as C
from .base import R

RECIPES = {
    # ---------------- Soups ----------------
    "Murungai Keerai Soup": R(
        "25 min",
        [
            "2 cups drumstick leaves (murungai keerai), washed",
            "2 tbsp moong dal cooked soft, with its water",
            "4 shallots, 4 garlic crushed, 1 tomato, ½ tsp pepper, ½ tsp cumin, salt",
            "1 tsp ghee, 4 cups water",
        ],
        [
            "Heat ghee, add cumin, shallots and garlic; sauté 2 minutes.",
            "Add tomato and the leaves; sauté 2 minutes.",
            "Add water and the cooked dal; simmer 10 minutes.",
            "Strain (or leave the leaves in for more fibre). Add pepper and salt.",
        ],
    ),
    "Fresh Tomato Soup with Croutons of Roasted Chapati": R(
        "30 min",
        [
            "6 ripe tomatoes, 1 carrot, 1 small onion, 4 garlic",
            "1 tsp butter, ½ tsp pepper, ½ tsp palm jaggery or sugar, salt, 3 cups water",
            "Croutons: 2 chapatis cut into small squares, ½ tsp ghee",
        ],
        [
            "Pressure-cook tomatoes, carrot, onion and garlic with 1 cup water, 2 whistles.",
            "Cool, blend smooth, and strain to remove the seeds and skin.",
            "Heat butter, pour in the puree with 2 cups water, salt, pepper and jaggery. Simmer 5 minutes.",
            "Croutons: toast the chapati squares in ghee on a tawa until crisp.",
            "Top each bowl with croutons just before serving.",
        ],
        tip="Carrot gives body and sweetness, so no cornflour or cream is needed.",
    ),
    "Sweet Corn Vegetable Soup": R(
        "30 min",
        [
            "2 fresh sweet corn cobs (about 1½ cups kernels)",
            "½ cup finely chopped carrot and beans, 2 tbsp spring onion",
            "3 garlic chopped, 1 tsp ginger, ½ tsp pepper, salt, 1 tsp butter, 4 cups water",
        ],
        [
            "Blend half the corn kernels with ½ cup water to a coarse paste.",
            "Heat butter, sauté garlic and ginger, then carrot and beans for 2 minutes.",
            "Add the whole kernels, the corn paste and water. Simmer 12 minutes - the corn paste thickens the soup naturally.",
            "Season with salt and pepper and top with spring onion.",
        ],
    ),
    "Kozhi Rasam (Chicken Clear Soup)": R(
        "40 min",
        [
            "300 g chicken bones and a few small pieces",
            "1 tsp pepper, 1 tsp cumin, 1 tsp coriander seeds - crushed; 6 garlic; 1-inch ginger crushed",
            "6 shallots, 1 tomato, ¼ tsp turmeric, curry leaves, coriander, salt",
            "1 tsp gingelly oil, 5 cups water",
        ],
        [
            "Heat oil, add curry leaves, shallots, ginger and garlic; sauté.",
            "Add the crushed spices, tomato and turmeric; sauté 1 minute.",
            "Add the chicken, salt and water. Pressure-cook 4 whistles (or simmer 30 minutes).",
            "Strain and add coriander. Serve hot in cups.",
        ],
        tip="Reduce pepper to ½ tsp for the children; it is a natural cold remedy.",
    ),
    "Mushroom Pepper Soup": R(
        "25 min",
        [
            "200 g fresh button mushrooms, chopped",
            "1 onion, 3 garlic, 1 tsp butter, ½ cup milk, 3 cups water",
            "½ tsp pepper, salt, coriander",
        ],
        [
            "Heat butter, sauté onion and garlic until soft.",
            "Add mushrooms and cook 5 minutes until they release water.",
            "Add water and simmer 8 minutes. Blend half for a creamy texture and stir it back.",
            "Add milk, pepper and salt; heat through without boiling.",
        ],
    ),
    "Carrot-Ginger Soup": R(
        "25 min",
        ["5 carrots chopped, 1 onion, 1-inch ginger, 2 garlic", "1 tsp butter or ghee, ½ tsp pepper, salt, 4 cups water", "Squeeze of lemon"],
        [
            "Sauté onion, ginger and garlic in butter.",
            "Add carrots and water; pressure-cook 2 whistles.",
            "Blend smooth. Reheat with salt and pepper, add lemon.",
        ],
    ),
    "Pumpkin Coconut Soup": R(
        "25 min",
        ["3 cups yellow pumpkin cubes, 1 onion, 3 garlic", "¾ cup coconut milk, 2½ cups water", "½ tsp pepper, pinch cumin powder, salt, 1 tsp ghee"],
        [
            "Sauté onion and garlic in ghee.",
            "Add pumpkin and water; cook until soft, about 10 minutes (or 2 whistles).",
            "Blend smooth. Stir in coconut milk, salt, pepper and cumin; heat gently.",
        ],
    ),
    "Mixed Vegetable Clear Soup": R(
        "25 min",
        [
            "1½ cups finely chopped carrot, beans and cabbage",
            "3 garlic, 1 tsp ginger, 2 tbsp spring onion",
            "1 tsp oil, ½ tsp pepper, salt, 4 cups water, squeeze of lemon",
        ],
        [
            "Heat oil, sauté garlic and ginger.",
            "Add vegetables and sauté 2 minutes on high.",
            "Add water and simmer 10 minutes. Add salt, pepper, lemon and spring onion.",
        ],
    ),
    "Moong Dal Soup": R(
        "25 min",
        ["½ cup moong dal, 1 tomato, ¼ tsp turmeric, 4 cups water", "1 tsp ghee, ½ tsp cumin, 2 garlic, salt, lemon, coriander"],
        [
            "Pressure-cook moong dal with tomato, turmeric and 2 cups water, 3 whistles.",
            "Whisk smooth and add 2 cups water; simmer 5 minutes with salt.",
            "Temper cumin and garlic in ghee, pour over. Add lemon and coriander.",
        ],
    ),
    "Palak Soup": R(
        "25 min",
        ["1 bunch spinach (palak), washed", "1 onion, 3 garlic, 1 tsp butter", "½ cup milk, 2½ cups water, ½ tsp pepper, salt, pinch nutmeg"],
        [
            "Blanch spinach in boiling water 2 minutes, then into cold water to keep it green.",
            "Sauté onion and garlic in butter until soft. Blend with the spinach and a little water.",
            "Heat the puree with water, salt, pepper and nutmeg. Add milk and warm through without boiling.",
        ],
    ),
    "Nandu Rasam (Crab Soup)": R(
        "45 min",
        [
            "4 medium crabs, cleaned and cut in half",
            "Crushed: 1 tsp pepper, 1 tsp cumin, 1 tsp coriander seeds, 6 garlic, 1-inch ginger",
            "6 shallots, 2 tomatoes, small piece tamarind, ¼ tsp turmeric, curry leaves, coriander, salt",
            "1 tsp gingelly oil, 5 cups water",
        ],
        [
            "Heat oil, add curry leaves and shallots, then the crushed spices; sauté 1 minute.",
            "Add tomatoes and turmeric; cook soft.",
            "Add crabs, tamarind water, salt and water. Simmer 25 minutes.",
            "Strain the rasam; serve the crab pieces separately for the adults. Add coriander.",
        ],
        tip="Lightly crack the claws before cooking so the flavour goes into the rasam.",
    ),
    "Beetroot-Tomato 'Pink' Soup": R(
        "25 min",
        ["1 beetroot, 3 tomatoes, 1 carrot, 1 onion, 3 garlic", "1 tsp butter, ½ tsp pepper, salt, lemon, 4 cups water"],
        [
            "Pressure-cook all vegetables with 2 cups water, 3 whistles.",
            "Blend smooth and strain.",
            "Heat with butter, the remaining water, salt and pepper. Add lemon.",
        ],
    ),
    # ---------------- Snacks ----------------
    "Channa Sundal with Coconut and Mango": R(
        "Soak overnight; 20 min",
        [
            "1 cup chickpeas (white or black), soaked overnight",
            "3 tbsp grated coconut, 2 tbsp grated raw mango (or lemon juice)",
            "1 tsp oil, ½ tsp mustard, 1 tsp urad dal, 1 dry red chilli, pinch asafoetida, curry leaves, salt",
        ],
        [
            "Pressure-cook chickpeas with salt, 4-5 whistles until soft but whole. Drain.",
            "Temper mustard, urad dal, chilli, asafoetida and curry leaves.",
            "Add chickpeas and toss 2 minutes. Switch off and mix in coconut and raw mango.",
        ],
    ),
    "Home-made Ragi Murukku": R(
        "45 min (makes about 25)",
        [
            "1 cup ragi flour, ½ cup rice flour, 2 tbsp roasted gram flour",
            "1 tsp sesame seeds, ½ tsp cumin, pinch asafoetida, ½ tsp chilli powder, salt",
            "1 tbsp butter (soft), water to knead",
            "Oil for frying (fry once; do not reuse the oil many times)",
        ],
        [
            "Mix the flours, spices, salt and butter. Add water slowly to make a smooth, soft dough that does not crack.",
            "Fill the murukku press with the star plate.",
            "Press spirals onto the back of a ladle or a greased sheet.",
            "Fry in medium-hot oil until the bubbles stop, about 3 minutes. Drain on paper.",
            "Cool fully and store in an airtight jar - stays crisp for 2 weeks.",
        ],
    ),
    "Baked Sweet Potato Masala Wedges": R(
        "40 min",
        [
            "3 medium sweet potatoes, scrubbed and cut into wedges (skin on)",
            "1 tbsp oil, ½ tsp kashmiri chilli, ½ tsp pepper, ½ tsp cumin powder, ¼ tsp amchur, salt",
            C.TOMATO_CHUTNEY_ING,
        ],
        [
            "Soak wedges in water 10 minutes, drain and pat completely dry.",
            "Toss with oil and spices.",
            "Spread in one layer and bake at 220°C for 25 minutes (or air-fry at 200°C for 15 minutes), turning halfway.",
            C.TOMATO_CHUTNEY_STEP,
            "Serve hot with tomato chutney as the dip - it beats any bottled dip.",
        ],
    ),
    "Air-fried Chicken Popcorn with Mint-Curd Dip": R(
        "Marinate 1 h; 30 min",
        [
            "400 g boneless chicken in small cubes",
            "Marinade: ¼ cup curd, 1 tsp ginger-garlic paste, ½ tsp pepper, ½ tsp kashmiri chilli, salt",
            "Coating: ¼ cup besan + 2 tbsp rice flour + ½ tsp pepper + salt",
            C.MINT_CURD_DIP_ING,
            "1 tbsp oil to brush",
        ],
        [
            "Marinate the chicken for 1 hour.",
            C.MINT_CURD_DIP_STEP,
            "Toss each piece in the coating mix.",
            "Air-fry at 200°C for 12-14 minutes, brushing with oil and shaking halfway. (Or bake at 220°C for 18 minutes.)",
            "Serve hot with mint-curd dip.",
        ],
    ),
    "Sweet Kozhukattai with Jaggery and Coconut": R(
        "45 min (makes about 15)",
        [
            "Outer: 1 cup rice flour, 1¼ cups water, pinch salt, 1 tsp ghee",
            "Filling: 1 cup grated coconut, ½ cup grated palm jaggery, ¼ tsp cardamom powder",
        ],
        [
            "Filling: melt jaggery with 2 tbsp water, strain, add coconut and cook until thick and sticky. Add cardamom and cool.",
            "Boil water with salt and ghee. Add rice flour, stir, switch off and cover 5 minutes. Knead while warm into a smooth dough.",
            "Flatten a small ball into a cup, fill with 1 tsp filling, and seal into a dumpling.",
            "Steam 10-12 minutes until shiny.",
        ],
    ),
    "Roasted Makhana with Ghee and Pepper": R(
        "10 min",
        ["3 cups makhana (fox nuts)", "1 tsp ghee, ½ tsp pepper, ¼ tsp turmeric, salt"],
        [
            "Roast makhana in a dry pan on low flame for 6-8 minutes, stirring, until one crushes with a crunch.",
            "Add ghee, turmeric, pepper and salt; toss 1 minute.",
            "Cool and store in an airtight jar.",
        ],
    ),
    "Peanut-Jaggery Chikki (home-made)": R(
        "30 min",
        ["1 cup peanuts, roasted and skinned", "¾ cup grated palm jaggery or jaggery", "1 tsp ghee, pinch cardamom"],
        [
            "Grease a plate and a rolling pin with ghee.",
            "Melt jaggery with 1 tbsp water on low flame and boil until a drop in cold water turns hard and snaps (hard-ball stage, about 5-6 minutes).",
            "Add peanuts and cardamom, mix fast and pour onto the plate.",
            "Roll flat quickly, cut into pieces while warm, and break when cool.",
        ],
    ),
    "Ellu Urundai (Sesame Balls)": R(
        "25 min (makes about 15)",
        ["1 cup black or white sesame seeds", "¾ cup grated jaggery", "¼ tsp cardamom powder"],
        [
            "Dry-roast sesame on low flame until it splutters and smells nutty. Cool.",
            "Pulse sesame and jaggery together in a mixer 3-4 times (do not make a paste).",
            "Add cardamom and roll into small balls while the mix is warm.",
        ],
    ),
    "Masala Sweet Corn Cup": R(
        "15 min",
        ["2 fresh sweet corn cobs", "1 tsp butter, ½ lemon, ¼ tsp chilli powder, ¼ tsp pepper, salt", "Coriander (optional)"],
        [
            "Remove the kernels and boil or steam them 5 minutes.",
            "Toss hot corn with butter, salt, chilli powder, pepper and lemon.",
            "Serve in cups with a spoon, like the mall corn cup.",
        ],
    ),
    "Ragi Laddu with Dates and Nuts": R(
        "25 min (makes about 12)",
        ["1 cup ragi flour", "10 soft dates, deseeded and chopped", "¼ cup almonds and cashews, chopped", "3 tbsp ghee, pinch cardamom"],
        [
            "Roast ragi flour in 1 tbsp ghee on low flame for 8 minutes until it smells nutty.",
            "Roast the nuts in the remaining ghee.",
            "Pulse dates into a paste, mix with ragi, nuts and cardamom while warm.",
            "Shape into laddus. Add a spoon of warm ghee if the mix does not hold.",
        ],
    ),
    "Masala Vadai (shallow-fried, once a week)": R(
        "Soak 3 h; 30 min (makes about 15)",
        [
            "1 cup chana dal, soaked 3 hours",
            "1 onion finely chopped, 1 green chilli, 1-inch ginger, 1 tsp fennel, curry leaves, coriander, salt",
            "Oil for shallow frying",
        ],
        [
            "Drain the dal well. Keep 2 tbsp aside; grind the rest coarsely without water.",
            "Mix in the whole dal, onion, chilli, ginger, fennel, leaves and salt.",
            "Shape into flat vadais.",
            "Shallow-fry on a tawa or paniyaram pan with 1 tsp oil each, on medium, until crisp on both sides.",
        ],
    ),
    "Karamani Sundal with Carrot": R(
        "Soak overnight; 20 min",
        [
            "1 cup karamani (black-eyed peas), soaked overnight",
            "1 carrot grated, 3 tbsp grated coconut",
            "1 tsp oil, mustard, urad dal, 1 dry red chilli, asafoetida, curry leaves, salt",
        ],
        [
            "Pressure-cook karamani with salt, 2 whistles - keep them whole. Drain.",
            "Temper the spices, add karamani and carrot and toss 2 minutes.",
            "Mix in coconut.",
        ],
    ),
    "Pepper Egg Masala Bites": R(
        "20 min",
        [
            "4 eggs, hard-boiled and cut into quarters",
            "1 onion finely chopped, 1 tsp oil, ½ tsp pepper, ¼ tsp kashmiri chilli, pinch turmeric, salt, curry leaves",
        ],
        [
            "Heat oil, add curry leaves and onion; sauté until golden.",
            "Add the spices and salt, then the egg quarters. Toss gently 2 minutes until coated.",
            "Serve with toothpicks.",
        ],
    ),
}
