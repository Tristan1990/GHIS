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

    # ─────────── INTROS (updated 2025-06-06) ───────────
    "intro_sock": {
        "banner": "banners/intro_sock.png",
        "prompt": "Scene 1: A Day with Sock",
        "narrative_steps": [
            {
                "text": "Yesterday evening was a whirlwind. Sock had been spiraling a bit, nervously googling the campus route - three times. What if they miss the bus? What if they show up underdressed? Overdressed? They laid out outfit options: one look that screams \"cunty queen\", and one back-up, just in case the morning self had regrets.",
                "delta": delta((3, +1), (0, -1))
            },
            {
                "text": "They'd meant to sleep early, but their brain had other plans. YouTube. Scrolling. A half hour of \"What I Wore to Uni\" videos turned into two. At some point, sleep won.",
                "delta": delta((0, -1), (1, +1))
            },
            {
                "text": "Now the alarm rings. Sock shoots up. Heart pounding, mental checklist: Bag? Packed. ID? Found. Outfit? Confirmed - going for the bold choice: a recently thrifted top, loose pants, favourite neon-green boots. The look slays.",
                "delta": delta((3, +1))
            },
            {
                "text": "They sip cold oat milk coffee while skimming past unread family messages. Just the preview makes their throat tighten. Not today.",
                "delta": delta((1, -1))
            },
            {
                "text": "Then buzz. A meme from their queer professor, a joke only they'd get. They snort. For a second, they feel seen.",
                "delta": delta((2, +1))
            },
            {
                "text": "Before stepping out, they do one last nervous check: piercings? All in. Chipped black nails? Flawless. The patch on their bag says, \"Guillotines for Billionaires\" - just in case anyone forgets where they stand.",
                "delta": delta((3, +1), (1, -1))
            },
        ],
        "next_scene": "char_a_scene2",
    },

    "intro_carol": {
        "banner": "banners/intro_carol.png",
        "prompt": "Scene 1: A Morning with Carol",
        "narrative_steps": [
            {
                "text": "Carol wakes up to her third alarm, sunlight already slicing through the blinds. She's buzzing with energy, her brain firing ideas for the day: new faces, new poems, maybe even a flirtation or two.",
                "delta": delta((2, +1), (0, -1))
            },
            {
                "text": "She throws on her favorite oversized tee and dances into the kitchen, blasting indie music and narrating her morning like a cooking show host. A full vegetarian breakfast takes shape: tomato egg stir-fry, scallion pancakes, perfectly brewed oolong.",
                "delta": delta((3, +1))
            },
            {
                "text": "But time slips through her fingers. She looks at the clock - late again. She curses under her breath and shoves the untouched breakfast into containers. It smells amazing but she doesn't have time for even a bite.",
                "delta": delta((0, -1), (1, -1))
            },
            {
                "text": "By the mirror, she quickly draws on her eyeliner, fluffs her hair, and throws on a leather jacket like armor. She looks confident. She is confident. Sort of.",
                "delta": delta((1, +1), (3, +1))
            },
            {
                "text": "As she rushes out, she spots a familiar orange street cat lounging on her doorstep. \"You better manifest a good day for me,\" she says, blowing it a kiss. The cat blinks. That's a yes.",
                "delta": delta((3, +1), (2, +1))
            },
        ],
        "next_scene": "char_b_scene2",
    },

    "intro_bram": {
        "banner": "banners/intro_bram.png",
        "prompt": "Scene 1: Dawn with Bram",
        "narrative_steps": [
            {
                "text": "The alarm buzzes just before seven. Bram sits up, blinking against the blur. Glasses on, world sharpened - slightly. He reaches for his phone, letting the app read the news and hockey scores aloud, before even leaving bed.",
                "delta": delta((3, +1), (0, -1))
            },
            {
                "text": "In the kitchen, his breakfast is functional: oats, protein shake, supplements lined up like clockwork. He moves efficiently, body trained for routine.",
                "delta": delta((0, +1))
            },
            {
                "text": "Before heading out, he double-checks his planner: training tomorrow, reading group on Wednesday, debate prep due soon. Satisfied, he tucks it away.",
                "delta": delta((3, +1))
            },
            {
                "text": "At the door, his hockey stick leans in the corner. Not today - but the sight grounds him. He pauses, then sends a quick voice message to his teammate about the next match lineup.",
                "delta": delta((2, +1))
            },
            {
                "text": "Backpack on, glasses slightly fogged, Bram steps outside. The air is brisk, but the path is familiar. A new day, one more chance to get it right.",
                "delta": delta((1, -1), (3, +1))
            },
        ],
        "next_scene": "char_c_scene2",
    },

    "intro_fatima": {
        "banner": "banners/intro_fatima.png",
        "prompt": "Scene 1: Fatima’s Morning Ritual",
        "narrative_steps": [
            {
                "text": "Fatima wakes before the sun, the world still hushed as she prays Fajr. The familiar rhythm of the verses centers her for the day ahead.",
                "delta": delta((3, +1), (0, -1))
            },
            {
                "text": "Instead of crawling back into bed, she lights her journal with early thoughts - reflections, hopes, and quiet strength spilled in ink.",
                "delta": delta((3, +1), (0, -1))
            },
            {
                "text": "In the kitchen, she takes her teaspoon of black cumin seeds, a small but sacred ritual, and eats breakfast in calm silence.",
                "delta": delta((0, +1), (3, +1))
            },
            {
                "text": "Her phone buzzes. It's her mom. Of course. Their voices weave through the still morning, warm and grounding.",
                "delta": delta((3, +1), (2, +1))
            },
            {
                "text": "Later, standing in front of the mirror, she hesitates, then chooses a vibrant hijab that reflects how she wants to feel today: bold, true, and alive.",
                "delta": delta((3, +1), (1, -1))
            },
            {
                "text": "Before leaving, she slips in her earbuds: no music, just affirmations and Quran recitations to steady her spirit.",
                "delta": delta((1, +1), (3, +1))
            },
        ],
        "next_scene": "char_d_scene2",
    },


    # ─────────── SCENE 2: Getting to the University ───────────
    # banner shared_2.png used for all four; prompts & options unique:
    "char_a_scene2": {
        "banner": "banners/shared_1.png",
        "prompt": "It’s the first day of Uni. Sock stands at the bus stop fifteen minutes early, fingers twitching as they re-check their bag: ID? Check. Water bottle? Check. Confidence? TBD. This has all been rehearsed a million times already - they’ve memorized the building’s name, floor count, and entrance photos. They take a deep breath and get ready: hood up, headphones on, playlist already on shuffle.",
        "options": [
            (
                "The bus arrives, crowded and humming with fluorescent tension. They slide into their usual seat. Familiar. Predictable. They press play - aggressively upbeat queer bops. One more distraction. One more breath. They check the bus schedule inside the bus. Twice. Okay, maybe four times. They’ve already texted their friend: “Wanna go in together?” Not out of fear, just for the gezelligheid.",
                "char_a_scene3",
                delta((1, +1), (0, -1), (2, +1))
            ),
            (
                "Their bike is chained nearby, a tempting escape route. Riding solo would be quiet, efficient, no scanning the crowd for stares. Just wind, wheels, and autonomy. But there’s no prep rituals, no buffer. It’s freedom, sure. But maybe too much of it.",
                "char_a_scene3",
                delta((1, -1), (0, +1), (3, -1))
            ),
            (
                "They laugh dryly at the thought of calling an Uber. It’d be late. They’d get there flustered but alone, stretched out in capitalist luxury. No staring teens. No crush of bodies. But they can already hear the guilt in their head: “You paid for that?” Still, it would be calm. Sort of.",
                "char_a_scene3",
                delta((0, +1), (1, -1), (3, -1))
            ),
        ],
    },

    "char_b_scene2": {
        "banner": "banners/shared_1.png",
        "prompt": (
            "It’s the first day of Uni, and Carol’s already in motion - leather jacket on, "
            "headphones around her neck, mind racing with everything and nothing. The city hums "
            "with possibility, and she’s got to pick her ride."
        ),
        "options": [
            (
                "The tram is packed, shoulder-to-shoulder with strangers, someone’s breath too close, "
                "someone else’s music too loud. It’s chaotic, overstimulating, but also alive. A cute "
                "stranger catches her eye for half a second, and for Carol, that half-second matters.",
                "char_b_scene3",
                delta((2, +1), (0, -1))
            ),
            (
                "Her bike leans against the railing, waiting. The solo ride would be easy enough: "
                "streets she knows, wind in her hair, no pressure, no surprises. But something about "
                "it feels too... quiet. She thrives on unexpected moments, and biking alone means "
                "missing them.",
                "char_b_scene3",
                delta((3, +1), (1, -1))
            ),
            (
                "She smirks at the idea of a taxi - classic Carol move. Ubered, unbothered, and definitely late. "
                "But she’d get to stretch out in the backseat, tunes playing, eyes closed, no one in her space. "
                "The cost? Missing the early chaos, and the chance to vibe with someone new.",
                "char_b_scene3",
                delta((1, +1), (2, -1), (3, -1))
            ),
        ],
    },

    "char_c_scene2": {
        "banner": "banners/shared_1.png",
        "prompt": (
            "On this momentous day: the first day of University year, Bram steps outside, "
            "bag packed with textbooks and prepped summer-reading notes. The morning is cool, "
            "sky grey, the kind of weather that makes him pick efficiency over comfort. He weighs "
            "his options - not just for time, but for how he wants to start the day."
        ),
        "options": [
            (
                "The tram is quick and gets him to campus in time to grab a coffee before class. "
                "But the noise, the crowd, and the jostling bodies set his nerves on edge. He hates "
                "being rushed, and this guarantees it.",
                "char_c_scene3",
                delta((1, -1), (0, -1))
            ),
            (
                "His bike ride is longer, but the rhythm of pedaling helps him settle into the day. "
                "No waiting, no unexpected delays, just movement and time to think. He knows the route "
                "like the back of his hand.",
                "char_c_scene3",
                delta((3, +1), (0, +1))
            ),
            (
                "He could also call a Taxi, avoiding the hassle altogether. It’s the most relaxed option, "
                "and he’ll arrive focused. Still, he can’t shake the feeling that he’s skipping a step - "
                "taking a shortcut he didn’t quite earn.",
                "char_c_scene3",
                delta((1, +1), (3, -1), (0, -1))
            ),
        ],
    },

    "char_d_scene2": {
        "banner": "banners/shared_1.png",
        "prompt": "It’s Fatima’s first day on campus, and the morning air carries the promise of possibility as she shoulders her backpack, deciding how she wants to face the world today.",
        "options": [
            (
                "The tram is the quickest option, but it’s also the one she dreads. The crowd, the stares, sometimes even the comments, weigh heavier than her bag.",
                "char_d_scene3",
                delta((1, -1), (0, -1))
            ),
            (
                "She glances at her bike. It’s not the easiest ride, but it’s hers. The path to campus might take longer, but the wind in her face, quiet streets, no stares, just breath and movement, provide a sense of freedom she doesn’t always feel in public. ",
                "char_d_scene3",
                delta((1, +1), (0, -1))
            ),
            (
                "Or maybe she could call a Taxi, stay tucked away in the backseat, grateful for the privacy. But the morning traffic makes her chest tighten. Will she be late? Is this worth it?",
                "char_d_scene3",
                delta((0, +1), (1, -1), (3, -1))
            ),
        ],
    },

    # ─────────── SCENE 3: Choosing a Seat ───────────
    # banner shared_3.png
    "char_a_scene3": {
        "banner": "banners/shared_2.png",
        "prompt": (
            "Sock steps into the lecture hall of the Introductory Info Session like it’s a battlefield. "
            "The lights feel too white, the chatter too sharp. They pick at their chipped nail polish, "
            "eyes scanning the rows like cover options. Where they sit could make or break the rest of the day."
        ),
        "options": [
            (
                "The front row pulses like a dare. It’s bold, exposed but every word sinks in here. "
                "They’d catch everything, maybe even ask a question afterward if the speaker seemed chill. "
                "But every glance would sting. The effort to stay composed might cost them more than it’s worth.",
                "char_a_scene4",
                delta((3, +1), (0, -1), (1, -1))
            ),
            (
                "The middle section feels like a coin toss. It’s safe enough if they keep their head down, "
                "risky if they don’t. They might manage to take a photo of the slides, whisper a question to the person next to them, "
                "and jot down some deadlines. But the ambient chaos is hard to block out.",
                "char_a_scene4",
                delta((0,  0), (1, +1))
            ),
            (
                "The back row calls like a refuge. No eyes. No pressure. Just space to breathe, observe, and maybe sketch a tiny Moss in the margin of their notes. "
                "They’d stay focused, write down the details, and double-log every deadline - pen and phone, always both. If they liked their neighbor, they might even ask a follow-up question. Quiet confidence.",
                "char_a_scene4",
                delta((1, +1), (2, -1))
            ),
        ],
    },
    "char_b_scene3": {
        "banner": "banners/shared_2.png",
        "prompt": (
            "Carol is late but unbothered as she gets to the room of the Introductory Info Session. "
            "The lecture hall doors swing open, and Carol steps inside, eyes wide with curiosity but brain already wandering. "
            "The room is energized: voices bouncing off the high ceilings, chairs scraping, someone laughing too loud in the back."
        ),
        "options": [
            (
                "The front row catches her eye. It’s loud, lively, full of bold energy. She spots someone with a tote bag from a queer bookshop she loves - tempting. "
                "She knows she’ll probably get distracted, maybe even end up whispering jokes mid-lecture. She may not absorb everything the lecturer says, but at least she won’t be bored.",
                "char_b_scene4",
                delta((2, +1), (1, -1))
            ),
            (
                "The middle feels like neutral ground - enough background chatter to stay engaged, but not so much that she spirals.",
                "char_b_scene4",
                delta((3, +1), (0,  0))
            ),
            (
                "Then there’s the back. Quiet, calm, and distant. She knows she could zone out there, scroll through memes, maybe write a quick poem or draw a doodle of cats with punk hairstyles. But zoning out too early might cost her focus for the rest of the day.",
                "char_b_scene4",
                delta((1, +1), (2, -1))
            ),
        ],
    },
    "char_c_scene3": {
        "banner": "banners/shared_2.png",
        "prompt": (
            "Bram arrives early to the Introductory Info Session, just like he planned. "
            "The lecture hall is still half-empty, sunlight filtering through the high windows. He takes a slow breath and surveys the room - not in hesitation, but in quiet control. Time to choose."
        ),
        "options": [
            (
                "The front is a clear choice. No distractions, no chatter - just focus. He likes the feeling of being prepared, of taking things seriously. "
                "He’s not worried about being watched; if anything, he hopes it shows he’s here to get things done.",
                "char_c_scene4",
                delta((2, +1), (0,  0))
            ),
            (
                "The middle is fine, neutral, really. Not too chaotic, not too exposed. If he needed to blend in or just observe, this would work. But with the freedom to choose, it doesn’t quite match his pace.",
                "char_c_scene4",
                delta((1, +1), (3,  0))
            ),
            (
                "The back is the last place he wants to be. People already whispering, scrolling on their phones, halfway tuned out. That kind of energy makes his jaw tighten. If he’s here, he wants to be here, and he wishes everyone else felt the same. Besides, if the slides are full of tiny text, he won’t catch any of it, and",
                "char_c_scene4",
                delta((3, +1), (2, -1))
            ),
        ],
    },
    "char_d_scene3": {
        "banner": "banners/shared_2.png",
        "prompt": (
            "It's the time for the first Introductory Info Session. Fatima steps into the large lecture hall, "
            "the hum of voices echoing off the walls. Rows of seats stretch out before her: front, middle, and back, "
            "each offering its own kind of experience. She clutches the strap of her bag and surveys the room."
        ),
        "options": [
            (
                "The front is far too exposed. She worries about being called on, or worse, being watched. If she forces herself to sit there, she’ll immediately feel the weight of eyes, her heart beating faster every time the lecturer looks up. But still, it might make her feel proud for facing her fear.",
                "char_d_scene4",
                delta((1, -1), (3, +1))
            ),
            (
                "The middle feels unpredictable. It’s not bad - not too exposed, not too hidden. But the constant movement and chatter around her might make it hard to focus.",
                "char_d_scene4",
                delta((1, +1), (2,  0))
            ),
            (
                "Her natural choice would be the back. It’s where she feels least visible. A quiet corner where she can breathe, observe, and ease into the rhythm of this new place. The chances of spontaneous interactions with new classmates are slim, though.",
                "char_d_scene4",
                delta((2, +1), (3, -1))
            ),
        ],
    },


    # ─────────── SCENE 4: Lunch Break Choices ───────────
    # banner shared_3.png  (replacing shared_4 with shared_3)
    "char_a_scene4": {
        "banner": "banners/shared_3.png",
        "prompt": (
            "Lunch break. Students spill into open spaces, laughing, calling out to each other. "
            "Sock clutches their bag a little tighter. They scan the options, calculating where "
            "they’ll feel least like they have to perform."
        ),
        "options": [
            (
                "The Cafeteria is loud and chaotic. People trying too hard. Jokes that don’t land. "
                "A few familiar faces. They could sit here, maybe get a compliment on their boots, "
                "maybe offer their spare snack to someone who forgot theirs. They’d mostly listen, "
                "nod, and ask safe questions - about hobbies, hometowns, the stuff that doesn't demand too much. "
                "It’s draining, but manageable if they pick the right seat. They won’t eat much though - their appetite is tangled in nerves.",
                "char_a_scene5",
                delta((2, +1), (1, -1), (0, -1))
            ),
            (
                "The Café has a better vibe: warm lights, chill music, and a smaller group of people. "
                "The nerves lessen and Sock is able to enjoy their food. The conversations are slow, "
                "thoughtful. No pressure to overshare, no need to perform. Just mutual quiet, good questions, "
                "and the soft clink of mugs. It’s calm and kind of lovely.",
                "char_a_scene5",
                delta((1, +1), (3, +1), (0, +1))
            ),
            (
                "An empty lab room is tucked behind the bio building. They sneak in, drop their bag, "
                "and eat one sandwich in silence, watching their petri dish from earlier that week settle under the light. "
                "It’s peaceful here. Maybe lonely. But peaceful. They text no one. They refuel quietly.",
                "char_a_scene5",
                delta((1, +1), (3, +1), (2, -1))
            ),
        ],
    },
    "char_b_scene4": {
        "banner": "banners/shared_3.png",
        "prompt": (
            "Lunch hits, and Carol’s stomach growls loud enough to turn heads. She digs through her bag "
            "and finds the glorious, slightly squashed breakfast she never had time to eat - still warm-ish in its foil wrap. "
            "Now the question is: where to post up and devour it?"
        ),
        "options": [
            (
                "She could head to the Cafeteria, where the energy is loud and wild. The buzz might drain her a little, "
                "but there’s always the thrill of spontaneous connection. Someone might compliment her tattoos and in no time "
                "the conversation will spiral into queer book recs and concert plans.",
                "char_b_scene5",
                delta((2, +1), (1, -1), (0, -1))
            ),
            (
                "The Café looks cute and cozy - low lighting, indie playlists, latte art. But the vegetarian options suck, "
                "and she can’t eat her own food there. She’d probably end up alone, watching other people hang out, "
                "feeling a little too still for her liking.",
                "char_b_scene5",
                delta((1, +1), (3, +1), (0, +1))
            ),
            (
                "There’s also a quiet private room she passed earlier. No one’s ever in there. She could sit by the window, "
                "scroll for a bit, reminisce about the time she met her favourite writer at an open-mic event that one time..ahh. "
                "But with no energy around her, she knows her brain might start drifting into boredom, or worse, self-doubt.",
                "char_b_scene5",
                delta((3, +1), (1, +1), (2, -1))
            ),
        ],
    },
    "char_c_scene4": {
        "banner": "banners/shared_3.png",
        "prompt": (
            "Lunchtime. Bram checks his watch, then his calendar. An hour free - enough to refuel and reset. "
            "He’s already thinking about the afternoon lecture, but for now, food comes first."
        ),
        "options": [
            (
                "The Cafeteria is buzzing. He spots a few people from the info session and debates whether to approach. "
                "He takes a breath, then asks if anyone knows about the university’s sports association. It’s a bit out of his comfort zone, "
                "but worth the effort. The bright lights give him a bit of a headache.",
                "char_c_scene5",
                delta((0, -1), (2, +1), (1, -1))
            ),
            (
                "The Café is calm, clean, and well-lit - his kind of place. The menu lists a few high-protein options, "
                "and he orders something balanced without thinking twice. He sits by the window, quietly satisfied.",
                "char_c_scene5",
                delta((1, +1), (3, +1))
            ),
            (
                "There’s a quiet room just down the hall - no food service, but perfect for a break. He unwraps his packed lunch "
                "and turns on an audiobook. Time slows. It’s not social, but he doesn’t mind.",
                "char_c_scene5",
                delta((2, -1), (3, +1))
            ),
        ],
    },
    "char_d_scene4": {
        "banner": "banners/shared_3.png",
        "prompt": (
            "The lunch time comes, and students pour into hallways and open spaces, chatting, laughing, forming quick clusters. "
            "But for Fatima, lunch isn’t just a break - it’s a balancing act. She needs somewhere quiet to pray - a space where she can focus and not feel watched. "
            "Her food, packed from home, sits in her bag, carefully prepared since halal options are hard to come by. She scans her options for this lunch break."
        ),
        "options": [
            (
                "The Cafeteria room is buzzing. She could sit here with others and eat her own food, maybe even chat a bit. "
                "But the noise, the crowd, and the uncertainty about prayer time make her tense.",
                "char_d_scene5",
                delta((2, +1), (1, -1), (0, -1))
            ),
            (
                "The Café is peaceful, warm, and softly lit - but she can’t eat her own food here, and there's no real space to pray. "
                "She feels like a guest rather than herself.",
                "char_d_scene5",
                delta((1, +1), (3, -1))
            ),
            (
                "She knows of a quiet, empty room with just enough space to lay down her prayer mat. After praying, she could sit by the window and eat her packed lunch in peace. "
                "It’s not social, but it feels right.",
                "char_d_scene5",
                delta((1, +1), (3, +1), (2, -1))
            ),
        ],
    },


    "char_a_scene5": {
        "banner": "banners/shared_5.png",
        "prompt": (
            "In the next lecture the professor starts reading names aloud. "
            "Group-assignment time. Sock feels their jaw tighten; group work is always a gamble. "
            "They scan the room, quietly assessing the faces around them."
        ),
        "options": [
            (
                "It’s better than expected! Someone cool-looking gives their pronouns first, "
                "and Sock follows. They mostly observe and only speak when grounded, but they discover "
                "one person they wouldn’t mind working with again.",
                "char_a_scene6",
                delta((3, +1), (1, +1), (2, +1))
            ),
            (
                "It starts fine… until a smirk, a misgendering, then a cheap joke at the teacher’s expense. "
                "Sock stiffens, then delivers a quiet razor-sharp comment that ends the laughter. "
                "No new friends here— and that’s probably for the best.",
                "char_a_scene6",
                delta((1, -1), (0, -1))
            ),
            (
                "The group isn’t rude, just closed. Sock masks, offers ideas nobody follows up on, "
                "and drifts through the meeting on autopilot. It’s surface-level, but still draining.",
                "char_a_scene6",
                delta((1, 0), (3, 0), (0, -1))
            ),
        ],
    },

    "char_b_scene5": {
        "banner": "banners/shared_5.png",
        "prompt": (
            "Names are called and Carol swivels to see her partners. Group work is a total gamble—"
            "a blast or a black-hole of awkward vibes. She smirks, ready to roll."
        ),
        "options": [
            (
                "Instant spark: everyone’s chill but focused. They swap ideas, share memes, and someone "
                "recognises her slam-poem from last week. She leaves on a high.",
                "char_b_scene6",
                delta((3, +1), (2, +1))
            ),
            (
                "From the first minute she knows she’s on the outside. They talk over her and a guy makes a weird "
                "tattoo comment. She powers through with a sarcastic smile, counting the minutes.",
                "char_b_scene6",
                delta((3, -1), (2, -1))
            ),
            (
                "Nobody’s mean, nobody leads. Carol realises she’ll have to steer or nothing gets done. "
                "She half-enjoys the leadership role, half resents how much energy it drains.",
                "char_b_scene6",
                delta((0, -1), (3, +1), (1, 0))
            ),
        ],
    },

    "char_c_scene5": {
        "banner": "banners/shared_5.png",
        "prompt": (
            "The professor announces project groups. Bram straightens, already weighing how seriously "
            "his teammates will take the task."
        ),
        "options": [
            (
                "It clicks immediately: everybody contributes and respects each other. One student even references "
                "the recent student-council debate; Bram can’t help smiling.",
                "char_c_scene6",
                delta((1, +1), (2, +1), (3, +1))
            ),
            (
                "Red flags appear fast—eye-rolls at his structured plan, jokes about ‘taking things too seriously’. "
                "He keeps cool but counts the minutes until freedom.",
                "char_c_scene6",
                delta((0, -1), (1, -1))
            ),
            (
                "Polite but unfocused. When they project the slides without zooming, Bram squints, then calmly takes "
                "charge, assigning roles. Necessary, but tiring.",
                "char_c_scene6",
                delta((3, +1), (0, -1))
            ),
        ],
    },

    "char_d_scene5": {
        "banner": "banners/shared_5.png",
        "prompt": (
            "Students shuffle as names are read. Fatima adjusts her sleeves and joins her assigned group, "
            "unsure what the next hour will reveal."
        ),
        "options": [
            (
                "Relief floods in: the group is warm and collaborative. They share tasks fairly and value her voice—"
                "she feels truly seen.",
                "char_d_scene6",
                delta((1, +1), (2, +1), (3, +1))
            ),
            (
                "Disappointment hits: subtle digs about her accent, ideas ignored, polite smiles masking impatience. "
                "She leaves drained and quiet.",
                "char_d_scene6",
                delta((1, -1), (0, -1))
            ),
            (
                "The table is courteous but distant. Work gets done, yet no real connection forms. "
                "Neither hostile nor welcoming—just… work.",
                "char_d_scene6",
                delta((2, +1), (0, -1))
            ),
        ],
    },


    # ─────────── SCENE 6: After-Class Socialising ───────────
    # banner shared_6.png
    # Nobody goes to “final_*” anymore. Instead each option → None (jump to pages/3_End.py)
    "char_a_scene6": {
        "banner": "banners/shared_6.png",
        "prompt": (
            "Class is over, but the day isn’t done. A classmate turns to Sock on the way out: "
            "“Hey, we’re heading out – you coming?”  Going out isn’t just going out – it’s choosing "
            "how much of yourself to show and how long you can keep it up."
        ),
        "options": [
            (
                "The place is loud, chaotic, and drenched in cheap neon. The crowd as always aggressively "
                "straight-coded, the conversations shallow, the music too much. Sock would probably make it "
                "through one drink, maybe get a compliment on their boots, and then quietly ghost.",
                None,
                delta((2, -1), (1, -1), (0, -1))
            ),
            (
                "Barefoot in the grass, warm food containers opened between them, and someone playing soft music "
                "on their phone. Sock can listen, ask a few gentle questions themself, and even laugh once or twice. "
                "Their chameleon would probably love this.",
                None,
                delta((1, +1), (2, +1))
            ),
            (
                "Queer art taped to the walls, angry poetry, someone selling vegan cupcakes under a disco ball. "
                "Best part: they can go home at any time, without anyone noticing or minding.",
                None,
                delta((2, +1), (3, +1), (0, -1))
            ),
        ],
    },

    "char_b_scene6": {
        "banner": "banners/shared_6.png",
        "prompt": (
            "Class wraps up, and Carol is still in a bit of a haze after the group project. A teammate grins: "
            "“Hey, we’re heading out – you coming?”  What kind of vibe does she want to close the day with?"
        ),
        "options": [
            (
                "Loud music, neon lights, drinks flowing. Sure, alcohol’s a risk (thanks, Asian flush), "
                "but she knows how to pace herself. She loves the pulse of a busy room, the people-watching, "
                "the boldness that hangs in the air.",
                None,
                delta((2, +1), (1, -1))
            ),
            (
                "Soft grass, a few snacks, watching the sky shift color. Chill, no pressure. Maybe too chill. "
                "As much as she enjoys nature, part of her worries she’ll get restless, her brain spiraling into "
                "half-thoughts and distractions. Still, it might be what she needs, even if it’s not what she wants.",
                None,
                delta((1, +1), (0, 0))
            ),
            (
                "Spoken word, fusion food, zines on folding tables. Her kind of scene. If she invites the group, "
                "it could be a shared spark, a night that actually means something. She could even bring her "
                "notebook – just in case.",
                None,
                delta((3, +1), (2, +1), (1, +1))
            ),
        ],
    },

    "char_c_scene6": {
        "banner": "banners/shared_6.png",
        "prompt": (
            "Bram gathers his things when a teammate calls: “We’re heading out – you coming?”  "
            "The part that wants structure hesitates; the part that wants to grow listens."
        ),
        "options": [
            (
                "A drink or two and he might loosen up, feel less like he has to perform. "
                "He joins them, listens more than he talks, and eventually joins the conversation. "
                "It’s a stretch, but it works.",
                None,
                delta((2, +1), (1, -1), (3, +1))
            ),
            (
                "Everyone just sits around, snacks in hand, chatting loosely. Bram suggests a casual game, "
                "maybe football, or even a round of frisbee, but no one’s interested. He nods, sits, and checks "
                "his phone more than once.",
                None,
                delta((1, +1), (0, -1), (2, -1))
            ),
            (
                "Food stalls, music, small exhibitions. Bram almost says no, but then he hears someone mention "
                "a travel-themed photography series. That catches his interest. He goes, unsure at first, but ends up "
                "in a conversation about hiking trails across Europe. Unexpected, but worth it.",
                None,
                delta((2, +1), (3, +1))
            ),
        ],
    },

    "char_d_scene6": {
        "banner": "banners/shared_6.png",
        "prompt": (
            "Class ends, and as Fatima gathers her things someone from the group calls: "
            "“Hey, we’re heading out – you coming?”  Connection beckons, but where will she feel most herself?"
        ),
        "options": [
            (
                "It’ll be loud and crowded, and drinks will dominate the evening. She knows it will lift the others’ "
                "spirits, but deep down, she’ll feel out of place. That quiet alienation might return, even if no one "
                "means harm.",
                None,
                delta((1, -1), (2, +1), (0, +1))
            ),
            (
                "A calm hangout under the trees, where everyone can just be. It won’t be flashy, "
                "but it might bring comfort and connection without pressure.",
                None,
                delta((1, +1), (2, +1))
            ),
            (
                "Taking a chance, she’ll share something meaningful: food, music, and stories from many backgrounds. "
                "If they come, it could be more than just fun. It could feel like home.",
                None,
                delta((3, +1), (2, +1))
            ),
        ],
    },

    # ─────────── (We no longer need any "final_*" entries) ───────────
}
