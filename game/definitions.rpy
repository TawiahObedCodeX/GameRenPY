# ==========================================================================
#  definitions.rpy
# --------------------------------------------------------------------------
#  This file declares everything the STORY (game/script.rpy) expects to
#  already exist before it runs:
#
#    1. `default` variables  -- starting values for the hidden stat system.
#    2. `define` characters  -- the speaker names used before each line.
#    3. the name-entry screen called by `label ask_name`.
#    4. a placeholder-image callback so the game runs without the artwork.
#    5. extra audio channel + safe audio helpers (play_bgm / play_ambience /
#       play_sfx) that skip missing files instead of crashing.
#
#  Image DECLARATIONS (which name maps to which PNG file) live in
#  game/images.rpy.  Interface screens live in game/screens.rpy.
#
#  SETTING: the story is set at a GHANAIAN girls' boarding school.  The
#  character names and story text are kept exactly as written; the Ghanaian
#  art/audio direction is documented in CHARACTER_REFERENCE.md,
#  BACKGROUND_REFERENCE.md and AUDIO_REFERENCE.md in the project root.
#
#  Ren'Py loads every *.rpy file in the game/ folder automatically, so you do
#  not have to "import" this file anywhere.  Everything here runs at startup.
#
#  HOW TO READ THIS FILE (for beginners)
#  -------------------------------------
#  Lines starting with '#' are comments -- Ren'Py ignores them completely.
#  They exist only to explain the code to a human.  You can read them without
#  affecting the game.  The actual code is the lines WITHOUT a leading '#'.
# ==========================================================================


# ==========================================================================
#  1. VARIABLES  (the hidden stat / flag system)
# --------------------------------------------------------------------------
#  `default` gives a variable its initial value and is also what makes the
#  variable part of the save file.  The story changes these with lines like
#  `$ trust += 1`, then reads them in `if` / `menu` checks to pick a branch.
#
#  Think of each variable as a labelled box that holds one piece of the
#  player's progress.  A number box (like `trust`) can grow/shrink; a True/False
#  box (like `mc_replied`) records that something happened.
# ==========================================================================

# The name the player types.  "" means "not chosen yet"; `ask_name` fills it in.
# `default` = the starting value; `player_name` is the box's name.
default player_name = ""

# ---- Core stats ---------------------------------------------------------
# These start at 0 and are raised/lowered by the player's choices.
default trust = 0        # overall good-will the school has toward the player
default confidence = 0   # how self-assured the player has acted
default curiosity = 0    # how often the player chose to investigate
default courage = 0      # bold choices (speaking up, exploring, etc.)
default kindness = 0     # helpful / gentle choices
default safety = 0       # cautious, rule-following choices
default discovery = 0    # clues / secrets uncovered

# ---- Friendship & tension ----------------------------------------------
# Per-character relationship meters.  Higher friendship = friendlier scenes.
default friendship_veronica = 0    # goodwill with Veronica
default friendship_stacy = 0       # goodwill with Stacy
default friendship_marcellina = 0  # goodwill with Marcellina
default tension_marcellina = 0     # friction with Marcellina

# ---- Episode 2 helper stats --------------------------------------------
default stacy_points = 0   # accumulates Stacy interactions in Episode 2
default attitude = 0       # tone of the player's reactions
default reserve = 0        # how quiet / withdrawn the player has been

# ---- Simple on/off flags ------------------------------------------------
# A "flag" is a True/False switch.  False = it has not happened yet.
default checked_marcellina = False  # did the player watch Marcellina in the dorm?
default mc_replied = False          # did the player answer Veronica in class?

