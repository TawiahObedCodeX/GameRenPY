default trust = 0
default confidence = 0
default curiosity = 0
default courage = 0
default kindness = 0
default friendship_veronica = 0
default friendship_stacy = 0
default friendship_marcellina = 0
default safety = 0
default discovery = 0
default checked_marcellina = False
default mc_replied = False
default stacy_points = 0 
default attitude = 0 
default reserve = 0 

# Player name variable
default player_name = ""


# Declare characters 
define mc = DynamicCharacter("[player_name]") 
define st = Character("Stacy") 
define miss_a = Character("Miss Amponsah") 
define ma = Character("Marcellina") 
define vr = Character("Veronica")
define mf = Character("Mr. Farrah")
define cl = Character("Class")
define ch = Character("Christiana")
define ca = Character("Charis")
define sr = Character("Sister")
define tr = Character("teacher")
define na = Character("Naa Aqueley")
define sd = Character("Random student")
define sd2 = Character("Random student 2")
define sd3 = Character("Rndom student 3")
define ra = Character("Head boy of St. Bartholomews'")
define aa = Character("Headmistress")
define co = Character("Headgirl")
define rs = Character("Random sister")
define rsii = Character("Random sister 2")
define rsiii = Character("Random sister 3")
define ga = Character("Grace Ansah")



# Relationship stats 


default tension_marcellina = 0 

 
# Game starts here


label start: 

    scene mc_dorm 
    with fade 

 
label ask_name:
    
    call screen name_input
    $ player_name = _return.strip()

    if player_name == "":
        $ player_name = "Michelle"

    return

    call ask_name
    mc "Hi! I'm [player_name]. Nice to meet you."

    "..."
    "The dorm smells faintly of detergent and old wood. Sunlight seeps through the narrow windows, lighting up the neatly arranged bunk beds."

    "[player_name] arrives, basket in hand, trying to make sense of the new environment."

 

    show miss_a normal at left 

    miss_a "Sisters! Help her settle in. Lay her bed, arrange her basket, fetch water for her, everything she needs." 

 

    "[player_name] watches the seniors move with practiced efficiency, feeling a knot of nerves in her stomach." 

    "How was she going to adjust? What about all the classes she had missed? And what if she gets bullied—or worse?"

 

    show st normal at right 

    st "Hi! I’m Stacy. I’m in charge of helping you adjust to the school." 

 

    "[player_name] notes Stacy’s friendly smile." 

    mc "Hi, Stacy. Thank you." 

 

    "Stacy gestures toward the only empty bed in the room. It is right next to a grumpy-looking senior, Marcellina." 

 

    show ma angry at center 

    "Marcellina glares briefly before turning away, muttering under her breath. [player_name] decides to..."

 

    menu: 
        "Talk to Stacy and ask about the dorm rules": 
            jump talk_stacy 

        "Check Marcellina quietly": 
            jump check_marcellina 

        "Explore the room quietly":
            jump explore_room 

 

# Scene options 

label talk_stacy: 

    $ friendship_stacy += 1
    $ trust += 1

    "[player_name] turns to Stacy, eager to learn the dorm routines." 

    st "First, you need to keep your bed neat and your locker organized every morning. I’ll show you how." 

    "Stacy showed her step by step, making [player_name] feel a little more at ease." 

    jump after_choice 

 

label check_marcellina:

    $ checked_marcellina = True
    $ friendship_marcellina += 1
    $ courage += 1
    $ kindness += 1 

    "[player_name] glances at Marcellina, who is busy tidying her bed and ignoring everyone else."

    "Her presence fels intimidating, so [player_name] decides to mind her own business for now." 

    jump after_choice 

 

label explore_room:
 
    $ curiosity += 1
    $ discovery += 1

    "[player_name] walkes slowly around the dorm, careful not to draw attention from Stacy or anyone."

    scene insides_dorm1 

    "She examines the arrangement of beds, baskets, and trunks, realizing it would be impossible to know everyone here well." 

    "Even though she stays quiet, Marcellina’s sharp eyes catches her glance more than once." 

    jump after_choice 

 

label after_choice: 

    "[player_name] continues settling in, feeling slightly less nervous but still aware of the challenges ahead." 

 
label scene2:

    # Atmosphere
    scene dorm_hallway with fade

    "The corridor hums softly with distant chatter and the occasional burst of laughter."

    "[player_name] adjusts the towel in her hands, then steps fully into the hall. She sighs visibly as she remembers that she has forgotten where the bathroom is."

    "Stacy and Marcellina stand a short distance away."

    menu:
        "Ask Stacy for directions":
            jump ask_stacy

        "Ask Marcellina for directions":
            jump ask_marcellina


label ask_stacy:

    mc "Hey… do you know where the bathroom is?"

    if checked_marcellina:
        $ friendship_stacy -= 1

        "Stacy barely looks up."
        "Her arms remain folded."

        st "You should ask someone else."

        "The conversation ends as quickly as it began."
        
        "She decides to look for the bathroom herself."

    else:
        $ friendship_stacy += 1
   
        "Stacy turns toward her, expression softening."

        st "It’s right after the strip—the place where everyone hangs their clothes."

        "She glances down the hallway."

        st "If you want, I can show you."

        "[player_name] quietly declines and heads towards the bathroom."

    jump scene2_end


label ask_marcellina:

    mc "Hey… do you know where the bathroom is?"

    if checked_marcellina:


        "Marcellina looks at her briefly."

        ma "It’s right after the strip."

        "[player_name] gives a small nod before walking off."

    else:
         
        "Marcellina ignores her."

        "[player_name] steps away almost immediately and looks for the bathroom herself."

    jump scene2_end


label scene2_end:

    "The hallway feels quieter as she makes her way to the bathroom."


label scene_three:

    scene mc_desk
    with fade

    "It is a morning physics class, right after devotion."
    "One week since the main character arrived."

    "The physics teacher is late again. No one seems surprised."

    "To save time, [player_name] quietly recopies her group's chemistry work before the next lesson."

    show vr sleepy at right

    "Beside her, Veronica lays slumped over her desk, cheek pressed against her notebook. One eye half-open."

    vr "Why are you writing so fast?"
    vr "He’s not even going to mark it."

    show ch normal at left

    "Across the room, Christiana watches them over the rim of her glasses. She hasn’t looked away once."

    menu:
        "Ignore the comment":
            $ mc_replied = False
            $ friendship_veronica -= 1
            $ safety += 1
            jump ignore_choice

        "Reply calmly":
            $ mc_replied = True
            $ friendship_veronica += 1
            $ courage += 1
            $ kindness += 1
            jump reply_choice


label ignore_choice:

    "[player_name] keps writing, pretending she hasn’t heard."

    show vr annoyed at right

    "Veronica rolles her eyes, turnes her head the other way, and goes back to her being half-sleep."

    "Christiana’s gaze lingeres for a moment longer before she finally looks away."

    jump teacher_enters


label reply_choice:

    mc "You never know what can happen."
    mc "These teachers are unpredictable."

    show veronica amused at right

    "Veronica huffs a small laugh, clearly entertained."

    show ch smug at left

    "Christiana’s lips twitch."
    "Not amusement. Calculation."

    "She leans toward the form leader and murmurs something."

    "The main character doesn’t hear it, but she feels it."

    "Her name would be written somewhere."

    jump teacher_enters


label teacher_enters:

    "Thirty minutes later, the door finally opens and the long awaited teacher comes in."

    scene classroom_doorway

    show mf in rush at center

    "Mr. Farrah walks in as though he had been chased into the classroom, apologising as usual for being late."

    show mf apologizing at center

    cl "Good morning, Mr. Farrah."

    "Mr. Farrah dismisses greetings"

    mf "Top student."

    show ca neutral at center

    "Charis looks up instantly."

    mf "Write the notes in this book on the board."

    "He hands her a marker and a small notebook, as though the rest of the class doesn’t exist."

    "As though the new curriculum rules don’t exist either."

    "Charis stands without a word."

    "No eye contact. No reaction."

    "She simply walks to the board and begins to write."

    "By now, the main character is used to this."

    "She put the group project aside, picked up her pen, and began copying from the board."

label scene_4:

    # mc spoke in Scene 3
    if mc_replied:

        # Kindness < 2 → correction
        if kindness <= 1:
            jump scene_4A

        # Kindness = 2 → excursion
        else:
            jump scene_4Bi

    # mc did not reply → excursion, isolated
    else:
        jump scene_4Bii

label scene_4A:

    scene prefect_assemblyground_morning

    with fade

    "The assembly ground is unusually quiet."

    "Rumors spread quickly — someone from [player_name]’s class is going to be corrected."

    "[player_name] stands in her house line, hands clasped, heart beating faster than it should."

    "When the head girl mounts the stage, the silence deepens."

    "Names are read out one by one."

    "Then—"

    "[player_name] of 1S9."

    "The words land heavier than she expects."

    "She is being corrected for talking during a physics lesson."

    "Suspension from academic and extracurricular activities follow. A week."

    "Her correction starts immediately."

    "[player_name] keps her gaze forward. She doesn’t look at anyone."

    "Stacy stands ahead of her, close enough that [player_name] sees her shoulders tense."

    "By the time the assembly is dismissed, the excursion announcement feels distant."

    "[player_name] already knows she wouldn’t be going."

    jump scene_5A  #default trust = 0
default confidence = 0
default curiosity = 0
default courage = 0
default kindness = 0
default friendship_veronica = 0
default friendship_stacy = 0
default friendship_marcellina = 0
default safety = 0
default discovery = 0
default checked_marcellina = False
default mc_replied = False
default stacy_points = 0 
default attitude = 0 
default reserve = 0 

# Player name variable
default player_name = ""


# Declare characters 
define mc = DynamicCharacter("[player_name]") 
define st = Character("Stacy") 
define miss_a = Character("Miss Amponsah") 
define ma = Character("Marcellina") 
define vr = Character("Veronica")
define mf = Character("Mr. Farrah")
define cl = Character("Class")
define ch = Character("Christiana")
define ca = Character("Charis")
define sr = Character("Sister")
define tr = Character("teacher")
define na = Character("Naa Aqueley")
define sd = Character("Random student")
define sd2 = Character("Random student 2")
define sd3 = Character("Rndom student 3")
define ra = Character("Head boy of St. Bartholomews'")
define aa = Character("Headmistress")
define co = Character("Headgirl")
define rs = Character("Random sister")
define rsii = Character("Random sister 2")
define rsiii = Character("Random sister 3")
define ga = Character("Grace Ansah")



# Relationship stats 


default tension_marcellina = 0 

 
# Game starts here


label start: 

    scene mc_dorm 
    with fade 

 
label ask_name:
    
    call screen name_input
    $ player_name = _return.strip()

    if player_name == "":
        $ player_name = "Michelle"

    return

    call ask_name
    mc "Hi! I'm [player_name]. Nice to meet you."

    "..."
    "The dorm smells faintly of detergent and old wood. Sunlight seeps through the narrow windows, lighting up the neatly arranged bunk beds."

    "[player_name] arrives, basket in hand, trying to make sense of the new environment."

 

    show miss_a normal at left 

    miss_a "Sisters! Help her settle in. Lay her bed, arrange her basket, fetch water for her, everything she needs." 

 

    "[player_name] watches the seniors move with practiced efficiency, feeling a knot of nerves in her stomach." 

    "How was she going to adjust? What about all the classes she had missed? And what if she gets bullied—or worse?"

 

    show st normal at right 

    st "Hi! I’m Stacy. I’m in charge of helping you adjust to the school." 

 

    "[player_name] notes Stacy’s friendly smile." 

    mc "Hi, Stacy. Thank you." 

 

    "Stacy gestures toward the only empty bed in the room. It is right next to a grumpy-looking senior, Marcellina." 

 

    show ma angry at center 

    "Marcellina glares briefly before turning away, muttering under her breath. [player_name] decides to..."

 

    menu: 
        "Talk to Stacy and ask about the dorm rules": 
            jump talk_stacy 

        "Check Marcellina quietly": 
            jump check_marcellina 

        "Explore the room quietly":
            jump explore_room 

 

# Scene options 

label talk_stacy: 

    $ friendship_stacy += 1
    $ trust += 1

    "[player_name] turns to Stacy, eager to learn the dorm routines." 

    st "First, you need to keep your bed neat and your locker organized every morning. I’ll show you how." 

    "Stacy showed her step by step, making [player_name] feel a little more at ease." 

    jump after_choice 

 

label check_marcellina:

    $ checked_marcellina = True
    $ friendship_marcellina += 1
    $ courage += 1
    $ kindness += 1 

    "[player_name] glances at Marcellina, who is busy tidying her bed and ignoring everyone else."

    "Her presence fels intimidating, so [player_name] decides to mind her own business for now." 

    jump after_choice 

 

label explore_room:
 
    $ curiosity += 1
    $ discovery += 1

    "[player_name] walkes slowly around the dorm, careful not to draw attention from Stacy or anyone."

    scene insides_dorm1 

    "She examines the arrangement of beds, baskets, and trunks, realizing it would be impossible to know everyone here well." 

    "Even though she stays quiet, Marcellina’s sharp eyes catches her glance more than once." 

    jump after_choice 

 

label after_choice: 

    "[player_name] continues settling in, feeling slightly less nervous but still aware of the challenges ahead." 

 
label scene2:

    # Atmosphere
    scene dorm_hallway with fade

    "The corridor hums softly with distant chatter and the occasional burst of laughter."

    "[player_name] adjusts the towel in her hands, then steps fully into the hall. She sighs visibly as she remembers that she has forgotten where the bathroom is."

    "Stacy and Marcellina stand a short distance away."

    menu:
        "Ask Stacy for directions":
            jump ask_stacy

        "Ask Marcellina for directions":
            jump ask_marcellina


