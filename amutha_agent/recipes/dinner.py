"""Dinner and fortnightly Treat Night recipes (serves 4)."""

from . import common as C
from .base import R

_SALNA = (
    "Salna: 1 onion, 2 tomatoes, 1 tsp ginger-garlic paste, 1 tsp kashmiri chilli, 2 tsp coriander powder, "
    "¼ tsp turmeric; paste of ½ cup coconut + 1 tsp fennel + 5 cashews; cinnamon, cloves, curry leaves, 2 tbsp oil"
)
_SALNA_STEPS = (
    "Salna: heat oil, add cinnamon, cloves and curry leaves, then onion until soft. Add ginger-garlic paste and tomatoes and cook until mushy. "
    "Add the spice powders, the coconut paste and 2½ cups water (with the vegetables or chicken). Simmer 15 minutes to a thin, flavourful gravy."
)
_PAROTTA_DOUGH = "Parotta dough: 2 cups maida + 1 cup whole wheat flour, 1 tsp sugar, 1 tsp salt, 1 egg (optional), 3 tbsp oil, about 1 cup water"
_PAROTTA_STEPS = [
    "Mix both flours, sugar, salt, egg and 1 tbsp oil. Add water slowly and knead 10 minutes into a very soft, smooth dough.",
    "Coat with oil, cover and rest at least 2 hours (or overnight in the fridge).",
    "Divide into 8 balls and oil them. Stretch each ball very thin on an oiled counter, pleat it like a fan, and coil it into a spiral. Rest 15 minutes.",
    "Flatten each spiral to a 5-inch round. Cook on a medium-hot tawa with a little oil, 2 minutes a side, until golden spots appear.",
    "While hot, stack 2-3 parottas and clap them between your palms to open the layers.",
]

