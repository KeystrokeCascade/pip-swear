"""
Profanity genorator for python
Generates very explicit swears in the style of Littlepip
"""

#sets the options for the variables
verb = ("rape", "fuck", "lick", "clop", "spank", "spin", "shit")
verbing = ("raping", "fucking", "licking", "clopping", "spanking", "spinning", "shitting")
amplifiers = ("", "Great");
names = ("Celestia", "Luna", "Goddesses", "Nightmare Moon")
objects = ("the moon", "moon rocks", "sunfire", "a solar flare", "a thousand star-devils")
bodyPartsSingle = ("clit", "moonheat", "libido", "horn", "cunt", "hoof", "mane", "butt")
bodyPartsMulti = ("wings", "forehooves", "hooves")
quantifiers = ("", "a hoof-full of", "an army of", "a mass of", "a train car full of")
adjectives = ("tidal", "moaning", "solar-flaring", "solar-heated")
allBodyParts = bodyPartsSingle + bodyPartsMulti

def swear():
    #randomly selects the variables to use
    import random
    verb_print = verb[random.randint(0,len(verb)-1)]
    verbing_print = verbing[random.randint(0,len(verbing)-1)]
    amplifiers_print = amplifiers[random.randint(0,len(amplifiers)-1)]
    names_print = names[random.randint(0,len(names)-1)]
    objects_print = objects[random.randint(0,len(objects)-1)]
    bodyPartsSingle_print = bodyPartsSingle[random.randint(0,len(bodyPartsSingle)-1)]
    bodyPartsMulti_print = bodyPartsMulti[random.randint(0,len(bodyPartsMulti)-1)]
    allBodyParts_print = allBodyParts[random.randint(0,len(allBodyParts)-1)]
    quantifiers_print = quantifiers[random.randint(0,len(quantifiers)-1)]
    adjectives_print = adjectives[random.randint(0,len(adjectives)-1)]

    #randomly selects the string to insert the variables into
    rand_str = random.randint(1,17)
    #*name *verb me like she loves me!
    if rand_str == 1:
        output = names_print + " " + verb_print + " me like she loves me!"
    #*name *verb my *bodyPart!
    elif rand_str == 2:
        output = names_print + " " + verb_print + " my " + bodyPartsSingle_print + "!"
    #*name *verb my *bodyPart with *quantifier *object.
    elif rand_str == 3:
        output = names_print + " " + verb_print + " my " + bodyPartsSingle_print + " with " + quantifiers_print + " " + objects_print + "."
    #*name *verb my *bodyPart with her *bodyPart.
    elif rand_str == 4:
        output = names_print + " " + verb_print + " my " + bodyPartsSingle_print + " with her " + allBodyParts_print + "."
    #*amplifier *name *verb me with *object.
    elif rand_str == 5:
        output = amplifiers_print + " " + names_print + " " + verb_print + " me with " + objects_print + "."
    #*amplifier *name *verb me with her *bodyPart.
    elif rand_str == 6:
        output = amplifiers_print + " " + names_print + " " + verb_print + " me with her " + allBodyParts_print + "."
    #*name's *adjective *bodyPart!
    elif rand_str == 7:
        output = names_print + "'s " + adjectives_print + " " + bodyPartsSingle_print + "!"
    #By the *bodyPart of *name!
    elif rand_str == 8:
        output = "By the " + allBodyParts_print + " of " + names_print + "!"
    #Holy hot sex with *name!
    elif rand_str == 9:
        output = "Holy hot sex with " + names_print + "!"
    #Sit on my *bodyPart and *verb.
    elif rand_str == 10:
        output = "Sit on my " + allBodyParts_print + " and " + verb_print + "."
    #*name-*verbing orgasms!
    elif rand_str == 11:
        output = names_print + "-" + verbing_print + " orgasms!"
    #*verb a *bodyPartsSingle where Celestia don't shine!
    elif rand_str == 12:
        output = verb_print + " a " + bodyPartsSingle_print + " where Celestia don't shine!"
    #*verbing orgasms of *name!
    elif rand_str == 13:
        output = verb_print + " orgasms of " + names_print + "!"
    #Oh *verb me with *name's *bodyPart!
    elif rand_str == 14:
        output = "Oh " + verb_print + " me with " + names_print + "'s " + allBodyParts_print + "!"
    #Oh no. No. *name *verb me with *object, no.
    elif rand_str == 15:
        output = "Oh no. No. " + names_print + " " + verb_print + " me with " + objects_print + " no."
    #*name shove my *bodyPart full of *object and call me home.
    elif rand_str == 16:
        output = names_print + " shove my " + bodyPartsSingle_print + " full of " + objects_print + " and call me home."
    #Oh sweet *name's *adjective orgasms!
    elif rand_str == 17:
        output = "Oh sweet " + names_print + "'s " + adjectives_print + " orgasms!"

    #removes double spaces
    for i in range(output.count("  ")):
        part_1 = output[:output.find("  ")]
        part_2 = output[output.find("  ") + len("  "):]
        output = part_1 + part_2

    #removes spaces at the beginning and end
    output = output.strip()
    #capitalizes first letter
    output1 = output[0].upper()
    output2 = output[1:]
    output = output1 + output2
    #returns full string
    return output

def menu():
    #menu, make a choice
    menu = input()
    #makes input not case sensitive
    menu = menu.lower()
    #lists commands
    if menu == "help":
        print("swear: make a Pip swear.\nhelp: what you are looking at.\ncredits: list credits.")
    #lists credits
    elif menu == "credits":
        print("Original generator by go-ive\nCharacter by Kkat\nPython conversion by KeystrokeCascade.")
    #swears
    elif menu == "swear":
        print(swear())
    #error message
    else:
        print("That is not a recognised command.\nFor the full list of commands, type help.")

#title text
print("Welcome to the Littlepip profanity generator in Python.")

#runs menu so always loops back
while True:
    menu()