# ---- Flags / stats used later but never declared in the original file ----
#  The original script referenced each of these without ever creating it,
#  which raised `NameError: name '...' is not defined` as soon as that branch
#  ran.  Declaring them here fixes those crashes.
default accept_headboy_help = False      # player accepted the head boy's offer
default club_name = ""                   # club the player joins (used in text)
default clue_teacher_tone = False        # noticed the teacher's odd tone
default focus_stat_low = False           # "did the player focus?" check
default headmistress_warning_seen = False  # witnessed the headmistress's warning
default mc_attitude = 0                  # Episode 3+ attitude counter
default mc_mackenzie_relationship = 0    # bond with Mackenzie
default mc_remembers_sister = False      # remembered the sister's advice
default mc_reserve = 0                   # Episode 3+ reserved counter
default mc_visits_stacy = False          # visited Stacy
default memory_stat_high = False         # recollection check
default naa_active = True                # whether Naa Aqueley is in the scene
default naa_relationship = 0             # bond with Naa Aqueley
default rumor_path = False               # player followed the rumour path
default sister_targeting = False         # the sister is targeting the player
default stacy_gossiped = False           # Stacy gossiped about the player
default stacy_path = False               # player took Stacy's path
default stacy_relationship = 0           # bond with Stacy (Episode 3+)
default stacy_talk_stat_high = False     # talked to Stacy enough
default varonica_trust = 0               # trust with "Varonic" (story spelling)
default veronica_relationship = 0        # bond with Veronica (Episode 3+)
default warning_path = False             # player chose the warning path


# ==========================================================================
#  2. CHARACTERS
# --------------------------------------------------------------------------
#  `Character("...")` creates a speaker.  The part before `=` is the short
#  name used in the script (e.g. `mc "Hello"`); the string is what appears in
#  the dialogue box.  `dynamic=True` means the shown name can contain a
#  [variable] substitution that is re-read every time the character speaks.
#
#  In the story you write:      mc "Good morning."
#  The engine shows in the box:  (the player's name)  Good morning.
# ==========================================================================

define mc = Character("[player_name]", dynamic=True)  # the player (dynamic name)
define st = Character("Stacy")                        # Stacy (short code "st")
define miss_a = Character("Miss Amponsah")            # a teacher
define ma = Character("Marcellina")                   # a senior student
define vr = Character("Veronica")                     # Veronica (short code "vr")
define mf = Character("Mr. Farrah")                   # a teacher
define cl = Character("Class")          # the whole class speaking as one
define ch = Character("Christiana")                   # a classmate
define ca = Character("Charis")                       # a classmate
define sr = Character("Sister")                       # a senior-girl prefect
define tr = Character("Teacher")                      # a generic teacher
define na = Character("Naa Aqueley")                  # a classmate
define sd = Character("Random student")               # anonymous crowd line
define sd2 = Character("Random student 2")
define sd3 = Character("Random student 3")
define ra = Character("Head boy of St. Bartholomews'")
define aa = Character("Headmistress")
define co = Character("Head girl")
define rs = Character("Random sister")                # anonymous prefect line
define rsii = Character("Random sister 2")
define rsiii = Character("Random sister 3")
define ga = Character("Grace Ansah")                  # Sister Grace Ansah

#  Speakers used in Episodes 3-5 that were never defined in the original.
#  Ren'Py is case-sensitive, so `Teacher` is a DIFFERENT speaker from `tr`.
#  Each of these is a separate name box; the text in quotes is what is shown.
define Teacher = Character("Teacher")
define headboy = Character("Head boy")                # head boy of the boys' school
define Headmistress = Character("Headmistress")
define assistant_headmistress = Character("Assistant Headmistress")
define hm = Character("Headmistress")                 # short code for Headmistress
define hg = Character("Head girl")
define mk = Character("Mackenzie")                    # the missing student
define dc = Character("DC")                           # the disciplinary officer
define r = Character("Richard")
define s = Character("Sister")
define v = Character("Veronica")                      # another code for Veronica
define sis = Character("Sister")
define sa = Character("Sister")
define girl = Character("Girl")                       # unnamed Form-One student
define Girl = Character("Girl")                       # same, capitalised
define girl_1 = Character("Girl 1")                   # crowd of girls
define girl_2 = Character("Girl 2")
define girl_3 = Character("Girl 3")
define student = Character("Student")
define Mc = Character("MC")                           # capitalised code for the player
define Bus_driver = Character("Bus driver")
define Sister_voice = Character("Sister")
define teacher_pet = Character("Teacher's pet")
define security = Character("Security")
define nurse = Character("Nurse")
define veronica = Character("Veronica")               # full-name code for Veronica


