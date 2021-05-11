from components.ai import HostileEnemy
from components.consumable import HealingConsumable
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

# small healing potions

open_front_unrounded_vowel = Item(
    char="Ω",
    color=(158, 48, 87),
    name="Open Front Unrounded Vowel",
    consumable=HealingConsumable(amount=4),
)

open_back_unrounded_vowel = Item(
    char="δ",
    color=(158, 48, 87),
    name="Open Back Unrounded Vowel",
    consumable=HealingConsumable(amount=5),
)

# medium healing potions

open_mid_front_unrounded_vowel = Item(
    char="∞",
    color=(158, 48, 87),
    name="Open-Mid Front Unrounded Vowel",
    consumable=HealingConsumable(amount=6),
)

open_mid_back_unrounded_vowel = Item(
    char="φ",
    color=(158, 48, 87),
    name="Open-Mid Back Unrounded Vowel",
    consumable=HealingConsumable(amount=7),
)

# large healing potions

close_mid_front_unrounded_vowel = Item(
    char="ε",
    color=(158, 48, 87),
    name="Close-Mid Front Unrounded Vowel",
    consumable=HealingConsumable(amount=8),
)

close_mid_back_unrounded_vowel = Item(
    char="∩",
    color=(158, 48, 87),
    name="Close-Mid Back Unrounded Vowel",
    consumable=HealingConsumable(amount=9),
)

# ultimate healing potions

close_front_unrounded_vowel = Item(
    char="≡",
    color=(158, 48, 87),
    name="Close Front Unrounded Vowel",
    consumable=HealingConsumable(amount=10),
)

close_back_unrounded_vowel = Item(
    char="±",
    color=(158, 48, 87),
    name="Close Back Unrounded Vowel",
    consumable=HealingConsumable(amount=11),
)

# future level 1 enemies:

