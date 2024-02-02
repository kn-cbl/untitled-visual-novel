﻿# The script of the game goes in this file.

define narrator = Character(None, kind=nvl)

label start:
    scene black_screen

    narrator """
        Pretending to be normal was a waste of time. Even if I try my best to
        act as one, the world will pull me back to the place where I belong. In
        my solitude, I am most comfortable. An apathetic life, ruthlessly cold
        tactics and with strategic words that pierce stronger than a bullet.
    """

    nvl clear

    narrator """
        I'm a detective. Not for the police or something private, but for the
        local mafia which my aunt had some connection with. Cigarettes, rough
        vocabulary, mostly slang, laughters at the shittiest joke ranging from
        the funniest I've heard (it's all nonsense), to champagne, wine, beer,
        vodka, prostitution, women with bare clothes, naked even, and whatever
        alcoholic drink atop the bar table.
    """

    narrator """
        But when it comes to business, there are rats. There are those ambitious
        kind. Those who are cold-blooded that they don't think twice about
        murder and betrayal - that's the environment I grew up with. And when
        the boss tried to give me some adult entertainment, my aunt would always
        instantly be behind him. Almost like teleporting, beating the shit out
        of him. Sometimes she just kicks the ass of everyone and leaves
        unscratched. She's one hell of a scary aunt.
    """

    nvl clear

    narrator "My lungs screamed as I caught my breath."
    narrator """
        I ran for twenty minutes straight from my workplace to Alice's house.
    """
    narrator "The road was uphill, but my legs continued regardless."

    nvl clear

    narrator "\"Your girlfriend sent you a letter.\""

    nvl clear

    narrator "I'm done."
    narrator "That's all the letter told me."
    narrator """
        My relationship with her was complicated, yet those words were
        enough to set my chest ablaze.
    """

    nvl clear

    narrator """
        It was easier to take the bus, but my brain didn't have any power
        to think so. I think it was because I met her that the swallowed me.
    """

    narrator """
        I reached the front yard of her house. The entrance gate was ajar.
    """

    narrator "My sweat continuously gushed, and my T-shirt drenched."
    narrator """
        Beyond the gate lies my anxiety. Their living room was entirely
        covered in darkness.
    """

    nvl clear

    narrator "\"Alice!\" I cried so hard I felt my throat reverberate."

    nvl clear

    narrator """
        In a rush, I tripped over and scraped my knees. It definitely bled,
        but still, I ran over to their door in desperation.
    """

    narrator "It was really dark. Anything inside was barely distinguishable."

    nvl clear

    narrator "There was a silhouette."
    narrator "It noticed me."
    narrator "It dropped something, and that let out a metal clank."

    nvl clear

    narrator "\"Alice!\""

    nvl clear

    narrator """
        The silhouette ran away, straight from where the motorcycle
        was parked.
    """
    narrator "My attention, however, was only focused where she was."

    nvl clear

    narrator "That's why..."
    narrator "I was reminded,"
    narrator "the moment I saw her lifeless body,"

    narrator ""
    narrator "Beautifully lying cold on the floor"
    narrator "That on that day—"

    nvl clear

    narrator """
        {i}
        She prayed her wish by the falling star—\n
        My sweet memory and a hopeful heart,\n
    """

    nvl clear
    scene living_room_bw
    with dissolve

    # centered text left align, add spaces between, nvl transparent
    narrator """
        {i}
        Moment's bliss and a broken bridge.\n
        The sudden storm and its gale of lies,\n
        Like a stranger's home in unwanted paradise.
    """

    nvl clear
    scene living_room_color
    with dissolve
    
    narrator """
        {i}
        All love confined, endured— a sadistic torture.\n
        A heart discouraged, persisted and twisted.
    """

    nvl clear

    narrator "{i}Alice, I wonder, had you remember?"

    nvl clear
    scene black_screen
    with fade

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
