# ==========================================================================
#  images.rpy  --  image declarations for "Fred SIS Project"
# --------------------------------------------------------------------------
#  SETTING: this story is set at a GHANAIAN girls' boarding school (a
#  mission/“Sisters” house school with a brother school, St. Bartholomew's).
#  The script itself establishes this (GUNSA, Fante kenkey, Hausa koko,
#  Crocs bag, jungle bag, Ghanaian names).  Draw every sprite and background
#  with a Ghanaian identity: varied complexions and hair across the cast,
#  white shirt + blue skirt uniform, tropical school architecture.  Full
#  direction is in CHARACTER_REFERENCE.md / BACKGROUND_REFERENCE.md /
#  AUDIO_REFERENCE.md in the project root.  Do not use generic Japanese
#  school art or invented real-school badges.
#
#  HOW TO READ THIS FILE (for beginners)
#  -------------------------------------
#  Lines beginning with '#' are comments (ignored by Ren'Py).  Every real line
#  is an `image` statement, which tells Ren'Py: "the name on the left refers to
#  the PNG file in quotes on the right".  The story then uses only the NAME,
#  e.g. `scene bg dorm_day` or `show mc neutral`.
# ==========================================================================

#  This file maps every image NAME used by the story (game/script.rpy) to the
#  PNG file that should be placed on disk.  Ren'Py needs these declarations
#  because the story refers to images only by name, e.g.:
#
#      scene bg dorm_day          -> image bg dorm_day = "images/backgrounds/bg_dorm_day.png"
#      show  mc neutral at center -> image mc neutral   = "images/characters/mc_neutral.png"
#
#  HOW THE PLACEHOLDER SYSTEM WORKS
#  --------------------------------
#  None of the PNG files exist yet.  When Ren'Py cannot open one of the files
#  below it calls `config.missing_image_callback` (see game/definitions.rpy),
#  which draws a labelled grey placeholder instead of crashing.  So the game is
#  fully playable today: backgrounds show a grey screen with their name, character
#  sprites show a silhouette with their name.
#
#  TO ADD A REAL ASSET
#  -------------------
#  1. Draw or download the image.
#  2. Save it at EXACTLY the path shown on the right-hand side of the `image`
#     statement (relative to the game/ folder).
#  3. That's it - Ren'Py picks it up on the next launch.  No code change needed.
#
#  See ASSET_REQUIREMENTS.md (project root) for the full checklist, dimensions
#  and suggested sources.
#
#  NAMING RULE: image name with spaces replaced by underscores, plus ".png".
#  Backgrounds  -> game/images/backgrounds/<name>.png
#  Characters   -> game/images/characters/<name>.png   (transparent PNG)
# ==========================================================================


# ==========================================================================
#  BACKGROUNDS  (game/images/backgrounds/*.png)
#  Recommended: 1280x720 or 1920x1080, 16:9, .png or .jpg.
#  Add new backgrounds by copying an `image` line and pointing it at the new file.
#
#  Each line below is:   image <name> = "<file on disk>"   # what the scene is
# ==========================================================================

# --- Dormitory / opening rooms ---
image mc_dorm = "images/backgrounds/mc_dorm.png"                       # player's dorm room
image insides_dorm1 = "images/backgrounds/insides_dorm1.png"           # inside the dorm
image dorm_hallway = "images/backgrounds/dorm_hallway.png"             # dorm corridor
image mc_desk = "images/backgrounds/mc_desk.png"                       # player's study desk
image dorm_morning = "images/backgrounds/dorm_morning.png"             # dorm at daybreak
image dorm_walkway_day = "images/backgrounds/dorm_walkway_day.png"     # outdoor dorm walkway
image bg dorm_day = "images/backgrounds/bg_dorm_day.png"               # dorm (generic day)
image bg dorm_evening = "images/backgrounds/bg_dorm_evening.png"       # dorm (evening)
image dorm_room = "images/backgrounds/dorm_room.png"                   # a dorm room (generic)

# --- Classrooms / school interior ---
image classroom_doorway = "images/backgrounds/classroom_doorway.png"           # classroom door
image classroom_day = "images/backgrounds/classroom_day.png"                   # classroom, day
image bg classroom_day = "images/backgrounds/bg_classroom_day.png"             # classroom (generic)
image bg classroom_saturday_day = "images/backgrounds/bg_classroom_saturday_day.png"  # Saturday class
image bg classroom_block_evening = "images/backgrounds/bg_classroom_block_evening.png" # evening block
image computing_lab = "images/backgrounds/computing_lab.png"                   # computer lab
image bg arts_block_morning = "images/backgrounds/bg_arts_block_morning.png"   # arts block, morning
image bg arts_block_stairs_day = "images/backgrounds/bg_arts_block_stairs_day.png"     # arts stairs
image sisters_class = "images/backgrounds/sisters_class.png"                   # senior girls' class
image club_venue = "images/backgrounds/club_venue.png"                         # club meeting room

