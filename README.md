# Fred SIS Project — Ren'Py Visual Novel

A story-driven (visual novel) game written in **Ren'Py** about a girl named
**Michelle** (name chosen by the player) who arrives at a **Ghanaian girls'
boarding school** dorm, makes friends and rivals, gets "corrected" by the
prefects, goes on a zoo excursion, and uncovers a mystery involving a missing
student (Mackenzie), a strange statue, and a mirror-version of her own school.

The game is split into **Episode 1 → Episode 5** and tracks hidden stat
variables (`trust`, `kindness`, `courage`, `friendship_stacy`, …) that decide
which branches the player sees.

> **Setting (Ghana).** The story is set in Ghana — established by `GUNSA —
> Ghana United Nations Students Association`, the dishes `Fante kenkey` and
> `Hausa koko`, the student items `Crocs bag` / `jungle bag`, and Ghanaian names
> throughout. The art/audio direction in this repo is therefore **specifically
> Ghanaian** (see the three reference docs below). The story contains **22 unique
> named characters** (29 distinct on-page identities) drawn with **41 sprite
> files**; see `CHARACTER_REFERENCE.md` for the full inventory.

---

## 1. Files in this project

| Path | What it is |
|------|------------|
| `game/script.rpy` | **The fixed story script** (labels, menus, dialogue). This is the game. Fully commented with a banner for every label. |
| `game/definitions.rpy` | Variables (`default`), characters (`define`), the name-entry screen, the placeholder-image callback, the safe audio helpers, and the continuous-music director. Fully commented. |
| `game/images.rpy` | **Declares all 99 images** the story uses (name → PNG file path). Add a file at the declared path to replace its placeholder. |
| `game/screens.rpy`, `game/gui.rpy`, `game/options.rpy`, `game/gui/` | The interface and project configuration (stock Ren'Py 8 GUI). These make the project self-contained and runnable. |
| `backup/script.original.rpy` | The **original corrupted file**, kept so every error below can be traced to a line number. |
| `tools/normalize_script.py` | The Python tool that repaired the script. Safe to re-run; it always rebuilds `game/script.rpy` from the backup. |
| `tools/validate_script.py` | A standalone checker that reports remaining errors without needing the Ren'Py SDK. Run `py tools/validate_script.py`. |
| `tools/list_assets.py` | Prints every art/audio file the story needs, with totals. Run `py tools/list_assets.py`. |
| `tools/generate_asset_tracker.py` | Rebuilds the tracker from the real source. Run `py tools/generate_asset_tracker.py`. |
| `tools/generate_placeholders.py` | Generates clean placeholder art + melodic audio for all 120 assets. Run `py tools/generate_placeholders.py`. |
| `tools/build_character_sprites.py` | Fits the supplied art in `PNG-IMAGES/` to 360×720 and derives the rest of the cast as distinct 2D sprites. Run `py tools/build_character_sprites.py`. |
| `PNG-IMAGES/` | Supplied full-body character art (8 images); source for the character sprites. |
| `tools/install_assets.py` | Drop-in installer: copies your real PNGs/audio into the right place and name. |
| `tools/make_preview.py` | Builds `PREVIEW_backgrounds.png` / `PREVIEW_characters.png` contact sheets. |
| `tools/pnglib.py` | Dependency-free PNG encode/decode/draw/text helpers used by the tools. |
| `assets_inbox/` | **Drop your real art/music here**, then run `py tools/install_assets.py`. See `assets_inbox/README.txt`. |
| `ASSET_TRACKER.md` / `ASSET_TRACKER.csv` | **120-row checklist** (one row per asset) with target path, character/area and a done-box; auto-generated. |
| `ASSET_REQUIREMENTS.md` | The full 120-file checklist (58 backgrounds, 41 sprites, 21 audio) with Ghanaian direction and counts. |
| `CHARACTER_REFERENCE.md` | **Character inventory** (22 named characters), Ghanaian art direction, and exact sprite filenames. |
| `BACKGROUND_REFERENCE.md` | **Location inventory** (~43 Ghanaian locations), per-file direction and filenames. |
| `AUDIO_REFERENCE.md` | **Music/ambience/SFX inventory** with Ghanaian musical direction and licensing. |
| `ASSET_INSTALLATION_GUIDE.md` | Step-by-step, no-code guide to adding art and sound. |
| `ASSET_CODE_REFERENCE.md` | How the code maps image/audio names to files, with snippets. |
| `DEVELOPMENT_STATUS.md` | Current status, verification results, and remaining work. |
| `README.md` | This file. |
| `.vscode/settings.json` | VS Code config: hides compiled files (`*.rpyc`, `cache/`) and stores the Ren'Py SDK path for the **Ren'Py Launch and Sync** extension (see §2, *Working in VS Code*). |

> ⚠️ The original file was called `game.py`. It was **not a Python program** —
> it was Ren'Py script, which is why running it with Python failed.

---

## 2. How to install and play (Windows)

You need the **Ren'Py SDK** (it bundles Python + the engine).

1. **Download the Ren'Py SDK** from <https://www.renpy.org/latest.html>
   (choose the Windows `.zip`, e.g. `renpy-8.x.x-sdk.zip`).
2. **Extract** it somewhere simple, e.g. `C:\renpy`.
3. Run the game directly (this folder is a complete project):

   ```bat
   C:\renpy\renpy.exe "C:\path\to\GameRenPY" run
   ```

   Or open **`renpy.exe`** (the launcher), choose **"Scan" / add project"**, point
   it at this folder, select it, and click **"Launch Project"**.
4. Type a name, click **Confirm**, and play.

> **No "Create New Project" step is needed any more.** Earlier, the project had
> no `screens.rpy` / `gui.rpy` / `options.rpy`, so it had to be dropped into a
> freshly generated project. Those files (and the `game/gui/` skin) are now
> included, so this folder runs as-is.

### Running from the command line (optional)

```bat
C:\renpy\renpy.exe "C:\path\to\GameRenPY" run
```

### Working in VS Code (build & run without leaving the editor)

You can develop, build and launch the game entirely inside **Visual Studio
Code**. Two extensions do the heavy lifting:

| Extension | ID | What it gives you |
|---|---|---|
| **Ren'Py Language (Official)** | `Ren'Py.language-renpy` | The official language support: syntax highlighting, autocompletion, hover docs, go-to-definition, and inline reporting of errors/typos in every `.rpy` file. It makes `script.rpy` / `definitions.rpy` readable and catches mistakes as you type. |
| **Ren'Py Launch and Sync** | `paisleysoftworks.renpywarp` | Adds **launch/run** commands and **"warp"** — jump the running game straight to the line or label you are editing, keeping the editor and the game in sync. It can also download and manage the Ren'Py SDK for you. This project is already configured for it: `.vscode/settings.json` sets `renpyWarp.sdkPath` to the SDK copy the extension downloaded (`…\paisleysoftworks.renpywarp\file-downloader-downloads\8.5.3`). |

**Set-up steps (once):**

1. Open this folder in VS Code (`File → Open Folder…` → `GameRenPY`).
2. Install both extensions: open the **Extensions** view (`Ctrl+Shift+X`), search
   for **"Ren'Py Language"** and **"Ren'Py Launch and Sync"**, and click
   **Install** on each. (Both are also linked from
   <https://www.renpy.org/latest.html>.)
3. If the SDK was not auto-detected, set **Ren'Py Launch and Sync → SDK Path**
   in Settings to your Ren'Py SDK folder — the same path already stored in
   `.vscode/settings.json` (`renpyWarp.sdkPath`).

**Build & run from VS Code:**

- Run the command palette (`Ctrl+Shift+P`) and pick a **Ren'Py Launch** command
  (e.g. *"Ren'Py: Launch Project"* / *"Launch and Sync"*) — the extension compiles
  the script (the same step as the launcher's **"Launch Project"**) and starts the
  game.
- With the game running, put the cursor on a line and use the extension's
  **warp** command to jump the build to that exact point — handy for testing a
  specific scene (e.g. deep in Episode 4) without replaying from the start.
- To check the whole project before playing, run the launcher's **Lint** (or
  `renpy.exe "…\GameRenPY" lint`) as described below.

> **Note:** VS Code only *drives* Ren'Py — the engine (from the SDK) still does
> the compiling and rendering. The extensions just add editing support and a
> one-click build/run, so you never have to leave the editor.

### Checking for errors before playing

The launcher has a **"Lint"** button. Run it after copying the files — it scans
the whole script and reports any remaining undefined labels, images, or
variables. Our fixed files pass the structure/speaker/label/variable checks; the
missing art and audio are normal (see *Placeholders* below).

### Placeholders (the game ships fully dressed)

The story references **58 backgrounds, 41 character sprites and 21 audio files**
(120 total). All 120 are **now included** as clean generated placeholders, so
the game has no grey boxes and plays with real (if simple) visuals and sound:

- **58 background PNGs** (1280×720) — a per-area tinted scene with the file name
  printed on it, so you can tell them apart.
- **41 character sprites** (360×720, transparent) — **real art** supplied in
  `PNG-IMAGES/` is used for MC/Michelle, Stacy, Marcellina, Naa Aqueley,
  Christiana, Sister Mawuli, Miss Amponsah and Mr. Farrah; the rest of the cast
  is **derived from the closest design as distinct 2D sprites** (hair repainted,
  outfit hue-shifted, some mirrored) so everyone matches the same design yet
  reads as a different person. Rebuild with `py tools/build_character_sprites.py`.
- **21 audio files** (16-bit WAV loops) — each music track is a **simple song**
  (melody + bass line), and a music director keeps one playing at all times;
  ambient beds and a tap SFX complete the set.

They are generated by `py tools/generate_placeholders.py`. **Replacing any file
with real art/audio of the same name is all it takes** — the engine uses the
file instead of nothing, and audio works whatever its extension.

To add real assets, drop them into **`assets_inbox/`** and run:

```bat
py tools/install_assets.py
```

It copies each file to the correct name (cutting plain backgrounds off sprites
automatically) and reports what is left. See `assets_inbox/README.txt`.

See **`ASSET_REQUIREMENTS.md`** for the full list and **`ASSET_TRACKER.md`** to
tick items off. Preview everything at a glance with
`py tools/make_preview.py` → `PREVIEW_backgrounds.png`, `PREVIEW_characters.png`.

### Recommended VS Code extensions (optional)

If you edit the story in **VS Code**, install these two extensions:

- **Ren'Py Language (Official)** — gives `.rpy` files proper syntax
  highlighting, bracket matching and snippets, so dialogue, `label`s, `menu`s
  and embedded Python are colour-coded and easier to read instead of plain text.
- **Ren'Py Launch and Sync** — runs your project directly from the editor
  (**Launch**) and **hot-reloads** it: save a `.rpy` file and the running game
  updates in place without restarting. It reads the SDK path from
  `.vscode/settings.json` (`renpyWarp.sdkPath`, here pointing at the Ren'Py
  8.5.3 SDK), so no manual SDK configuration is needed.

---

## 3. Errors found and how they were fixed

Line numbers in the table refer to the **original** file
(`backup/script.original.rpy`). "Fix" describes what `tools/normalize_script.py`
or `game/definitions.rpy` now does.

### 3.1 Blocking errors (game would not even start)

| # | Original line(s) | Faulty code | Problem | Fix |
|---|---|---|---|---|
| 1 | file name | `game.py` | Ren'Py only loads `*.rpy` from a `game/` folder. A `.py` file is never loaded, and it is not valid Python either. | Renamed to `game/script.rpy` and placed under `game/`. |
| 2 | 1–1291 | Entire header + story repeated **4 times** (`default trust = 0` … `label start:` at lines 56, 480, 880, 1347) | 17 labels defined 4× → "label … is defined twice". | `extract_body()` keeps only the last (complete) copy. |
| 3 | 22 | `define mc = DynamicCharacter("[player_name]")` | `DynamicCharacter` is deprecated. | Replaced with `Character("[player_name]", dynamic=True)`. |
| 4 | 70, 494, 894, 1361 | `return` right after the name prompt in `ask_name` | `label start` fell into `label ask_name`; the `return` **ended the game immediately**; all following lines (72–…) were dead code. | `rebuild_opening()` now does `call ask_name` and lets the story continue. |
| 5 | 64, 488, 888, 1355 | `call screen name_input` | No `screen name_input` existed anywhere. | Added `screen name_input()` in `game/definitions.rpy`. |
| 6 | 3362, 3436, 3472, 5618, … | `scene bg warners_river_day:` | A stray `:` turned a `scene` statement into an invalid block opener. | Strip trailing `:` from all `scene`/`show` lines. |
| 7 | 825, 1271, 1292, 1738, 1764, 3303 | e.g. `"When the head girldefault trust = 0`, ` distant."`, `"…feelsdefault trust = 0`, `"…suddenly␠␠␠␠scene bg staircase` | A bad paste **merged two lines** into one (unterminated string / orphan text), a hard syntax error. | Repaired each merged line (see `fix_merged_lines()`); orphaned fragments deleted. |
| 8 | 2652–5191 (536+ lines) | indentation made of **U+202F** (narrow no-break space), e.g. lines 2703, 3140, 4757, 5161 | Python/Ren'Py only accept ASCII spaces for indentation → `SyntaxError: invalid non-printable character U+202F`. | `reindent()` treats U+202F/U+00A0 as spaces and re-emits every line with clean 4-space indentation. |
| 9 | many (Episodes 3–5) | `scene`/`if` at column 0 with dialogue at column 4 | "Line is indented, but the preceding statement does not expect a block." | `reindent()` normalises the entire block structure to 4-space levels. |

### 3.2 Broken control flow (jumps to labels that did not exist)

| # | Original line | Faulty code | Fix |
|---|---|---|---|
| 10 | 1819 | `jump scene_5Bii` (label is `scene_5Bii_reward_no_veronica`) | `fix_jumps()` retargets it. |
| 11 | 1865, 1981, 2217 | `jump scene_6` (label is `episode1scene_6`) | Retargeted to `episode1scene_6`. |
| 12 | 3217 | `jump ep2_scene8` (label is `ep2_scene8_identity`) | Retargeted. |
| 13 | 3354 | `jump ep3_start` — **no such label** | `fix_jumps()` inserts `label ep3_start:` before Episode 3 Scene 1. |
| 14 | 1718, 1744, 1766 | `label scene_4Bi` defined **3 times** | `remove_duplicate_label_blocks()` keeps the last (complete) one. |

### 3.3 Runtime `NameError`s (undefined variables)

The story used these without ever declaring them; each would crash the game the
first time that branch is reached. All are now `default`-ed in
`game/definitions.rpy`.

| # | Original line | Code |
|---|---|---|
| 15 | 2703 | `$ mc_attitude += 1` |
| 16 | 2711, 2773 | `$ mc_reserve += 1` / `elif mc_reserve >= 3:` |
| 17 | 3140, 3185 | `$ veronica_relationship -= 1` / `+= 1` |
| 18 | 4720 | `if accept_headboy_help:` (read before it was ever set) |
| 19 | 4811 | `elif headmistress_warning_seen:` |
| 20 | 5161+ | `$ club_name = "Red Cross"` (used in `[club_name]`) |
| 21 | 2802, 2806, 2808 | `naa_active`, `naa_relationship` |
| 22 | 3481, 3589, 3598, 4095, 4169, 4397, 4550, 4574, 4590, 4630, 4647, 4662 | `stacy_relationship`, `stacy_gossiped`, `mc_mackenzie_relationship`, `mc_remembers_sister`, `mc_visits_stacy`, `rumor_path`, `warning_path`, `stacy_path`, `memory_stat_high`, `focus_stat_low`, `stacy_talk_stat_high` |
| 30 | 2356, 2378, 2433, 2443, 2477, 2519, 2545, 2645 | `"[mc_name] sat quietly…"` — the text substitution `[mc_name]` was used **8 times** but the variable was never declared anywhere, so Ren'Py raises `NameError: name 'mc_name' is not defined` the moment Episode 2 scene 3 plays. | `fix_substitutions()` rewrites every `[mc_name]` to `[player_name]` (the player's chosen name). |

### 3.4 Runtime `NameError`s (undefined characters)

Speakers used in Episodes 3–5 that were never `define`d. Ren'Py is
case-sensitive, so `Teacher` ≠ `tr`, `Headmistress` ≠ `aa`, `veronica` ≠ `vr`.
All are now defined in `game/definitions.rpy`.

`Teacher`, `headboy`, `Headmistress`, `assistant_headmistress`, `hm`, `mk`,
`hg`, `dc`, `r`, `s`, `v`, `sis`, `sa`, `girl`, `Girl`, `girl_1`, `girl_2`,
`girl_3`, `student`, `Mc`, `Bus_driver`, `Sister_voice`, `teacher_pet`,
`security`, `nurse`, `veronica`.

### 3.5 Content / quality issues

| # | Original line(s) | Issue | Fix |
|---|---|---|---|
| 23 | 1857 | A whole paragraph was used as a menu *button* and had no body: `"[player_name] searches for the sister…"` | Turned into narration under the `"Look for the sister"` choice (`fix_scan_menu()`). |
| 24 | 5244, 5567, 5623, 5675 | `play music “quiet_night.mp3”` uses **curly quotes** as delimiters → syntax error. | All `play …` lines are commented out (audio is absent anyway). |
| 25 | 1874, 3458, 4704, 5202, 5244 | Audio paths such as `audio/zoo_ambience.mp3`, `school_grounds.mp3` do not exist in the project. | Playback disabled; documented above. |
| 26 | 36 | `define sd3 = Character("Rndom student 3")` (typo) | Corrected to "Random student 3". |
| 27 | 417, 1445, 1456, 1788, 1882, 3258 | Typos: `keps`, `fels`, `walkes`, `fells`, `watches`, `girldefault` | Left as-is in the story text (cosmetic); the fatal merged lines were fixed. |
| 28 | — | Dead stats: `attitude`, `reserve`, `tension_marcellina`, `friendship_marcellina`, `clue_teacher_tone`, `sister_targeting` are set but never read. | Kept (harmless). Listed as **follow-up work**. |
| 29 | 5718 | Story ends with `return` after `"The screen fades to black."` — Episode 5 Scene 8. | Kept as a valid ending; more story can be appended. |

### 3.6 Additional errors found on the second pass

`tools/validate_script.py` was written specifically to catch problems the first
sweep missed. It found four more real errors, all now fixed:

| # | Original line(s) | Faulty code | Problem | Fix |
|---|---|---|---|---|
| 31 | 5439 | `"It looks exactly the same.  ` (no closing `"`) | An **unterminated string**: Ren'Py sees the quote open and never close → `SyntaxError` when Episode 5 Scene 4 loads. | `fix_unterminated_strings()` appends the missing `"`. |
| 32 | 286 | `show mf in rush at center` | `in` is a **Python keyword** and not a valid sprite attribute; the `show` statement fails to parse. | Renamed the attribute: `show mf rushed at center`. |
| 33 | 2765–2781 | `if stacy_points >= 3:` … `elif mc_reserve >= 3:` … `else:` — all written at the **same** indent level with their bodies | The re-indenter could not tell where each branch began, so it left `elif`/`else` nested inside the previous branch → "Line is indented, but the preceding statement does not expect a block." | `reindent()` now tracks open `if` statements (`if_stack`) so `elif`/`else` always align with their `if`. |
| 34 | 3437, 3510, 3580, … (16 lines) | `stop ambience fadeout 2` | Ren'Py only defines the `music`, `sound` and `voice` channels; `ambience` is a **custom channel** that was never registered → `Exception: Channel "ambience" is not defined.` | `definitions.rpy` now calls `renpy.music.register_channel("ambience", ...)`, so the `stop ambience` lines are valid. |

### 3.7 Errors found by the real Ren'Py lint (third pass)

The standalone checker is good, but nothing beats the engine itself. Running
`renpy.exe <this folder> lint` with the **Ren'Py 8.5.3 SDK** reported four more
problems that only the real parser catches. All are fixed in
`tools/normalize_script.py`, and `lint` now exits **0**.

| # | Script line | Faulty code | Problem | Fix |
|---|---|---|---|---|
| 35 | 1523 | `if naa_active:` (body lost when the `default` lines were extracted) | `if statement expects a non-empty block.` — a block opener with nothing under it. | `fix_empty_blocks()` gives every empty opener (`if`/`else`/`menu`/`label`) a `pass` statement. |
| 36 | 2356 | `if stacy_gossiped: … else: … else:` — the second `else` (the *alone* path) was left flat at the same level as the first | `expected statement.` — an `if` can only have one `else`; the inner `if/else` chain had been flattened out of `if stacy_relationship >= 6:`. | `fix_nested_else()` detects a dangling `else` and indents the preceding `if … else` block one level, so the second `else` binds to the outer `if` again. |
| 37 | 4239 | `"Something about the way he reacts feels strange."s` | A stray `s` glued after the closing quote → `expected statement.` | `fix_trailing_junk()` removes leftover text after a closed dialogue string. |
| 38 | 1569 | `voice "tap"` | Loads a voice file that does not exist → lint warning `voice file 'tap' is not playable` (the `play …` lines were already commented out, `voice`/`queue` were missed). | Commented out like the other audio, in `fix_merged_lines()`. |

The validator now runs three extra checks so these cannot come back unnoticed:
**Empty blocks (no body)**, **Stray text after closing quote**, and a stricter
**Orphan elif/else** (the old version did not notice a *second* `else` for the
same `if`).


---

## 4. Verification that was performed

Run the standalone checker any time (no Ren'Py SDK needed):

```bat
py tools/validate_script.py
```

It currently reports **ALL CHECKS PASSED**, covering:

| Check | Result |
|---|---|
| Undefined text substitutions `[name]` | 0 |
| Duplicate labels | 0 |
| Missing `jump` / `call` targets | 0 |
| Undefined speakers | 0 |
| Bad whitespace (U+202F / NBSP / tab) | 0 |
| Unterminated quoted strings | 0 |
| Unbalanced `{}` in dialogue | 0 |
| Image attributes that are Python keywords | 0 |
| Stray `:` on non-opener lines | 0 |
| Empty menu choices | 0 |
| Orphan `elif` / `else` (incl. a second `else` for one `if`) | 0 |
| Empty blocks (`if`/`else`/`menu`/`label` with no body) | 0 |
| Stray text after a closing quote (`…"s`) | 0 |
| Active `play` / `voice` / `queue` audio lines | 0 |
| Unknown audio channels | 0 |
| Bare statements / unquoted narration | 0 |
| Curly-quote code delimiters | 0 |

### The real engine check (recommended)

With the Ren'Py SDK installed, the engine itself is the final word:

```bat
renpy.exe "C:\path\to\GameRenPY" lint
```

That was run with **Ren'Py 8.5.3** and exits **0** with **no warnings and no
errors**. It reports:

```
The game contains 1,495 dialogue blocks, containing 8,551 words and 50,316
characters, for an average of 5.7 words and 34 characters per block.

The game contains 8 menus, 99 images, and 24 screens.
```

(Every image used by the story is now declared in `game/images.rpy`, so the old
`… is not an image` warnings are gone, and every declared file exists, so the
placeholder callback no longer fires in normal play — see *Placeholders* above.)

**Asset completeness** is checked with:

```bat
py tools/generate_asset_tracker.py
```

which prints `Rows: 120 | Present: 120 | Missing: 0` for the shipped placeholder
set (refresh the art/audio any time with `py tools/generate_placeholders.py`).

`tools/normalize_script.py` is also **idempotent**: running it twice produces a
byte-for-byte identical `game/script.rpy`.


---

## 5. Comments added to the code

Every file is commented so it can be read by someone who has never seen Ren'Py:

- **`game/script.rpy`** — a header block explains the syntax, then every one of
  the 38 `label`s gets a banner comment naming the scene (e.g.
  `# label scene_4Bi  --  excursion day (positive variant)`), and every `menu:`
  gets a note marking it as a player choice. Comments are generated by
  `annotate()` in `tools/normalize_script.py`, so they survive re-runs.
- **`game/definitions.rpy`** — grouped and explained: variables (with what each
  stat means), characters, the name-entry screen (line by line), the
  placeholder-image callback, the custom `ambience` audio channel, the safe
  audio helpers (`play_bgm` / `play_ambience` / `play_sfx`), and the
  continuous-music director.
- **`game/images.rpy`** — every image declaration, grouped by scene type, with a
  header explaining how to add a file and how the placeholder system works.
- **`tools/normalize_script.py`'s `rewrite_audio()`** — documents how broken
  `play …` / `voice …` lines become guarded helper calls.
- **`tools/normalize_script.py`** — a numbered docstring lists every repair it
  performs, and each function has a docstring/comment explaining its job.
- **`tools/validate_script.py`** — documents each check and why it matters.
- **`tools/generate_asset_tracker.py`** — rebuilds `ASSET_TRACKER.md`/`.csv` from
  `game/images.rpy` and `game/script.rpy`, so the checklist can never drift.

---

## 6. Where to continue (next steps)

The game now loads and plays from `label start` → Episode 5. Suggested
follow-up work:

1. **Replace the placeholders with real assets (optional).** All 120 slots
   already ship with clean placeholders. Drop your files into `assets_inbox/` and
   run `py tools/install_assets.py`; it copies each to the right name (cutting
   backgrounds off sprites as needed) and reports what is left. Use
   **`ASSET_TRACKER.md`** (the 120-row checklist; regenerate with
   `py tools/generate_asset_tracker.py`) and **`ASSET_REQUIREMENTS.md`** plus the
   three reference docs for detail. Anything not supplied keeps its placeholder.
2. **Wire up the unused stats.** `friendship_marcellina`, `tension_marcellina`,
   `attitude`/`reserve`, `clue_teacher_tone`, `sister_targeting` are tracked but
   never checked. Add `if`/`menu` branches in `game/script.rpy` to use them.
3. **Continue the story.** The last scene (`game/script.rpy`, the block that
   ends with `"The screen fades to black."` then `return`) is Episode 5 Scene 8.
   Add `label ep6_start:` and a `jump` to it before that `return`.
4. **Rename/expand Episodes 3–5.** They are currently all inside one
   `label ep3_start:` block; split them into `ep3_scene1`, `ep4_scene1`, … for
   easier maintenance.
5. **Re-run the repair tool any time** with:
   ```bat
   py tools/normalize_script.py
   py tools/validate_script.py
   py tools/list_assets.py
   ```
   The repair tool always rebuilds from `backup/script.original.rpy`, so it never
   double-applies, and the validator confirms there are still no errors.
6. **Run Lint** in the Ren'Py launcher after adding art/audio to catch anything
   new.

---

### Quick reference: enter the game at any point

In the Ren'Py launcher you can use **"Navigate Script"** or set
`config.developer = True` (default) and press **Shift+O** in-game to open the
console. To jump to a specific scene type, e.g.:

```python
jump ep3_start
```