label ask_stacy:

    mc "Hey… do you know where the bathroom is?"

    if checked_marcellina:
        $ friendship_stacy -= 1

        "Stacy barely looks up."
        "Her arms remain folded."

        st "You should ask someone else."

        "The conversation ends as quickly as it began."
        
        "She decides to look for the bathroom herself."

    else:
        $ friendship_stacy += 1
   
        "Stacy turns toward her, expression softening."

        st "It’s right after the strip—the place where everyone hangs their clothes."

        "She glances down the hallway."

        st "If you want, I can show you."

        "[player_name] quietly declines and heads towards the bathroom."

    jump scene2_end


label ask_marcellina:

    mc "Hey… do you know where the bathroom is?"

    if checked_marcellina:


        "Marcellina looks at her briefly."

        ma "It’s right after the strip."

        "[player_name] gives a small nod before walking off."

    else:
         
        "Marcellina ignores her."

        "[player_name] steps away almost immediately and looks for the bathroom herself."

    jump scene2_end


label scene2_end:

    "The hallway feels quieter as she makes her way to the bathroom."


label scene_three:

    scene mc_desk
    with fade

    "It is a morning physics class, right after devotion."
    "One week since the main character arrived."

    "The physics teacher is late again. No one seems surprised."

    "To save time, [player_name] quietly recopies her group's chemistry work before the next lesson."

    show vr sleepy at right

    "Beside her, Veronica lays slumped over her desk, cheek pressed against her notebook. One eye half-open."

    vr "Why are you writing so fast?"
    vr "He’s not even going to mark it."

    show ch normal at left

    "Across the room, Christiana watches them over the rim of her glasses. She hasn’t looked away once."

    menu:
        "Ignore the comment":
            $ mc_replied = False
            $ friendship_veronica -= 1
            $ safety += 1
            jump ignore_choice

        "Reply calmly":
            $ mc_replied = True
            $ friendship_veronica += 1
            $ courage += 1
            $ kindness += 1
            jump reply_choice


label ignore_choice:

    "[player_name] keps writing, pretending she hasn’t heard."

    show vr annoyed at right

    "Veronica rolles her eyes, turnes her head the other way, and goes back to her being half-sleep."

    "Christiana’s gaze lingeres for a moment longer before she finally looks away."

    jump teacher_enters


label reply_choice:

    mc "You never know what can happen."
    mc "These teachers are unpredictable."

    show veronica amused at right

    "Veronica huffs a small laugh, clearly entertained."

    show ch smug at left

    "Christiana’s lips twitch."
    "Not amusement. Calculation."

    "She leans toward the form leader and murmurs something."

    "The main character doesn’t hear it, but she feels it."

    "Her name would be written somewhere."

    jump teacher_enters


label teacher_enters:

    "Thirty minutes later, the door finally opens and the long awaited teacher comes in."

    scene classroom_doorway

    show mf in rush at center

    "Mr. Farrah walks in as though he had been chased into the classroom, apologising as usual for being late."

    show mf apologizing at center

    cl "Good morning, Mr. Farrah."

    "Mr. Farrah dismisses greetings"

    mf "Top student."

    show ca neutral at center

    "Charis looks up instantly."

    mf "Write the notes in this book on the board."

    "He hands her a marker and a small notebook, as though the rest of the class doesn’t exist."

    "As though the new curriculum rules don’t exist either."

    "Charis stands without a word."

    "No eye contact. No reaction."

    "She simply walks to the board and begins to write."

    "By now, the main character is used to this."

    "She put the group project aside, picked up her pen, and began copying from the board."

label scene_4:

    # mc spoke in Scene 3
    if mc_replied:

        # Kindness < 2 → correction
        if kindness <= 1:
            jump scene_4A

        # Kindness = 2 → excursion
        else:
            jump scene_4Bi

    # mc did not reply → excursion, isolated
    else:
        jump scene_4Bii

label scene_4A:

    scene prefect_assemblyground_morning

    with fade

    "The assembly ground is unusually quiet."

    "Rumors spread quickly — someone from [player_name]’s class is going to be corrected."

    "[player_name] stands in her house line, hands clasped, heart beating faster than it should."

    "When the head girldefault trust = 0
default confidence = 0
default curiosity = 0
default courage = 0
default kindness = 0
default friendship_veronica = 0
default friendship_stacy = 0
default friendship_marcellina = 0
default safety = 0
default discovery = 0
default checked_marcellina = False
default mc_replied = False
default stacy_points = 0 
default attitude = 0 
default reserve = 0 

# Player name variable
default player_name = ""


# Declare characters 
define mc = DynamicCharacter("[player_name]") 
define st = Character("Stacy") 
define miss_a = Character("Miss Amponsah") 
define ma = Character("Marcellina") 
define vr = Character("Veronica")
define mf = Character("Mr. Farrah")
define cl = Character("Class")
define ch = Character("Christiana")
define ca = Character("Charis")
define sr = Character("Sister")
define tr = Character("teacher")
define na = Character("Naa Aqueley")
define sd = Character("Random student")
define sd2 = Character("Random student 2")
define sd3 = Character("Rndom student 3")
define ra = Character("Head boy of St. Bartholomews'")
define aa = Character("Headmistress")
define co = Character("Headgirl")
define rs = Character("Random sister")
define rsii = Character("Random sister 2")
define rsiii = Character("Random sister 3")
define ga = Character("Grace Ansah")



# Relationship stats 


default tension_marcellina = 0 

 
# Game starts here


label start: 

    scene mc_dorm 
    with fade 

 
label ask_name:
    
    call screen name_input
    $ player_name = _return.strip()

    if player_name == "":
        $ player_name = "Michelle"

    return

    call ask_name
    mc "Hi! I'm [player_name]. Nice to meet you."

    "..."
    "The dorm smells faintly of detergent and old wood. Sunlight seeps through the narrow windows, lighting up the neatly arranged bunk beds."

    "[player_name] arrives, basket in hand, trying to make sense of the new environment."

 

    show miss_a normal at left 

    miss_a "Sisters! Help her settle in. Lay her bed, arrange her basket, fetch water for her, everything she needs." 

 

    "[player_name] watches the seniors move with practiced efficiency, feeling a knot of nerves in her stomach." 

    "How was she going to adjust? What about all the classes she had missed? And what if she gets bullied—or worse?"

 

    show st normal at right 

    st "Hi! I’m Stacy. I’m in charge of helping you adjust to the school." 

 

    "[player_name] notes Stacy’s friendly smile." 

    mc "Hi, Stacy. Thank you." 

 

    "Stacy gestures toward the only empty bed in the room. It is right next to a grumpy-looking senior, Marcellina." 

 

    show ma angry at center 

    "Marcellina glares briefly before turning away, muttering under her breath. [player_name] decides to..."

 

    menu: 
        "Talk to Stacy and ask about the dorm rules": 
            jump talk_stacy 

        "Check Marcellina quietly": 
            jump check_marcellina 

        "Explore the room quietly":
            jump explore_room 

 

# Scene options 

label talk_stacy: 

    $ friendship_stacy += 1
    $ trust += 1

    "[player_name] turns to Stacy, eager to learn the dorm routines." 

    st "First, you need to keep your bed neat and your locker organized every morning. I’ll show you how." 

    "Stacy showed her step by step, making [player_name] feel a little more at ease." 

    jump after_choice 

 

label check_marcellina:

    $ checked_marcellina = True
    $ friendship_marcellina += 1
    $ courage += 1
    $ kindness += 1 

    "[player_name] glances at Marcellina, who is busy tidying her bed and ignoring everyone else."

    "Her presence fels intimidating, so [player_name] decides to mind her own business for now." 

    jump after_choice 

 

label explore_room:
 
    $ curiosity += 1
    $ discovery += 1

    "[player_name] walkes slowly around the dorm, careful not to draw attention from Stacy or anyone."

    scene insides_dorm1 

    "She examines the arrangement of beds, baskets, and trunks, realizing it would be impossible to know everyone here well." 

    "Even though she stays quiet, Marcellina’s sharp eyes catches her glance more than once." 

    jump after_choice 

 

label after_choice: 

    "[player_name] continues settling in, feeling slightly less nervous but still aware of the challenges ahead." 

 
label scene2:

    # Atmosphere
    scene dorm_hallway with fade

    "The corridor hums softly with distant chatter and the occasional burst of laughter."

    "[player_name] adjusts the towel in her hands, then steps fully into the hall. She sighs visibly as she remembers that she has forgotten where the bathroom is."

    "Stacy and Marcellina stand a short distance away."

    menu:
        "Ask Stacy for directions":
            jump ask_stacy

        "Ask Marcellina for directions":
            jump ask_marcellina


label ask_stacy:

    mc "Hey… do you know where the bathroom is?"

    if checked_marcellina:
        $ friendship_stacy -= 1

        "Stacy barely looks up."
        "Her arms remain folded."

        st "You should ask someone else."

        "The conversation ends as quickly as it began."
        
        "She decides to look for the bathroom herself."

    else:
        $ friendship_stacy += 1
   
        "Stacy turns toward her, expression softening."

        st "It’s right after the strip—the place where everyone hangs their clothes."

        "She glances down the hallway."

        st "If you want, I can show you."

        "[player_name] quietly declines and heads towards the bathroom."

    jump scene2_end


label ask_marcellina:

    mc "Hey… do you know where the bathroom is?"

    if checked_marcellina:


        "Marcellina looks at her briefly."

        ma "It’s right after the strip."

        "[player_name] gives a small nod before walking off."

    else:
         
        "Marcellina ignores her."

        "[player_name] steps away almost immediately and looks for the bathroom herself."

    jump scene2_end


label scene2_end:

    "The hallway feels quieter as she makes her way to the bathroom."


label scene_three:

    scene mc_desk
    with fade

    "It is a morning physics class, right after devotion."
    "One week since the main character arrived."

    "The physics teacher is late again. No one seems surprised."

    "To save time, [player_name] quietly recopies her group's chemistry work before the next lesson."

    show vr sleepy at right

    "Beside her, Veronica lays slumped over her desk, cheek pressed against her notebook. One eye half-open."

    vr "Why are you writing so fast?"
    vr "He’s not even going to mark it."

    show ch normal at left

    "Across the room, Christiana watches them over the rim of her glasses. She hasn’t looked away once."

    menu:
        "Ignore the comment":
            $ mc_replied = False
            $ friendship_veronica -= 1
            $ safety += 1
            jump ignore_choice

        "Reply calmly":
            $ mc_replied = True
            $ friendship_veronica += 1
            $ courage += 1
            $ kindness += 1
            jump reply_choice


label ignore_choice:

    "[player_name] keps writing, pretending she hasn’t heard."

    show vr annoyed at right

    "Veronica rolles her eyes, turnes her head the other way, and goes back to her being half-sleep."

    "Christiana’s gaze lingeres for a moment longer before she finally looks away."

    jump teacher_enters


label reply_choice:

    mc "You never know what can happen."
    mc "These teachers are unpredictable."

    show veronica amused at right

    "Veronica huffs a small laugh, clearly entertained."

    show ch smug at left

    "Christiana’s lips twitch."
    "Not amusement. Calculation."

    "She leans toward the form leader and murmurs something."

    "The main character doesn’t hear it, but she feels it."

    "Her name would be written somewhere."

    jump teacher_enters


label teacher_enters:

    "Thirty minutes later, the door finally opens and the long awaited teacher comes in."

    scene classroom_doorway

    show mf in rush at center

    "Mr. Farrah walks in as though he had been chased into the classroom, apologising as usual for being late."

    show mf apologizing at center

    cl "Good morning, Mr. Farrah."

    "Mr. Farrah dismisses greetings"

    mf "Top student."

    show ca neutral at center

    "Charis looks up instantly."

    mf "Write the notes in this book on the board."

    "He hands her a marker and a small notebook, as though the rest of the class doesn’t exist."

    "As though the new curriculum rules don’t exist either."

    "Charis stands without a word."

    "No eye contact. No reaction."

    "She simply walks to the board and begins to write."

    "By now, the main character is used to this."

    "She put the group project aside, picked up her pen, and began copying from the board."

label scene_4:

    # mc spoke in Scene 3
    if mc_replied:

        # Kindness < 2 → correction
        if kindness <= 1:
            jump scene_4A

        # Kindness = 2 → excursion
        else:
            jump scene_4Bi

    # mc did not reply → excursion, isolated
    else:
        jump scene_4Bii

label scene_4A:

    scene prefect_assemblyground_morning

    with fade

    "The assembly ground is unusually quiet."

    "Rumors spread quickly — someone from [player_name]’s class is going to be corrected."

    "[player_name] stands in her house line, hands clasped, heart beating faster than it should."

    "When the head girl mounts the stage, the silence deepens."

    "Names are read out one by one."

    "Then—"

    "[player_name] of 1S9."

    "The words land heavier than she expects."

    "She is being corrected for talking during a physics lesson."

    "Suspension from academic and extracurricular activities follow. A week."

    "Her correction starts immediately."

    "[player_name] keps her gaze forward. She doesn’t look at anyone."

    "Stacy stands ahead of her, close enough that [player_name] sees her shoulders tense."

    "By the time the assembly is dismissed, the excursion announcement feels distant."

    "[player_name] already knows she wouldn’t be going."

    jump scene_5A  # corrected students skip excursion & clue

label scene_4Bi:

    scene excursion_line
    with fade

    "The compound buzzes with energy as students gather for the excursion."

    "[player_name] adjusts her bag strap and scans the crowd."

    "Part of her is still stuck in the morning."

    "She waited for her name."

    "It never came."

    "The relief hadn’t settled properly — it hovered, fragile, like it could be taken back."

    show vr normal at right

    vr "You look like you survived something."
    " mounts the stage, the silence deepens."

    "Names are read out one by one."

    "Then—"

    "[player_name] of 1S9."

    "The words land heavier than she expects."

    "She is being corrected for talking during a physics lesson."

    "Suspension from academic and extracurricular activities follow. A week."

    "Her correction starts immediately."


    "[player_name] keps her gaze forward. She doesn’t look at anyone."

    "Stacy stands ahead of her, close enough that [player_name] sees her shoulders tense."

    "By the time the assembly is dismissed, the excursion announcement feelsdefault trust = 0
