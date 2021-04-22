from entity import Entity


player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

#future level 1 enemies:
glottal_stop = Entity(char="[", color=(157, 48, 87), name="Glottal Stop", blocks_movement=True)
voiceless_glottal_fricative = Entity(char="h", color=(157, 48, 87), name="Voiceless Glottal Fricative", blocks_movement=True)
voiced_glottal_fricative = Entity(char="_", color=(157, 48, 87), name="Voiced Glottal Fricative", blocks_movement=True)
voiceless_pharyngeal_fricative = Entity(char="]", color=(157, 48, 87), name="Voicless Pharyngeal Fricative", blocks_movement=True)
voiced_pharyngeal_fricative = Entity(char="^", color=(157, 48, 87), name="Voiced Pharyngeal Fricative", blocks_movement=True)