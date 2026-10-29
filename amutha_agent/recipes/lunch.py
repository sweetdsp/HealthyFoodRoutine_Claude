"""Lunch main-dish recipes (serves 4: 2 adults + 2 teenagers)."""

from . import common as C
from .base import R

KID_MILD = "Children's tongues first: cook it mild, then fry 2 extra dry chillies in oil and stir them into the adults' portion."

RECIPES = {
    # ---------------- Fish ----------------
    "Madurai Meen Kuzhambu with Tawa Meen Varuval": R(
        "15 min marinate; 45 min",
        [
            "750 g seer fish (vanjaram) slices: 4 slices for fry, rest for kuzhambu",
            "Marinade: ½ tsp turmeric, 1 tsp kashmiri chilli powder, 1 tsp lemon juice, salt",
            "Kuzhambu: lemon-size tamarind soaked in 2 cups water, 15 shallots, 2 tomatoes, 8 garlic cloves",
            "2 tsp coriander powder, 1 tsp kashmiri chilli powder, ½ tsp turmeric, ½ cup grated coconut ground smooth",
            "3 tbsp gingelly oil, ½ tsp mustard, ½ tsp fenugreek, curry leaves, salt",
        ],
        [
            "Clean the fish, rub with the marinade and keep 15 minutes.",
            "Heat gingelly oil, add mustard and fenugreek (do not let it burn), then curry leaves, shallots and garlic. Sauté until golden.",
            "Add tomatoes and cook until mushy. Add chilli, coriander and turmeric powder and cook 1 minute.",
            "Pour in the tamarind water with salt and boil 10 minutes until the raw smell goes and oil floats.",
            "Add the coconut paste and simmer 3 minutes. Slide in the fish slices, simmer 6-8 minutes without stirring; swirl the pan instead.",
            "Fry: shallow-fry the 4 marinated slices on a tawa with 1 tbsp oil, 3 minutes each side until crisp.",
            "Kuzhambu tastes best after resting 1 hour. Serve with rice and the fried fish.",
        ],
        tip=KID_MILD,
    ),
    "Coconut Milk Fish Curry (mild)": R(
        "35 min",
        [
            "600 g pomfret or seer fish pieces, ½ tsp turmeric, salt",
            "1 cup thick coconut milk and 1 cup thin coconut milk (from 1 coconut)",
            "1 onion sliced, 2 tomatoes, 1-inch ginger and 4 garlic (crushed), 2 slit green chillies",
            "1 tsp coriander powder, ½ tsp pepper powder, curry leaves, 2 tbsp coconut oil",
        ],
        [
            "Rub fish with turmeric and salt.",
            "Heat coconut oil, sauté onion, ginger, garlic, chillies and curry leaves until soft.",
            "Add tomatoes and cook until soft. Add coriander powder and pepper.",
            "Pour the thin coconut milk and bring to a gentle simmer for 5 minutes.",
            "Add the fish and cook 6 minutes on low flame.",
            "Pour the thick coconut milk, heat until just steaming (do not boil, or it splits). Switch off.",
        ],
        tip="Very mild - the best 'first fish curry' for children who complain of spice.",
    ),
    "Nethili Meen Kuzhambu with Nethili Fry": R(
        "50 min",
        [
            "500 g nethili (anchovies), cleaned (heads removed, kept whole)",
            "Fry coating (for half the fish): 1 tsp kashmiri chilli powder, ½ tsp turmeric, 2 tbsp rice flour, 1 tsp ginger-garlic paste, salt",
            "Kuzhambu: lemon-size tamarind in 2 cups water, 12 shallots, 6 garlic, 2 tomatoes",
            "1 tbsp home-made kuzhambu masala (or 2 tsp coriander + 1 tsp chilli powder), ½ tsp turmeric",
            "3 tbsp gingelly oil, ½ tsp mustard, ½ tsp fenugreek, curry leaves, salt",
        ],
        [
            "Wash the nethili 3-4 times with salt water. Divide into two halves.",
            "Kuzhambu: heat oil, add mustard, fenugreek and curry leaves, then shallots and garlic; sauté until golden.",
            "Add tomatoes, then the masala and turmeric. Cook 2 minutes.",
            "Add tamarind water and salt and boil 10 minutes.",
            "Add half the nethili and simmer 5 minutes only - anchovies cook fast. Do not stir; swirl the pan.",
            "Fry: mix the other half with the coating, rest 10 minutes. Shallow-fry in batches on a tawa until crisp, 2-3 minutes a side.",
        ],
        tip="Eat the small bones - they are a great natural source of calcium.",
    ),
    "Fish Kola Urundai Kuzhambu": R(
        "50 min",
        [
            "Fish balls: 400 g boneless fish fillet (seer or tuna), ¼ cup roasted gram (pottukadalai) powdered, 1 small onion, ½ tsp fennel, 1 green chilli, coriander, salt",
            "Gravy: 1 onion, 2 tomatoes, 1 tsp ginger-garlic paste, 1 tsp chilli powder, 2 tsp coriander powder, ¼ tsp turmeric",
            "Paste: ¼ cup coconut, 1 tsp fennel, 5 cashews",
            "2 tbsp oil, curry leaves, salt",
        ],
        [
            "Steam the fish fillet 8 minutes, cool and crumble finely, removing any bones.",
            "Grind onion, fennel and chilli coarsely. Mix with fish, roasted gram powder, coriander and salt. Shape into 20 small balls.",
            "Steam the balls 8 minutes so they hold together in the gravy.",
            "Gravy: sauté onion in oil, add ginger-garlic paste and tomatoes and cook until mushy. Add the spice powders.",
            "Add the ground coconut paste and 2 cups water, simmer 8 minutes.",
            "Drop in the fish balls and simmer 5 minutes on low. Do not stir hard.",
        ],
    ),
    "Vanjaram Fish Fry with Pepper Rasam and Paruppu": R(
        "Marinate overnight (or 1 h); 45 min",
        [
            "Fry: 4-6 vanjaram (seer fish) slices; 1 tbsp ginger-garlic paste, 1 tsp kashmiri chilli, 1 tsp pepper powder, ½ tsp turmeric, 1 tbsp lemon juice, 1 tbsp rice flour, salt",
            "Paruppu: ½ cup toor dal, ¼ tsp turmeric, 1 tsp ghee, ½ tsp cumin, salt",
            "Pepper rasam: small lemon-size tamarind in 2 cups water, 2 tomatoes, 1 tsp pepper, 1 tsp cumin, 5 garlic, ¼ tsp turmeric, coriander",
            "Tempering: 1 tsp ghee, ½ tsp mustard, pinch asafoetida, curry leaves",
        ],
        [
            "Coat the fish slices with the marinade and keep in the fridge.",
            "Paruppu: pressure-cook toor dal with turmeric, 4 whistles. Mash with salt, temper cumin in ghee.",
            "Rasam: crush pepper, cumin and garlic coarsely. Boil tamarind water with tomatoes, turmeric, salt and the crushed spices for 8 minutes.",
            "Add 2 tbsp of the cooked dal water and 1 cup water. Heat until frothy - do not boil hard. Temper and add coriander.",
            "Fry the fish on a hot tawa with 2 tbsp gingelly oil, 3-4 minutes each side, until crisp outside and flaky inside.",
            "Serve rice with paruppu and ghee first, then rasam, with the fish fry.",
        ],
    ),
    # ---------------- Chicken ----------------
    "Chettinad Chicken Kuzhambu (kid-mild)": R(
        "1 h",
        [
            "750 g country chicken (or regular chicken), curry cut; ½ tsp turmeric",
            "Chettinad masala (dry roast): 1 tbsp coriander seeds, 1 tsp pepper, 1 tsp fennel, 1 tsp cumin, 2 dry red chillies, 1-inch cinnamon, 3 cloves, 1 star anise, 3 tbsp grated coconut",
            "15 shallots, 2 tomatoes, 1 tbsp ginger-garlic paste, curry leaves",
            "3 tbsp gingelly oil, salt, coriander leaves",
        ],
        [
            "Dry-roast all masala items on low flame until aromatic and the coconut is golden. Cool and grind to a smooth paste with water.",
            "Heat oil, add curry leaves and shallots, sauté until golden. Add ginger-garlic paste.",
            "Add tomatoes and cook until mushy.",
            "Add chicken, turmeric and salt; cook on high 5 minutes until it changes colour.",
            "Add the ground masala and 1½ cups water. Pressure-cook 3 whistles (country chicken 5-6), or simmer covered 25 minutes.",
            "Simmer open until the gravy thickens. Finish with coriander.",
        ],
        tip=KID_MILD,
    ),
    "Milagu Kozhi Varuval with Rasam and Paruppu": R(
        "Marinate 30 min; 45 min",
        [
            "750 g chicken, small pieces; marinate with ½ tsp turmeric, 1 tbsp ginger-garlic paste, salt",
            "2 tsp black pepper and 1 tsp fennel, freshly crushed; 1 tsp coriander powder",
            "20 shallots, sliced; 2 sprigs curry leaves; 3 tbsp gingelly oil",
            C.PARUPPU_ING,
            C.PEPPER_RASAM_ING,
        ],
        [
            "Marinate the chicken for 30 minutes.",
            "Heat oil, add curry leaves and shallots; fry until golden.",
            "Add the chicken and cook on high 5 minutes. Cover and cook on low in its own juice for 15-20 minutes.",
            "Open, add coriander powder and the crushed pepper-fennel. Roast on medium, stirring, until dry and dark brown.",
            "While the chicken cooks, make the paruppu and rasam:",
            C.PARUPPU_STEP,
            *C.PEPPER_RASAM_STEPS,
        ],
        tip="Pepper is gentler on young tongues than chilli; adjust to 1½ tsp for the children.",
    ),
    "Home-made Chicken 65 (air-fried) with Keerai Paruppu": R(
        "Marinate overnight (or 2 h); 45 min",
        [
            "Chicken 65: 600 g boneless chicken cubes; ½ cup thick curd, 1 tbsp ginger-garlic paste, 1½ tsp kashmiri chilli powder (for colour, mild heat), ½ tsp garam masala, 2 tbsp rice flour, 1 tbsp besan, juice of ½ lemon, salt, curry leaves",
            "1 tbsp oil for brushing",
            "Keerai paruppu: 1 bunch spinach or arai keerai (chopped), ½ cup moong dal, 1 tomato, 4 garlic, ½ tsp cumin, ¼ tsp turmeric, salt, 1 tsp ghee",
        ],
        [
            "Mix all Chicken 65 marinade items with the chicken. Keep in the fridge overnight.",
            "Air-fry at 200°C for 15-18 minutes, shaking and brushing with oil halfway, until crisp at the edges. (No air fryer: bake at 220°C for 25 minutes, or shallow-fry on a tawa.)",
            "Toss with curry leaves crisped in 1 tsp oil.",
            "Keerai paruppu: pressure-cook moong dal with tomato, garlic and turmeric, 3 whistles.",
            "Add the greens and salt, cook open 5 minutes. Mash lightly and temper cumin in ghee.",
        ],
        tip="No artificial colour - kashmiri chilli gives the red colour.",
    ),
    "Chicken Kurma with Coconut and Cashew": R(
        "45 min",
        [
            "750 g chicken, curry cut; ½ cup curd; 1 tbsp ginger-garlic paste; salt",
            "Paste: ¾ cup grated coconut, 10 cashews, 1 tsp fennel, 2 green chillies, 1 tbsp poppy seeds (optional)",
            "2 onions, 2 tomatoes, mint and coriander leaves",
            "Whole spices: 1-inch cinnamon, 3 cloves, 2 cardamom, 1 bay leaf; 2 tbsp oil",
        ],
        [
            "Marinate chicken with curd, ginger-garlic paste and salt for 20 minutes.",
            "Grind the paste ingredients smooth with water.",
            "Heat oil, add whole spices, then onion; sauté until light golden. Add tomatoes and cook soft.",
            "Add the chicken and cook on high 5 minutes.",
            "Add the coconut paste and 1 cup water. Cover and simmer 20 minutes until the chicken is tender.",
            "Finish with mint and coriander. Good with millet rice or phulka.",
        ],
    ),
    "Seeraga Samba Chicken Biryani (more chicken, less rice) with Onion Raita": R(
        "Marinate overnight; 1 h 15 min",
        [
            "Rice: 1½ cups seeraga samba rice (only ⅓ cup per person), soaked 20 minutes",
            "800 g chicken, curry cut",
            "Marinade: ¾ cup curd, 1½ tbsp ginger-garlic paste, 1 tsp kashmiri chilli, ½ tsp turmeric, 1 tbsp home-made biryani masala, handful mint and coriander, salt",
            "1 cup mixed vegetables (carrot, beans, peas) to bulk up the biryani",
            "3 onions sliced, 2 tomatoes, 2 green chillies; 2 tbsp ghee + 2 tbsp oil; whole spices (cinnamon, cloves, cardamom, bay leaf, star anise)",
            "Raita: 1½ cups curd, 1 onion, ½ cucumber, coriander, salt, pinch roasted cumin powder",
        ],
        [
            "Marinate the chicken overnight in the fridge.",
            "In a heavy pot or cooker, heat ghee and oil. Fry whole spices, then onions until golden brown.",
            "Add green chillies and tomatoes and cook until soft.",
            "Add the chicken with all its marinade and the vegetables. Cook on high 8 minutes.",
            "Add 2¼ cups water (1½ times the rice), check salt, and bring to a boil.",
            "Add the drained rice, stir once gently. Pressure-cook 1 whistle on medium, then 5 minutes on lowest flame. (Or cover tightly and cook on low 18 minutes.)",
            "Rest 10 minutes before opening. Fluff gently.",
            "Raita: mix chopped onion, cucumber and coriander into whisked curd with salt and cumin.",
        ],
        tip="Seeraga samba is a small fragrant rice, so a little looks like a lot.",
    ),
    # ---------------- Egg ----------------
    "Muttai Kuzhambu with Beans Paruppu Usili": R(
        "50 min",
        [
            "6 eggs, hard-boiled and peeled; ¼ tsp turmeric; 1 tsp oil",
            "Kuzhambu: lemon-size tamarind in 2 cups water, 12 shallots, 2 tomatoes, 1½ tbsp kuzhambu masala (or 2 tsp coriander + 1 tsp chilli powder), ¼ cup coconut ground smooth",
            "2 tbsp gingelly oil, ½ tsp mustard, ½ tsp fenugreek, curry leaves, salt",
            "Usili: 250 g beans chopped fine; ¼ cup toor dal + ¼ cup chana dal soaked 1 hour, 2 dry red chillies, salt; 1 tbsp oil, mustard, urad dal, curry leaves",
        ],
        [
            "Make small slits in the eggs, toss in 1 tsp oil with turmeric until golden. Keep aside.",
            "Kuzhambu: temper mustard, fenugreek and curry leaves. Sauté shallots, then tomatoes until mushy.",
            "Add the masala, tamarind water and salt, boil 10 minutes. Add coconut paste and the eggs; simmer 5 minutes.",
            "Usili: grind the soaked dals with red chillies and salt coarsely, without water. Steam 10 minutes in an idli plate, cool and crumble.",
            "Cook the beans with salt and a splash of water until just done.",
            "Temper mustard, urad dal and curry leaves, add the crumbled dal and roast until golden and crumbly. Mix in the beans.",
        ],
    ),
    "Egg Masala with Dal Fry": R(
        "40 min",
        [
            "Egg masala: 6 boiled eggs (halved), 2 onions finely chopped, 2 tomatoes pureed, 1 tsp ginger-garlic paste, 1 tsp kashmiri chilli, 1½ tsp coriander powder, ½ tsp garam masala, ¼ tsp turmeric, 2 tbsp oil, coriander",
            "Dal fry: ¾ cup toor dal, 1 onion, 1 tomato, 4 garlic, 1 tsp cumin, ¼ tsp turmeric, 1 tsp ghee, salt",
        ],
        [
            "Dal: pressure-cook toor dal with turmeric, 4 whistles, and mash.",
            "Heat ghee, add cumin and garlic, then onion and tomato; cook soft. Add the dal, salt and water to a pouring consistency. Simmer 5 minutes.",
            "Egg masala: heat oil, sauté onions until deep golden (10 minutes - this gives the dhaba taste).",
            "Add ginger-garlic paste, then tomato puree. Cook until oil separates.",
            "Add spice powders and salt with ½ cup water. Simmer to a thick masala.",
            "Place the egg halves yolk-side up, spoon the masala over and simmer 3 minutes. Add coriander.",
        ],
    ),
    "Egg Podimas with Paruppu Rasam": R(
        "30 min",
        [
            "Podimas: 6 eggs, 2 onions finely chopped, 1 green chilli, ½ tsp pepper, ¼ tsp turmeric, curry leaves, 1 tbsp oil, salt",
            "Paruppu rasam: ¼ cup toor dal cooked and mashed, small gooseberry-size tamarind in 2 cups water, 2 tomatoes, 1 tsp rasam powder (home-made), salt",
            "Tempering: 1 tsp ghee, mustard, cumin, asafoetida, curry leaves, coriander",
        ],
        [
            "Rasam: boil tamarind water with crushed tomatoes, rasam powder and salt for 8 minutes.",
            "Add the mashed dal and 1½ cups water. Heat until it froths; do not boil hard. Temper and add coriander.",
            "Podimas: heat oil, add curry leaves, onion and chilli; sauté until soft.",
            "Add turmeric, salt and the beaten eggs. Stir continuously on medium until scrambled into small crumbs.",
            "Finish with pepper. Serve with rice or millet and rasam.",
        ],
    ),
    # ---------------- Mutton (max once a week) ----------------
    "Madurai Mutton Kola Urundai Kuzhambu": R(
        "1 h 15 min",
        [
            "Kola urundai: 400 g lean mutton mince, ¼ cup roasted gram powdered, 2 tbsp grated coconut, 1 small onion, 1 tsp fennel, 1-inch ginger, 3 garlic, 1 green chilli, coriander and mint, salt",
            "Gravy: 15 shallots, 2 tomatoes, 1 tsp ginger-garlic paste, 1 tsp kashmiri chilli, 2 tsp coriander powder, ½ tsp turmeric",
            "Paste: ½ cup coconut, 1 tsp fennel, 5 cashews",
            "3 tbsp gingelly oil, cinnamon, 2 cloves, curry leaves, salt",
        ],
        [
            "Pressure-cook the mince with salt and ¼ cup water for 3 whistles. Drain fully and cool (keep the stock for the gravy).",
            "Grind onion, fennel, ginger, garlic and chilli coarsely. Mix with the cooked mince, roasted gram powder, coconut, herbs and salt. Grind once more so it binds.",
            "Shape into lime-size balls. Steam 10 minutes so they stay firm.",
            "Gravy: heat oil, add whole spices and curry leaves, then shallots until golden. Add ginger-garlic paste and tomatoes and cook until mushy.",
            "Add spice powders, the coconut paste, the mutton stock and 1 cup water. Simmer 10 minutes.",
            "Add the kola urundai, simmer 5 minutes on low. Swirl, do not stir.",
        ],
        tip=KID_MILD,
    ),
    "Mutton Elumbu Kuzhambu with Vegetables": R(
        "1 h 30 min (or bones cooked the night before)",
        [
            "300 g mutton bones + 200 g lean mutton pieces, ½ tsp turmeric, salt",
            "2 drumsticks cut, 2 potatoes cubed, 2 tomatoes, 15 shallots, 1 tbsp ginger-garlic paste",
            "Masala: 1 tsp kashmiri chilli, 2 tsp coriander powder, 1 tsp pepper, 1 tsp fennel, ½ cup coconut ground smooth",
            "2 tbsp gingelly oil, cinnamon, cloves, curry leaves, coriander",
        ],
        [
            "Pressure-cook bones and mutton with turmeric, salt and 3 cups water for 8-10 whistles until soft. Keep the stock.",
            "Heat oil, add whole spices and curry leaves, then shallots and ginger-garlic paste. Add tomatoes and cook soft.",
            "Add chilli and coriander powder, then the drumstick and potato. Stir 2 minutes.",
            "Add the mutton with all the stock. Simmer 15 minutes until the vegetables are cooked.",
            "Add the coconut-pepper-fennel paste and simmer 5 minutes more.",
        ],
        tip="Skim the fat from the top of the stock after cooking to keep it lean.",
    ),
    # ---------------- Dal / vegetarian ----------------
    "Drumstick Sambar with Tomato Rasam": R(
        "45 min",
        [
            "Sambar: ½ cup toor dal, 2 drumsticks, 10 shallots, 1 tomato, gooseberry-size tamarind, 1½ tbsp sambar powder, ¼ tsp turmeric, salt",
            "Rasam: 3 tomatoes, small piece tamarind, 1 tsp pepper, 1 tsp cumin, 4 garlic, 1 tsp rasam powder, salt, coriander",
            "Tempering for each: 1 tsp ghee or oil, mustard, cumin, asafoetida, curry leaves",
        ],
        [
            "Pressure-cook toor dal with turmeric, 4 whistles; mash. Keep 2 tbsp dal water for the rasam.",
            "Sambar: boil drumstick, shallots and tomato in tamarind water with sambar powder and salt for 10 minutes.",
            "Add the dal and 1 cup water; simmer 5 minutes. Temper.",
            "Rasam: crush pepper, cumin and garlic. Boil with mashed tomatoes, tamarind water, rasam powder and salt for 8 minutes.",
            "Add the dal water and 1 cup water, heat until frothy. Temper and add coriander.",
        ],
    ),
    "Keerai Masiyal with Paruppu and Ghee": R(
        "30 min",
        [
            "Masiyal: 2 bunches amaranth (mulai/arai keerai), washed and chopped; 4 garlic; 1 green chilli; ½ tsp cumin; salt",
            "Paruppu: ½ cup moong dal, ¼ tsp turmeric, salt",
            "Tempering: 2 tsp ghee, ½ tsp mustard, 1 tsp urad dal, 1 dry red chilli",
        ],
        [
            "Cook the greens with garlic, chilli, cumin and ¼ cup water, open, for 6-8 minutes until soft. Keep the green colour - do not overcook.",
            "Mash with a wooden masher (or pulse once) and add salt.",
            "Pressure-cook moong dal with turmeric, 3 whistles. Mash with salt.",
            "Temper mustard, urad dal and red chilli in ghee and pour over the masiyal.",
            "Serve rice with paruppu and a spoon of ghee first, then masiyal.",
        ],
    ),
    "Mor Kuzhambu with Paruppu Usili": R(
        "40 min",
        [
            "Mor kuzhambu: 2 cups thick curd (slightly sour), 2 cups ash gourd cubes, ¼ tsp turmeric, salt",
            "Paste: ½ cup coconut, 1 tbsp toor dal + 1 tsp rice (soaked 30 min), 1 tsp cumin, 1 green chilli, small piece ginger",
            "Tempering: 1 tsp coconut oil, mustard, fenugreek, 1 dry red chilli, curry leaves",
            C.USILI_ING,
        ],
        [
            "Grind the paste ingredients smooth with a little water.",
            "Cook ash gourd with turmeric, salt and ½ cup water until soft.",
            "Whisk curd with the paste and ½ cup water until smooth.",
            "Pour into the ash gourd and heat on low, stirring, until it just begins to bubble. Switch off at once - boiling splits the curd.",
            "Temper and pour over.",
            *C.USILI_STEPS,
        ],
    ),
    "Chow Chow Kootu with Pepper Rasam": R(
        "35 min",
        [
            "Kootu: 2 chow chow (chayote), peeled and cubed; ⅓ cup moong dal; ¼ tsp turmeric; salt",
            "Paste: ¼ cup coconut, 1 tsp cumin, ½ tsp pepper, 1 dry red chilli",
            "Tempering: 1 tsp coconut oil, mustard, urad dal, curry leaves",
            C.PEPPER_RASAM_ING,
        ],
        [
            "Cook moong dal with turmeric until soft (3 whistles). Keep 2 tbsp of the dal water for the rasam.",
            "Cook chow chow with salt and ½ cup water until tender.",
            "Grind the paste and add to the vegetable with the dal. Simmer 5 minutes to a thick, creamy kootu.",
            "Temper and pour over.",
            *C.PEPPER_RASAM_STEPS,
        ],
    ),
    "Channa Kuzhambu with Vegetable Poriyal": R(
        "Soak overnight; 45 min",
        [
            "1 cup chickpeas (kondaikadalai), soaked overnight",
            "2 onions, 2 tomatoes, 1 tbsp ginger-garlic paste, 1 tsp kashmiri chilli, 2 tsp coriander powder, ½ tsp garam masala, ¼ tsp turmeric",
            "Paste: ¼ cup coconut, 1 tsp fennel, 5 cashews",
            "2 tbsp oil, cinnamon, 2 cloves, curry leaves, salt, coriander",
            "Cabbage-carrot poriyal: 3 cups shredded cabbage, 1 carrot grated, 3 tbsp coconut, salt; 1 tbsp oil, mustard, urad dal, curry leaves",
        ],
        [
            "Pressure-cook the chickpeas with salt, 5-6 whistles, until soft.",
            "Heat oil, add whole spices and curry leaves, then onions until golden. Add ginger-garlic paste and tomatoes and cook until mushy.",
            "Add the spice powders and cook 1 minute.",
            "Add the chickpeas with their water and the coconut paste. Simmer 10 minutes, mashing a few chickpeas to thicken.",
            "Finish with coriander.",
            "Poriyal: temper mustard, urad dal and curry leaves; add cabbage, carrot and salt and cook open 6-7 minutes. Toss in the coconut.",
        ],
    ),
}