default confidence = 0
default curiosity = 0
default courage = 0
default kindness = 0
default friendship_veronica = 0
default friendship_stacy = 0
default friendship_marcellina = 0
default safety = 0
default discovery = 0
default checked_marcellina = False
default mc_replied = False
default stacy_points = 0 
default attitude = 0 
default reserve = 0 

# Player name variable
default player_name = ""


# Declare characters 
define mc = DynamicCharacter("[player_name]") 
define st = Character("Stacy") 
define miss_a = Character("Miss Amponsah") 
define ma = Character("Marcellina") 
define vr = Character("Veronica")
define mf = Character("Mr. Farrah")
define cl = Character("Class")
define ch = Character("Christiana")
define ca = Character("Charis")
define sr = Character("Sister")
define tr = Character("teacher")
define na = Character("Naa Aqueley")
define sd = Character("Random student")
define sd2 = Character("Random student 2")
define sd3 = Character("Rndom student 3")
define ra = Character("Head boy of St. Bartholomews'")
define aa = Character("Headmistress")
define co = Character("Headgirl")
define rs = Character("Random sister")
define rsii = Character("Random sister 2")
define rsiii = Character("Random sister 3")
define ga = Character("Grace Ansah")



# Relationship stats 


default tension_marcellina = 0 

 
# Game starts here


label start: 

    scene mc_dorm 
    with fade 

 
label ask_name:
    
    call screen name_input
    $ player_name = _return.strip()

    if player_name == "":
        $ player_name = "Michelle"

    return

    call ask_name
    mc "Hi! I'm [player_name]. Nice to meet you."

    "..."
    "The dorm smells faintly of detergent and old wood. Sunlight seeps through the narrow windows, lighting up the neatly arranged bunk beds."

    "[player_name] arrives, basket in hand, trying to make sense of the new environment."

 

    show miss_a normal at left 

    miss_a "Sisters! Help her settle in. Lay her bed, arrange her basket, fetch water for her, everything she needs." 

 

    "[player_name] watches the seniors move with practiced efficiency, feeling a knot of nerves in her stomach." 

    "How was she going to adjust? What about all the classes she had missed? And what if she gets bullied—or worse?"

 

    show st normal at right 

    st "Hi! I’m Stacy. I’m in charge of helping you adjust to the school." 

 

    "[player_name] notes Stacy’s friendly smile." 

    mc "Hi, Stacy. Thank you." 

 

    "Stacy gestures toward the only empty bed in the room. It is right next to a grumpy-looking senior, Marcellina." 

 

    show ma angry at center 

    "Marcellina glares briefly before turning away, muttering under her breath. [player_name] decides to..."

 

    menu: 
        "Talk to Stacy and ask about the dorm rules": 
            jump talk_stacy 

        "Check Marcellina quietly": 
            jump check_marcellina 

        "Explore the room quietly":
            jump explore_room 

 

# Scene options 

label talk_stacy: 

    $ friendship_stacy += 1
    $ trust += 1

    "[player_name] turns to Stacy, eager to learn the dorm routines." 

    st "First, you need to keep your bed neat and your locker organized every morning. I’ll show you how." 

    "Stacy showed her step by step, making [player_name] feel a little more at ease." 

    jump after_choice 

 

label check_marcellina:

    $ checked_marcellina = True
    $ friendship_marcellina += 1
    $ courage += 1
    $ kindness += 1 

    "[player_name] glances at Marcellina, who is busy tidying her bed and ignoring everyone else."

    "Her presence fels intimidating, so [player_name] decides to mind her own business for now." 

    jump after_choice 

 

label explore_room:
 
    $ curiosity += 1
    $ discovery += 1

    "[player_name] walkes slowly around the dorm, careful not to draw attention from Stacy or anyone."

    scene insides_dorm1 

    "She examines the arrangement of beds, baskets, and trunks, realizing it would be impossible to know everyone here well." 

    "Even though she stays quiet, Marcellina’s sharp eyes catches her glance more than once." 

    jump after_choice 

 

label after_choice: 

    "[player_name] continues settling in, feeling slightly less nervous but still aware of the challenges ahead." 

 
label scene2:

    # Atmosphere
    scene dorm_hallway with fade

    "The corridor hums softly with distant chatter and the occasional burst of laughter."

    "[player_name] adjusts the towel in her hands, then steps fully into the hall. She sighs visibly as she remembers that she has forgotten where the bathroom is."

    "Stacy and Marcellina stand a short distance away."

    menu:
        "Ask Stacy for directions":
            jump ask_stacy

        "Ask Marcellina for directions":
            jump ask_marcellina


label ask_stacy:

    mc "Hey… do you know where the bathroom is?"

    if checked_marcellina:
        $ friendship_stacy -= 1

        "Stacy barely looks up."
        "Her arms remain folded."

        st "You should ask someone else."

        "The conversation ends as quickly as it began."
        
        "She decides to look for the bathroom herself."

    else:
        $ friendship_stacy += 1
   
        "Stacy turns toward her, expression softening."

        st "It’s right after the strip—the place where everyone hangs their clothes."

        "She glances down the hallway."

        st "If you want, I can show you."

        "[player_name] quietly declines and heads towards the bathroom."

    jump scene2_end


label ask_marcellina:

    mc "Hey… do you know where the bathroom is?"

    if checked_marcellina:


        "Marcellina looks at her briefly."

        ma "It’s right after the strip."

        "[player_name] gives a small nod before walking off."

    else:
         
        "Marcellina ignores her."

        "[player_name] steps away almost immediately and looks for the bathroom herself."

    jump scene2_end


label scene2_end:

    "The hallway feels quieter as she makes her way to the bathroom."


label scene_three:

    scene mc_desk
    with fade

    "It is a morning physics class, right after devotion."
    "One week since the main character arrived."

    "The physics teacher is late again. No one seems surprised."

    "To save time, [player_name] quietly recopies her group's chemistry work before the next lesson."

    show vr sleepy at right

    "Beside her, Veronica lays slumped over her desk, cheek pressed against her notebook. One eye half-open."

    vr "Why are you writing so fast?"
    vr "He’s not even going to mark it."

    show ch normal at left

    "Across the room, Christiana watches them over the rim of her glasses. She hasn’t looked away once."

    menu:
        "Ignore the comment":
            $ mc_replied = False
            $ friendship_veronica -= 1
            $ safety += 1
            jump ignore_choice

        "Reply calmly":
            $ mc_replied = True
            $ friendship_veronica += 1
            $ courage += 1
            $ kindness += 1
            jump reply_choice


label ignore_choice:

    "[player_name] keps writing, pretending she hasn’t heard."

    show vr annoyed at right

    "Veronica rolles her eyes, turnes her head the other way, and goes back to her being half-sleep."

    "Christiana’s gaze lingeres for a moment longer before she finally looks away."

    jump teacher_enters


label reply_choice:

    mc "You never know what can happen."
    mc "These teachers are unpredictable."

    show veronica amused at right

    "Veronica huffs a small laugh, clearly entertained."

    show ch smug at left

    "Christiana’s lips twitch."
    "Not amusement. Calculation."

    "She leans toward the form leader and murmurs something."

    "The main character doesn’t hear it, but she feels it."

    "Her name would be written somewhere."

    jump teacher_enters


label teacher_enters:

    "Thirty minutes later, the door finally opens and the long awaited teacher comes in."

    scene classroom_doorway

    show mf in rush at center

    "Mr. Farrah walks in as though he had been chased into the classroom, apologising as usual for being late."

    show mf apologizing at center

    cl "Good morning, Mr. Farrah."

    "Mr. Farrah dismisses greetings"

    mf "Top student."

    show ca neutral at center

    "Charis looks up instantly."

    mf "Write the notes in this book on the board."

    "He hands her a marker and a small notebook, as though the rest of the class doesn’t exist."

    "As though the new curriculum rules don’t exist either."

    "Charis stands without a word."

    "No eye contact. No reaction."

    "She simply walks to the board and begins to write."

    "By now, the main character is used to this."

    "She put the group project aside, picked up her pen, and began copying from the board."

label scene_4:

    # mc spoke in Scene 3
    if mc_replied:

        # Kindness < 2 → correction
        if kindness <= 1:
            jump scene_4A

        # Kindness = 2 → excursion
        else:
            jump scene_4Bi

    # mc did not reply → excursion, isolated
    else:
        jump scene_4Bii

label scene_4A:

    scene prefect_assemblyground_morning

    with fade

    "The assembly ground is unusually quiet."

    "Rumors spread quickly — someone from [player_name]’s class is going to be corrected."

    "[player_name] stands in her house line, hands clasped, heart beating faster than it should."

    "When the head girl mounts the stage, the silence deepens."

    "Names are read out one by one."

    "Then—"

    "[player_name] of 1S9."

    "The words land heavier than she expects."

    "She is being corrected for talking during a physics lesson."

    "Suspension from academic and extracurricular activities follow. A week."

    "Her correction starts immediately."

    "[player_name] keps her gaze forward. She doesn’t look at anyone."

    "Stacy stands ahead of her, close enough that [player_name] sees her shoulders tense."

    "By the time the assembly is dismissed, the excursion announcement feels distant."

    "[player_name] already knows she wouldn’t be going."

    jump scene_5A  # corrected students skip excursion & clue

label scene_4Bi:

    scene excursion_line
    with fade

    "The compound buzzes with energy as students gather for the excursion."

    "[player_name] adjusts her bag strap and scans the crowd."

    "Part of her is still stuck in the morning."

    "She waited for her name."

    "It never came."

    "The relief hadn’t settled properly — it hovered, fragile, like it could be taken back."

    show vr normal at right

    vr "You look like you survived something."
    vr "You look like you survived something."
    " distant."

    "[player_name] already knows she wouldn’t be going."

    jump scene_5A  # corrected students skip excursion & clue

label scene_4Bi:

    scene excursion_line
    with fade

    "The compound buzzes with energy as students gather for the excursion."

    "[player_name] adjusts her bag strap and scans the crowd."

    "Part of her is still stuck in the morning."

    "She waited for her name."

    "It never came."

    "The relief hadn’t settled properly — it hovered, fragile, like it could be taken back."

    show vr normal at right

    vr "You look like you survived something."
    vr "You look like you survived something."
    " distant."

    "[player_name] already knows she wouldn’t be going."

    jump scene_5A  # corrected students skip excursion & clue

label scene_4Bi:

    scene excursion_line
    with fade

    "The compound buzzes with energy as students gather for the excursion."

    "[player_name] adjusts her bag strap and scans the crowd."

    "Part of her is still stuck in the morning."

    "She waited for her name."

    "It never came."

    "The relief hadn’t settled properly — it hovered, fragile, like it could be taken back."

    show vr normal at right

    vr "You look like you survived something."


mc "It fells like I almost didn’t."

    "Veronica laughs softly, nudging her forward with the group."

    "As the buses come into view, [player_name] finally lets herself breathe."

    "For now, she was here."

    jump scene_5Bi

label scene_4Bii:

    scene excursion_line
    with fade

    "The compound buzzes with excitement, but [player_name] stands slightly apart from it."

    "Students cluster in familiar groups, laughter overlapping in bursts."

    "[player_name] holds onto her bag strap and waits."

    "She hadn’t spoken in class."

    "There is no fear hanging over her morning — just distance."

    "When the buses arrive, she boards quietly and takes a seat by the window."

    scene bus_outlooks

    "The excursion starts."

    jump scene_5Bii

label scene_5A:

    scene staircase_scrubbing
    with fade

    "[player_name] kneels at the steps, scrubbing a stubborn stain. Knees ache, arms burn, and the sunlight glints off the wet floor."

    show sister neutral at left

    "A sister appears nearby, standing perfectly still. Her posture is impeccable, every line of her body calm and controlled. Her eyes are fixed on [player_name]."

    "Some students pass by, stepping into the freshly scrubbed area. Soap streaks smear, puddles topple. [player_name] stiffens. The senior is watches."

    # Flashback: first “scrub again”
    "As she continues, [player_name] recalls an earlier incident that happened in the morning:"

    scene staircase_scrubbing with fade

    "[player_name] had been scrubbing when the sister first appeared and said, ‘Start again.’ She had obeyed, repeating the steps until her hands ached. The memory of that struggle made her current work feel heavier."

    scene staircase_scrubbing with fade

    "Shaking off the memory, she keeps scrubbing, determined to finish this round."

    # Sister returns second time with final instructions
    sr "Scrub again, and make sure you wipe the floor well."

    "She gives precise instructions, then steps back and walks away. [player_name] is left staring at the mixture of ruined and intact scrubbed steps. Her hands ache, her back stiffens."

    "Anna finishes scrubbing but the sister is nowhere to be found."

    # Player choice after work is fully completed

    menu:
        "Look for the sister":
            $ courage += 1
        "[player_name] searches for the sister to clarify any remaining instructions. The sister sees the work but the work is already ruined. She pardons her. She let's out a sigh of relief."

        "Run away":
            $ courage -= 1
            $ sister_targeting = True
            "[player_name] decides to leave quietly, ignoring the ruined work."


    jump scene_6
 

