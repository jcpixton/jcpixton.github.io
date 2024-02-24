word_list = ["yak", "tickle", "kindly", "spiffy", "replace", "mushy", "trade", "overjoyed", "abashed", "kind", "fear",
    "opposite", "cabbage", "nappy", "grubby", "extend", "sleet", "abject", "bite-sized", "jagged", "weigh",
    "crayon", "oceanic", "tearful", "functional", "tested", "fruit", "relax", "trucks", "obscene", "confess",
    "delay", "onerous", "hesitant", "square", "page", "tail", "zany", "faulty", "grumpy", "woebegone",
    "materialistic", "oil", "deserve", "truthful", "curious", "belong", "filthy", "dapper", "green",
    "high-pitched", "optimal", "quartz", "rigid", "bang", "dramatic", "wheel", "wiry", "practice", "scrawny",
    "relieved", "plants", "lock", "brave", "deadpan", "towering", "current", "cuddly", "light", "girl",
    "cultured", "moor", "swanky", "nostalgic", "brush", "righteous", "harbor", "fearful", "cracker", "tramp",
    "rifle", "worthless", "oatmeal", "object", "reminiscent", "harass", "smelly", "squeak", "sock", "spiky",
    "curly", "grieving", "ignorant", "nest", "glamorous", "interesting", "label", "claim", "ethereal", "unlock",
    "absorbed", "mean", "astonishing", "experience", "super", "pest", "medical", "pinch", "yielding", "compete",
    "unusual", "card", "smash", "hop", "makeshift", "toad", "utopian", "unadvised", "cause", "vein", "rescue",
    "endurable", "crib", "momentous", "nosy", "knowledgeable", "stamp", "rely", "contain", "introduce", "voracious",
    "parcel", "carriage", "unit", "scene", "hunt", "branch", "plug", "rat", "knock", "wash", "extra-large",
    "interrupt", "protective", "calendar", "psychotic", "route", "rare", "glass", "scintillating", "classy",
    "spotless", "advertisement", "cream", "slimy", "station", "bubble", "distance", "repair", "volleyball",
    "hard-to-find", "brief", "religion", "invite", "chemical", "outgoing", "striped", "frantic", "frail", "spade",
    "rude", "sheet", "fit", "damp", "imaginary", "dull", "steel", "common", "arrest", "flower", "open", "moldy",
    "prickly", "six", "knife", "festive", "country", "sister", "playground", "silver", "shut", "volcano",
    "plantation", "subtract", "pretty", "mixed", "cub", "time", "average", "precede", "thaw", "capable", "complex",
    "distribution", "identify", "abortive", "property", "quiver", "nine", "abusive", "guarantee", "hysterical",
    "kitty", "tremendous", "ruthless", "living", "dusty", "heal", "obnoxious", "soup", "forgetful", "wander", "icky",
    "back", "lowly", "drown", "coil", "strip", "prose", "feeling", "ad hoc", "laughable", "dad", "river", "sincere",
    "transport", "tranquil", "soothe", "sun", "domineering", "hole", "coordinated", "fuel", "squirrel", "snow",
    "drip", "discussion", "increase", "annoying", "observe", "drawer", "handy", "ten", "equable", "beam", "real",
    "horses", "zealous", "choke", "tasteless", "perfect", "faded", "grade", "invincible", "lethal", "launch", "impolite", 
    "pizzas", "abiding","riddle", "minister", "minor", "unruly", "vivacious", "park", "warm", "jeans", "past", "brake",
    "vulgar", "correct", "furtive", "queue", "womanly", "graceful", "instruct", "exclusive", "divide", "better",
    "succinct", "raspy", "attractive", "realize", "previous", "meek", "aloof", "saw", "birthday", "way", "tense",
    "lavish", "room", "embarrassed", "big", "loss", "bird", "sweater", "horse", "hissing", "doll", "society", "dirt",
    "pigs", "tin", "mailbox", "report", "pear", "abhorrent", "sip", "man", "female", "van", "rub", "explain", "jelly",
    "mess up", "callous", "worry", "futuristic", "hospitable", "pleasant", "luxuriant", "absurd", "delicious", "somber",
    "ducks", "retire", "damage", "lace", "private", "glistening", "pretend", "snobbish", "song", "adaptable", "helpful",
    "gainful", "eyes", "shave", "condemned", "scary", "breath", "gentle", "voyage", "addicted", "fence", "terrible",
    "snotty", "pickle", "verse", "enter", "teeth", "grateful", "trashy", "tree", "announce", "literate", "shaggy", "ban",
    "bit", "deafening", "yoke", "stain", "calculating", "hour", "mist", "decay", "bolt", "borrow", "rural", "chilly",
    "songs", "develop", "planes", "habitual", "available", "venomous", "hapless", "sable", "seashore", "circle", "babies",
    "grab", "bat", "sweltering", "occur", "beginner", "dispensable", "low", "complete", "accept", "consist", "murder",
    "middle", "unbiased", "live", "stroke", "throat", "gather", "toys", "mountain", "highfalutin", "fly", "machine",
    "legs", "macho", "troubled", "groovy", "promise", "sisters", "plate", "word", "attraction", "frightening", "bright",
    "pump", "self", "number", "trust", "flock", "berry", "elated", "lazy", "preach", "boat", "writer", "stupendous",
    "juicy", "snake", "wretched", "nice", "vest", "male", "meeting", "force", "moan", "spring", "simplistic", "well-made",
    "trite", "instinctive", "shelter", "berserk", "agree", "snatch", "spark", "innocent", "few", "normal", "march",
    "cable", "unaccountable", "heat", "sick", "dark", "happy", "selection", "loose", "handle", "greet", "modern",
    "fantastic", "flat", "giraffe", "belief", "telling", "cannon", "haircut", "chew", "threatening", "fail", "relation",
    "tacky", "fabulous", "fact", "aromatic", "delicate", "attend", "curved", "rapid", "merciful", "crime", "guide",
    "jolly", "lucky", "public", "scientific", "wealth", "teaching", "terrify", "imagine", "try", "certain", "slip",
    "juice", "mute", "avoid", "substantial", "fat", "ticket", "fanatical", "intend", "possess", "encourage", "field",
    "squeeze", "iron", "change", "arrive", "cheer", "book", "action", "sloppy", "air", "teeny"]

opening_art = '''                                                                            
            88                                                                            
            88                                                                            
            88                                                                            
            88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,  
            88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a 
            88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88  
            88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88  
            88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88  
                                                aa,    ,88                                
                                                "Y8bbdP"                                  
'''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']