# --- Corridors / stairs / offices ---
image corridor_morning = "images/backgrounds/corridor_morning.png"             # corridor, morning
image school_corridor = "images/backgrounds/school_corridor.png"              # school corridor
image bg staircase = "images/backgrounds/bg_staircase.png"                    # staircase
image staircase_scrubbing = "images/backgrounds/staircase_scrubbing.png"      # stairs being cleaned
image bg office_corridor_day = "images/backgrounds/bg_office_corridor_day.png"  # office corridor
image bg dc_office_day = "images/backgrounds/bg_dc_office_day.png"            # disciplinary office

# --- Assembly halls / chapel ---
image prefect_assemblyground_morning = "images/backgrounds/prefect_assemblyground_morning.png"  # prefect assembly
image assembly_ground_morning = "images/backgrounds/assembly_ground_morning.png"        # assembly ground
image bg assembly_ground_morning = "images/backgrounds/bg_assembly_ground_morning.png"  # assembly (generic)
image assembly_morning = "images/backgrounds/assembly_morning.png"                     # morning assembly
image school_assembly_morning = "images/backgrounds/school_assembly_morning.png"        # school assembly
image assemblyhall_outside = "images/backgrounds/assemblyhall_outside.png"              # outside the hall
image assemblyhall_inauguration = "images/backgrounds/assemblyhall_inauguration.png"    # inauguration setup
image assembly_hall_night = "images/backgrounds/assembly_hall_night.png"               # assembly hall, night
image chapel_full = "images/backgrounds/chapel_full.png"                               # chapel interior

# --- Dining hall / notice boards ---
image bg dininghall_noticeboard_day = "images/backgrounds/bg_dininghall_noticeboard_day.png"  # dining + notices
image dining_hall_evening = "images/backgrounds/dining_hall_evening.png"      # dining hall, evening
image dining_hall_morning = "images/backgrounds/dining_hall_morning.png"      # dining hall, morning
image notice_board = "images/backgrounds/notice_board.png"                    # the notice board
image bg noticeboard_friday = "images/backgrounds/bg_noticeboard_friday.png"  # notices, Friday

# --- Outdoors / grounds ---
image compound_day = "images/backgrounds/compound_day.png"                    # the school compound
image school_grounds = "images/backgrounds/school_grounds.png"                # school grounds
image bg school_lane_morning = "images/backgrounds/bg_school_lane_morning.png"  # school lane
image bg path_day = "images/backgrounds/bg_path_day.png"                      # a path, day
image bg school_bench_day = "images/backgrounds/bg_school_bench_day.png"      # a bench outdoors
image twins_lane = "images/backgrounds/twins_lane.png"                        # the "twins" lane

# --- Excursion / zoo ---
image excursion_line = "images/backgrounds/excursion_line.png"                # queue for the bus
image bus = "images/backgrounds/bus.png"                                     # the excursion bus
image bus_outlooks = "images/backgrounds/bus_outlooks.png"                    # view from the bus
image zoo_gate = "images/backgrounds/zoo_gate.png"                            # zoo entrance
image zoo_path = "images/backgrounds/zoo_path.png"                            # path inside the zoo
image alligator_area = "images/backgrounds/alligator_area.png"                # alligator enclosure
image poolside = "images/backgrounds/poolside.png"                            # zoo poolside
image bg zoo_poolside_day = "images/backgrounds/bg_zoo_poolside_day.png"      # poolside (generic)

# --- Visiting day / mystery / other locations ---
image school_visiting_day = "images/backgrounds/school_visiting_day.png"      # visiting day
image bg visiting_area = "images/backgrounds/bg_visiting_area.png"            # visiting area
image bg warners_river_day = "images/backgrounds/bg_warners_river_day.png"    # river scene
image queens_school = "images/backgrounds/queens_school.png"                  # another school
image house = "images/backgrounds/house.png"                                  # a house / building


