# data/scenes.py

# ─── helper: variadic delta builder ────────────────────────────────────────────
def delta(*pairs: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Build a list of (trait_index, change) tuples.
    Pass anywhere from 0 to 4 (index, delta) pairs.
    """
    return list(pairs)

# ─── master scene table ───────────────────────────────────────────────────────
SCENES = {
    # ─────────── INTROS (unchanged) ───────────
    "intro_sock": {
        "banner": "banners/intro_sock.png",
        "prompt": "Scene 1: A Day with Sock",
        "narrative_steps": [
            { "text": "Sock wakes tangled in neon cables and feels a surge of anxiety.",
              "delta": delta((0, +1), (2, -1)) },
            { "text": "They hack together a quick script, boosting their confidence.",
              "delta": delta((1, +1)) },
            { "text": "A bold iced latte helps calm their nerves.",
              "delta": delta((1, +1), (0, -1)) },
            { "text": "They check messages—friends want to hang out, but they hesitate.",
              "delta": delta((3, +1), (2, -1)) },
            { "text": "Before leaving, Sock picks a sharp jacket that turns heads.",
              "delta": delta((1, +1), (3, -1)) },
        ],
        "next_scene": "char_a_scene2",
    },
    "intro_carol": {
        "banner": "banners/intro_carol.png",
        "prompt": "Scene 1: A Morning with Carol",
        "narrative_steps": [
            { "text": "Carol oversleeps again and curses her punctuality... too late for the bus.",
              "delta": delta((2, -1)) },
            { "text": "She kneels by the curb to soothe street cats, sharing quiet moments.",
              "delta": delta((0, +1)) },
            { "text": "An idea sparks—she scribbles a short poem on scrap paper.",
              "delta": delta((3, +1)) },
            { "text": "Spontaneously, she dashes into a pop-up gallery across the street.",
              "delta": delta((1, +1), (2, -1)) },
            { "text": "She livestreams a snippet of her poem and feels a rush.",
              "delta": delta((3, +1)) },
        ],
        "next_scene": "char_b_scene2",
    },
    "intro_bram": {
        "banner": "banners/intro_bram.png",
        "prompt": "Scene 1: Dawn with Bram",
        "narrative_steps": [
            { "text": "Bram laces up before sunrise, determination sharpening his focus.",
              "delta": delta((2, +1), (0, +1)) },
            { "text": "He runs through the playbook in his head—every pass and play.",
              "delta": delta((1, +1), (3, +1)) },
            { "text": "A quick gym session leaves him invigorated.",
              "delta": delta((0, +1)) },
            { "text": "He visualizes the blackout game plan, heart pounding.",
              "delta": delta((2, +1)) },
            { "text": "Finally, he skates out onto the ice, ready to conquer.",
              "delta": delta((0, +1), (2, +1)) },
        ],
        "next_scene": "char_c_scene2",
    },
    "intro_fatima": {
        "banner": "banners/intro_fatima.png",
        "prompt": "Scene 1: Fatima’s Morning Ritual",
        "narrative_steps": [
            { "text": "Fatima greets dawn with Fajr prayer, grounding her spirit.",
              "delta": delta((3, +1), (1, -1)) },
            { "text": "She pours her thoughts into a journal beneath a candle’s glow.",
              "delta": delta((3, +1)) },
            { "text": "Breakfast of cumin seeds fuels her quietly.",
              "delta": delta((2, +1), (3, +1)) },
            { "text": "A call with her mother warms her heart.",
              "delta": delta((3, +1), (0, +1)) },
            { "text": "She selects a vibrant hijab—bold against morning light.",
              "delta": delta((3, +1), (2, -1)) },
        ],
        "next_scene": "char_d_scene2",
    },

    # ─────────── SCENE 2: Getting to the University ───────────
    # banner shared_2.png used for all four; prompts & options unique:
    "char_a_scene2": {
        "banner": "banners/shared_2.png",
        "prompt": "It’s the first day of Uni. Sock stands at the bus stop fifteen minutes early, hood up and headphones on, playlist already on shuffle.",
        "options": [
            ("Wait for the crowded bus, dive into the fluorescent hum of strangers.", 
             "char_a_scene3", delta((1, +1), (0, -1), (2, +1))),
            ("Unlock their bike and pedal off into the dawn, freedom circulating.", 
             "char_a_scene3", delta((1, -1), (0, +1), (3, -1))),
            ("Laugh at the idea of Uber—maybe a stranger’s playlist will calm them.", 
             "char_a_scene3", delta((0, +1), (1, -1), (3, -1))),
        ],
    },
    "char_b_scene2": {
        "banner": "banners/shared_2.png",
        "prompt": "It’s the first day of Uni, and Carol’s already in motion—leather jacket zipped up, hair dyed pink, the city humming with possibility.",
        "options": [
            ("Jam into the packed tram and ride the buzz of the crowd.", 
             "char_b_scene3", delta((2, +1), (0, -1))),
            ("Hop on her bike, feel the wind between her tattoos.", 
             "char_b_scene3", delta((3, +1), (1, -1))),
            ("Call a taxi—promise of a private car, promise of escaping the chaos.", 
             "char_b_scene3", delta((1, +1), (2, -1), (3, -1))),
        ],
    },
    "char_c_scene2": {
        "banner": "banners/shared_2.png",
        "prompt": "On this momentous day—first day of university—Bram stands at the station in quiet control, hockey stick angled against the wall, considering his transport options.",
        "options": [
            ("Board the tram: swift and punctual, guarantees he won’t miss first lecture.", 
             "char_c_scene3", delta((1, -1), (0, -1))),
            ("Pedal his bike: every turn of the wheel sharpens focus and boosts fulfillment.", 
             "char_c_scene3", delta((3, +1), (0, +1))),
            ("Call a taxi: skip the hassle, arrive calm but feels unearned.", 
             "char_c_scene3", delta((1, +1), (3, -1), (0, -1))),
        ],
    },
    "char_d_scene2": {
        "banner": "banners/shared_2.png",
        "prompt": "It’s Fatima’s first day on campus, and the morning air carries the promise of possibility as she shoulders her backpack, deciding how she wants to face the world today.",
        "options": [
            ("Take the tram: quickest route but a sea of faces makes her uneasy.", 
             "char_d_scene3", delta((1, -1), (0, -1))),
            ("Hop on her bike: familiar rhythm brings comfort even if it tires her out.", 
             "char_d_scene3", delta((1, +1), (0, -1))),
            ("Call a taxi: private and gentle, though it costs more than she earned.", 
             "char_d_scene3", delta((0, +1), (1, -1), (3, -1))),
        ],
    },

    # ─────────── SCENE 3: Choosing a Seat ───────────
    # banner shared_3.png
    "char_a_scene3": {
        "banner": "banners/shared_3.png",
        "prompt": "Sock steps into the lecture hall of the Introductory Info Session. The choice of seat could make or break the day.",
        "options": [
            ("Front row: bold and exposed, signal they can handle the glare.", 
             "char_a_scene4", delta((3, +1), (0, -1), (1, -1))),
            ("Middle: safe ground, enough buzz to feel alive but not overwhelmed.", 
             "char_a_scene4", delta((0,  0), (1, +1))),
            ("Back row: sanctuary of shadows, distance shields them from prying eyes.", 
             "char_a_scene4", delta((1, +1), (2, -1))),
        ],
    },
    "char_b_scene3": {
        "banner": "banners/shared_3.png",
        "prompt": "Carol arrives late to the info session, scanning for a seat that matches her mood.",
        "options": [
            ("Front row: she feeds off the energy, ready to own the room.", 
             "char_b_scene4", delta((2, +1), (1, -1))),
            ("Middle: a little distance keeps her prepared but not lonely.", 
             "char_b_scene4", delta((3, +1), (0,  0))),
            ("Back row: privacy and space to think, even if it means missing nuance.", 
             "char_b_scene4", delta((1, +1), (2, -1))),
        ],
    },
    "char_c_scene3": {
        "banner": "banners/shared_3.png",
        "prompt": "Bram chooses his seat with strategy—where will optimize his focus?",
        "options": [
            ("Front: best sightlines, can anticipate questions ahead of time.", 
             "char_c_scene4", delta((2, +1), (0,  0))),
            ("Middle: supportive hum but not too much distraction.", 
             "char_c_scene4", delta((1, +1), (3,  0))),
            ("Back: room to observe without pressure to perform.", 
             "char_c_scene4", delta((3, +1), (2, -1))),
        ],
    },
    "char_d_scene3": {
        "banner": "banners/shared_3.png",
        "prompt": "Fatima finds herself choosing: front for clarity, middle for comfort, back for calm.",
        "options": [
            ("Front: clear view but potential discomfort amid interruptions.", 
             "char_d_scene4", delta((1, -1), (3, +1))),
            ("Middle: gentle balance of awareness and ease.", 
             "char_d_scene4", delta((1, +1), (2,  0))),
            ("Back: peaceful refuge, though she might feel distant.", 
             "char_d_scene4", delta((2, +1), (3, -1))),
        ],
    },

    # ─────────── SCENE 4: Lunch Break Choices ───────────
    # banner shared_4.png
    "char_a_scene4": {
        "banner": "banners/shared_4.png",
        "prompt": "Lunch break. Students spill into open spaces—where will Sock refuel?",
        "options": [
            ("Cafeteria: loud chatter, test their nerves but boost social energy.", 
             "char_a_scene5", delta((2, +1), (1, -1), (0, -1))),
            ("Café: warm lights, chill music, a calm reset for their mind.", 
             "char_a_scene5", delta((1, +1), (3, +1), (0, +1))),
            ("Empty lab: quiet solitude, refuel thoughts though feel alone.", 
             "char_a_scene5", delta((1, +1), (3, +1), (2, -1))),
        ],
    },
    "char_b_scene4": {
        "banner": "banners/shared_4.png",
        "prompt": "Lunch hour beckons—Carol must pick a spot to recharge or perform.",
        "options": [
            ("Cafeteria: dive into the chaos, slam a sandwich mid-poem.", 
             "char_b_scene5", delta((2, +1), (1, -1), (0, -1))),
            ("Café: notebooks open, pen ready for fresh lines.", 
             "char_b_scene5", delta((1, +1), (3, +1), (0, +1))),
            ("Empty hall: echoes support her need for space—write in peace.", 
             "char_b_scene5", delta((3, +1), (1, +1), (2, -1))),
        ],
    },
    "char_c_scene4": {
        "banner": "banners/shared_4.png",
        "prompt": "Lunch break arrives—Bram weighs community versus focus.",
        "options": [
            ("Cafeteria: energy of the crowd, but noise disrupts strategy.", 
             "char_c_scene5", delta((0, -1), (2, +1), (1, -1))),
            ("Café: structured calm—a chance to plan next play.", 
             "char_c_scene5", delta((1, +1), (3, +1))),
            ("Quiet library nook: solitude sharpens mind but feels lonely.", 
             "char_c_scene5", delta((2, -1), (3, +1))),
        ],
    },
    "char_d_scene4": {
        "banner": "banners/shared_4.png",
        "prompt": "It’s midday—Fatima must choose where her heart and mind feel best.",
        "options": [
            ("Cafeteria: warm faces around a bustling table.", 
             "char_d_scene5", delta((2, +1), (1, -1), (0, -1))),
            ("Café: gentle light and soft music soothe her spirit.", 
             "char_d_scene5", delta((1, +1), (3, -1))),
            ("Quiet study room: sanctuary for reflection and prayer.", 
             "char_d_scene5", delta((1, +1), (3, +1), (2, -1))),
        ],
    },

    # ─────────── SCENE 5: Group Assignment ───────────
    # banner shared_5.png
    "char_a_scene5": {
        "banner": "banners/shared_5.png",
        "prompt": "In the next lecture, the professor announces a group assignment—who will Sock end up with?",
        "options": [
            ("Inclusive group: collaboration boosts fulfillment and comfort.", 
             "char_a_scene6", delta((3, +1), (1, +1), (2, +1))),
            ("Microaggressive group: draining remarks test their resilience.", 
             "char_a_scene6", delta((1, -1), (0, -1))),
            ("Neutral group with barriers: polite but distant, leaves mixed feelings.", 
             "char_a_scene6", delta((1,  0), (3,  0), (0, -1))),
        ],
    },
    "char_b_scene5": {
        "banner": "banners/shared_5.png",
        "prompt": "Professor pairs Carol with classmates for the first group project.",
        "options": [
            ("Inclusive team: sparks fly, poetry finds new ears.", 
             "char_b_scene6", delta((3, +1), (2, +1))),
            ("Microaggressive team: barbs in verse leave her cold.", 
             "char_b_scene6", delta((3, -1), (2, -1))),
            ("Neutral but barred: effort expected, rewards unclear.", 
             "char_b_scene6", delta((0, -1), (3, +1), (1,  0))),
        ],
    },
    "char_c_scene5": {
        "banner": "banners/shared_5.png",
        "prompt": "Bram joins his assigned project group, ready or not.",
        "options": [
            ("Supportive colleagues: shared drive ignites his passion.", 
             "char_c_scene6", delta((1, +1), (2, +1), (3, +1))),
            ("Toxic clique: carries slackers, saps his energy.", 
             "char_c_scene6", delta((0, -1), (1, -1))),
            ("Neutral group: polite but passive—he must push himself.", 
             "char_c_scene6", delta((3, +1), (0, -1))),
        ],
    },
    "char_d_scene5": {
        "banner": "banners/shared_5.png",
        "prompt": "Fatima stands among her new group, wondering where she belongs.",
        "options": [
            ("Welcoming circle: shared faith and support uplift her.", 
             "char_d_scene6", delta((1, +1), (2, +1), (3, +1))),
            ("Exclusive clique: subtle judgments drain her spirit.", 
             "char_d_scene6", delta((1, -1), (0, -1))),
            ("Quiet cluster: polite but distant, she steps in quietly.", 
             "char_d_scene6", delta((2, +1), (0, -1))),
        ],
    },

    # ─────────── SCENE 6: After-Class Socializing ───────────
    # banner shared_6.png
    "char_a_scene6": {
        "banner": "banners/shared_6.png",
        "prompt": "Class is over, but the day isn’t done. Sock’s classmates invite them out—where to?",
        "options": [
            ("Head to the local bar: loud, chaotic, a chance to connect.", 
             "final_sock", delta((2, -1), (1, -1), (0, -1))),
            ("Join the park gathering: barefoot refuge under the trees.", 
             "final_sock", delta((1, +1), (2, +1))),
            ("Check out the community event: culture and music calling.", 
             "final_sock", delta((2, +1), (3, +1), (0, -1))),
        ],
    },
    "char_b_scene6": {
        "banner": "banners/shared_6.png",
        "prompt": "Class wraps up, and Carol must choose how to cap off her day’s whirlwind.",
        "options": [
            ("Encore at the local bar: raw energy meets late-night crowd.", 
             "final_carol", delta((2, +1), (1, -1))),
            ("Stroll to the nearby park: calm air and soft laughter.", 
             "final_carol", delta((1, +1), (0,  0))),
            ("Attend the cultural event: poetry, food, and shared stories.", 
             "final_carol", delta((3, +1), (2, +1), (1, +1))),
        ],
    },
    "char_c_scene6": {
        "banner": "banners/shared_6.png",
        "prompt": "Bram packs up his gear. A teammate offers plans—where will he go?",
        "options": [
            ("Local bar: raucous cheering and quick camaraderie.", 
             "final_bram", delta((2, +1), (1, -1), (3, +1))),
            ("Quiet park: space to breathe and reflect under open sky.", 
             "final_bram", delta((1, +1), (0, -1), (2, -1))),
            ("Community event: music and stories from home abroad.", 
             "final_bram", delta((2, +1), (3, +1))),
        ],
    },
    "char_d_scene6": {
        "banner": "banners/shared_6.png",
        "prompt": "Class ends, and Fatima is invited out—she considers where feels most like home.",
        "options": [
            ("Local bar: a flood of noise, but warmth in shared laughter.", 
             "final_fatima", delta((1, -1), (2, +1), (0, +1))),
            ("Park gathering: gentle breeze and whispered greetings.", 
             "final_fatima", delta((1, +1), (2, +1))),
            ("Cultural event: familiar rhythms and community stories.", 
             "final_fatima", delta((3, +1), (2, +1))),
        ],
    },

    # ─────────── FINALES (unchanged) ───────────
    "final_sock": {
        "banner": "banners/final_sock.png",
        "prompt": "Sock’s art illuminates the café as power returns.",
        "options": [("Roll credits", None, delta())],
    },
    "final_carol": {
        "banner": "banners/final_carol.png",
        "prompt": "Carol leads an impromptu concert to celebrate.",
        "options": [("Roll credits", None, delta())],
    },
    "final_bram": {
        "banner": "banners/final_bram.png",
        "prompt": "Bram’s patch becomes tomorrow’s headline breakthrough.",
        "options": [("Roll credits", None, delta())],
    },
    "final_fatima": {
        "banner": "banners/final_fatima.png",
        "prompt": "Fatima records oral histories of the blackout in four languages.",
        "options": [("Roll credits", None, delta())],
    },
}