# ==========================================================================
#  3. NAME-ENTRY SCREEN
# --------------------------------------------------------------------------
#  `label ask_name` does `call screen name_input`.  When the player presses
#  Confirm the screen returns the typed name, and `ask_name` copies it into the
#  `player_name` variable.  `VariableInputValue` also keeps `player_name`
#  updated live as the player types, so either route gives the same result.
#
#  A "screen" is a piece of interface (buttons, text, input boxes).  This one
#  is a simple centred panel asking for the player's name.
# ==========================================================================

screen name_input():
    modal True          # block clicks to everything behind this screen
    zorder 200          # draw it above the normal game UI (higher = on top)

    add Solid("#1b1b28")  # dim the whole screen with a dark background

    frame:               # a bordered panel that holds the text + input + button
        align (0.5, 0.5)   # centre the panel (0.5,0.5 = middle of the screen)
        padding (40, 40)   # 40px of empty space inside the panel's edges

        vbox:              # a "vertical box": its children stack top-to-bottom
            spacing 24     # 24px gap between each child
            xalign 0.5     # centre the column horizontally

            text "What is your name?" xalign 0.5 size 34   # the prompt label

            input:                              # a text-entry box
                value VariableInputValue("player_name")  # typing edits player_name
                length 20                       # allow at most 20 characters
                xalign 0.5                      # centre it

            textbutton "Confirm":               # a clickable button
                xalign 0.5                      # centre it
                # Return the typed name.  (A bare `Return()` would return the
                # boolean True in-game, which is not a string - ask_name only
                # accepts a real string, so pass `player_name` explicitly.)
                action Return(player_name)      # what happens when clicked


# ==========================================================================
#  4. PLACEHOLDER IMAGES
# --------------------------------------------------------------------------
#  The story references ~99 background/sprite images that are not part of the
#  project yet.  Every image NAME is declared in game/images.rpy and points at a
#  file under game/images/backgrounds/ or game/images/characters/.  When one of
#  those files does not exist, Ren'Py calls `config.missing_image_callback`
#  below and gets a labelled placeholder instead of crashing.
#
#  So the game runs end-to-end with zero artwork:
#     backgrounds -> grey screen with the file name
#     sprites     -> standing silhouette with the file name
#
#  Drop a PNG at the declared path and it replaces the placeholder automatically.
#  See ASSET_REQUIREMENTS.md for the full list.
# ==========================================================================

init python:
    # `init python:` runs this block once at startup, before the story begins.
    # It defines a Python function and wires it into Ren'Py's config.

    def _missing_image_callback(name):
        # Ren'Py calls this function whenever an image file fails to load.
        # `name` arrives either as a tuple ("bg", "dorm_day") or as the file
        # path declared in images.rpy ("images/backgrounds/bg_dorm_day.png").
        if isinstance(name, (tuple, list)):
            # Tuple form: join the parts with spaces, e.g. ("bg","dorm_day")
            # becomes "bg dorm_day", so the checks below still work.
            name = " ".join(str(part) for part in name)

        # Choose a placeholder style: flat grey for backgrounds, a standing
        # silhouette for character sprites (so sprites do not cover the scene).
        is_bg = ("backgrounds/" in name) or ("/bg_" in name) or name.startswith("bg")
        base = "bg" if is_bg else None   # Placeholder("bg") = grey rectangle

        # Only the short file name is shown on the placeholder.
        short = name.replace("\\", "/").rsplit("/", 1)[-1]   # take text after last '/'
        placeholder = Placeholder(base, text=short)          # build the placeholder
        # The background placeholder draws its label from `.name`, while the
        # sprite placeholder uses `.text`; set both so either style shows it.
        placeholder.name = [short]       # background style reads this
        return placeholder               # hand it back to Ren'Py to display

    # Ren'Py calls this whenever an image (file) fails to load.
    config.missing_image_callback = _missing_image_callback


# ==========================================================================
#  5. EXTRA AUDIO CHANNEL
# --------------------------------------------------------------------------
#  Ren'Py only knows the `music`, `sound` and `voice` channels by default.
#  The original script also used `play/stop ambience ...`, which would raise
#  "channel 'ambience' is not defined".  Registering the channel here makes
#  those `stop ambience ...` lines valid.
#
#  A "channel" is an independent audio track player.  Music and ambience can
#  play at the same time because they use different channels.
# ==========================================================================