glottal_stop = Actor(
    char="░",
    color=(157, 48, 87),
    name="Glottal Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_glottal_fricative = Actor(
    char="▒",
    color=(157, 48, 87),
    name="Voiceless Glottal Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_glottal_fricative = Actor(
    char="▓",
    color=(157, 48, 87),
    name="Voiced Glottal Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_pharyngeal_fricative = Actor(
    char="Ç",
    color=(157, 48, 87),
    name="Voiceless Pharyngeal Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_pharyngeal_fricative = Actor(
    char="ü",
    color=(157, 48, 87),
    name="Voiced Pharyngeal Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

# future level 2 enemies:

voiceless_uvular_stop = Actor(
    char="ë",
    color=(157, 48, 87),
    name="Voiceless Uvular Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_uvular_stop = Actor(
    char="è",
    color=(157, 48, 87),
    name="Voiced Uvular Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_uvular_nasal = Actor(
    char="ï",
    color=(157, 48, 87),
    name="Voiced Uvular Nasal",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_uvular_trill = Actor(
    char="î",
    color=(157, 48, 87),
    name="Voiced Uvular Trill",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_uvular_fricative = Actor(
    char="ì",
    color=(157, 48, 87),
    name="Voiceless Uvular Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_uvular_fricative = Actor(
    char="Ä",
    color=(157, 48, 87),
    name="Voiced Uvular Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

# future level 3 enemies:

voiceless_velar_stop = Actor(
    char="é",
    color=(157, 48, 87),
    name="Voiceless Velar Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_velar_stop = Actor(
    char="â",
    color=(157, 48, 87),
    name="Voiced Velar Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_velar_nasal = Actor(
    char="ä",
    color=(157, 48, 87),
    name="Voiced Velar Nasal",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_velar_fricative = Actor(
    char="à",
    color=(157, 48, 87),
    name="Voiceless Velar Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_velar_fricative = Actor(
    char="å",
    color=(157, 48, 87),
    name="Voiced Velar Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_velar_approximant = Actor(
    char="ç",
    color=(157, 48, 87),
    name="Voiced Velar Approximant",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_velar_lateral_approximant = Actor(
    char="ê",
    color=(157, 48, 87),
    name="Voiced Velar Lateral Approximant",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

# future level 4 enemies:

voiceless_palatal_stop = Actor(
    char="Å",
    color=(157, 48, 87),
    name="Voiceless Palatal Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_palatal_stop = Actor(
    char="É",
    color=(157, 48, 87),
    name="Voiced Palatal Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_palatal_nasal = Actor(
    char="æ",
    color=(157, 48, 87),
    name="Voiced Palatal Nasal",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_palatal_fricative = Actor(
    char="Æ",
    color=(157, 48, 87),
    name="Voiceless Palatal Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_palatal_fricative = Actor(
    char="ô",
    color=(157, 48, 87),
    name="Voiced Palatal Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_palatal_approximant = Actor(
    char="ö",
    color=(157, 48, 87),
    name="Voiced Palatal Approximant",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_palatal_lateral_approximant = Actor(
    char="ò",
    color=(157, 48, 87),
    name="Voiced Palatal Lateral Approximant",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

# future level 5 enemies:

voiceless_retroflex_stop = Actor(
    char="û",
    color=(157, 48, 87),
    name="Voiceless Retroflex Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_retroflex_stop = Actor(
    char="ù",
    color=(157, 48, 87),
    name="Voiced Retroflex Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_retroflex_nasal = Actor(
    char="ÿ",
    color=(157, 48, 87),
    name="Voiced Retroflex Nasal",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_retroflex_flap = Actor(
    char="Ö",
    color=(157, 48, 87),
    name="Voiced Retroflex Flap",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_retroflex_fricative = Actor(
    char="Ü",
    color=(157, 48, 87),
    name="Voiceless Retroflex Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_retroflex_fricative = Actor(
    char="¢",
    color=(157, 48, 87),
    name="Voiced Retroflex Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_retroflex_approximant = Actor(
    char="£",
    color=(157, 48, 87),
    name="Voiced Retroflex Approximant",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_retroflex_lateral_approximant = Actor(
    char="¥",
    color=(157, 48, 87),
    name="Voiced Retroflex Lateral Approximant",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

# future level 6 enemies:

voiceless_alveolar_stop = Actor(
    char="₧",
    color=(157, 48, 87),
    name="Voiceless Alveolar Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_alveolar_stop = Actor(
    char="ƒ",
    color=(157, 48, 87),
    name="Voiced Alveolar Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_alveolar_nasal = Actor(
    char="á",
    color=(157, 48, 87),
    name="Voiced Alveolar Nasal",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_alveolar_trill = Actor(
    char="í",
    color=(157, 48, 87),
    name="Voiced Alveolar Trill",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_alveolar_flap = Actor(
    char="ó",
    color=(157, 48, 87),
    name="Voiced Alveolar Flap",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_dental_fricative = Actor(
    char="ú",
    color=(157, 48, 87),
    name="Voiceless Dental Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_dental_fricative = Actor(
    char="ñ",
    color=(157, 48, 87),
    name="Voiced Dental Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_alveolar_fricative = Actor(
    char="Ñ",
    color=(157, 48, 87),
    name="Voiceless Alveolar Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_alveolar_fricative = Actor(
    char="ª",
    color=(157, 48, 87),
    name="Voiced Alveolar Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_postalveolar_fricative = Actor(
    char="º",
    color=(157, 48, 87),
    name="Voiceless Postalveolar Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_postalveolar_fricative = Actor(
    char="¿",
    color=(157, 48, 87),
    name="Voiced Postalveolar Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_alveolar_lateral_fricative = Actor(
    char="µ",
    color=(157, 48, 87),
    name="Voiceless Alveolar Lateral Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_alveolar_lateral_fricative = Actor(
    char="τ",
    color=(157, 48, 87),
    name="Voiced Alveolar Lateral Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_alveolar_approximant = Actor(
    char="Φ",
    color=(157, 48, 87),
    name="Voiced Alveolar Approximant",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_alveolar_lateral_approximant = Actor(
    char="Θ",
    color=(157, 48, 87),
    name="Voiced Alveolar Lateral Approximant",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

# future level 7 enemies:

voiced_labiodental_nasal = Actor(
    char="⌐",
    color=(157, 48, 87),
    name="Voiced Labiodental Nasal",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_labiodental_flap = Actor(
    char="¬",
    color=(157, 48, 87),
    name="Voiced Labiodental Flap",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_labiodental_fricative = Actor(
    char="½",
    color=(157, 48, 87),
    name="Voiceless Labiodental Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_labiodental_fricative = Actor(
    char="¼",
    color=(157, 48, 87),
    name="Voiced Labiodental Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_labiodental_approximant = Actor(
    char="¡",
    color=(157, 48, 87),
    name="Voiced Labiodental Approximant",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

# future level 8 enemies:

voiceless_bilabial_stop = Actor(
    char="α",
    color=(157, 48, 87),
    name="Voiceless Bilabial Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_bilabial_stop = Actor(
    char="ß",
    color=(157, 48, 87),
    name="Voiced Bilabial Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_bilabial_nasal = Actor(
    char="Γ",
    color=(157, 48, 87),
    name="Voiced Bilabial Nasal",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_bilabial_trill = Actor(
    char="π",
    color=(157, 48, 87),
    name="Voiced Bilabial Trill",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiceless_bilabial_fricative = Actor(
    char="Σ",
    color=(157, 48, 87),
    name="Voiceless Bilabial Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

voiced_bilabial_fricative = Actor(
    char="σ",
    color=(157, 48, 87),
    name="Voiced Bilabial Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)