RECIPES = {
    "Phulka with Channa Masala": R(
        "Soak chickpeas in the morning; 45 min",
        [
            C.PHULKA_ING,
            "Channa: 1 cup chickpeas (soaked 8 h), 2 onions, 3 tomatoes pureed, 1 tbsp ginger-garlic paste",
            "1 tsp kashmiri chilli, 2 tsp coriander powder, 1 tsp chana masala or garam masala, ¼ tsp turmeric, 1 tsp amchur or lemon juice",
            "2 tbsp oil, 1 tsp cumin, 1 bay leaf, coriander leaves, salt",
        ],
        [
            "Pressure-cook chickpeas with salt for 6 whistles until very soft.",
            "Heat oil, add cumin and bay leaf, then onions until golden brown.",
            "Add ginger-garlic paste, then tomato puree; cook until oil separates.",
            "Add the spice powders and cook 1 minute. Add chickpeas with 1 cup of their water.",
            "Simmer 10 minutes, mashing a few chickpeas to thicken. Add amchur and coriander.",
            *C.PHULKA_STEPS,
            "Serve the phulkas hot with channa masala.",
        ],
    ),
    "Egg Kothu Chapati": R(
        "30 min (use 8 chapatis, fresh or from lunch)",
        [
            "8 whole wheat chapatis, torn into small bits",
            "4 eggs, 2 onions sliced, 2 tomatoes chopped, 1 cup shredded cabbage, 1 carrot grated, 1 green chilli",
            "½ cup salna or any leftover kuzhambu (or ½ cup thin tomato gravy)",
            "1 tsp kashmiri chilli, ½ tsp garam masala, ¼ tsp turmeric, salt, 2 tbsp oil, curry leaves, coriander",
        ],
        [
            "Heat oil on a wide tawa or kadai. Add curry leaves, onion and chilli and sauté until soft.",
            "Add tomatoes, cabbage and carrot; cook 4 minutes. Add the spice powders and salt.",
            "Push to the side, break the eggs into the centre and scramble.",
            "Add the chapati bits and the salna. Mix and chop everything together with a steel tumbler or spatula, Madurai style, for 3-4 minutes.",
            "Finish with coriander. Serve with raita or more salna.",
        ],
        tip="The chopping sound is half the fun - let the children do the chopping.",
    ),
    "Millet Masala Dosa with Potato-Carrot Masala": R(
        "Batter: soak 6 h + ferment overnight; 40 min cooking",
        [
            "Millet dosa batter: 1½ cups kuthiraivali or varagu millet + ½ cup urad dal + ¼ tsp fenugreek, salt",
            "Masala: 3 potatoes boiled and crumbled, 1 carrot grated, ¼ cup peas, 2 onions sliced, 1-inch ginger, 1 green chilli, ¼ tsp turmeric, curry leaves, salt",
            "Tempering: 1 tbsp oil, mustard, 1 tsp chana dal, 1 tsp urad dal",
            "Ghee or oil for the dosa",
            C.COCONUT_CHUTNEY_ING,
        ],
        [
            "Batter (start the day before): soak millet, and urad dal with fenugreek, separately for 6 hours. Grind smooth with salt, ferment overnight, and thin with water to dosa consistency.",
            "Masala: temper mustard and dals, add curry leaves, onion, ginger and chilli and sauté until soft.",
            "Add carrot and peas, then turmeric and salt. Add potatoes and ¼ cup water and mash lightly. Cook 3 minutes.",
            "Spread a ladle of batter thinly on a very hot tawa. Drizzle ghee.",
            "When crisp and golden, place 2 tbsp masala in the centre and fold.",
            C.COCONUT_CHUTNEY_STEP,
            "Serve with coconut chutney.",
        ],
    ),
    "Chapati with Mixed Vegetable Kurma": R(
        "45 min",
        [
            C.PHULKA_ING + " (rolled a little thicker for chapati)",
            *C.VEG_KURMA_ING,
        ],
        [
            *C.VEG_KURMA_STEPS,
            "Chapati: knead the flour, salt and water into a soft dough, rub in the oil and rest 20 minutes.",
            "Roll the dough into 6-inch rounds. Cook on a hot tawa, adding a few drops of oil, pressing with a cloth until puffed and spotted on both sides.",
            "Serve chapatis hot with kurma.",
        ],
    ),
    "Chicken Chapati Roll with Mint-Curd Dip": R(
        "Marinate 1 h; 40 min",
        [
            "8 whole wheat chapatis",
            "Filling: 400 g boneless chicken strips; marinade of ¼ cup curd, 1 tsp ginger-garlic paste, 1 tsp kashmiri chilli, ½ tsp garam masala, ½ tsp pepper, salt",
            "1 onion and 1 capsicum sliced thin; ½ cucumber in strips; lemon",
            "Mint-curd dip: 1 cup thick curd hung in a cloth 1 hour, ½ cup mint, ¼ cup coriander, 1 small green chilli, 1 garlic clove, salt",
            "1 tbsp oil",
        ],
        [
            "Marinate the chicken for at least 1 hour.",
            "Dip: grind mint, coriander, chilli and garlic. Whisk into the hung curd with salt. Keep cold.",
            "Cook the chicken strips on a hot tawa with oil, 8-10 minutes, until charred at the edges.",
            "Toss onion and capsicum on the same tawa for 1 minute.",
            "Warm each chapati, spread the dip, add chicken, vegetables and cucumber, squeeze lemon, and roll tightly.",
            "Wrap the bottom in butter paper for a shawarma-shop feel.",
        ],
        tip="Hung curd makes a thick, creamy dip - the home answer to shop spreads.",
    ),
    "Idli with Nattu Kozhi Kuzhambu": R(
        "Batter: soak 6 h + ferment overnight; 1 h 15 min cooking",
        [
            C.IDLI_BATTER_ING,
            "Kuzhambu: 750 g country chicken (nattu kozhi), curry cut; 15 shallots; 2 tomatoes; 1 tbsp ginger-garlic paste",
            "Masala: 1 tbsp coriander seeds, 1 tsp pepper, 1 tsp fennel, 1 tsp cumin, 2 dry red chillies, ¼ cup coconut - dry roast and grind",
            "3 tbsp gingelly oil, ½ tsp turmeric, curry leaves, salt",
        ],
        [
            *C.IDLI_BATTER_STEPS,
            "Masala: dry-roast the masala items on low flame until the coconut is golden, cool and grind smooth with water.",
            "Heat oil, add curry leaves and shallots and sauté until golden. Add ginger-garlic paste and tomatoes and cook until mushy.",
            "Add chicken, turmeric and salt; cook on high 5 minutes.",
            "Add the ground masala and 2 cups water. Pressure-cook 6 whistles (country chicken is tougher).",
            "Simmer open 5 minutes to a thin, peppery gravy.",
            "Steam the idlis 10-12 minutes and serve with the kuzhambu.",
        ],
        tip="Thin kozhi kuzhambu soaks into idli - children love this weekend-style combo.",
    ),
    "Samai Vegetable Kichadi with Raita": R(
        "35 min",
        [
            "1 cup samai (little millet), ½ cup moong dal, washed together",
            "2 cups chopped vegetables (carrot, beans, peas), 1 onion, 1 tomato, 1 green chilli, 1-inch ginger",
            "2 tbsp ghee, 1 tsp cumin, ¼ tsp turmeric, 4½ cups water, salt",
            "Raita: 1½ cups curd, ½ cucumber grated, salt, roasted cumin powder",
            "Topping: 1 onion thinly sliced and fried crisp in 1 tbsp oil (home-made fried onions)",
        ],
        [
            "Heat ghee in a cooker, add cumin, ginger, chilli and onion; sauté 2 minutes.",
            "Add tomato and vegetables, then turmeric and salt.",
            "Add the millet and dal with 4½ cups water. Pressure-cook 3 whistles.",
            "Stir well; it should be soft and porridge-like. Add hot water if too thick.",
            "Mix the raita. Top the kichadi with fried onions and a spoon of ghee.",
        ],
    ),
    "Vegetable Wheat Paratha with Curd": R(
        "45 min",
        [
            "Dough: 2½ cups whole wheat flour, salt, water, 1 tsp oil",
            "Filling: 2 potatoes boiled and mashed, 1 carrot and 1 cup cabbage finely grated (squeezed dry), 1 green chilli, coriander, ½ tsp cumin powder, ½ tsp garam masala, salt",
            "Ghee or home-made butter for cooking; 2 cups curd to serve",
        ],
        [
            "Knead a soft dough and rest 15 minutes.",
            "Mix all filling items. Squeeze out any water so the paratha does not tear.",
            "Roll a ball of dough to 4 inches, place 2 tbsp filling in the centre, gather the edges and seal.",
            "Roll gently into a 7-inch paratha with a little dry flour.",
            "Cook on a medium-hot tawa, 1 minute a side, then brush with ghee and press until golden spots appear.",
            "Serve hot with curd and a small dollop of home-made butter.",
        ],
    ),
    "Appam with Vegetable Stew": R(
        "Soak 4 h + ferment overnight; 40 min",
        [
            "Appam: 1½ cups raw rice (soaked 4 h), ½ cup cooked rice, ¾ cup grated coconut, 1 tbsp sugar or palm jaggery, ½ tsp salt",
            "Stew: 2 potatoes, 1 carrot, 1 cup beans and peas, 1 onion, 2 green chillies, 1-inch ginger, 1 cup thin + 1 cup thick coconut milk",
            "1 tbsp coconut oil, cinnamon, 3 cloves, 2 cardamom, ½ tsp crushed pepper, curry leaves, salt",
        ],
        [
            "Grind soaked rice, cooked rice and coconut to a smooth batter. Ferment overnight. Mix in sugar and salt in the morning; batter should be thinner than dosa batter.",
            "Stew: heat coconut oil, add whole spices, onion, ginger, chillies and curry leaves; sauté until soft.",
            "Add vegetables, salt and the thin coconut milk. Cover and cook until tender.",
            "Add the thick coconut milk and pepper; heat gently without boiling.",
            "Appam: heat the appam pan, pour a ladle of batter and swirl it round so the edges are thin. Cover and cook 2 minutes on medium until the centre is soft and the edges crisp.",
        ],
    ),
    "Masala Kuzhi Paniyaram with Tomato Chutney": R(
        "Batter: soak 6 h + ferment overnight (or use 2-day-old batter); 30 min cooking",
        [
            C.IDLI_BATTER_ING + " - 2-day-old batter works best",
            "1 onion, 1 carrot grated, 1 green chilli, 1 tsp grated ginger, coriander and curry leaves",
            "Tempering: 1 tsp oil, mustard, 1 tsp urad dal, 1 tsp chana dal",
            C.TOMATO_CHUTNEY_ING,
            "Gingelly oil for the pan",
        ],
        [
            *C.IDLI_BATTER_STEPS,
            "Temper mustard and dals. Add onion, carrot, chilli and ginger; sauté 2 minutes. Mix into the batter with the leaves.",
            "Heat the paniyaram pan and add a few drops of oil to each hole.",
            "Fill each hole three-quarters full. Cover and cook 2 minutes.",
            "Flip with a skewer and cook 2 minutes more until golden.",
            C.TOMATO_CHUTNEY_STEP,
            "Serve with tomato chutney.",
        ],
    ),
    "Egg Curry with Phulka": R(
        "40 min",
        [
            C.PHULKA_ING,
            "Curry: 6 boiled eggs, 2 onions, 2 tomatoes, 1 tsp ginger-garlic paste, ¼ cup coconut ground smooth",
            "1 tsp kashmiri chilli, 2 tsp coriander powder, ½ tsp garam masala, ¼ tsp turmeric, 2 tbsp oil, curry leaves, salt",
        ],
        [
            "Heat oil, add curry leaves and onions; sauté until golden. Add ginger-garlic paste and tomatoes and cook until mushy.",
            "Add the spice powders and salt, then the coconut paste and 1½ cups water. Simmer 8 minutes.",
            "Slit the eggs, add to the gravy and simmer 5 minutes so they soak up the flavour.",
            *C.PHULKA_STEPS,
            "Cut the eggs in half when serving so the yolk soaks into the gravy.",
        ],
    ),
    "Jowar Roti with Dal Tadka": R(
        "40 min",
        [
            "Roti: 2 cups jowar flour, about 1 cup hot water, pinch salt",
            "Dal: ¾ cup toor dal, 1 tomato, ¼ tsp turmeric, salt",
            "Tadka: 2 tsp ghee, 1 tsp cumin, 5 garlic sliced, 1 dry red chilli, pinch asafoetida, ½ tsp kashmiri chilli, coriander",
        ],
        [
            "Dal: pressure-cook toor dal with tomato and turmeric, 4 whistles. Mash, add salt and water, simmer 5 minutes.",
            "Tadka: heat ghee, fry cumin, garlic until golden, then red chilli, asafoetida and chilli powder. Pour over the dal at the table for the sizzle.",
            "Roti: add hot water to jowar flour and mix with a spoon, then knead while warm into a smooth dough.",
            "Pat each ball into a thin round on a floured plate with your palm (or roll between two sheets).",
            "Cook on a hot tawa, sprinkle water on top, flip after 1 minute, then puff on the open flame.",
        ],
    ),
    "Ragi Idiyappam with Coconut Milk and Egg Roast": R(
        "45 min",
        [
            "Idiyappam: 2 cups ragi flour (steamed 10 min or roasted), about 2 cups boiling water, salt, 1 tsp oil",
            "1½ cups coconut milk sweetened with 2 tbsp palm jaggery and a pinch of cardamom",
            "Egg roast: 6 boiled eggs, 3 onions thinly sliced, 2 tomatoes, 1 tsp ginger-garlic paste, 1 tsp kashmiri chilli, 1 tsp coriander powder, ½ tsp pepper, ½ tsp garam masala, curry leaves, 2 tbsp coconut oil",
        ],
        [
            "Pour boiling salted water with oil over the ragi flour, mix with a spoon, then knead into a soft dough.",
            "Press into idiyappam on greased idli plates and steam 8-10 minutes.",
            "Egg roast: heat coconut oil, sauté onions slowly until deep brown (12 minutes). Add ginger-garlic paste, tomatoes and the spices; cook to a thick masala.",
            "Slit the eggs, add and roast 5 minutes so the masala coats them.",
            "Serve idiyappam with the sweet coconut milk and the egg roast on the side.",
        ],
    ),
    "Wheat Rava Kichadi with Coconut Chutney": R(
        "35 min",
        [
            "1 cup broken wheat (godhumai rava / dalia), dry-roasted 3 minutes",
            "2 cups vegetables (carrot, beans, peas), 1 onion, 1 tomato, 1 green chilli, 1 tsp ginger",
            "2 tbsp ghee, ½ tsp mustard, 1 tsp urad dal, 10 cashews, curry leaves, ¼ tsp turmeric, 3½ cups water, salt",
            C.COCONUT_CHUTNEY_ING,
        ],
        [
            "Heat ghee, fry mustard, urad dal and cashews. Add curry leaves, onion, chilli and ginger.",
            "Add tomato and vegetables, then turmeric and salt.",
            "Add water and bring to a boil. Add the roasted broken wheat.",
            "Pressure-cook 3 whistles (or cook covered 15 minutes, stirring).",
            "Finish with a spoon of ghee.",
            C.COCONUT_CHUTNEY_STEP,
        ],
    ),
    # ---------------- Treat Night (the only maida dishes; once every 14 days) ----------------
    "Treat Night: Madurai Chicken Kothu Parotta (home-made)": R(
        "Dough rests 2 h (or overnight); 1 h 15 min",
        [
            _PAROTTA_DOUGH,
            "Chicken salna: 400 g chicken, plus the salna ingredients below",
            _SALNA,
            "Kothu: 3 eggs, 2 onions sliced, 2 tomatoes, 1 cup shredded cabbage, 1 carrot grated, 1 green chilli, ½ tsp garam masala, curry leaves, coriander, 2 tbsp oil",
        ],
        [
            *_PAROTTA_STEPS,
            _SALNA_STEPS + " Add the chicken with the water and cook until tender. Shred a cup of chicken for the kothu.",
            "Tear 6 parottas into small bits.",
            "On a wide tawa, sauté onion, chilli and curry leaves; add tomatoes, cabbage and carrot. Scramble the eggs in the middle.",
            "Add the parotta bits, shredded chicken and 1 cup salna. Chop and mix with a steel tumbler for 4-5 minutes.",
            "Serve with the remaining salna and onion raita.",
        ],
        tip="Treat Night is once every two weeks - make it a celebration, and pile on the vegetables.",
    ),
    "Treat Night: Madurai Bun Parotta with Vegetable Salna": R(
        "Dough rests 2 h (or overnight); 1 h 15 min",
        [
            _PAROTTA_DOUGH,
            "Vegetable salna: 2 cups mixed vegetables (carrot, beans, peas, potato) plus the salna ingredients below",
            _SALNA,
        ],
        [
            _PAROTTA_STEPS[0],
            _PAROTTA_STEPS[1] + " Divide into 6 bigger balls for bun parotta.",
            "For bun parotta: stretch each ball thin, fold the edges in, roll into a thick spiral 3 inches wide and 1 inch tall. Rest 20 minutes.",
            "Cook on a low-medium tawa with oil, covered, 4-5 minutes a side so the inside cooks through and puffs like a bun.",
            "Clap each bun parotta to fluff the layers.",
            _SALNA_STEPS,
            "Serve bun parottas soaked in plenty of salna.",
        ],
    ),
    "Treat Night: Egg Veechu Parotta with Chicken Salna": R(
        "Dough rests 2 h (or overnight); 1 h 15 min",
        [
            _PAROTTA_DOUGH,
            "4 eggs beaten with 1 small onion (finely chopped), pinch pepper and salt",
            "Chicken salna: 400 g chicken plus the salna ingredients below",
            _SALNA,
        ],
        [
            _PAROTTA_STEPS[0],
            _PAROTTA_STEPS[1],
            "Stretch each oiled ball paper-thin on the counter (veechu = 'thrown/stretched').",
            "Place on a medium-hot tawa, pour 3 tbsp beaten egg in the centre, and fold the four sides over to make a square parcel.",
            "Cook with a little oil, 2 minutes a side, until golden and the egg is set.",
            _SALNA_STEPS + " Add the chicken with the water and cook until tender.",
            "Cut each parcel into squares and serve with the chicken salna.",
        ],
    ),
}
