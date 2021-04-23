from components.ai import HostileEnemy
from components.consumable import HealingConsumable
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item


player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=HealingConsumable(amount=4),
)

#future level 1 enemies:
glottal_stop = Actor(
    char="[",
    color=(157, 48, 87),
    name="Glottal Stop",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
)

voiceless_glottal_fricative = Actor(
    char="h",
    color=(157, 48, 87),
    name="Voiceless Glottal Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
)

voiced_glottal_fricative = Actor(
    char="_", color=(157, 48, 87),
    name="Voiced Glottal Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
)

voiceless_pharyngeal_fricative = Actor(
    char="]",
    color=(157, 48, 87),
    name="Voiceless Pharyngeal Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
)

voiced_pharyngeal_fricative = Actor(
    char="^",
    color=(157, 48, 87),
    name="Voiced Pharyngeal Fricative",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
)