label scene_5Bi: 

    scene bg zoo_poolside_day 

    with fade 

    play music "audio/zoo_ambience.mp3" fadein 1.0 

 
    "After the tours, [player_name]’s batch is led to a poolside area inside the zoo." 

    "Students sit around, laughing and talking while they wait to return to school." 

    show veronica sitting at left 

    with dissolve 

    vr "Finally. My legs are dead." 

    mc "Same." 

    "A teacher steps forward, holding a paper." 

    show teacher neutral at center 

    with dissolve 

    tr "Alright. Roll call." 

    "Some students groan." 

    tr "Answer when I call your name." 

    "The teacher begins reading." 

    tr "Samantha Adu." 

    sd "Here!" 

    tr "Kofi Addo." 

    sd "Here!" 

    "The list continues." 

    "[player_name] is one of the last names, so she waits quietly." 

    "Then—" 

    tr "Angelina Mensah." 

    "The teacher’s tone changes." 

    "Not harsh like before." 

    "Softer." 

    sa "Here." 

    "[player_name] glances up." 

    "Angelina doesn’t look worried at all." 

    "The teacher continues quickly, as if nothing happened." 

    tr "Mensah, Aba." 

    sd "Here!" 

    "Veronica leans toward [player_name] slightly." 

    "Did you hear that?" 

    mc "Yeah." 

    "[player_name] keeps her expression calm, but her stomach twists." 

    "The way the teacher said Angelina’s name…" 

    "It didn’t sound like a normal roll call." 

    "[player_name]’s name is called soon after." 

    tr "[player_name]." 

    mc "Here." 

    "The teacher folds the paper." 

    tr "Good. Ten minutes. Stay here." 

    hide teacher 

    with dissolve 

    "Students go back to chatting." 

    "But [player_name] doesn’t." 

    show veronica neutral at left 

    veronica "That was weird." 

    mc "Very." 

    "[player_name] looks toward Angelina again." 

    "Angelina is already laughing with other students, completely unbothered." 

    "And somehow, that makes it worse." 

    stop music fadeout 1.0 

    jump scene_6 

label scene_5Bii_reward_no_veronica: 

    scene black 

    with fade 

    play music "audio/ambient_morning.mp3" fadein 1.0 

    "Friday comes faster than it should." 

    scene dorm_morning 

    with dissolve 

    "[player_name] wakes up earlier than usual." 

    "Not because she is excited." 

    "Because part of her still expects to hear her name called on the assembly ground." 

    "But nothing happens." 

    "No whispers."

    "No list." 

    "No correction." 

    "Still, she can't stop herself from waiting for it." 

    scene corridor_morning 

    with dissolve 

    "Outside, the school moves like it always does—sharp, organized, and emotionless." 

    "Students rush in lines." 

    "Teachers pass like they own the air itself." 

    scene assembly_ground_morning 

    with dissolve 

    "After devotion, the headmistress reminded them about the excursion." 

    "Her voice carried across the grounds like a warning disguised as kindness." 

    tr "All batches will be taken in turns." 

    tr "If you disgrace this school, you will answer to me personally." 

    "[player_name] stands still, hands clasped, eyes forward." 

    "Her courage doesn’t feel like bravery." 

    "It fells likes pretending she isn’t scared." 

    scene black 

    with fade 

    stop music fadeout 1.0 

    play music "audio/bus_ride.mp3" fadein 1.0 

    "The bus ride is loud."

    "Too loud."

    "Students laugh, argue, gossip." 

    "Even the quiet ones look lighter than they did inside school walls." 

    "[player_name] sits by the window." 

    "She doesn’t join any conversation."

    "She doesn’t need to." 

    "For the first time in a while…" 

    "she fells like she is allowed to breathe." 

    scene zoo_gate 

    with dissolve 

    "When they arrived, the heat hit them like a slap." 

    "The zoo smelled like dust, sweat, and something metallic." 

    tr "Listen up!" 

    tr "No wandering. No nonsense."

    tr "If I call your name and you don’t answer, I will personally ruin your weekend."

    "The teacher’s voice didn’t sound like a joke." 

    "It never did." 

    scene zoo_path 

    with dissolve 

    "They walk through the zoo in clusters." 

    "Guides speak. Students pretend to listen." 

    "[player_name] watches the animals." 

    "But she also watches the people." 

    "Because in a place like this, the real danger is never in the cages." 

    scene alligator_area 

    with dissolve 

    "The alligator section is the worst." 

    "Not because of the animals." 

    "Because of how close everything feels."

    "How easily something could happen and nobody would admit it." 

    "[player_name] stayed a little behind." 

    "She watches the water." 

    "The stillness." 

    "The way the surface looks harmless… until it moved." 

    scene black 

    with fade 

    "Later, after the tours, their batch iss taken to a poolside area inside the zoo’s premises."

    scene poolside 

    with dissolve 

    "Some students sit on the ground." 

    "Others lean against walls, laughing like they are outside a school for the first time in years." 

    "[player_name] stays standing." 

    "Not because she wants to." 

    "Because she doesn’t know how to relax properly." 

    tr "Everyone gather." 

    tr "I’m taking roll-call." 

    "The teacher begins calling names." 

    "[player_name] listens without meaning to."

    "Her name is always called near the end." 

    tr "…Abena Mensah."

    "A girl answers from the front." 

    "The teacher pauses for half a second, then continues." 

    "[player_name] doesn’t know why that pause fells strange." 

    "But it did." 

    tr "…Angelina Mensah."

    "Someone answers again, louder this time." 

    "The teacher’s tone changed." 

    "Not dramatically." 

    "Just slightly." 

    "But [player_name] noticed."

    tr "Good." 

    tr "Stay where I can see you." 

    "[player_name] frowns slightly." 

    "Why did that sound different?"

    "Why did it sound like a warning…" 

    "and not an instruction?" 

    tr "…" 

    "The teacher continues reading." 

    "[player_name]’s name comes later."

    tr "[player_name]." 

    mc "Here." 

    "The teacher doesn’t even look up." 

    "But [player_name] still fells something tighten in her chest." 

    "Not fear." 

    "Not exactly." 

    "Something closer to instinct." 

    "A quiet thought forming in her head....." 

    "Something is going on." 

    stop music fadeout 1.0 

    scene black 

    with fade 

    # Flag that [player_name] has noticed the first clue. 

    $ clue_teacher_tone = True
  
    jump scene_6

label episode1scene_6:  


    scene black with fade 

    play music "audio/chapel_ambience.mp3" fadein 1.5 

    "Sunday morning." 

    scene chapel_full with dissolve 

    "The chapel is packed—students from different classes, different grades, all squeezed into rows like it’s a competition." 

    "The excitement from yesterday’s excursion still hangs in the air like perfume." 

    "William House sisters sit together, scattered whispers bouncing between benches." 

    # Background chatter 

    "Some girls are already talking about the zoo." 

    "Some are arguing over who took the best pictures." 

    "Others are still laughing like they never left the bus." 

    "Then the chapel doors open." 

    show ms_amponsah at center with dissolve 

    "Ms. Amponsah steps in." 

    "The noise dies down so quickly it’s almost suspicious." 

    miss_a "Good morning, William House sisters." 

    "Good morning, Miss Amponsah!, the whole house choruses." 

    miss_a "As we all know, the school hosted an excursion yesterday." 

    miss_a "And I know you all enjoyed yourselves." 

    "The room starts filling with chatter again." 

    miss_a "Young ladies." 

    miss_a "Five-second reactions, please." 

    "The noise fades, but not completely." 

    miss_a "As you are all aware, St. Bibiana is our brother school." 

    miss_a "They will be hosting their own excursion next week." 

    "A few heads lift." 

    miss_a "Therefore, on Monday, shareholdersof both schools—as well as school heads—shall be having a meeting, here." 

    "A pause." 

    miss_a "Now, a warning." 

    "The chapel becomes quiet in a different way." 

    miss_a "No one from William House should be caught and corrected for anything." 

    miss_a "Especially on that date." 

    miss_a "If anyone is found guilty, you will be corrected on school level..." 

    miss_a "...and on house level." 

    "A ripple of discomfort passes through the benches." 

    miss_a "School sessions will follow as usual." 

    miss_a "Just avoid correction." 

    miss_a "With extra caution." 

    miss_a "That is all." 

    hide miss_a with dissolve 

    stop music fadeout 1.0 

    "She steps away from the front and gestures." 

    show sister_mawuli at center with dissolve 

    "Sister Mawuli, the house prefect, takes her place as Miss Amponsah exits." 

    "The rest of the assembly continues, but the warning stays stuck in the air." 

    # Transition out 

    scene black with fade 

    "Later..." 

    scene dorm_walkway_day with dissolve 

    play music "audio/school_day_soft.mp3" fadein 1.5 

    "As [player_name] walks back to the dorm, the chapel crowd has already scattered." 

    "Students drift in groups, like fish moving in the same direction." 

    "Then [player_name] notices her." 

    show angelina at center with dissolve 

    "For the first time, she sees Angelina Mensah in person." 

    "She heads toward the second floor, smiling at her friends like she just won the lottery." 

    "And somehow..." 

    "That smile makes [player_name]'s stomach tighten." 

    scene black with fade 

    stop music fadeout 1.0 

label ep2_scene1: 

    scene classroom_day 

    play music "audio/school_day.ogg" fadein 1.5 

    show mc neutral at left 

    show vanessa bored at right 

    "Break time." 

    "Most students had either rushed outside or gathered in small groups to talk." 

    "Meanwhile, [mc_name] sat quietly at her desk, revising her notes." 

    show vanessa thinking 

    vr "{size=-5}Do you know what the shareholders are coming to discuss today?{/size}" 

    show mc neutral 

    Mc "No idea." 

    show vanessa bored 

    vr "{size=-5}What if they’re planning to stop the food vendors from selling food?{/size}" 

    show mc unimpressed 

    "She shook her head." 

    show vanessa thinking 

    vr "{size=-5}Then what is it…?{/size}" 

    "Vanessa rested her chin on her palm, thinking deeply while [mc_name] continued revising." 

    pause 1.0 

    show vanessa shocked 

    vr "{size=-5}Yes. I’ve got it.{/size}" 

    vr "{size=-5}Maybe… just maybe they’re about to elect a new headmistress.{/size}" 

    vr "{size=-5}You know our headmistress is old. Even her fashion sense speaks for itself.{/size}" 

    show mc surprised 

    Mc "No way." 

    show vanessa smug 

    vr "Yes way." 

    "The two stared at each other." 

    "One shaking her head repeatedly." 

    "The other nodding with complete confidence."

# SCENE 2 — TWO PEOPLE 

 

label ep2_scene2: 

 
    scene compound_day 

    play music "audio/school_day.ogg" fadein 1.5 
 
    "Lunch break for the form ones." 

    "Across the compound, form three sisters leaned against walls and corridors, loudly counting down." 

    rs "EIGHT!" 

    rsii "THREE!" 

    rsiii "TEN!" 

    "Nobody even knew which countdown to follow anymore." 

    "Some sisters shouted with terrifying seriousness." 

    "Others were clearly enjoying themselves far too much." 

    show mc tired at center 

    "Under the scorching sun, [mc_name] hurried across the compound with her crockery bag swinging against her side." 

    "If she got to the dining hall late, the queue would become a punishment of its own." 

    show girl nervous at left 

    "A form one girl crashed into her shoulder." 

    Girl "Sorry!" 

    "The crockery bag slipped from [mc_name]’s hand and landed on the ground with a metallic clatter." 

    show mc surprised 

    "As she bent to pick it up, something nearby caught her attention." 

    scene assemblyhall_outside  

    show angelina neutral at left 

    show headboy neutral at right 

    "Angelina stood outside the assembly hall." 

    "Ignoring the countdown chaos completely." 

    "Beside her stood a tall boy in the official prefect attire of St. Bartholomew’s." 

    "The two seemed deep in conversation." 

    "Neither of them noticed her." 

    pause 0.5 

    Sister_voice "FREEZE!" 

    scene compound_day 

    show mc shocked 

    "Immediately, students scattered like startled birds." 

    "Correction was not something anybody volunteered for." 

    "Gripping her bag tightly, [mc_name] broke into a run again." 

    "Still, the brief image lingered somewhere in the back of her mind." 

    jump ep2_scene3 

 

# SCENE 3 — ANNOUNCEMENT 

 
label ep2_scene3: 

    scene assembly_morning 

    play music "audio/assembly_theme.ogg" fadein 1.0 

 
    "Thursday morning assembly." 

    "As usual, whispers drifted across the rows of students." 

    "Form ones talked." 

    "Form threes talked louder."

    "A sister at the front was even laughing hard enough to bend over." 

    "Then suddenly…"

    stop music fadeout 1.0 

    pause 0.5 

    "Silence." 

    "Complete silence." 

    "The kind that spread so quickly it almost felt unnatural." 

    show mc surprised at center 

    "At first, [mc_name] only caught the end of the announcement." 

    co "…the appointment of the new headmistress." 

    "New headmistress?"

    "Her thoughts stalled." 

    "Wait." 

    "New rules too… right?" 

    "New officials?" 

    "Around her, the atmosphere shifted almost instantly." 

    "Some students looked curious." 

    "Others already looked exhausted by possibilities that did not even exist yet." 

    sd "{size=-5}What if they cancel visiting weekends?{/size}" 

    sd2 "{size=-5}No, no. They’re definitely changing dining hall rules.{/size}"  

    "The head girl stepped away from the microphone." 

    "Only then did [mc_name] notice someone else standing near the stage." 

    show headboy formal at right 

    "A boy in the official prefect attire of St. Bartholomew’s." 

    "For a brief second, he looked strangely unsure of himself." 

    "Then his expression settled." 

    ra "Good morning." 

    ra "My name is Adrian Mensah, head boy of St. Bartholomew’s." 

    ra "On behalf of our officials, I would like to express our support for the incoming administration." 

    ra "I believe the management of both schools will improve greatly." 

    "He smiled politely." 

    "And suddenly…" 

    show mc thinking 

    "Recognition clicked." 

    "She had seen him before." 

    jump ep2_scene4 

 