# ==========================================================================
#  CHARACTER SPRITES  (game/images/characters/*.png)
#  Recommended: transparent PNG (PNG-32), full body with the feet on the
#  bottom edge, on a 360x720 canvas (the game's native screen is 1280x720, so
#  a 360x720 sprite shows head-to-toe without being scaled up).
#  One file per expression; keep the same character design and canvas size
#  across every expression so the character never jumps between lines.
#  41 sprite files cover 18 characters.  Full Ghanaian art direction and the
#  exact per-file spec are in CHARACTER_REFERENCE.md (project root).
#
#  Character code -> person  (names below are what the story calls them):
#    mc            = the player (name entered at the start; "Michelle" default)
#    st / stacy    = Stacy                    (two names, same person)
#    vr / veronica = Veronica                 (two names, same person)
#    vanessa       = Vanessa  (Ep.2 classmate/rival; separate from Veronica)
#    ma            = Marcellina               mf    = Mr. Farrah (teacher)
#    ch            = Christiana               ca    = Charis
#    miss_a / ms_amponsah = Miss Amponsah     na/naa = Naa Aqueley
#    sister        = a senior-girl prefect    sister_mawuli = Sister Mawuli
#    headboy       = Head boy of St. Bartholomew's
#    headmistress  = the Headmistress         teacher = a teacher (Ep.1 poolside)
#    angelina      = Angelina Mensah          grace = Sister Grace Ansah
#    girl          = an unnamed Form-One girl
#  NOTE: "Sisters" here are senior-girl house prefects (Ghanaian boarding
#  usage), not nuns.  Characters the story never `show`s (Mackenzie, the Head
#  Girl, the DC Officer, ...) have no sprite here; see CHARACTER_REFERENCE.md
#  §5 for optional additions (adding them also needs matching `show` lines).
#
#  Each line below is:   image <codes> = "<file on disk>"   # expression / pose
# ==========================================================================

# --- Player (mc) ---
image mc neutral = "images/characters/mc_neutral.png"           # normal, calm
image mc surprised = "images/characters/mc_surprised.png"       # surprised
image mc shocked = "images/characters/mc_shocked.png"           # shocked
image mc thinking = "images/characters/mc_thinking.png"         # thinking
image mc tired = "images/characters/mc_tired.png"               # tired
image mc unimpressed = "images/characters/mc_unimpressed.png"   # unimpressed

# --- Stacy (st / stacy) ---
image st normal = "images/characters/st_normal.png"             # neutral
image stacy neutral = "images/characters/stacy_neutral.png"     # neutral (long code)

# --- Veronica (vr / veronica) ---
image vr normal = "images/characters/vr_normal.png"             # neutral
image vr sleepy = "images/characters/vr_sleepy.png"             # sleepy
image vr annoyed = "images/characters/vr_annoyed.png"           # annoyed
image veronica neutral = "images/characters/veronica_neutral.png"  # neutral (long code)
image veronica amused = "images/characters/veronica_amused.png"    # amused
image veronica grin = "images/characters/veronica_grin.png"        # grinning
image veronica sitting = "images/characters/veronica_sitting.png"  # sitting

# --- Vanessa (classmate / rival, Episode 2) ---
image vanessa bored = "images/characters/vanessa_bored.png"         # bored
image vanessa thinking = "images/characters/vanessa_thinking.png"   # thinking
image vanessa shocked = "images/characters/vanessa_shocked.png"     # shocked
image vanessa smug = "images/characters/vanessa_smug.png"           # smug
image vanessa grin = "images/characters/vanessa_grin.png"           # grinning
image vanessa suspicious = "images/characters/vanessa_suspicious.png"  # suspicious

# --- Marcellina (ma) ---
image ma angry = "images/characters/ma_angry.png"               # angry

# --- Mr. Farrah (mf, teacher) ---
image mf rushed = "images/characters/mf_rushed.png"             # in a hurry
image mf apologizing = "images/characters/mf_apologizing.png"   # apologising

# --- Christiana (ch) / Charis (ca) ---
image ch normal = "images/characters/ch_normal.png"             # Christiana, neutral
image ch smug = "images/characters/ch_smug.png"                 # Christiana, smug
image ca neutral = "images/characters/ca_neutral.png"           # Charis, neutral

# --- Miss Amponsah / Sister(s) ---
image miss_a normal = "images/characters/miss_a_normal.png"     # Miss Amponsah, neutral
image ms_amponsah = "images/characters/ms_amponsah.png"         # Miss Amponsah (long code)
image sister neutral = "images/characters/sister_neutral.png"   # a senior-girl prefect
image sister_mawuli = "images/characters/sister_mawuli.png"     # Sister Mawuli

# --- Naa Aqueley (na / naa) ---
image naa neutral = "images/characters/naa_neutral.png"         # neutral

# --- Prefects / staff ---
image headboy neutral = "images/characters/headboy_neutral.png"           # head boy
image headboy formal = "images/characters/headboy_formal.png"             # head boy, formal
image headboy uneasy = "images/characters/headboy_uneasy.png"             # head boy, uneasy
image headmistress neutral = "images/characters/headmistress_neutral.png" # headmistress
image teacher neutral = "images/characters/teacher_neutral.png"           # a teacher

# --- Other named / background students ---
image angelina = "images/characters/angelina.png"               # Angelina Mensah
image angelina neutral = "images/characters/angelina_neutral.png"  # Angelina, neutral
image grace neutral = "images/characters/grace_neutral.png"     # Sister Grace Ansah
image girl nervous = "images/characters/girl_nervous.png"       # unnamed Form-One girl
