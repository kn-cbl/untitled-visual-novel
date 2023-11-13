# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = nvl_narrator
define eve = Character(None, kind = nvl, what_prefix = "\"", what_suffix = "\"", what_color = "#2980b9")
define chad = Character(None, kind = nvl, what_prefix = "\"", what_suffix = "\"", what_color = "#c8ffc8")

# The game starts here.

label start:

    scene bg room

    show eileen happy

    eve "You're at the club room again..."
    eve "Your attendance has been so poor that our class advisor approached me to do something about it."

    chad "School is nothing but a fucked up system, Eve. All your efforts would die out before you even know it."

    eve "That's not true . Education is essential."

    chad "How? Are you telling me you use trigonometry every single day or something? That's stupid."

    eve "You're stupid."

    chad "W-wah."

    nvl clear

    eve "Even if you don't, some people will, like those who would take engineering at college."

    chad "But I don't, Eve. That's the point. Algebra, research, fucking quantum physics, who gives a damn."

    eve "You were not like this before."

    nvl clear

    "Silence filled the clubroom after our abrupt awkward conversations. The truth was, if she was any other student, I would've been so pissed."

    nvl clear

    eve "If this is what you have chosen to do, then fine! Don't ever tell me that I didn't try to persuade you to do better, because I did!"

    chad "Just shut up."

    eve "Asshole!"

    return