# SCENE 4 — THE INAUGURATION 

 
label ep2_scene4: 


    scene assemblyhall_inauguration 

    play music "audio/ceremony.ogg" fadein 1.5 

    "Saturday morning." 

    "The entire assembly hall seemed heavier than usual." 

    "Rows of students sat unusually straight." 

    "Even whispers sounded cautious." 

    show headmistress neutral at center 

    "The new headmistress processed toward the platform in official inauguration attire." 

    "She was neither stern-looking nor particularly warm." 

    "Just composed." 

    "Too composed." 

    "All eyes followed her movements." 

    "A ceremonial torch was placed into her hands." 

    "Whispers rippled briefly across the hall before fading again." 

    "Then she stepped toward the microphone." 

    pause 1.0 

    aa "Good morning, girls." 

    aa "Discipline is not punishment." 

    aa "It is structure." 

    aa "And from today onward, this school will have plenty of it." 

    "That was all." 

    "The speech ended so abruptly that several students looked genuinely confused." 

    "The headmistress stepped away from the microphone without another word." 

    "Near the side of the platform, Adrian stood still." 

    show headboy uneasy at right 

    "For the briefest moment, he looked like he wished he were somewhere else entirely." 

    "Then the expression disappeared." 

    show headboy formal at right 

    ra "The updated school rules will be posted on the notice board later this afternoon." 

    "A wave of uneasy murmuring spread through the hall."

    show mc thinking 

    "And once again, [mc_name] remembered seeing him beside Angelina earlier that week." 


label ep2_scene5: 

 

    scene bg dininghall_noticeboard_day 

    with dissolve 

 

    show mc neutral at left 

    show stacy neutral at right 

    with dissolve 


    "A crowd had formed around the notice board outside the dining hall." 

    "Pinned neatly beneath yesterday's meal schedule was a fresh sheet of paper." 

    "At the top, in bold red ink, were the words:" 

    centered "{b}NEW DORMITORY REGULATIONS{/b}\nEffective Immediately" 

    centered "1. Curfew is now 8:45 PM." 

    centered "2. Students must remain in their assigned dormitory block after curfew." 

    centered "3. No gatherings of more than three students after lights out." 

    centered "4. Students are prohibited from entering restricted areas without permission." 

    centered "5. Failure to comply will result in disciplinary action." 

    mc "8:45?" 

    mc "Since when?" 

    mc "No gatherings after lights out..."  

    mc "Okay..." 

    mc "Restricted areas?" 

    "You stare at the paper a moment longer before stepping back." 

    st "Are they serious?" 

    st "Why does this feel dramatic for no reason?" 

 

    menu: 
        "Reply casually": 
            $ mc_attitude += 1 
            jump ep2_scene5_casual 

        "Reply enthusiastically": 
            $ stacy_points += 1 
            jump ep2_scene5_enthusiastic 
 
        "Reply coldly": 
            $ mc_reserve += 1 
            jump ep2_scene5_cold 

 
 

label ep2_scene5_casual: 

    mc "Maybe someone got caught doing something stupid." 

    st "Then why punish everyone?" 
 
    mc "Because that's how schools work." 

    st "Unfortunately true." 

    jump ep2_scene5_end 

label ep2_scene5_enthusiastic: 

    mc "Honestly?" 

    mc "This might actually make things more interesting." 

    st "Interesting?" 

    mc "Think about it. New rules usually mean something happened." 

    st "Or someone important got angry." 

    mc "Exactly." 

    st "You worry me sometimes." 

    jump ep2_scene5_end 
 
label ep2_scene5_cold: 

    mc "They're just rules." 

    st "Just rules?" 

    st "They literally moved curfew." 

    mc "Then be in your dorm by 8:45." 

    st "Wow." 

    st "You are no fun at all." 

    jump ep2_scene5_end 

label ep2_scene5_end: 
 
    if stacy_points >= 3: 

    st "Still..." 

    st "If everyone's talking about this tonight, you're sitting with me." 

    mc "We'll see." 

    elif mc_reserve >= 3: 

    st "You're weirdly calm about this." 

    mc "Should I panic instead?" 

    st "Maybe a little." 

    else: 

    st "Something about this feels off." 

    mc "Yeah." 

    mc "Maybe." 

    "The bell rings across the compound." 

    st "Great. Time for class." 

    hide stacy with dissolve 

    hide mc with dissolve 


    jump ep2_scene6 

 

if naa_active: 

 

default naa_relationship = 0 

default naa_active = True 

 

label ep2_scene6: 

 

    scene bg noticeboard_friday 

    with dissolve 

    show mc neutral at center

    with dissolve 



    "Friday morning." 

    "You stand in front of the notice board again." 

    "This time, not for rules." 

    "Sheets of paper overlapped across the board—class lists, announcements, club notices..." 

    "And somewhere among them..." 

    "the work-duty list." 

    mc "(Where did they even paste it?)" 

    mc "(1A... 1B... 2C...)" 

    mc "(Why is this so long?)" 

    "You scan line after line, trying to find your class among the dreadful list of assigned working areas." 

    voice "tap" 

    "A light tap lands on your shoulder." 

 

    show naa neutral at right

    with dissolve 



    na "Hey." 

    na "[player_name]." 

    "You turn." 

    " points to another corner of the board." 

    na "You're looking at the wrong paper." 

    na "There." 

    "You follow her finger." 

    "A smaller sheet is pinned beside the work-duty list." 

    "The title reads:" 

    centered "{b}SHOUT OUTS{/b}" 

    "Your eyes move down the page." 

    "Then stop." 

    "Your name is written there." 

    "Boldly." 

    mc "(...What?)" 

    "You slowly look at Naa." 

    "She stares back at you like she's seeing someone completely new." 

 

    menu: 
        "What? Have you not received a shout-out before?": 
            $ naa_relationship -= 2 
            jump ep2_scene6_negative 

        "Who on earth is writing to me?": 
            $ naa_relationship += 2 
            jump ep2_scene6_positive 

 
 

label ep2_scene6_positive: 


    mc "Who on earth is writing to me?" 

    na "You really don't know?" 

    mc "No." 

    "Naa glances back at the paper." 

    na "It happens." 

    na "Sometimes boys get a girl's details from someone and send a shout-out to test their luck." 

    mc "Randomly?" 

    na "Very." 

    mc "That is slightly terrifying." 

    na "Welcome to school." 

    mc "Should I be concerned?" 

    na "Not yet." 

    na "Unless he starts writing poetry." 

    mc "That bad?" 

    na "Worse." 

    "You laugh before looking back at the paper." 

    "Your name still sits there like it belongs to someone else." 
 

    jump ep2_scene6_end 

 
 

label ep2_scene6_negative: 


    mc "What?" 

    mc "Have you not received a shout-out before?" 

    "Naa's expression shifts." 

    "Only slightly." 

    na "..." 

    "She lowers her hand." 

    na "Right." 

    "Without another word, she checks the work-duty list beside you." 

    "Finds her class." 

    "Then walks away." 

    hide naa with dissolve 

    "You look back at the shout-out sheet." 

    "Your name is still there." 

    "Bold." 

    "Impossible to ignore." 

    $ naa_active = False 

    jump ep2_scene6_end 

 
 

label ep2_scene6_end: 

 
    if naa_relationship >= 2: 

    na "By the way..." 

    na "Your class is assigned behind the assembly hall." 

    mc "Thanks." 
 
    na "Try not to look too shocked all day."
 
    mc "No promises." 

    "The first bell rings." 

    "Students begin leaving the notice board in noisy clusters." 

    "You stay for one second longer..." 

    "still staring at your name." 

    hide mc with dissolve 

    hide naa with dissolve 


jump ep2_scene7


label ep2_scene7: 

 

    scene bg classroom_saturday_day 

    with dissolve 

 

    show mc neutral at left 

    show vanessa grin at right 

    with dissolve 



    "Saturday." 

    "The classroom sat unusually quiet." 

    "Most students were outside for work duty." 

    "Only the distant scrape of chairs and voices from the compound drifted through the windows." 

    "The folded shout-out lay on your desk." 

    "Vanessa leaned over before you even touched it." 

    vr "Open it." 

    mc "..." 

    vr "Come on." 

    vr "I still can't believe you of all people received a shout-out." 

    vr "Who sent it?" 

    vr "Hurry up." 

    "You unfold the paper carefully." 

    "Vanessa shifts closer beside you, whisper-reading over your shoulder." 

    "Your eyes move over the first lines." 

    mc "(Richard Acquay...)" 

    "The head boy of St. Bartholomew's." 

    "You keep reading." 

    "Vanessa goes quiet." 

    "Your eyes move faster down the page." 

    show mc surprised 

    "Surprise." 

    show mc shocked  

    "Shock." 

    show mc neutral 

    "Then stillness." 

    "You reread one line." 

    "Then another." 

    "By the time you reach the end, your fingers have tightened slightly around the paper." 

    mc "Why...?" 

    "You don't mean to say it aloud." 

    "But Vanessa hears." 

 

    if varonica_trust <= 2: 



    show vanessa suspicious  

    vr "Why what?" 

    mc "..." 

    vr "Hold on." 

    vr "You know something about this?" 

    mc "No." 

    vr "Then why are you looking like that?" 

    "You fold the paper without answering." 

    vr "Michelle." 

    vr "Are you hiding something from me?" 

    mc "I said no." 

    "Vanessa studies your face for a second longer." 

    "Then leans back in her chair." 

    vr "Fine." 

    "The silence between you feels different after that." 

 

        $ veronica_relationship -= 1 

 

    else: 


    show veronica grin 

    vr "No way." 

    vr "No actual way." 

    mc "..." 

    vr "The head boy?" 

    vr "Of St. Bartholomew's?" 

    vr "Writing to you?" 

    mc "Vanessa." 

    vr "What?" 

    vr "Should I start greeting Madam Richard now?" 

    mc "Please stop." 

    vr "I mean it." 

    vr "He even writes like a head boy." 

    mc "I'm serious." 

    vr "And I'm serious too." 

    "She laughs quietly." 

    "But you barely hear her." 

    "Your eyes remain fixed on the folded paper in your hand." 

 

        $ veronica_relationship += 1 

 

    "Richard Acquay." 

    "The assistant head boy of St. Bartholomew's." 

    "Writing to you." 

    "About something you don't understand." 

    "And somehow expecting that you might." 

    "Outside, voices rise from the compound." 

    "Someone shouts across the courtyard." 

    "The siren rings somewhere in the distance." 

    "But in the classroom, everything feels strangely still." 

 

    hide veronica 

    hide mc 

    with dissolve 



    jump ep2_scene8 

 

# EPISODE 2 FINALE — SCENE 8: IDENTITY 

# Unlocked if MC's previous choices suggest interest in drama/curiosity. 

 

label ep2_scene8_identity: 

 

    scene bg dorm_day 

    with fade 

 

    "It was the first Saturday of December." 

    "Visiting day." 

    "Girls moved around the dorm in excitement—opening trunks, arranging clothes, rushing to meet their families downstairs." 

    "I sat on my bed, folding my things into neat piles." 

 

    show grace neutral at center 

    with dissolve 

 

    "A shadow fell over me." 

    "I looked up." 

    "Sister Grace Ansah stood in front of me." 

    "The strict dorm monitor." 

    "Rule-focused. Sharp-eyed. Never out of place." 

    "But something about her looked wrong."

    "One hand rested against her waist." 

    "Her breathing was uneven, like she had hurried upstairs." 

    ga "You have a visitor." 

    mc "A visitor?" 

    "My hands froze on the cloth in my lap." 

    ga "They're waiting downstairs." 

    "I stood immediately." 

    "A visitor?" 

    "That couldn't be right." 

    "My parents told me they wouldn't be coming." 

    "Not this month." 

    "I looked at Sister Grace again, hoping she'd explain." 

    "She didn't." 

    "She only watched me." 

 

    hide grace 

    with dissolve 

 

    "I set the folded clothes aside." 

    "My heartbeat suddenly    scene bg staircase 

    with dissolve 

 

    "I held the railing as I walked down the stairs." 

    "Parents' voices echoed from below." 

    "Laughter." 

    "Conversations." 

    "Footsteps." 

 

    "But all I could hear was my heartbeat." 

 

    mc "Who came to see me?" 

 

    scene bg visiting_area 

    with fade 

 

    "I reached the last step." 

    "And stopped." 

    "My breath caught." 

 

    stop music fadeout 2.0 

    scene black 

    with Fade(1.0, 0.5, 1.0) 
 
 
    "..." 

 

    jump ep3_start 

 

# EPISODE 3 — SCENE 1: THE VISITOR 

 

scene bg warners_river_day: 

 
    "Visiting day at Warners River was never quiet." 

    "Voices carried across the compound. Parents waved from tables. Students laughed too loudly. Bags changed hands. Food containers opened. Chairs scraped against concrete." 

    "MC stepped into the visiting area, brushing her fingers against the side of her dress." 

    "Then she stopped." 

    "Standing beside her house table, pen in hand, signing neatly into the visitor’s book..." 

    "...was Richard Acquay." 

    "The assistant head boy." 

    "For a second, MC thought she had seen the wrong person." 

    "But Richard looked up." 

    "And saw her." 

    "MC turned around immediately." 

    "Her body moved before her mind could." 

    "She took two steps away and forced herself to breathe." 

    "Why is he here?" 

    "No." 

    "The question was not why." 

    "It was how." 

    "How had Richard Acquay come to Warners River..." 

    "...as her visitor?" 

    mc "Think clearly." 

    "She stared at the dusty path ahead of her as if the answer might be written there." 

    Behind her— 
    r "MC." 

    "Her name." 

    "His voice saying her name startled her more than seeing him had." 

    "MC turned slowly." 

    "And smiled." 
 
    "It was the same smile she always gave whenever nerves found her before words did." 

    mc "Richard." 

    "He gave a small nod." 

    r "Can we talk?" 

    "MC glanced around." 

    "Too many people." 

    "Too many ears." 

    Without another word, she led him away from the visiting area. 

 

scene bg school_bench_day: 

 
    "They sat on a stone bench in front of an empty classroom block." 

    "No footsteps passed nearby." 

    "No voices interrupted them." 

    "Only wind moving through the trees and the distant noise from visiting grounds." 

    "Richard leaned forward, elbows resting against his knees." 

    "For once, the assistant head boy looked unsure where to begin." 

    "MC waited." 

    "Then he started talking." 

    "And with every sentence..." 

    "...MC felt herself pulled deeper into something she still did not understand." 

    "Even after everything he told her..." 

    "...one question remained in her mind." 

    "Why was she involved in any of it?" 

 
 