init python:
    # Register a new looping audio channel called "ambience" that is mixed
    # with the `music` slider (mixer="music").
    renpy.music.register_channel("ambience", mixer="music", loop=True)


# ==========================================================================
#  6. AUDIO HELPERS (safe playback while the soundtrack is incomplete)
# --------------------------------------------------------------------------
#  The story calls these instead of `play music ...` directly:
#
#      $ play_bgm("audio/music/school_day.ogg")      # background music
#      $ play_ambience("audio/ambience/dorm_room.ogg")
#      $ play_sfx("audio/sfx/tap.ogg")               # one-shot sound effect
#
#  Each helper checks `renpy.loadable()` first and simply does nothing if the
#  file has not been added yet.  This means:
#     * the game never crashes because a music/sound file is missing, and
#     * the moment you drop an .ogg/.mp3/.wav into game/audio/... it starts
#       playing, with no code change required.
#
#  The helpers also try the other supported extensions: the story may name a
#  track ".../school_day.ogg" while the file on disk is "school_day.wav", and
#  `_resolve_audio()` finds whichever exists.  So you can supply any of
#  .ogg / .mp3 / .wav / .opus / .flac / .m4a without editing the story.
#
#  `stop music ...` / `stop ambience ...` (used by the story) are always safe.
#  Add new tracks by dropping the file in the folder and calling the helper.
# ==========================================================================

init python:
    # This whole block is Python: it defines helper functions the story calls.

    AUDIO_EXTENSIONS = (".ogg", ".mp3", ".wav", ".opus", ".flac", ".m4a")
    # ^ the filename endings we will try when looking for a track.

    def _resolve_audio(track):
        """Return a loadable path for `track`, trying other extensions too."""
        if renpy.loadable(track):
            # The exact path the story asked for exists -> use it.
            return track
        base = track.rsplit(".", 1)[0]   # strip the old extension
        for ext in AUDIO_EXTENSIONS:     # try every supported ending
            candidate = base + ext       # e.g. "audio/music/school_day" + ".wav"
            if renpy.loadable(candidate):
                return candidate         # found one on disk -> use it
        return None                      # nothing matched -> caller does nothing

    def play_bgm(track, fadein=1.0, loop=True):
        """Background music on the `music` channel (looped)."""
        resolved = _resolve_audio(track)          # find the real file (or None)
        if resolved:                              # only play if it exists
            renpy.music.play(resolved, channel="music", fadein=fadein, loop=loop)

    def play_ambience(track, fadein=1.0, loop=True):
        """Looping background ambience on the custom `ambience` channel."""
        resolved = _resolve_audio(track)          # find the real file (or None)
        if resolved:                              # only play if it exists
            renpy.music.play(resolved, channel="ambience", fadein=fadein, loop=loop)

    def play_sfx(track):
        """One-shot sound effect on the standard `sound` channel."""
        resolved = _resolve_audio(track)          # find the real file (or None)
        if resolved:                              # only play if it exists
            renpy.sound.play(resolved, channel="sound")


# ==========================================================================
#  7. CONTINUOUS BACKGROUND MUSIC (the "music director")
# --------------------------------------------------------------------------
#  The story stops the music in a few places, which used to leave the game
#  silent.  This helper is registered as a periodic callback: every moment it
#  checks the `music` channel and, if nothing is playing, fades a gentle theme
#  back in.  So there is always a song under the scene, and every track the
#  story cues still plays at its own convenient moment -- the bed only starts
#  when the channel is actually empty.
# ==========================================================================

init python:
    # The gentle default song used to fill any silent gap.
    MUSIC_BED = "audio/music/school_day_soft.wav"

    def _keep_music_playing():
        # Ren'Py calls this repeatedly (a "periodic callback").
        if renpy.music.get_playing(channel="music"):
            # Something is already playing -> leave it alone and return.
            return
        resolved = _resolve_audio(MUSIC_BED)   # locate the bed track
        if resolved:                           # play it only if present on disk
            renpy.music.play(resolved, channel="music", fadein=3.0, loop=True)

    # Register the function so Ren'Py keeps calling it during the game.
    config.periodic_callbacks.append(_keep_music_playing)
