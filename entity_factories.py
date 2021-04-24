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

health_potion = Item(
    char="!",
    color=(158, 48, 87),
    name="Health Potion",
    consumable=HealingConsumable(amount=4),
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