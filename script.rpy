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

    narrator """
        Every single weekday, a normal student goes to school and studies
        for their own sake. They were the words of every single teacher
        I've met.
    """

    narrator """
        It's been six months since I left Track and Field. I used to be an
        athlete. They called me their ace until my ankle got injured in an
        accident. It was just an unfortunate incident.
    """

    nvl clear

    narrator "I used to feel hatred for it."
    narrator """
        That night, there were two lousy adults, drunk and driving.
        Then there's me, a victim of their recklessness. 
    """
    narrator """
        I detested adults strongly, but I hated how my life turned out
        even more.
    """

    narrator """
        I never wanted to be stuck in a mentality in which I coped
        by blaming other people, even if they fully deserved it.
    """

    narrator """
        The tragic tale of my life—all I could do was laugh at
        how absurd it is. I could never erase the memory that blooms
        and haunts me.
    """

    nvl clear
    scene smp_club1_day1
    with fade

    narrator """
        In a clubroom, the room was the same as ever. The reader's club 
        was the club I ended up with after I quit the last one I joined.
    """
    
    narrator """
        There were only a few of us. In fact, the members only met its
        minimum requirement.
    """
    narrator """
        I, Eve, and the other man whose name I can't recall. He barely 
        attended our club activities—can't blame me for that, honestly.
    """

    nvl clear

    narrator """
        After a few months of my injury, I was discharged from the 
        hospital. I could walk just fine, but it was still difficult
        to run. I'm essentially a crippled person compared to who I was 
        before.
    """

    narrator """
        In my leisure time, I was reading a book written by Stephen King.
        It was a horror novel. Apparently, this work was Eve's
        favorite. I stayed here until the afternoon and read about a
        hundred pages.
    """

    nvl clear
    scene smp_club1_evening1
    with dissolve

    narrator """
        Time flowed so fast that I barely noticed. I skipped class,
        but it didn't mean anything to me. Simply because, one day,
        I couldn't care less about my grades.
    """
    narrator """
        I never got curious why, and although I have my own reasons,
        I would rather keep it to myself.
    """

    nvl clear

    narrator """
        A clack of the door as the sound of the wood softly banged
        the wall beside the club entrance had distracted me from
        reading peacefully.
    """
    narrator "There was a rude visitor."

    nvl clear

    narrator "\"You're in the club room again.\""
    narrator """
        The stranger intruded rudely, and as she sighed so hard,
        I easily felt how disappointed she was.
    """
    
    narrator """
        No, not exactly a stranger. Her name is Eve. She is one
        of my clubmates.
    """

    nvl clear
    show eve_neutral at left:
        xalign 0.1
        zoom 0.5
    with dissolve

    narrator """
        \"Your attendance has been so poor that our class advisor 
        approached me to do something about it.\"
    """
    
    nvl clear

    narrator """
        I didn't say anything. Every ounce of my focus was directed
        at the book I'm reading.
    """
    narrator """
        I could hear her footsteps. They were in an interval fast
        enough for me to sense something ominous.
    """
    
    hide eve_neutral
    with fade
    show eve_angry at center:
        yalign 1
    with dissolve

    narrator """
        Before I knew it, she picked up the book that I was reading.
        I was surprised. Her pretty face and serious demeanor
        caught me unguarded.
    """

    nvl clear
    hide eve_angry
    show eve_angry at center:
        zoom 0.5
    with dissolve

    narrator """
        \"This isn't a joke, you could've gotten expelled,\"
        said Eve as she fixed her posture.
    """

    nvl clear
    narrator """
        \"There's no reason for me to attend classes.\"
        I calmly retorted.{nw}
    """

    hide eve_angry
    show eve_surprise at center:
        zoom 0.5
    with dissolve
    pause
    
    nvl clear
    hide eve_surprise
    show eve_aloof at center:
        zoom 0.5
    with dissolve

    narrator "\"I'm sorry, but I don't want to waste my time learning something useless.\""

    narrator "\"That's not true,\" she argued confidently. \"It's not useless because education is essential.\""

    nvl clear
    hide eve_aloof
    show eve_neutral at center:
        zoom 0.5
    with dissolve

    narrator "\"How?\" I patronazingly asked. \"Are you telling me you use trigonometry every single day or something? That's stupid.\""
    narrator "\"You're stupid.\""
    narrator "\"What do you even mean by that?\""
    narrator "\"Even if you don't, some people will, like those who would take engineering at college.\""
    narrator "\"But I won't, Eve. That's the point. Algebra, research, and seriously, quantum physics?\" Lazily, I shrugged my shoulders."

    nvl clear
    hide eve_neutral
    show eve_cry at center:
        zoom 0.5
    with dissolve

    narrator "\"You were not like this before...\""
    narrator "\"Yeah... I know.\""
    narrator "..."

    nvl clear
    hide eve_cry
    show eve_worried at center:
        zoom 0.5
    with dissolve

    """
        The pause after was awkward.
        The atmosphere got heavier as the silence continued.
        Eve frowned, seemingly discouraged.
    """

    hide eve_worried
    show eve_saddest at center:
        zoom 0.5
    with dissolve
    
    """
        I was unnecessarily rude when she showed concern.
        If anything, it was just right to apologize.
    """

    nvl clear

    narrator "\"I'm sorry, Eve...\""
    
    hide eve_saddest
    show eve_surprise at center:
        zoom 0.5
    with dissolve

    narrator "I sighed while probably frowning. \"That was immature of me. By the way, I was starting to enjoy that book. May I borrow it?\""

    nvl clear 

    narrator "Eve submissively returned the book. The intensity and awkwardness between us calmed down. Although it felt like she wanted to say something, Eve evidently held back."

    nvl clear

    narrator "\"Okay, but can you at least attend your class? Your grades wouldn't matter if our professors decided to drop you out.\""
    narrator "\"Alright.\" I sighed dramatically."

    nvl clear
    hide eve_surprise
    with dissolve

    narrator "Excitedly, Eve grabbed the chair beside me and sat. There was a total transformation from her mood a minute ago and now. It was like day and night."

    nvl clear
    show eve_smile at left:
        xalign 0.1
        yalign 1
    with dissolve

    narrator "\"So? How did you like The Shining? so far\" asks Eve, her eyes glimmering from curiosity."

    nvl clear

    narrator """
        \"It was tense. The characters are interesting. I enjoyed how
        the narration focused on the psychological aspect.\"
    """

    hide eve_smile
    show eve_happiest at left:
        xalign 0.1
        yalign 1
    with dissolve

    narrator "\"I see...\""

    nvl clear
    hide eve_happiest
    show eve_happiest at left:
        xalign 0.1
        zoom 0.5
    with dissolve

    pause 1.0
    hide eve_happiest
    show eve_aloof at left:
        xalign 0.1
        zoom 0.5
    with dissolve

    narrator """
        Everything turned to normal again after I gave her my opinion.
        It marked the end of our banter.
    """
    narrator """
        The club room was filled with silence. Its wooden floor
        was covered with a golden shine. The temperature was just
        right. It wasn't too hot or too cold.
    """

    nvl clear

    narrator """
        Eve prepared tea and biscuits. This was her offer at the
        start of the semester: "To anyone who joins the reader's
        club, you'll get free tea and biscuits as long as you read during
        our time."
    """
    narrator """
        She brewed them perfectly, and the aroma that the tea had
        was soothing. The biscuits brand was unfamiliar to me.
        The language seemed French—a luxury.
    """
    narrator "Every sweets and tea she offered were certainly delicious."
    narrator """
        It was such a shame that not a lot of students were
        interested, but at the same time I prefer it that way.
    """

    return
