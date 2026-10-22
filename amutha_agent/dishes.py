"""Amutha's dish catalogue.

Every dish is home-made, Indian (mostly Tamil / Madurai style), free of beef,
pork, cheese, outside mayonnaise and processed foods. Each dish carries the
tags the planner and the rule checker need:

* ``rice``   - how much rice it adds to the day (0 none, 1 a little, 2 a rice base)
* ``spice``  - 1 mild, 2 medium (still child-safe). Nothing hotter is listed.
* ``maida``  - True only for the fortnightly Madurai treat dishes.
* ``protein``- fish / chicken / egg / mutton / dal / veg
* ``kid_hook`` - why a junk-food-loving teenager will actually eat it.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Dish:
    name: str
    tamil: str
    slot: str
    ingredients: tuple[str, ...]
    nutrition: str
    kid_hook: str = ""
    protein: str = "veg"
    rice: int = 0
    spice: int = 1
    maida: bool = False
    cuisine: str = "tamil"
    one_pot: bool = False
    prep_ahead: str = ""
    months: tuple[int, ...] = field(default=tuple(range(1, 13)))


def _d(*args, **kwargs) -> Dish:
    kwargs["ingredients"] = tuple(kwargs["ingredients"])
    if "months" in kwargs:
        kwargs["months"] = tuple(kwargs["months"])
    return Dish(*args, **kwargs)


# --------------------------------------------------------------------------
# Morning tiffin
# --------------------------------------------------------------------------
BREAKFAST = [
    _d("Ragi Dosa with Peanut-Tomato Chutney", "கேழ்வரகு தோசை", "breakfast",
       ingredients=["ragi flour", "urad dal", "onion", "peanut", "tomato", "curry leaves"],
       nutrition="Calcium and iron from ragi; protein and good fats from peanut.",
       kid_hook="Make it thin and crispy like a 'chocolate-coloured' roast dosa.",
       prep_ahead="Mix ragi-urad batter tonight and let it ferment."),
    _d("Kuthiraivali Millet Idli with Drumstick Sambar", "குதிரைவாலி இட்லி", "breakfast",
       ingredients=["barnyard millet", "urad dal", "toor dal", "drumstick", "tomato", "sambar powder"],
       nutrition="Low-GI millet with high fibre; sambar adds protein and vitamins.",
       kid_hook="Serve as mini button idlis floating in sambar - easy to finish.",
       spice=2, prep_ahead="Soak millet and urad dal in the morning, grind and ferment overnight."),
    _d("Paasi Payaru Dosa with Ginger Chutney", "பாசிப்பயறு தோசை", "breakfast",
       ingredients=["green gram", "ginger", "green chilli", "onion", "coconut"],
       nutrition="Very high plant protein and folate, easy to digest.",
       kid_hook="Roll it like a wrap with a little ghee and onion filling.",
       protein="dal", prep_ahead="Soak whole green gram overnight."),
    _d("Adai with Avial", "அடை அவியல்", "breakfast",
       ingredients=["rice", "chana dal", "toor dal", "urad dal", "coconut", "carrot", "beans", "curd"],
       nutrition="Four-dal protein punch; avial gives mixed vegetables and probiotic curd.",
       kid_hook="Make small thick 'adai pancakes' with jaggery on the side.",
       protein="dal", rice=1, spice=2, prep_ahead="Soak rice and dals for adai tonight."),
    _d("Thinai Pongal with Sambar and Coconut Chutney", "தினை பொங்கல்", "breakfast",
       ingredients=["foxtail millet", "moong dal", "pepper", "cumin", "ghee", "cashew", "coconut"],
       nutrition="Foxtail millet is rich in magnesium and fibre; moong adds protein.",
       kid_hook="Top with ghee-roasted cashews - they love the crunch."),
    _d("Vegetable Rava Upma with Coconut Chutney", "காய்கறி உப்புமா", "breakfast",
       ingredients=["wheat rava", "carrot", "beans", "peas", "onion", "coconut", "curry leaves"],
       nutrition="Quick energy with lots of vegetables; coconut gives healthy fats.",
       kid_hook="Shape into cups with a katori and add colourful veg - looks like a cafe dish."),
    _d("Idiyappam with Vegetable Kurma", "இடியாப்பம் குருமா", "breakfast",
       ingredients=["rice flour", "coconut milk", "carrot", "potato", "peas", "beans", "fennel"],
       nutrition="Steamed, light and oil-free; kurma adds vegetables.",
       kid_hook="Call it 'Tamil noodles' - same fun as noodles, zero packet masala.",
       rice=1),
    _d("Muttai Dosa with Tomato Chutney", "முட்டை தோசை", "breakfast",
       ingredients=["dosa batter", "egg", "onion", "pepper", "tomato", "garlic"],
       nutrition="Egg adds complete protein, B12 and choline to a regular dosa.",
       kid_hook="Madurai street-style egg dosa - they will ask for a second one.",
       protein="egg", rice=1, prep_ahead="Make sure dosa batter is ready."),
    _d("Godhumai Dosa with Onion Chutney", "கோதுமை தோசை", "breakfast",
       ingredients=["whole wheat flour", "rice flour", "onion", "cumin", "shallots", "tamarind"],
       nutrition="Whole wheat fibre; no fermentation needed - a busy-day saver.",
       kid_hook="Make it lacy and crisp like a rava roast."),
    _d("Kambu Kuzhi Paniyaram with Coconut Chutney", "கம்பு குழிப்பணியாரம்", "breakfast",
       ingredients=["pearl millet", "urad dal", "onion", "carrot", "coriander", "coconut"],
       nutrition="Pearl millet gives iron and zinc; carrots add vitamin A.",
       kid_hook="Bite-size balls - serve with toothpicks like party snacks.",
       prep_ahead="Soak kambu and urad dal; grind and ferment overnight."),
    _d("Desi Pizza Uthappam with Mint Chutney", "காய்கறி ஊத்தப்பம்", "breakfast",
       ingredients=["dosa batter", "onion", "tomato", "capsicum", "carrot", "coriander", "mint"],
       nutrition="Colourful vegetables give vitamins A and C on a fermented base.",
       kid_hook="Looks just like a pizza - cut into slices, no cheese needed.",
       rice=1, prep_ahead="Keep dosa batter ready and chop toppings at night."),
    _d("Ragi Puttu with Banana and Coconut", "கேழ்வரகு புட்டு", "breakfast",
       ingredients=["ragi flour", "grated coconut", "banana", "palm jaggery", "cardamom"],
       nutrition="Calcium-rich ragi, potassium from banana, natural sweetness.",
       kid_hook="Sweet breakfast - feels like dessert in the morning."),
    _d("Soft Idli with Sambar and Two Chutneys", "இட்லி சாம்பார்", "breakfast",
       ingredients=["idli batter", "toor dal", "shallots", "tomato", "coconut", "coriander"],
       nutrition="Fermented, gut-friendly and steamed; sambar adds protein.",
       kid_hook="Make 'idli fry' cubes in a little ghee and podi for the lunchbox.",
       rice=1, spice=2, prep_ahead="Grind idli batter and let it ferment overnight."),
    _d("Aval Upma with Peanuts", "அவல் உப்புமா", "breakfast",
       ingredients=["red poha", "peanut", "onion", "curry leaves", "lemon", "turmeric"],
       nutrition="Red aval is iron-rich; peanuts add protein. Ready in 10 minutes.",
       kid_hook="Crunchy peanuts plus lemon - tastes like a chaat.", rice=1),
    _d("Egg Bhurji with Wheat Phulka", "முட்டை பொடிமாஸ்", "breakfast",
       ingredients=["egg", "onion", "tomato", "pepper", "whole wheat flour", "coriander"],
       nutrition="High-protein breakfast that keeps teenagers full till lunch.",
       kid_hook="Roll it up like an egg wrap - grab and go.",
       protein="egg", cuisine="indian"),
]

# --------------------------------------------------------------------------
# Lunch: protein main (kuzhambu / curry) by protein type
# --------------------------------------------------------------------------
LUNCH_MAIN = [
    # Fish
    _d("Madurai Meen Kuzhambu with Tawa Meen Varuval", "மதுரை மீன் குழம்பு", "lunch_main",
       ingredients=["seer fish", "tamarind", "shallots", "tomato", "gingelly oil", "fish masala (home-ground)"],
       nutrition="Omega-3 fats for brain and eyes; lean protein.",
       kid_hook="Give them the crispy tawa fish piece first - it opens the appetite.",
       protein="fish", spice=2, prep_ahead="Clean fish and marinate in turmeric, salt and lemon."),
    _d("Coconut Milk Fish Curry (mild)", "தேங்காய்ப்பால் மீன் குழம்பு", "lunch_main",
       ingredients=["pomfret", "coconut milk", "tomato", "ginger", "green chilli", "curry leaves"],
       nutrition="Omega-3 rich fish in a mild coconut gravy - gentle on young tongues.",
       kid_hook="Mild and creamy - perfect for kids who complain about spice.",
       protein="fish"),
    _d("Nethili Meen Kuzhambu with Nethili Fry", "நெத்திலி குழம்பு", "lunch_main",
       ingredients=["anchovy", "tamarind", "shallots", "garlic", "tomato", "rice flour"],
       nutrition="Anchovies eaten with bones = superb calcium and omega-3.",
       kid_hook="Crispy nethili fry is Tamil 'fish chips' - addictive.",
       protein="fish", spice=2),
    _d("Fish Kola Urundai Kuzhambu", "மீன் கோலா உருண்டை", "lunch_main",
       ingredients=["fish fillet", "roasted gram", "onion", "fennel", "coconut", "tomato"],
       nutrition="Fish balls give lean protein; roasted gram adds more protein.",
       kid_hook="Home-made 'fish nuggets' in gravy - no bones to fuss about.",
       protein="fish"),
    _d("Vanjaram Fish Fry with Pepper Rasam and Paruppu", "வஞ்சிரம் வறுவல்", "lunch_main",
       ingredients=["seer fish", "pepper", "ginger-garlic paste", "lemon", "toor dal", "tomato"],
       nutrition="Shallow-fried seer fish with dal = complete protein meal.",
       kid_hook="Fish fry steak - like restaurant tawa fish, cooked at home.",
       protein="fish", prep_ahead="Marinate fish slices overnight in the fridge."),
    # Chicken
    _d("Chettinad Chicken Kuzhambu (kid-mild)", "செட்டிநாடு கோழி குழம்பு", "lunch_main",
       ingredients=["country chicken", "shallots", "tomato", "pepper", "fennel", "coconut"],
       nutrition="High-quality protein; pepper and fennel aid digestion.",
       kid_hook="Same Chettinad aroma, fewer chillies - temper extra chilli for adults only.",
       protein="chicken", spice=2),
    _d("Milagu Kozhi Varuval with Rasam and Paruppu", "மிளகு கோழி வறுவல்", "lunch_main",
       ingredients=["chicken", "black pepper", "curry leaves", "shallots", "toor dal", "tomato"],
       nutrition="Lean chicken protein with immunity-boosting pepper.",
       kid_hook="Dry pepper chicken bites - like a starter, but it's lunch.",
       protein="chicken", spice=2),
    _d("Home-made Chicken 65 (air-fried) with Keerai Paruppu", "சிக்கன் 65", "lunch_main",
       ingredients=["chicken", "curd", "ginger-garlic paste", "kashmiri chilli", "rice flour", "spinach", "moong dal"],
       nutrition="All the Chicken 65 taste with hardly any oil; keerai paruppu adds iron.",
       kid_hook="Their favourite hotel starter - but home-made, no colour, no ajinomoto.",
       protein="chicken", spice=2, prep_ahead="Marinate chicken in curd and spices overnight."),
    _d("Chicken Kurma with Coconut and Cashew", "கோழி குருமா", "lunch_main",
       ingredients=["chicken", "coconut", "cashew", "fennel", "onion", "tomato", "mint"],
       nutrition="Protein with healthy fats from coconut and cashew.",
       kid_hook="Rich and creamy - great with phulka or millet rice.",
       protein="chicken"),
    _d("Seeraga Samba Chicken Biryani (more chicken, less rice) with Onion Raita",
       "சீரக சம்பா கோழி பிரியாணி", "lunch_main",
       ingredients=["seeraga samba rice", "chicken", "curd", "mint", "coriander", "onion", "carrot", "beans"],
       nutrition="Half the usual rice, double chicken and vegetables; raita adds probiotics.",
       kid_hook="It's BIRYANI - the one word every teenager says yes to.",
       protein="chicken", rice=2, spice=2, one_pot=True,
       prep_ahead="Marinate chicken in curd, mint and biryani masala overnight."),
    # Egg
    _d("Muttai Kuzhambu with Beans Paruppu Usili", "முட்டை குழம்பு", "lunch_main",
       ingredients=["egg", "tamarind", "shallots", "tomato", "coconut", "beans", "toor dal"],
       nutrition="Eggs give complete protein and vitamin D.",
       kid_hook="Fry the boiled eggs with turmeric till golden before adding to the gravy.",
       protein="egg", spice=2),
    _d("Egg Masala with Dal Fry", "முட்டை மசாலா", "lunch_main",
       ingredients=["egg", "onion", "tomato", "garam masala", "toor dal", "garlic"],
       nutrition="Protein-packed combo of egg and dal.",
       kid_hook="Thick dhaba-style masala - they will wipe the plate.",
       protein="egg", cuisine="indian", spice=2),
    _d("Egg Podimas with Paruppu Rasam", "முட்டை பொடிமாஸ் ரசம்", "lunch_main",
       ingredients=["egg", "onion", "pepper", "toor dal", "tomato", "tamarind"],
       nutrition="Easy protein; rasam helps digestion.",
       kid_hook="Scrambled eggs, Tamil style - quick and loved.",
       protein="egg"),
    # Mutton (planner keeps this to max once a week)
    _d("Madurai Mutton Kola Urundai Kuzhambu", "மதுரை மட்டன் கோலா உருண்டை", "lunch_main",
       ingredients=["lean mutton mince", "roasted gram", "coconut", "fennel", "shallots", "tomato"],
       nutrition="Iron and B12 from mutton - kept to once a week at most.",
       kid_hook="Madurai's famous kola urundai - meatballs they will fight over.",
       protein="mutton", spice=2, prep_ahead="Buy fresh lean mutton mince and keep in the fridge."),
    _d("Mutton Elumbu Kuzhambu with Vegetables", "மட்டன் எலும்பு குழம்பு", "lunch_main",
       ingredients=["mutton bones", "lean mutton", "drumstick", "potato", "tomato", "shallots"],
       nutrition="Bone broth gives collagen and minerals; vegetables balance the meal.",
       kid_hook="Slow-cooked, soft meat that falls off the bone.",
       protein="mutton", spice=2, prep_ahead="Pressure-cook mutton bones the night before."),
    # Dal / vegetarian
    _d("Drumstick Sambar with Tomato Rasam", "முருங்கைக்காய் சாம்பார்", "lunch_main",
       ingredients=["toor dal", "drumstick", "shallots", "tomato", "tamarind", "sambar powder"],
       nutrition="Classic protein and fibre; drumstick is rich in vitamin C and calcium.",
       kid_hook="Serve with crispy vazhakkai roast on the side.",
       protein="dal", spice=2),
    _d("Keerai Masiyal with Paruppu and Ghee", "கீரை மசியல் பருப்பு", "lunch_main",
       ingredients=["amaranth greens", "moong dal", "garlic", "cumin", "ghee"],
       nutrition="Iron, folate and calcium from greens with dal protein.",
       kid_hook="A spoon of ghee and garlic tadka makes greens taste rich.",
       protein="dal"),
    _d("Mor Kuzhambu with Paruppu Usili", "மோர் குழம்பு", "lunch_main",
       ingredients=["curd", "coconut", "ash gourd", "toor dal", "chana dal", "beans"],
       nutrition="Probiotic curd plus dal protein - cooling and gut-friendly.",
       kid_hook="Tangy and mild - pair it with crispy vazhakkai roast.",
       protein="dal"),
    _d("Chow Chow Kootu with Pepper Rasam", "சௌ சௌ கூட்டு", "lunch_main",
       ingredients=["chayote", "moong dal", "coconut", "pepper", "tomato", "tamarind"],
       nutrition="Light, high-fibre vegetable and dal combination.",
       kid_hook="Pair with a crunchy side so the meal has 'crunch + soft'.",
       protein="dal"),
    _d("Channa Kuzhambu with Vegetable Poriyal", "கொண்டைக்கடலை குழம்பு", "lunch_main",
       ingredients=["chickpeas", "onion", "tomato", "coconut", "fennel", "garlic"],
       nutrition="Chickpeas give protein, fibre and iron.",
       kid_hook="Tastes like chole - North Indian taste with Tamil masala.",
       protein="dal", spice=2, prep_ahead="Soak chickpeas overnight."),
]

# Small carb base for lunch. Rice is kept to a half cup per person.
LUNCH_BASE = [
    _d("Ponni Rice - half cup per person", "பொன்னி சாதம் (அரை கப்)", "lunch_base",
       ingredients=["ponni rice"], nutrition="Small portion; fill the rest of the plate with veg and protein.",
       rice=2),
    _d("Hand-pound Red Rice - half cup per person", "கைக்குத்தல் அரிசி (அரை கப்)", "lunch_base",
       ingredients=["hand-pound rice"], nutrition="More fibre and B vitamins than polished rice.",
       rice=2),
    _d("Kuthiraivali (Barnyard Millet) Rice", "குதிரைவாலி சாதம்", "lunch_base",
       ingredients=["barnyard millet"], nutrition="Looks like rice, five times the fibre, low GI.",
       kid_hook="Looks exactly like rice - most kids will not notice."),
    _d("Varagu (Kodo Millet) Rice", "வரகு சாதம்", "lunch_base",
       ingredients=["kodo millet"], nutrition="Rich in antioxidants and fibre; keeps energy steady."),
    _d("Samai (Little Millet) Rice", "சாமை சாதம்", "lunch_base",
       ingredients=["little millet"], nutrition="Iron-rich millet that cooks just like rice."),
    _d("Soft Wheat Phulka (2-3 per person)", "புல்கா சப்பாத்தி", "lunch_base",
       ingredients=["whole wheat flour"], nutrition="Oil-free whole wheat, good fibre.",
       cuisine="indian", kid_hook="Fresh off the flame and puffed up - fun to watch."),
]

LUNCH_SIDE = [
    _d("Beans Poriyal", "பீன்ஸ் பொரியல்", "lunch_side",
       ingredients=["beans", "coconut", "mustard", "urad dal"], nutrition="Fibre and vitamin K."),
    _d("Cabbage-Carrot Poriyal", "முட்டைகோஸ் கேரட் பொரியல்", "lunch_side",
       ingredients=["cabbage", "carrot", "coconut", "green chilli"], nutrition="Vitamin A and C."),
    _d("Beetroot Poriyal", "பீட்ரூட் பொரியல்", "lunch_side",
       ingredients=["beetroot", "coconut", "curry leaves"], nutrition="Folate and natural nitrates for stamina.",
       kid_hook="Bright pink colour - call it 'pink poriyal'."),
    _d("Vazhakkai Roast", "வாழைக்காய் வறுவல்", "lunch_side",
       ingredients=["raw banana", "chilli powder", "rice flour", "gingelly oil"],
       nutrition="Resistant starch and potassium.",
       kid_hook="Crispy like chips - the healthy answer to a packet of chips."),
    _d("Avarakkai Poriyal", "அவரைக்காய் பொரியல்", "lunch_side",
       ingredients=["broad beans", "coconut", "mustard"], nutrition="Plant protein and fibre."),
    _d("Vendakkai Crispy Fry", "வெண்டைக்காய் வறுவல்", "lunch_side",
       ingredients=["okra", "besan", "chilli powder", "gingelly oil"],
       nutrition="Soluble fibre; good for gut and focus.",
       kid_hook="Crispy okra fingers - no sliminess."),
    _d("Kovakkai Fry", "கோவைக்காய் வறுவல்", "lunch_side",
       ingredients=["ivy gourd", "sambar powder", "gingelly oil"], nutrition="Helps keep blood sugar steady."),
    _d("Carrot-Peas Poriyal", "கேரட் பட்டாணி பொரியல்", "lunch_side",
       ingredients=["carrot", "green peas", "coconut"], nutrition="Vitamin A and plant protein.",
       kid_hook="Sweet and colourful - a safe choice for fussy eaters."),
    _d("Cauliflower Pepper Fry", "காலிஃபிளவர் மிளகு வறுவல்", "lunch_side",
       ingredients=["cauliflower", "pepper", "onion", "curry leaves"], nutrition="Vitamin C and fibre.",
       kid_hook="Tastes like gobi 65 but roasted, not deep fried."),
    _d("Murungai Keerai Poriyal", "முருங்கைக்கீரை பொரியல்", "lunch_side",
       ingredients=["drumstick leaves", "coconut", "moong dal"], nutrition="A superfood - iron, calcium and vitamin A."),
    _d("Pudalangai Kootu", "புடலங்காய் கூட்டு", "lunch_side",
       ingredients=["snake gourd", "moong dal", "coconut", "cumin"], nutrition="Hydrating and high in fibre."),
    _d("Mixed Vegetable Thoran", "காய்கறி தோரன்", "lunch_side",
       ingredients=["carrot", "beans", "cabbage", "coconut", "shallots"], nutrition="Many vegetables in one side."),
]

# --------------------------------------------------------------------------
# Night tiffin
# --------------------------------------------------------------------------
DINNER = [
    _d("Phulka with Channa Masala", "சப்பாத்தி சன்னா", "dinner",
       ingredients=["whole wheat flour", "chickpeas", "onion", "tomato", "garam masala"],
       nutrition="Whole wheat and chickpea protein.",
       kid_hook="Restaurant 'chole roti' at home.", protein="dal", cuisine="indian", spice=2,
       prep_ahead="Soak chickpeas in the morning."),
    _d("Egg Kothu Chapati", "முட்டை கொத்து சப்பாத்தி", "dinner",
       ingredients=["whole wheat chapati", "egg", "onion", "tomato", "cabbage", "carrot", "salna"],
       nutrition="Uses wheat chapati instead of maida parotta; egg and vegetables add nutrition.",
       kid_hook="Madurai kothu parotta sound and taste - made with healthy chapati.",
       protein="egg", spice=2),
    _d("Millet Masala Dosa with Potato-Carrot Masala", "சிறுதானிய மசாலா தோசை", "dinner",
       ingredients=["millet dosa batter", "potato", "carrot", "onion", "peas", "ginger"],
       nutrition="Millet base with a vegetable-rich filling.",
       kid_hook="Hotel-style crispy masala dosa - a favourite.", rice=1),
    _d("Chapati with Mixed Vegetable Kurma", "சப்பாத்தி வெஜ் குருமா", "dinner",
       ingredients=["whole wheat flour", "carrot", "beans", "peas", "potato", "coconut", "fennel"],
       nutrition="Many vegetables in a mild coconut gravy.",
       kid_hook="Mild hotel kurma - goes down easily."),
    _d("Chicken Chapati Roll with Mint-Curd Dip", "சிக்கன் சப்பாத்தி ரோல்", "dinner",
       ingredients=["whole wheat chapati", "chicken", "onion", "capsicum", "curd", "mint", "cucumber"],
       nutrition="Lean protein wrap; home-made curd dip instead of shop mayonnaise.",
       kid_hook="Shawarma / frankie style roll - the junk-food craving, solved at home.",
       protein="chicken", cuisine="indian", spice=2,
       prep_ahead="Marinate chicken strips in curd and spices; hang curd for the dip."),
    _d("Idli with Nattu Kozhi Kuzhambu", "இட்லி நாட்டுக்கோழி குழம்பு", "dinner",
       ingredients=["idli batter", "country chicken", "shallots", "pepper", "fennel", "tomato"],
       nutrition="Light fermented idli with high-protein country chicken gravy.",
       kid_hook="Weekend-style idli-kozhi combo on a weekday.",
       protein="chicken", rice=1, spice=2, prep_ahead="Keep idli batter ready."),
    _d("Samai Vegetable Kichadi with Raita", "சாமை கிச்சடி", "dinner",
       ingredients=["little millet", "moong dal", "carrot", "beans", "peas", "curd", "cucumber"],
       nutrition="One-pot millet, dal and vegetables - a complete light dinner.",
       kid_hook="Top with crispy fried onions (home-made) and ghee.", protein="dal"),
    _d("Vegetable Wheat Paratha with Curd", "காய்கறி பராத்தா", "dinner",
       ingredients=["whole wheat flour", "carrot", "cabbage", "potato", "coriander", "curd"],
       nutrition="Vegetables hidden inside whole wheat.",
       kid_hook="Stuffed paratha with a dollop of butter (home-made) - very filling.",
       cuisine="indian"),
    _d("Appam with Vegetable Stew", "ஆப்பம் வெஜ் ஸ்டூ", "dinner",
       ingredients=["appam batter", "coconut milk", "potato", "carrot", "beans", "pepper"],
       nutrition="Fermented appam with a mild coconut stew.",
       kid_hook="Lacy appam with a soft centre - slightly sweet, kids love it.",
       rice=1, prep_ahead="Grind appam batter and ferment overnight."),
    _d("Masala Kuzhi Paniyaram with Tomato Chutney", "குழிப்பணியாரம்", "dinner",
       ingredients=["idli batter", "onion", "carrot", "coriander", "tomato", "curry leaves"],
       nutrition="Uses leftover batter, packed with vegetables.",
       kid_hook="Crispy outside, soft inside - like Indian 'pop bites'.", rice=1),
    _d("Egg Curry with Phulka", "முட்டை கறி புல்கா", "dinner",
       ingredients=["egg", "onion", "tomato", "coconut", "whole wheat flour"],
       nutrition="Protein-rich dinner, light on oil.",
       kid_hook="Cut eggs in half so the yolk soaks the gravy.", protein="egg", spice=2),
    _d("Jowar Roti with Dal Tadka", "சோள ரொட்டி பருப்பு", "dinner",
       ingredients=["jowar flour", "toor dal", "garlic", "cumin", "ghee", "tomato"],
       nutrition="Gluten-free jowar with dal protein.",
       kid_hook="Garlic-ghee tadka on dal - restaurant dal fry taste.", protein="dal", cuisine="indian"),
    _d("Ragi Idiyappam with Coconut Milk and Egg Roast", "கேழ்வரகு இடியாப்பம்", "dinner",
       ingredients=["ragi flour", "coconut milk", "egg", "onion", "pepper"],
       nutrition="Calcium-rich ragi plus egg protein.",
       kid_hook="Brown 'Tamil noodles' with a spicy-sweet egg roast.", protein="egg"),
    _d("Wheat Rava Kichadi with Coconut Chutney", "கோதுமை ரவா கிச்சடி", "dinner",
       ingredients=["broken wheat", "carrot", "beans", "peas", "onion", "coconut", "ghee"],
       nutrition="Broken wheat is whole grain - high in fibre.",
       kid_hook="Hotel kichadi with lots of ghee and cashew."),
]

# --------------------------------------------------------------------------
# The fortnightly Madurai treat - the ONLY maida dishes in the catalogue.
# The planner allows exactly one of these every 14 days.
# --------------------------------------------------------------------------
MAIDA_TREAT = [
    _d("Treat Night: Madurai Chicken Kothu Parotta (home-made)", "மதுரை சிக்கன் கொத்து பரோட்டா", "dinner",
       ingredients=["maida", "chicken", "egg", "onion", "tomato", "salna", "cabbage", "carrot"],
       nutrition="Once-in-two-weeks treat; loaded with chicken, egg and vegetables to balance it.",
       kid_hook="The real Madurai street-food treat - celebrate it as their reward night.",
       protein="chicken", maida=True, spice=2,
       prep_ahead="Make parotta dough with a little whole wheat mixed in and rest it overnight."),
    _d("Treat Night: Madurai Bun Parotta with Vegetable Salna", "மதுரை பன் பரோட்டா", "dinner",
       ingredients=["maida", "whole wheat flour", "carrot", "beans", "peas", "coconut", "onion"],
       nutrition="Once-in-two-weeks treat; vegetable salna adds fibre.",
       kid_hook="Fluffy Madurai bun parotta - a treat they will wait two weeks for.",
       maida=True, spice=2, prep_ahead="Make parotta dough and rest it overnight."),
    _d("Treat Night: Egg Veechu Parotta with Chicken Salna", "முட்டை வீச்சு பரோட்டா", "dinner",
       ingredients=["maida", "egg", "onion", "chicken", "tomato", "coconut"],
       nutrition="Once-in-two-weeks treat with egg and chicken protein.",
       kid_hook="Madurai veechu parotta - flaky, eggy and special.",
       protein="chicken", maida=True, spice=2, prep_ahead="Make parotta dough and rest it overnight."),
]

# --------------------------------------------------------------------------
# Daily soup for the children (evening, mild)
# --------------------------------------------------------------------------
SOUP = [
    _d("Murungai Keerai Soup", "முருங்கைக்கீரை சூப்", "soup",
       ingredients=["drumstick leaves", "moong dal water", "garlic", "pepper", "cumin"],
       nutrition="Iron, calcium and vitamin A - a Tamil superfood soup."),
    _d("Fresh Tomato Soup with Croutons of Roasted Chapati", "தக்காளி சூப்", "soup",
       ingredients=["tomato", "carrot", "garlic", "pepper", "butter", "whole wheat chapati"],
       nutrition="Lycopene and vitamin C; chapati croutons instead of bread.",
       kid_hook="Crunchy chapati croutons make it feel like a cafe soup."),
    _d("Sweet Corn Vegetable Soup", "ஸ்வீட் கார்ன் சூப்", "soup",
       ingredients=["fresh sweet corn", "carrot", "beans", "spring onion", "pepper"],
       nutrition="Fibre and vitamins from fresh corn - no packet soup powder.",
       kid_hook="Restaurant-style corn soup, made from fresh corn."),
    _d("Kozhi Rasam (Chicken Clear Soup)", "கோழி ரசம்", "soup",
       ingredients=["chicken bones", "pepper", "garlic", "tomato", "coriander"],
       nutrition="Protein-rich broth; pepper and garlic boost immunity.",
       protein="chicken", spice=2),
    _d("Mushroom Pepper Soup", "காளான் மிளகு சூப்", "soup",
       ingredients=["fresh mushroom", "onion", "pepper", "garlic", "milk"],
       nutrition="Vitamin D and B vitamins from mushrooms."),
    _d("Carrot-Ginger Soup", "கேரட் இஞ்சி சூப்", "soup",
       ingredients=["carrot", "ginger", "onion", "pepper"], nutrition="Very high vitamin A for eyes.",
       kid_hook="Bright orange and slightly sweet."),
    _d("Pumpkin Coconut Soup", "பூசணி சூப்", "soup",
       ingredients=["yellow pumpkin", "coconut milk", "garlic", "pepper"],
       nutrition="Beta-carotene and potassium; creamy without cream.",
       kid_hook="Silky and sweet - tastes like a dessert soup."),
    _d("Mixed Vegetable Clear Soup", "காய்கறி சூப்", "soup",
       ingredients=["carrot", "beans", "cabbage", "spring onion", "pepper", "garlic"],
       nutrition="Light and hydrating with many vegetables."),
    _d("Moong Dal Soup", "பாசிப்பருப்பு சூப்", "soup",
       ingredients=["moong dal", "tomato", "cumin", "ghee", "lemon"],
       nutrition="Easy-to-digest protein soup.", protein="dal"),
    _d("Palak Soup", "பாலக் சூப்", "soup",
       ingredients=["spinach", "onion", "garlic", "milk", "pepper"],
       nutrition="Iron and folate - great for growing teenagers."),
    _d("Nandu Rasam (Crab Soup)", "நண்டு ரசம்", "soup",
       ingredients=["crab", "pepper", "garlic", "tomato", "tamarind", "coriander"],
       nutrition="Seafood protein, zinc and selenium; traditional cold-and-cough remedy.",
       protein="fish", spice=2),
    _d("Beetroot-Tomato 'Pink' Soup", "பீட்ரூட் சூப்", "soup",
       ingredients=["beetroot", "tomato", "garlic", "pepper", "lemon"],
       nutrition="Iron, folate and nitrates for stamina.",
       kid_hook="Call it 'pink soup' - teens love the colour for photos."),
]

# --------------------------------------------------------------------------
# Daily fruit or fresh juice (no added sugar, never packaged)
# --------------------------------------------------------------------------
FRUIT = [
    _d("Guava slices with a pinch of salt and pepper", "கொய்யா", "fruit",
       ingredients=["guava"], nutrition="More vitamin C than an orange.", months=[8, 9, 10, 11, 12, 1, 2]),
    _d("Papaya bowl with lime", "பப்பாளி", "fruit",
       ingredients=["papaya", "lime"], nutrition="Vitamin A and digestive enzymes."),
    _d("Rasthali / Nendran Banana", "வாழைப்பழம்", "fruit",
       ingredients=["banana"], nutrition="Potassium and quick energy before sports."),
    _d("Pomegranate pearls", "மாதுளை", "fruit",
       ingredients=["pomegranate"], nutrition="Antioxidants and iron support.",
       kid_hook="Serve ready-peeled in a glass - zero effort for them."),
    _d("Fresh Watermelon Juice (no sugar)", "தர்பூசணி ஜூஸ்", "fruit",
       ingredients=["watermelon", "mint", "lime"], nutrition="Hydration in hot Madurai summers.",
       months=[3, 4, 5, 6]),
    _d("Fresh Sathukudi (Mosambi) Juice", "சாத்துக்குடி ஜூஸ்", "fruit",
       ingredients=["sweet lime"], nutrition="Vitamin C for immunity."),
    _d("Apple slices with peanut butter (home-ground)", "ஆப்பிள்", "fruit",
       ingredients=["apple", "peanut"], nutrition="Fibre plus protein - keeps them full.",
       kid_hook="Home-ground peanut butter dip turns fruit into a snack."),
    _d("Mango slices", "மாம்பழம்", "fruit",
       ingredients=["mango"], nutrition="Vitamin A and C.", months=[4, 5, 6, 7]),
    _d("Sapota (Chikoo) Milkshake (no sugar)", "சப்போட்டா மில்க்ஷேக்", "fruit",
       ingredients=["sapota", "milk", "dates"], nutrition="Natural sweetness, fibre and calcium.",
       kid_hook="Thick milkshake sweetened only with dates - tastes like a cafe shake."),
    _d("Pineapple chunks with pepper", "அன்னாசி", "fruit",
       ingredients=["pineapple"], nutrition="Vitamin C and bromelain for digestion."),
    _d("Muskmelon Juice", "முலாம்பழம் ஜூஸ்", "fruit",
       ingredients=["muskmelon", "mint"], nutrition="Cooling and hydrating.", months=[3, 4, 5, 6, 7]),
    _d("Jackfruit pieces", "பலாப்பழம்", "fruit",
       ingredients=["jackfruit"], nutrition="Fibre and B vitamins - a Tamil summer treat.",
       months=[4, 5, 6, 7]),
    _d("Mixed fruit bowl with lime and chaat spice", "பழக் கலவை", "fruit",
       ingredients=["banana", "apple", "papaya", "pomegranate", "lime"],
       nutrition="Many colours = many vitamins.", kid_hook="Fruit chaat - tangy and fun."),
    _d("Orange segments", "ஆரஞ்சு", "fruit",
       ingredients=["orange"], nutrition="Vitamin C and folate.", months=[10, 11, 12, 1, 2, 3]),
    _d("Grapes", "திராட்சை", "fruit",
       ingredients=["black grapes"], nutrition="Antioxidants; freeze them for a 'popsicle' bite.",
       kid_hook="Frozen grapes = natural ice candy.", months=[1, 2, 3, 4, 5]),
]

# --------------------------------------------------------------------------
# After-school snack (healthy answers to junk food)
# --------------------------------------------------------------------------
SNACK = [
    _d("Channa Sundal with Coconut and Mango", "கொண்டைக்கடலை சுண்டல்", "snack",
       ingredients=["chickpeas", "coconut", "raw mango", "mustard"], nutrition="Plant protein and fibre.",
       protein="dal", prep_ahead="Soak chickpeas overnight for tomorrow's sundal."),
    _d("Home-made Ragi Murukku", "கேழ்வரகு முறுக்கு", "snack",
       ingredients=["ragi flour", "rice flour", "sesame", "butter"], nutrition="Calcium-rich crunchy snack.",
       kid_hook="Crunch like chips, but home-made with ragi."),
    _d("Baked Sweet Potato Masala Wedges", "சர்க்கரைவள்ளி கிழங்கு வெட்ஜஸ்", "snack",
       ingredients=["sweet potato", "chilli powder", "pepper", "olive oil"], nutrition="Fibre and vitamin A.",
       kid_hook="The healthy French-fries - serve with home-made tomato chutney as 'ketchup'."),
    _d("Air-fried Chicken Popcorn with Mint-Curd Dip", "சிக்கன் பாப்கார்ன்", "snack",
       ingredients=["chicken", "curd", "besan", "pepper", "mint"],
       nutrition="Lean protein snack - fast-food taste without the deep fryer.",
       kid_hook="KFC-style popcorn chicken at home - their junk craving, satisfied.",
       protein="chicken", spice=2),
    _d("Sweet Kozhukattai with Jaggery and Coconut", "கொழுக்கட்டை", "snack",
       ingredients=["rice flour", "coconut", "palm jaggery", "cardamom"], nutrition="Steamed sweet, no oil.",
       rice=1),
    _d("Roasted Makhana with Ghee and Pepper", "மக்கானா", "snack",
       ingredients=["fox nuts", "ghee", "pepper"], nutrition="Light, high-protein crunchy snack.",
       cuisine="indian", kid_hook="Popcorn-like crunch without the packet."),
    _d("Peanut-Jaggery Chikki (home-made)", "கடலை மிட்டாய்", "snack",
       ingredients=["peanut", "palm jaggery"], nutrition="Protein, iron and good fats.",
       kid_hook="Tamil 'candy bar' - better than any chocolate bar."),
    _d("Ellu Urundai (Sesame Balls)", "எள்ளு உருண்டை", "snack",
       ingredients=["sesame", "palm jaggery", "cardamom"], nutrition="Calcium and iron powerhouse."),
    _d("Masala Sweet Corn Cup", "மசாலா ஸ்வீட் கார்ன்", "snack",
       ingredients=["fresh sweet corn", "butter", "lime", "chilli powder"], nutrition="Fibre and energy.",
       kid_hook="Just like the mall corn cup."),
    _d("Ragi Laddu with Dates and Nuts", "கேழ்வரகு லட்டு", "snack",
       ingredients=["ragi flour", "dates", "almond", "ghee"], nutrition="Calcium, iron and healthy fats."),
    _d("Masala Vadai (shallow-fried, once a week)", "மசால் வடை", "snack",
       ingredients=["chana dal", "onion", "fennel", "curry leaves"], nutrition="Protein-rich lentil snack.",
       protein="dal", kid_hook="Tea-shop vadai at home.", prep_ahead="Soak chana dal for 3 hours before evening."),
    _d("Karamani Sundal with Carrot", "காராமணி சுண்டல்", "snack",
       ingredients=["black-eyed peas", "carrot", "coconut"], nutrition="Protein and folate.",
       protein="dal", prep_ahead="Soak karamani overnight."),
    _d("Pepper Egg Masala Bites", "முட்டை மசாலா", "snack",
       ingredients=["egg", "pepper", "chilli powder", "onion"], nutrition="Quick protein after school.",
       protein="egg"),
]

# Bedtime drink (helps sleep and calcium intake)
BEDTIME = [
    _d("Manjal Paal - turmeric pepper milk with palm jaggery", "மஞ்சள் பால்", "bedtime",
       ingredients=["milk", "turmeric", "pepper", "palm jaggery"], nutrition="Calcium plus anti-inflammatory turmeric."),
    _d("Ragi Malt with Milk", "கேழ்வரகு கஞ்சி", "bedtime",
       ingredients=["ragi flour", "milk", "palm jaggery", "cardamom"], nutrition="Calcium and iron before sleep."),
    _d("Home-made Badam Milk", "பாதாம் பால்", "bedtime",
       ingredients=["milk", "almond", "saffron", "cardamom"], nutrition="Protein, vitamin E and calcium.",
       kid_hook="Tastes like a dessert drink - zero packet powder.", prep_ahead="Soak almonds in the morning."),
    _d("Dates Milk", "பேரீச்சம்பழ பால்", "bedtime",
       ingredients=["milk", "dates"], nutrition="Iron and natural sweetness."),
    _d("Warm Milk with Nutmeg and Cardamom", "ஜாதிக்காய் பால்", "bedtime",
       ingredients=["milk", "nutmeg", "cardamom"], nutrition="Calcium; nutmeg helps relaxation."),
]

DAILY_HYDRATION = "Neer Mor (spiced buttermilk) with lunch and 6-8 glasses of water through the day."

ALL_DISHES = (
    BREAKFAST + LUNCH_MAIN + LUNCH_BASE + LUNCH_SIDE + DINNER + MAIDA_TREAT
    + SOUP + FRUIT + SNACK + BEDTIME
)