# EPISODE 3 — SCENE 2: BACK IN THE DORM 

 

scene bg dorm_evening: 

  
    "By the time MC returned to the dorm, the news had already arrived before she had." 

    "The door barely opened before stacy threw herself toward her." 

 

if stacy_relationship >= 6: 

    st "MC!" 

    "Stacy grabbed both her arms." 

    st "Was that Richard Acquay?" 

    st "Why was he here?" 

    st "Why did he sign in as your visitor?" 

    st "How do you know him?" 

    "Questions came faster than MC could answer." 

    "Girls across the room looked up from folding clothes and washing buckets." 

    "Some stared openly." 

    "Others pretended not to." 

    "But everyone was listening." 

    "MC forced a small smile." 
 
    mc "Slow down." 

    "stacy lowered her voice immediately." 

    st "Sorry." 

    st "I just... everyone has been talking." 

    "MC's stomach tightened." 

    "Even with stacy beside her, the room suddenly felt too small." 

 

else: 



    "The room quieted when MC entered." 

    "Not silent." 

    "Just the kind of quiet people make when they have been talking about you seconds before." 

    "stacy sat on her bed among the others." 

    "She looked up." 

    "Their eyes met for barely a second." 

    "Then stacy turned back to the conversation beside her." 

    "A whisper followed." 

    "Another." 

    "Then laughter quickly swallowed." 

    "mc said nothing." 

    "mc changed quickly." 

    "Pulled on another shirt." 

    "Folded away the one she wore outside." 

    "Brushed her hair with shaking fingers." 

    "The air in the dorm felt heavier than before." 

    "Suffocating." 

    "Like every glance had touched her before she could escape it." 

 

if stacy_relationship >= 6: 

    st "MC..." 

    "MC picked up her notebook." 

    mc "I'm going out for a bit." 

    "stacy hesitated before standing." 

    st "I'll come." 

 

    scene bg classroom_block_evening 



    "They walked in silence past the dormitories." 
 
    "Past the courtyard." 

    "Until they reached the empty classroom block." 

    "stacy sat beside her on the stone bench." 

if stacy_gossiped: 

    "For once, stacy had nothing to say." 

    "MC looked ahead." 

    "The silence between them felt strange." 

 
else: 

    st "So..." 

    st "Are you going to tell me why the assistant head boy came all the way here to visit you?" 

    "MC stared ahead." 

    "She did not answer." 

    "stacy looked at her for a moment..." 

    "...then let the silence stay." 

else:

    scene bg classroom_block_evening 

    "MC walked alone to the classroom block." 

    "She sat on the stone bench outside for a while, letting the evening air settle around her." 

    "Footsteps approached." 

    v "MC?" 

    "MC looked up." 

    "Veronica stood there, holding a notebook to her chest." 

    v "You've been missing since prep." 

    mc "Just needed air." 

    v "Everything okay?" 

    mc "Yeah." 

    "Veronica sat beside her." 

    "They talked about ordinary things." 

    "Assignments." 

    "Teachers."  

    "Who forgot prep notes again." 

    "Nothing important." 

    "And MC was grateful for that." 

    "Still..." 

    "No matter who sat beside her..." 

    "...MC could not shake the feeling that something had changed." 

    "Like the entire dorm had looked at her differently." 

    "Like her social life had been weighed, discussed..." 

    "...and quietly decided by everyone except her." 

 
 

# EPISODE 2 — SCENE 3: THE KNOCK 

 

scene bg school_lane_morning 

 

    "Saturday morning line-up had already begun." 

    "The girls stood in straight rows beneath the pale morning sky." 

    "Blue skirts." 

    "Sleepy eyes." 

    "And silence that was never really silence." 

    "MC looked down at herself and sighed." 

    "The front of her white shirt was stained grey." 

    "Dirty mop water." 

    "Still wet in places." 

    "It had dripped from the first floor balcony only minutes earlier." 

    "Right onto her." 

    "She still didn't know whether it had been an accident." 

    "Or not." 

    "The house gate behind her was locked." 

    "No way back inside." 
 
    "No spare shirt." 

    "No escape from line-up." 

    "Only inspection ahead." 

    "The Head Girl stood near the front like a guard at a checkpoint." 
  
    "Beside her stood the Second Assistant Girls’ Prefect, clipboard tucked beneath her arm." 

    "They inspected collars." 

    "Socks." 
 
    "Hair." 

    "Shoes." 

    "And wrote names down without mercy." 

    "MC joined the slow-moving line." 

    "Her stomach twisted." 

    "If the stain was noticed, she would be stopped immediately." 

    "Sent out of line." 

    "Questioned." 

    "Possibly punished." 
 
    "Knock. Knock. Knock." 

    "The sound echoed across the compound." 

    "Sharp." 

    "Fast." 
 
    "Urgent." 

    "It came from De'Pores House." 
 
    "The Head Girl looked toward the building." 

    "Then looked forward again." 

    hg "Face front." 

    "The line obeyed." 
 
    "But whispers rose anyway." 

    girl_1 "Who's knocking?" 

    girl_2 "Is someone locked in there?" 

    girl_3 "This early?" 

    "Knock. Knock. Knock." 

    "Louder this time." 

    "The Head Girl's expression hardened." 

    hg "Quiet." 

    "The murmuring dropped." 

    "But never disappeared." 

    "It remained under everything like moving air." 

    "MC kept walking." 

    "Step." 

    "Step." 

    "Step." 

    "Eyes forward." 

    "Heart racing." 

    "The Head Girl turned again toward De'Pores." 

    "The knocking continued." 

    "MC passed directly in front of her." 

    "The stain cold against her shirt." 

    "But the Head Girl never looked down." 
 
    "Never noticed." 

    "MC crossed to the other side of the lane." 

    "Free." 

    "She kept walking." 

    "Not too fast." 

    "Not too slow." 

    "Only when she reached the corridor did she breathe." 

    "A breath she felt she had been holding all morning." 

    "Behind her..." 

    "Knock. Knock. Knock." 

    "The sound continued." 

 
 

# EPISODE 3 — SCENE 4: THE BOND 

 

scene bg assembly_ground_morning 



    "Morning devotion felt longer than usual." 

    "The girls stood in rows beneath the bright Wednesday sun." 

    "Uniforms straight." 

    "Faces forward."  

    "Half-awake." 

    "Half-listening." 

    "And entirely ready for gossip." 

    "Mackenzie stood with her house, arms folded behind her back." 

    "Her attention drifted in and out of the Headmistress's speech." 

    "Announcements." 

    "Warnings." 

    "Integrity." 

    "Discipline." 
 
    "The usual." 
     
    hm "...and students are reminded once again that honesty remains one of the core values of this institution." 
    
    "Mackenzie barely listened." 
    
    "Then—" 
    
    hm "Mackenzie." 

    "Her head lifted." 

    hm "Step forward." 

    "For one second, Mackenzie thought she had heard wrong." 

    "The girl beside her glanced over immediately." 

    "Then another." 

    "And another." 

    "The line shifted around her." 

    "Mackenzie stepped out slowly." 

    "The entire assembly watched her walk toward the stage." 

    "Her face stayed calm." 

    "But confusion had already found its way into her chest." 

    "At the front stood the Headmistress." 

    "Beside her was a teacher holding papers." 

    "And just behind them..." 

    "...stood her sister." 

    "Arms folded." 
 
    "Expression unreadable." 

    "Mackenzie stopped before the stage." 

    mc "Why am I here?" 

    "No answer." 

    "The Headmistress continued speaking into the microphone as though Mackenzie had not spoken." 

    hm "Every student must understand that actions have consequences." 

    "Mackenzie looked past her."  

    "Straight at her sister." 

    mc "Why am I being called?" 

    "Her sister kept her face stern." 

    "Said nothing." 

    "Mackenzie's voice lowered." 

    mc "Why am I here?" 

    "Her sister finally leaned slightly toward her." 

    sis "You were reported." 

    "Mackenzie frowned." 
 
    mc "For what?" 

    sis "Signing on behalf of another student." 

    "Mackenzie stared." 

    "As if the sentence had reached the wrong person." 

    "What?" 

    "The Headmistress finished her speech and turned toward the table." 

    hm "Bring the pen." 

    "A pen was placed in her hand." 
 
    hm "Sign here." 

    "Mackenzie looked down at the paper." 

    "A disciplinary bond." 

    "Her name already written above the signature line." 

    "Her fingers tightened around the pen." 

    mc "No." 

    "The Headmistress paused." 

    "Murmuring began immediately across the assembly." 

    mc "I'm not the one." 

    "The whispers grew louder." 

    girl_1 "What happened?" 

    girl_2 "Wasn't it her?" 

    girl_3 "I heard she signed for someone." 
    
    "Mackenzie lifted her head." 
    
    mc "There must be a mistake." 
    
    "The Headmistress held out her hand for the pen." 
   
    hm "This matter will be discussed further." 

    "The crowd continued reacting." 

    "Whispers." 

    "Gasps." 

    "Open staring." 

    "The Headmistress stepped toward the microphone." 

    hm "Quiet." 

    "The noise reduced." 

    hm "Reactions should last five seconds." 

    "Silence." 
 
    "Or something close to it." 

    "Mackenzie stood frozen before the stage." 

    "With hundreds of eyes on her." 

    "And no clearer answer than when she had first been called forward."

# EPISODE 3 — SCENE 5: WHY ME?  
 
  
 
scene bg classroom_day  
 
 
 
    "The classroom was louder than usual."  
 
    "Not loud in the normal way."  
 
    "Not laughter."  
 
    "Not arguments."  
 
    "Whispers."  
 
    "Soft."  
 
    "Constant."  
 
    "And always ending the moment Mackenzie looked up."  
 
    "Mackenzie sat at her desk, staring at an open notebook she had not read once."  
 
    "Girls hovered nearby."  
 
    "Some leaning against desks."  
 
    "Some pretending to borrow pens."  
 
    "Some simply standing close enough to ask..."  
 
    "...but not brave enough to."  
 
    girl_1 "Mackenzie..."  
 
    girl_2 "What actually happened?"  
 
    girl_3 "Did you really sign it?"  
 
    "Mackenzie said nothing."  
 
    "The silence answered for her."  
 
    A Sister appeared at the classroom doorway.  
 
    sis "Mackenzie."  
 
    "Every head turned."  
    
    s "DC office."  
  
    "Mackenzie stood."  
 
    "Chairs shifted."  
 
    "Whispers rose again."  
 
    "She ignored the eyes following her to the door."  
 
    "And the louder whispers after she left."  
 
  
 
scene bg office_corridor_day  
 
 
 
    "The walk to the DC office felt longer than usual."  
 
    "Each step heavier than the last."  
 
  
 
scene bg dc_office_day  
 
 
    "Mackenzie entered."  
 
    "And stopped."  
 
  
 
# BRANCH A — MC present and speaks  
 
if mc_mackenzie_relationship >= 7 and mc_remembers_sister:  
 
  
 
    "MC was already there."  
 
    "Standing near the desk."  
 
    "Arms folded."  
 
    "Waiting."  
 
    "Mackenzie's eyes moved from her..."  
 
    "...to the woman seated behind the desk."  
 
    "...then back again."  
 
    dc "Good. You're here."  
 
    dc "Please sit."  
 
    "Mackenzie remained standing."  
 
    "MC spoke before anyone else could."  
 
    mc "She didn't do it."  
 
    "The room went quiet."  
 
    "Mackenzie looked at her sharply."  
 
    mc "The person you saw wasn't Mackenzie."  
 
    mc "There's another sister who looks like her."  
 
    dc "Another sister?"  
 
    mc "Yes."  
 
    mc "Same face. Similar height."  
  
    mc "You accused the wrong person."  
 
    "The DC officer exchanged a glance with the teacher beside her."  
 
    "Paper shifted."  
 
    "A long silence followed."  
 
    dc "...We'll investigate further."  
 
    "The bond paper was slowly removed from the table."  
 
    "Mackenzie stared at it being taken away."  
 
    "Like she wasn't fully sure it was real."  
 
    "When they stepped outside..."  
 
    "Neither spoke immediately."  
 
    mk "You remembered."  
 
    mc "Of course I did."  
 
    "Mackenzie looked away before MC could read her expression."  
 
    "But something inside her softened."  
 
  
 
# BRANCH B — MC present but silent  
 
elif mc_mackenzie_relationship >= 4 and mc_remembers_sister:  
 
  
 
    "MC was already there."   
 
    "Mackenzie's breath caught."  
 
    "Relief arrived before she could stop it."  
 
    "MC remembered."  
 
    "She had to."  
 
    "The sister."  
 
    "The resemblance."  
 
    "The explanation."  
 
    dc "Mackenzie, sit."  
 
    "Mackenzie sat."  
 
    "The bond paper was placed before her."  
 
    dc "Sign."  
 
    "Mackenzie looked at MC."  
 
    "MC stayed quiet."  
 
    "Eyes lowered."  
 
    "Saying nothing."  
 
    mk "MC."  
 
    "Nothing."  
 
    mk "Tell them."  
 
    "Silence."  
 
    "The room suddenly felt smaller."  
 
    "Hotter."  
 
    "Crueler."  
 
    dc "Sign."  
 
    "Mackenzie's fingers tightened around the pen."  
 
    "She signed."  
 
    "The scratching of ink across paper sounded louder than anything else in the room."  
 
    scene bg office_corridor_day  
 
    "Outside the office—"  
 
    mk "You knew."  
 
    "MC opened her mouth."  
 
    mk "You knew."  
 
    "Mackenzie's voice shook."  
 
    mk "And you said nothing."  
 
    "She walked away before MC could answer."  
 
    "The resentment stayed with her long after."  
 
  
 
# BRANCH C — MC absent  
 
