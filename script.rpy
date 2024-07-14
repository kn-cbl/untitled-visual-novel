# The script of the game goes in this file.

define narrator = Character(None, kind=nvl)

label start:
    # TODO: recheck quotes
    
    call prelude

    nvl clear
    scene black_screen
    with fade

    # narrator """

    # """

    call prologue_1
    call prologue_2
    call prologue_3

    call chapter_1

    return
