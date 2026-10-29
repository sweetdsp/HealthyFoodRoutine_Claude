"""Lunch base (rice / millet / phulka) and vegetable side recipes (serves 4)."""

from .base import R

_PORIYAL_TEMPER = "Tempering: 1 tbsp oil (coconut or gingelly), ½ tsp mustard, 1 tsp urad dal, 1 dry red chilli, curry leaves"


def _millet_rice(name: str) -> object:
    return R(
        "Soak 30 min; 20 min",
        [f"1 cup {name}", "2½ cups water", "¼ tsp salt, ½ tsp ghee"],
        [
            "Wash the millet 3 times and soak for 30 minutes.",
            "Boil the water with salt and ghee in a pot.",
            "Add the drained millet, cover and cook on low flame 12-15 minutes until the water is absorbed.",
            "Switch off and keep covered 5 minutes, then fluff with a fork.",
        ],
        tip="Pressure cooker: 1 cup millet + 2½ cups water, 2 whistles on medium.",
    )


RECIPES = {
    # ---------------- Lunch base ----------------
    "Ponni Rice - half cup per person": R(
        "25 min",
        ["1 cup ponni rice (makes about 2 cups cooked - half a cup each for 4)", "3 cups water", "Pinch of salt (optional)"],
        [
            "Wash the rice 3 times and soak 15 minutes.",
            "Pressure-cook with 3 cups water, 3 whistles on medium.",
            "Rest until the pressure drops, then fluff.",
            "Serve half a cup per person. Fill the rest of the plate with kuzhambu, poriyal and curd.",
        ],
    ),
    "Hand-pound Red Rice - half cup per person": R(
        "Soak 1 h; 35 min",
        ["1 cup hand-pound (kaikuthal) red rice", "3½ cups water"],
        [
            "Wash well and soak for 1 hour - unpolished rice needs it.",
            "Pressure-cook with 3½ cups water, 5-6 whistles.",
            "Rest 10 minutes and fluff. Serve half a cup per person.",
        ],
    ),
    "Kuthiraivali (Barnyard Millet) Rice": _millet_rice("kuthiraivali (barnyard millet)"),
    "Varagu (Kodo Millet) Rice": _millet_rice("varagu (kodo millet)"),
    "Samai (Little Millet) Rice": _millet_rice("samai (little millet)"),
    "Soft Wheat Phulka (2-3 per person)": R(
        "Rest 20 min; 25 min",
        ["2½ cups whole wheat flour (atta)", "About 1 cup warm water", "Pinch of salt, 1 tsp oil", "Ghee to brush (optional)"],
        [
            "Mix flour and salt, add water little by little and knead 5 minutes into a soft dough. Rub in the oil.",
            "Cover and rest 20 minutes.",
            "Divide into 10-12 balls. Roll each thin and even, about 6 inches, using a little dry flour.",
            "Cook on a hot tawa 15 seconds until bubbles appear, flip, cook 30 seconds.",
            "Hold with tongs directly over the gas flame - it puffs up in seconds. Brush with ghee.",
        ],
        tip="Keep phulkas in a cloth-lined box so they stay soft.",
    ),
    # ---------------- Vegetable sides ----------------
    "Beans Poriyal": R(
        "20 min",
        ["300 g beans, finely chopped", "3 tbsp grated coconut", "¼ tsp turmeric, salt", _PORIYAL_TEMPER],
        [
            "Heat oil, add mustard, urad dal, red chilli and curry leaves.",
            "Add beans, turmeric, salt and 3 tbsp water. Cover and cook on low 8 minutes until tender but still green.",
            "Add coconut, toss 1 minute and switch off.",
        ],
    ),
    "Cabbage-Carrot Poriyal": R(
        "20 min",
        ["3 cups cabbage, finely shredded", "1 carrot, grated", "1 green chilli, slit", "3 tbsp grated coconut, salt", _PORIYAL_TEMPER],
        [
            "Temper mustard, urad dal, red chilli and curry leaves. Add green chilli.",
            "Add cabbage, carrot and salt. Cook uncovered on medium 6-7 minutes, stirring - no water needed.",
            "Add coconut and toss.",
        ],
    ),
    "Beetroot Poriyal": R(
        "25 min",
        ["2 medium beetroots, peeled and finely chopped", "1 small onion (optional)", "3 tbsp grated coconut, salt", _PORIYAL_TEMPER],
        [
            "Temper, then add onion and sauté 1 minute.",
            "Add beetroot, salt and ¼ cup water. Cover and cook on low 10-12 minutes until soft.",
            "Dry out any water, add coconut and toss.",
        ],
    ),
    "Vazhakkai Roast": R(
        "30 min",
        [
            "2 raw bananas (vazhakkai), peeled and cut into thin rounds",
            "1 tsp kashmiri chilli powder, ¼ tsp turmeric, 1 tbsp rice flour, salt",
            "2 tbsp gingelly oil, curry leaves",
        ],
        [
            "Keep the slices in water so they do not darken. Drain well and pat dry.",
            "Toss with chilli powder, turmeric, rice flour and salt.",
            "Spread in a single layer on a wide pan with oil. Roast on medium 6-8 minutes a side until crisp at the edges.",
            "Add curry leaves at the end. Serve hot - crunchy like chips.",
        ],
    ),
    "Avarakkai Poriyal": R(
        "20 min",
        ["300 g broad beans (avarakkai), strings removed, chopped", "3 tbsp grated coconut, salt", _PORIYAL_TEMPER],
        [
            "Temper mustard, urad dal, chilli and curry leaves.",
            "Add avarakkai, salt and ¼ cup water. Cover and cook 10 minutes until soft.",
            "Add coconut and toss.",
        ],
    ),
    "Vendakkai Crispy Fry": R(
        "25 min",
        [
            "300 g okra (vendakkai), washed and wiped completely dry, cut into 1-inch pieces",
            "2 tbsp besan, 1 tbsp rice flour, 1 tsp kashmiri chilli, ¼ tsp turmeric, ½ tsp amchur or few drops lemon, salt",
            "3 tbsp gingelly oil",
        ],
        [
            "Make sure the okra is fully dry - this prevents sliminess.",
            "Toss with all the flours and spices; sprinkle 1 tsp water so the coating sticks.",
            "Shallow-fry in a wide pan on medium, stirring gently, 10-12 minutes until crisp.",
        ],
    ),
    "Kovakkai Fry": R(
        "25 min",
        ["300 g kovakkai (ivy gourd), cut into thin lengthwise strips", "1 tsp sambar powder, ¼ tsp turmeric, salt", "2 tbsp gingelly oil, curry leaves"],
        [
            "Heat oil, add the kovakkai and stir-fry on medium 10 minutes, uncovered.",
            "Add turmeric, sambar powder and salt and roast 5 more minutes until crisp and browned.",
            "Add curry leaves at the end.",
        ],
    ),
    "Carrot-Peas Poriyal": R(
        "20 min",
        ["3 carrots, finely chopped", "½ cup fresh green peas", "3 tbsp grated coconut, salt", _PORIYAL_TEMPER],
        [
            "Temper mustard, urad dal, chilli and curry leaves.",
            "Add carrot, peas, salt and 3 tbsp water. Cover and cook 7 minutes.",
            "Add coconut and toss.",
        ],
    ),
    "Cauliflower Pepper Fry": R(
        "25 min",
        [
            "1 medium cauliflower, cut into small florets",
            "1 onion sliced, 1 tsp ginger-garlic paste, 1 tsp crushed pepper, ½ tsp fennel powder, ¼ tsp turmeric, salt",
            "2 tbsp oil, curry leaves",
        ],
        [
            "Blanch the florets in hot salted water with turmeric for 3 minutes. Drain.",
            "Heat oil, add curry leaves and onion; sauté until golden. Add ginger-garlic paste.",
            "Add cauliflower, salt and fennel; roast on medium 8 minutes until browned at the edges.",
            "Add pepper and toss 1 minute.",
        ],
    ),
    "Murungai Keerai Poriyal": R(
        "25 min",
        [
            "3 cups drumstick leaves (murungai keerai), stripped from stems and washed",
            "¼ cup moong dal, soaked 30 minutes",
            "1 onion chopped, 4 tbsp grated coconut, salt",
            _PORIYAL_TEMPER,
        ],
        [
            "Temper, add onion and sauté until soft.",
            "Add the soaked moong dal with ¼ cup water; cook covered 5 minutes.",
            "Add the leaves and salt, cook covered on low 6-8 minutes until soft (they shrink a lot).",
            "Add coconut and toss.",
        ],
    ),
    "Pudalangai Kootu": R(
        "30 min",
        [
            "1 snake gourd (pudalangai), deseeded and chopped",
            "⅓ cup moong dal, ¼ tsp turmeric, salt",
            "Paste: ¼ cup coconut, 1 tsp cumin, 1 green chilli",
            _PORIYAL_TEMPER,
        ],
        [
            "Cook moong dal with turmeric until soft.",
            "Cook snake gourd with salt and ½ cup water for 6 minutes.",
            "Add the dal and the ground paste; simmer 5 minutes to a thick kootu.",
            "Temper and pour over.",
        ],
    ),
    "Mixed Vegetable Thoran": R(
        "20 min",
        [
            "3 cups finely chopped vegetables (carrot, beans, cabbage)",
            "Crushed: ½ cup coconut, 4 shallots, 1 green chilli, ½ tsp cumin, ¼ tsp turmeric",
            "1 tbsp coconut oil, ½ tsp mustard, curry leaves, salt",
        ],
        [
            "Pulse the coconut, shallots, chilli, cumin and turmeric coarsely - do not make a paste.",
            "Heat coconut oil, crackle mustard and curry leaves.",
            "Add the vegetables, salt and 2 tbsp water. Cover and cook 5 minutes.",
            "Add the coconut mix and toss on medium for 3 minutes until dry.",
        ],
    ),
}