else:  
 
  
 
    "MC was not there."  
 
    "Only the DC officer."  
 
    "A teacher."  
 
    "And the bond paper waiting on the desk."  
 
    dc "Sit."  
 
    "Mackenzie sat."  
 
    dc "You understand why you're here."  
 
    mk "No."  
 
    dc "You were identified."  
 
    mk "Then they identified the wrong person."  
 
    dc "Mackenzie."  
 
    "The DC officer slid the paper toward her."  
 
    dc "Sign it."  
 
    mk "I didn't do it."  
 
    dc "Sign."  
 
    "Her voice remained calm."  
 
    "Which somehow felt worse."  
 
    "Mackenzie looked at the signature line."  
 
    "Her own name already written there."  
 
    "Waiting."  
 
    "Like the decision had already been made before she entered."  
 
    "After a long silence..."  
 
    "She signed."  
 
    scene bg office_corridor_day   
 
    "When she stepped out of the office..."  
 
    "...she felt smaller."  
 
    "Like something had been taken from her."  
 
    "And nobody had even needed to raise their voice to do it."  
 
    "Why me?"  
 
    "The question stayed with Mackenzie the rest of the day."  
 
    "And no answer ever came."  
 
  
 
# EPISODE 3 — SCENE 6: THE ANNEX  
 
  
 
scene bg arts_block_morning  
 
 
 
    "It was Saturday."  
 
    "stacy was the first to arrive at the Arts Block."  
 
    "The corridor was unusually quiet."  
 
    "Most girls were still drifting between breakfast and prep."  
 
    "stacy adjusted the books in her arms and climbed the stairs."  
 
    "Then she stopped."  
 
    "At the far end of the corridor..."  
 
    "...the Headmistress's personal assistant unlocked the Annex door."  
 
    "He slipped inside."  
 
    "And locked it behind him."  
 
    "Stacy stared."  
 
    st "(The Annex?)"  
 
    "That room was supposed to be a reading room."  
 
    "Unused most days."  
 
    "But stacy knew better."  
 
    "Girls talked."  
 
    "Sisters talked more."  
 
    "And stacy listened."  
 
    "She walked on."  
 
    "But not before memorising exactly what she had seen."  
 
  
 
scene bg classroom_day  
 
 
 
    "Later, stacy sat in class pretending to listen."  
 
    "Her notebook stayed open."  
 
    "Her attention didn't."  
 
    "She kept thinking about the locked door."  
 
    "And who could already be inside it."  
 
    "A note landed on her desk."  
 
    girl "Run this to the next block for me and I'll tell you what happened after prep."  
 
    "stacy smirked."  
 
    st "Deal."  
 
  
 
scene bg arts_block_stairs_day  
 
  
 
# BRANCH A — MC reaches the block  
 
if mc_visits_stacy:  
 
    "By the time stacy reached the staircase, MC was already there waiting."  
 
    st "You're late."  
 
    mc "By thirty seconds."  
 
    st "Still late."  
 
    "They began climbing."  
 
    "Halfway up—"  
 
    "Footsteps."  
 
    "Measured."  
 
    "Approaching from above."  
 
    "The Headmistress descended the staircase."  
 
    "stacy immediately stepped aside."  
 
    "MC did the same."  
 
    "The Headmistress passed..."  
 
    "Then stopped."  
 
    hm "You."  
 
    "MC looked up."  
 
    "stacy looked between them."  
 
    "The Headmistress's eyes remained on MC."  
 
    hm "We've met before."  
 
    mc "Yes, Sister."  
 
    "A pause."  
 
    hm "Stay focused on your programme."  
 
    hm "Some matters become heavier the more hands carry them."  
 
    "MC said nothing."  
 
    hm "Enjoy your afternoon."  
 
    "She walked past." 
  
    "Her heels echoed down the stairs."  
 
    "stacy waited until the sound disappeared."  
 
    st "Why does she know you?"  
 
    mc "I don't know."  
 
    "stacy raised a brow."  
 
    "MC began walking."  
 
    "stacy followed."  
 
    "But she didn't believe that answer for a second."  
 
  
 
# BRANCH B — MC doesn't reach before  
 
else:  
 
    "stacy waited near the staircase."  
 
    "The Headmistress's personal assistant came out of the Annex."  
 
    "Then the Headmistress herself stepped into the corridor."  
 
    "stacy lowered her eyes at once."  
 
    "The two walked past her without a word."  
 
    "But stacy noticed everything."  
 
    "The locked door."  
 
    "The low voices."  
 
    "The quick silence."  
 
  
 
scene bg path_day  
 
  
 
    "Later, stacy met MC near the path between the blocks."  
 
    st "Come with me."  
 
    mc "Where?"  
 
    st "Errand."  
 
    mc "That doesn't answer my question."  
 
    st "Exactly."  
 
    "MC followed anyway."  
 
    "As they walked..."  
 
    "stacy kept replaying the morning in her head."  
 
    "The locked Annex."  
 
    "The personal assistant."  
 
    "The Headmistress."  
 
    "And if MC had been there..."  
 
    "...would she have seen it too?"  
 
  
  
 
# EPISODE 3 — SCENE 8  
 
# Saturday Morning Assembly  
 
  
 
scene school_assembly_morning  
 
 
    with fade 
 
 
    play ambience "morning_school.mp3"  
 
    "The Saturday sun hangs low over the assembly grounds."  
     
    "Rows of students stand in neat lines, uniforms bright in the light."  
 
    "The usual announcements begin."  
 
  
 
if rumor_path:  
 
 
 
    Headmistress "Before we continue, management would like to address an issue."  
 
    "The murmuring across the assembly quiets immediately."  
 
    Headmistress "False information has been spreading among students."  
 
    Headmistress "Rumours can damage reputations, create fear, and cause unnecessary confusion."  
 
    Headmistress "Anyone found deliberately spreading false stories will face correction."  
 
    "A teacher steps forward and calls a few names."  
 
    "Students exchange glances but no one speaks."  
 
    Mc "(So it really reached management…)"  
 
    Mc "(I didn’t think it would get this far.)"  
 
  
 
elif warning_path:

    "The announcements continue, but your thoughts drift."  
 
    mc "(Why did she stop me that day?)"  
 
    mc "(It wasn’t just a warning…)"  
 
    mc "(She looked like she wanted to say something else.)"  
 
    mc "(Was she protecting me… or warning me away?)"  
 
    "You stare ahead but barely hear the voices from the microphone."  
 
  
 
elif stacy_path:  
 
  
 
    "You stand in William House line beside Stacy."  
 
    st "Did you sleep at all?"  
 
    mc "Barely."  
 
    st "Same."  
 
  
 
    pause 0.5  
 
  
 
    mc "You really saw her there?"  
 
    st "I know what I saw."  
 
    mc "But why there?"  
 
    st "That’s the part I still can’t figure out."  
 
    mc "Maybe there’s something we’re missing."  
 
    st "Or maybe we’re only seeing part of it."  
 
    "You both fall silent as assembly continues."  
 
    mc "(The more we talk about it… the stranger it feels.)"   
 
  
 
# END consequence based on stats  
 
  
 
if memory_stat_high:  
 
  
 
    "A teacher walking past slows near your line."  
  
    Teacher "You. Why aren’t you singing?"  
 
    "Your chest tightens."  
 
    Teacher "Step out of line."  
 
    "A few students turn to look."  
 
    "You walk forward under everyone’s eyes."  
 
 
elif focus_stat_low:  
 
 
    "You don’t notice the song ending until the line goes silent."  
 
    Teacher "You there."  
 
    Teacher "Where is your attention?"  
 
    "Your stomach drops."  
 
    Teacher "Step out."  
 
  
 
elif stacy_talk_stat_high:  
 
 
    Teacher "Talking during assembly?"  
 
    Teacher "Both of you, enough."  
 
    "Stacy straightens immediately."  
 
    Teacher "You—step out of the line."  
    "Stacy gives you a quick apologetic glance."  
 
  
 
  
 
scene twins_lane  
 
 
    with dissolve  
 
    "The punishment is simple."  
 
    "But standing alone at Twins Lane while the rest of assembly continues somehow feels worse."  
 
    mc "(Great.)"  
 
    mc "(What a way to start Saturday.)"  
 
  
 
    stop ambience fadeout 2  
 
    # EPISODE 4 — SCENE 1  
 
    # The Other Visiting Day  
 
  
    scene school_visiting_day  
 
    with fade  
 
    play ambience "school_grounds.mp3"  
 
    "Saturday."  
 
    "You recognize the person waiting near your usual spot."  
 
    mc "(He's here again?)"  
 
    headboy "You're surprised."  
 
    mc "A little."  
 
    "He smiles."  
 
    headboy "Can we talk?"  
 
if accept_headboy_help:  
 
    mc "About Mackenzie?" 
 
    headboy "Yes."  
 
    "He tells you what he knows."  
 
    "But some parts of his explanation remain unclear."  
 
    mc "(He's still hiding something.)"  
 
else:  
 
    mc "I told you. I don't want your help."  
 
    headboy "You'd rather handle this yourself?"  
 
    mc "Yes."  
 
    "He studies you for a moment."  
 
    headboy "Alright."  
 
    "He doesn't argue."  
 
  
    scene school_grounds  
 
    with dissolve  
 
    headboy "If you change your mind, I'll still help."  
 
    mc "(Why does he care this much?)"  
 
    menu:  
        "Accept his help.":  
            $ accept_headboy_help = True  
            mc "Maybe I shouldn't do this alone."  
 
        "Handle it alone.":  
            $ accept_headboy_help = False  
            mc "I'll figure this out myself."  
 
  
stop ambience fadeout 2  
 
  
 
# EPISODE 4 — SCENE 2  
 
# The Aftermath  
 
  
    scene computing_lab  
 
    with fade  
 
    play ambience "school_corridor.mp3"  
 
  
    "Monday morning."  
 
    "Your class files out of the computing lab after the lesson."  
 
    teacher_pet "Excuse me, teacher said I should call one of the sisters."  
 
    teacher_pet "She needs to mark our latest assignment."  
 
    "The teacher's pet walks back toward the lab."  
 
    "You glance through the open door."  
 
    "For a split second, you see your name—or part of it—written on the board."  
 
    mc "(Was that my name?)"  
 
if accept_headboy_help:  
 
 
    mc "(They know.)"  
 
    mc "(They must know about him.)"  
 
    "You look back at the board."  
 
    "But the writing is already being erased."  
 
    mc "(What did he get me involved in?)"  
 
  
elif headmistress_warning_seen:  
 
  
    mc "(Did she tell the headmistress?)"  
 
    mc "(Is this because I refused his help?)"  
 
    "You quickly look away."  
 
  
else:  
 
  
    mc "(Why would my name be on that board?)"  
 
    "You glance back toward the lab."  
 
    mc "(I need to keep an eye out for it.)"  
 
    "Your class continues down the corridor."  
 
    "Whatever was written on that board, you didn't get a chance to see it."  
 
  
stop ambience fadeout 2   
 
  
 
# EPISODE 4 — SCENE 3  
 
# Are We Close?  
 
  
    scene notice_board  
 
    with fade  
 
    play ambience "school_morning.mp3"  
 
  
    "Monday morning."  
 
    "The usual crowd gathers around the notice board."  
 
    "Today, the shoutouts have arrived."  
 
    "Out of curiosity, you walk closer."  
 
    "You scan the list."  
 
    "And there it is."  
 
    "Your name."  
 
    "Again."  
 
    mc "(That's the third time this month.)"  
 
    mc "(Three times means trouble.)"  
 
    "You quickly remove your name from the list before anyone else can notice."  
 
    mc "(I need to get the shoutouts before the sister gets curious.)"  
 
    "You hurry toward the sister's classroom."  
 
    mc "(Please don't let it be him.)"  
 
    mc "(No. No, not him.)"  
 
  
scene sisters_class  
 
with dissolve  
 
  
    "You open the door without knocking."  
 
    "Every eye in the classroom turns toward you."  
 
  
    pause   
  
    stop ambience fadeout 2  
 
  
 
# EPISODE 4 — SCENE 4  
 
# Mackenzie's Twin  
 
  
    scene mc_dorm  
 
    with fade  
 
    play ambience "dorm_room.mp3"  
 
  
    "Later that morning."  
 
    "You sit on your bed, holding the letter."  
 
    mc "(I still can't believe he sent this.)"  
 
    "You unfold it."  
 
    headboy "There was a sister who came to our school with the choir."  
 
    headboy "She looked like Mackenzie."  
 
    mc "(But Mackenzie wasn't in the choir.)"  
 
    headboy "I'm certain Mackenzie wasn't there."  
 
    headboy "Besides, this girl sounded like a frog."  
 
    mc "(He really wrote that?)"  
 
    "Your eyes move to the next part."  
 
    headboy "I found something in Mackenzie's records."  
 
    headboy "In Class Six, she suddenly grew after recovering from a skin disease."  
 
    headboy "The following term, she returned to normal."  
 
    mc "(Grew... then returned to normal?)"  
 
    headboy "The records say the disease was caused by an allergic reaction to a specific food."  
 
    headboy "That food is served in the dining hall."  
 
    "You stare at the letter."  
 
    headboy "There's a chip in her records, but the information is encrypted."  
 
    headboy "It doesn't say what the food was."  
 
    mc "(So someone knows.)"  
 
    mc "(But they're hiding it.)"  
 
    "You fold the letter slowly."  
 
    mc "(And who was that girl?)"  
 
  
    stop ambience fadeout 2  
 
  
 
# EPISODE 4 — SCENE 5  
 
# Dining Hall Food  
 
  
    scene dining_hall_evening  
 
    with fade  
 
    play ambience "dining_hall.mp3"  
 
  
 
    "That evening, you head to the dining hall."  
 
    "Your third time watching Mackenzie's table."  
 
    "Thankfully, your table is right beside hers."  
 
    mc "(Fante kenkey.)"  
 
    mc "(Let's see.)"  
 
    "Mackenzie sits down with the others."  
 
    "She starts eating."  
 
    "You watch carefully."  
 
    "Nothing happens."  
 
    mc "(So she's not allergic to kenkey.)"  
 
    "You look down at your own food."  
 
    mc "(Then what is it?)"  
 
    "Your eyes move toward the other dishes."  
 
    mc "(I'll have to keep watching.)"  
 
  
    stop ambience fadeout 2  
 
  
 
# EPISODE 4 — SCENE 6  
 
# The Foreigners  
 
  
    scene dining_hall_morning  
 
    with fade  
 
    play ambience "dining_hall.mp3"  
 
  
 
    "The next morning, you sit at your usual table."  
 
    "Hausa koko is being served."  
 
    mc "(Let's see if Mackenzie eats it.)"  
 
    "Before you can watch her, a group of visitors enters the dining hall."  
 
    "Five of them appear to be Black Americans."  
 
    assistant_headmistress "Students, please remain quiet and comport yourselves."  
 
    assistant_headmistress "These visitors are here as part of an exchange programme."  
 
    "The visitors are escorted straight to the prefects' table."  
 
    "Fruit and cake are placed in front of them."  
 
    "A murmur spreads across the dining hall."  
 
    student "Cake?"  
 
    student "We get koko."  
 
    student "And they're sitting at the prefects' table?"  
 
    mc "(They're actually allowed to sit there?)"  
 
    "The prefects' table is strictly reserved for prefects."  
 
    "The nurse on duty steps forward."  
 
    nurse "After the prayer, students are to file out briskly."  
 
    nurse "Do not rush."  
 
    "Everyone goes quiet."  
 
    mc "(Right. Because apparently we can suddenly take our time.)"  
 
    "The prayer ends."  
 
    "Students immediately rush out of the dining hall."  
 
    "Nobody follows the instruction."  
 
    "Within seconds, the dining hall empties."  
 
    mc "(So much for filing out slowly.)"  
 
    mc "(And I still don't know if Mackenzie ate the koko.)"  
 
  
    stop ambience fadeout 2  
 
  
 
# EPISODE 4 — SCENE 7  
 
# The Exchange Programme  
 
 
    scene assembly_hall_night  
 
    with fade  
 
    play ambience "evening_event.mp3"  
 
    "Friday night."  
 
    "The main event of the exchange programme has finally arrived."  
 
    "The gallery is packed."  
 
    "Then you notice someone familiar."  
 
    mc "(Sebastian?)"  
 
    "He's here."  
 
    "The entire prefect body from the brother school has arrived as well."  
 
    "The programme begins."  
 
    "Five exchange students from Man City School in India walk onto the stage."  
 
    "The first performance begins."  
 
  
    play music "exchange_song.mp3"  
 
  
    "The song is slow."  
 
    "And strangely unsettling."  
 
    "MC watches the stage."  
 
    mc "(This is... creepy.)"  
 
    "The students around you remain perfectly composed."  
 
    "Nobody reacts."  
 
    mc "(Are we all pretending this sounds good?)"  
 
    "The song continues."  
 
    "You notice something else."  
 
    mc "(Wait.)"  
 
    mc "(Isn't this secular?)"  
 
    "Secular (not religious) music is against the school's rules."  
 
    "Yet nobody says a word."  
 
 
    stop music fadeout 2      
 
 
    mc "(So the rules don't apply tonight?)"  
 
  
    stop ambience fadeout 2  
 
#Track: Piano and choir mystical journey   
 
# CLUB SELECTION  
 
  
    "After classes, it's time to choose a club."  
 
    "Which club would you like to join?"  
 
  
    menu:   
        "Red Cross":  
            $ club_name = "Red Cross"  
 
        "Eco Rangers":  
            $ club_name = "Eco Rangers"  
  
        "Choir":  
            $ club_name = "Choir"  
 
        "Music":  
            $ club_name = "Music"  
 
        "Regimental Band":  
            $ club_name = "Regimental Band"  
 
        "Drama":  
            $ club_name = "Drama"  
    
        "Science":  
            $ club_name = "Science"  
  
        "Debate":  
            $ club_name = "Debate"  
 
        "AFS — American Field Service":  
            $ club_name = "AFS"  
 
        "GUNSA — Ghana United Nations Students Association":  
            $ club_name = "GUNSA"  
 
        "HOSA": 
            $ club_name = "HOSA" 
 
# EPISODE 4 — SCENE 8  
 
# Everyone Knows  
 
  
scene school_corridor  
 
    with fade  
 
    play ambience "school_corridor.mp3"  
 
  
    "You're already one minute late for your club meeting."  
 
    "You hurry down the corridor."  
 
    "Then you pass a security man."  
 
    "He looks at you."  
 
    "That look."  
 
    mc "(Oh, come on.)"  
 
    "He quickly changes his expression."  
 
    security "You won't greet?"  
 
    "You stop."  
 
    mc "Good morning, sir."  
 
    "Before he can respond, you hurry away."  
 
    mc "(I'm already late!)"  
 
    "You run toward the [club_name] meeting."  
 
  
    stop ambience fadeout 2  
 
 
# EPISODE 5 — SCENE 1  
 
# Then, That Man  
 
  
    scene school_corridor  
 
    with fade  
 
    play ambience “school_corridor.mp3”  
 
  
    "On your way to the club meeting, your mind keeps returning to that man."  
 
    mc "(Why did he ask me to quit?)" 
 
    mc "(And why did he say it so suddenly?)"  
 
    "The farther you walk, the stranger the question feels."  
 
  
scene club_venue  
 
with dissolve  
 
  
    "You arrive at the club meeting."  
 
    Teacher "There will be an event at Cleanse High this Saturday."  
 
    Teacher "Some students will be selected to represent the school."  
 
    "The students begin whispering among themselves."  
 
    Teacher "Two students will be chosen to attend."  
 
    Teacher "Your teacher and a security guard will accompany you as chaperones."  
 
    "Names are called."  
 
    "After a short selection, you are chosen."  
 
    mc "(Saturday…?)"  
 
    "You suddenly remember something."  
 
    mc "(I don’t have a proper bag for this.)"  
 
    "Your only bags are your school bag and your Crocs bag."  
 
    mc "(I can’t exactly take that.)"  
 
    mc "(Time to call home.)"  
 
  
    stop ambience fadeout 2  
 
  
 
# EPISODE 5 — SCENE 2  
 
# The Outing  
 
  
    scene bus  
 
    with fade  
 
    play ambience “bus_ride.mp3”  
 
    "You climb onto the bus with your jungle bag."  
 
    "The teacher checks the students before everyone settles down."  
 
    "You take your seat."  
 
    "But that feeling returns."  
 
    mc "(Someone’s watching me again.)"  
 
    "You look around."  
 
    "Nothing."  
 
    mc "(Maybe I’m imagining it.)"  
 
  
    scene queens_school  
 
    with dissolve  
 
  
    "You arrive at Queen’s School."  
 
    "The students begin getting off the bus."  
 
  
    stop ambience fadeout 2  
 
  
 
# EPISODE 5 — SCENE 3  
 
# Family Ties?  
 
  
    scene queens_school  
 
    with fade  
 
    play ambience “school_grounds.mp3”  
 
  
    "The teacher pulls you aside."  
 
    mc "(I thought I was in trouble for being late.)"  
 
    Teacher "Is a girl named Stacy in your dorm?"  
 
    "You pause."  
 
    mc "(Why is he asking about Stacy?)"  
 
    mc "(Did she get into trouble?)"  
 
    "You hesitate."  
 
    mc "Why?"  
 
    "He looks at you calmly."  
 
    Teacher "Because I’m her brother."  
 
    "You stare at him."  
 
    mc "I need proof."  
 
    Teacher "You’ll have it before the week is over."  
 
    "He walks away."  
 
    "You remain there for a moment."  
 
    mc "(Stacy’s brother…?)"  
 
  
    scene bus  
 
    with dissolve  
 
  
    "You slowly walk back to the bus."  
 
    "Your mind is still trying to process what you just heard."  
 
  
    stop ambience fadeout 2  
 
  
 
# EPISODE 5 — SCENE 4  
 
# The Mirror  
 
  
    scene queens_school  
 
    with fade  
 
    play ambience “school_grounds.mp3”  
 
  
    "You walk through the school grounds, taking in the unfamiliar surroundings."  
 
    "Then something catches your attention."  
 
    "You stop."  
 
    mc "(Wait…)"  
 
    "There’s a statue."  
 
    "Not just any statue."  
 
    mc "(That’s the same statue from my school.)"  
 
    "You look around."  
 
    "Then you notice something else."  
 
    "The layout."  
 
    "The buildings."  
 
    "The paths."  
 
    "Even the direction some of the main structures face."  
 
    mc "(Everything is… opposite.)"  
 
    "You stare at the statue again."  
 
    "But unlike everything else…"  
 
    "It looks exactly the same.  
 
    mc "(Why?)"  
 
  
    stop ambience fadeout 2  
 
  
 
# EPISODE 5 — SCENE 5  
 
# Keep Me Alive  
 
  
    scene school_grounds  
 
    with fade  
 
    play ambience “school_grounds.mp3"  
 
    "The bus slowly pulls into the school grounds."  
 
    "You watch through the window as it comes to a stop."  
 
    "Then—"  
 
    "THUD."  
 
    "You jolt in your seat."  
 
    mc "What was that?"  
 
    "You look outside."  
 
    "The bus had bumped into the statue."  
 
    "The statue shifts slightly."  
 
    mc "(Oh no…)"  
 
    "You immediately notice Desmond’s expression."  
 
    "He’s staring at the statue, looking just as shocked as you are."  
 
    "The bus driver quickly turns off the engine and gets down."  
 
    Teacher "Everyone, stay on the bus."  
 
    "The students begin whispering among themselves."  
 
    Teacher "I said stay on the bus."  
 
    "The driver’s face looks tense."  
 
    "Something about the way he reacts feels strange."s  
 
    "After a moment, the teachers begin sending the students away from the area."  
 
    mc "(Why are they acting like this?)"  
 
    "You watch as the driver and your favorite teacher remain behind."  
 
    "They think everyone has left."  
 
    "But you haven’t."  
 
    "You stay where you can hear them."  
 
    "The teacher lowers his voice."  
 
    Teacher "What are we going to do?"  
 
    Bus_driver "I don’t know."  
 
    Teacher "They saw it move."  
 
    "The driver looks back at the statue."  
 
    Bus_driver "We need to report this."  
 
    Teacher "And say what?"  
 
    "The two fall silent."  
 
    mc "(They’re scared.)"   
 
    "You quickly move away before they notice you."  
 
  
    scene school_grounds  
 
    with dissolve  
 
  
    "You run toward the house."  
 
    mc "(I need to get water before the taps stop.)"
    scene house  
 
    with dissolve  
 
  
    "You rush to the tap."  
 
    "Water is flowing."  
 
    mc "(Finally.)"  
 
    "You grab the container and begin filling it."  
 
    "Your mind keeps returning to what you saw."  
 
    mc "(Why were they so afraid of the statue?)"  
 
  
    stop ambience fadeout 2  
 
  
 
# EPISODE 5 — SCENE 6  
 
# Keep Me Alive  
 
  
    scene dorm_room  
 
    with fade  
 
    play music “quiet_reflection.mp3”  
 
  
    "You sit quietly on your bed, staring at the floor."  
 
    "Your mind keeps going back to what happened."  
 
    "The statue."  
 
    "The teacher."  
 
    "The bus driver." 
 
    "And Stacy’s supposed brother."  
 
    mc "(Why is everything happening at once?)"  
 
    "You sigh and lie back."  
 
    mc "(Maybe I should just forget about it.)"  
 
    "You close your eyes."  
 
    "Then a thought crosses your mind."  
 
    mc "(But what if I don’t?)"  
 
    "You sit up again."  
 
    mc "(What if something happens to me because I know too much?)"  
 
    "Your expression changes."  
 
    mc "(No.)"  
 
    mc "(I’m not going to let fear make that decision for me.)"  
 
    "Whatever is happening in this school…"  
 
    "…you need to stay alive long enough to understand it."  
 
  
    stop music fadeout 2  
 
  
# EPISODE 5 — SCENE 7  
 
# The Clue  
 
  
 
scene dorm_room  
 
with fade  
 
  
play music “quiet_night.mp3”  
 
  
    "You sit at your desk, trying to focus on your work."  
 
    "But your mind keeps returning to the statue." 
 
    mc "(Why would a statue scare them that much?)"  
 
    "You remember what the teacher said."  
 
    mc "They saw it move."  
 
    "You pause." 
 
    mc "Wait."  
 
    "You suddenly remember something."  
 
    "Earlier that day, you had noticed something strange about the statue."  
 
    "You reach for your notebook."  
 
    "You quickly sketch what you remember." 
 
    mc "(If I’m right…)"  
 
    "You compare it with the layout of your own school."  
 
    "Something doesn’t match." 
 
    mc "(There has to be a reason.)"  
 
    "Before you can think further, you hear footsteps outside."  
 
    "You quickly close the notebook."  
 
  
stop music fadeout 2  
 
  
 
# EPISODE 5 — SCENE 8  
 
# The Discovery  
 
  
 
scene dorm_room  
 
with fade  
 
play music “mystery.mp3”  
 
  
    "You wait until the footsteps disappear."  
 
    "Then you open your notebook again." 
 
    "You look at the sketch."  
 
    "And suddenly, you notice it."  
 
    mc "No way…"  
 
    "The position of the statue."  
 
    "The buildings." 
 
    "The direction of the chapel."  
 
    "Everything begins to line up."  
 
    mc "The school isn’t just similar to ours."  
 
    "You stare at the page." 
 
    mc "It’s a mirror."  
 
    "Your heart starts beating faster."  
 
    mc "But why?"  
 
    "You turn the page."  
 
    "There is one final detail you hadn’t noticed before."  
 
    "A name." 
 
    "You stare at it."  
 
    mc "(This can’t be a coincidence.)" 
 
    "The screen fades to black."  
 
    return