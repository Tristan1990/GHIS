# data/characters.py

CHARACTERS = {
    "char_a": {
        "name":    "Sock",
        "stem":    "base_a",
        "pronouns":"they/them",
        "desc":   """
Bold, guarded, and deeply self-aware, Sock is a transgender Dutch biology student with a striking alternative style and a stormy inner world. Tattoos, piercings, and dyed hair speak their truth out loud – whether the world is ready or not. They’re the kind of person who can hold a protest sign in one hand and their pet chameleon (his name is Moss) in the other. Underneath their cool exterior lies a constant hum of anxiety, and sometimes, when it all becomes too much, words just won’t come.
*Choose Sock if you’re drawn to authentic characters who speak up for others, even when they’re still learning to care for themselves.*""",
        "intro":   "intro_sock",
        "finale":  "final_sock",
        "traits": [
            "Energy ⚡️",
            "Comfort 🌿",
            "Social 💬",
            "Fulfillment 🌈",
        ],
        # Optional: you can override these default scores by specifying here
        # If omitted, defaults will apply
    },
    "char_b": {
        "name":    "Carol",
        "stem":    "base_b",
        "pronouns":"she/they",
        "desc":   """
Bold, funny, and full of fire, Carol is a queer English studies student born and raised in the Netherlands, shaped by both her Asian heritage and her Dutch surroundings. She’s all tattoos, piercings, and poetry – cool on the outside, but still learning to love herself on the inside. ADHD makes daily life a bit of a chaos spiral, but Carol meets it head-on with therapy, a leather jacket, and a pack of street cats by her side.
*Choose Carol if you’re into late-night concerts, impulsive choices, and the kind of heart that spills raw truth into a mic at a slam poetry event.*""",
        "intro":   "intro_carol",
        "finale":  "final_carol",
        "traits": [
            "Energy ⚡️",
            "Comfort 🌿",
            "Social 💬",
            "Fulfillment 🌈",
        ],
    },
    "char_c": {
        "name":    "Bram",
        "stem":    "base_c",
        "pronouns":"he/him",
        "desc":   """
Ambitious, composed, and deeply committed, Bram is a low-vision hockey player and governance student navigating the demands of both sport and academia. Between training sessions and political meetings, he keeps his standards sky-high – for himself and others. Bram wears glasses but needs contact lenses to compete, even though they often irritate his eyes. He’s not the most spontaneous person, but with time and trust, he opens up in meaningful ways.
*Choose Bram if you value determination, quiet confidence, and the challenge of balancing structure with vulnerability.*""",
        "intro":   "intro_bram",
        "finale":  "final_bram",
        "traits": [
            "Energy ⚡️",
            "Comfort 🌿",
            "Social 💬",
            "Fulfillment 🌈",
        ],
    },
    "char_d": {
        "name":    "Fatima",
        "stem":    "base_d",
        "pronouns":"she/her",
        "desc":   """
Kind, curious, and full of quiet strength, Fatima is originally from Morocco, studies engineering in France, and is currently on exchange in the Netherlands. She’s navigating a new environment while staying true to her Muslim faith. Fatima prays five times a day, finds comfort in her mosque community, and is family-oriented. Thoughtful and compassionate, she sometimes struggles to stand her ground, but she’s learning how to find her place without letting go of who she is.
*Choose Fatima if you’re up for heartfelt moments and meaningful choices.*""",
        "intro":   "intro_fatima",
        "finale":  "final_fatima",
        "traits": [
            "Energy ⚡️",
            "Comfort 🌿",
            "Social 💬",
            "Fulfillment 🌈",
        ],
        # Fatima's custom starting values:
        "scores": {
            "Energy ⚡️": 10,
            "Comfort 🌿": 10,
            "Social 💬": 10,
            "Fulfillment 🌈": 10,
        },
    },
}

# Assign default scores of 10 for any character without custom starting values
for meta in CHARACTERS.values():
    meta.setdefault(
        "scores", {trait: 10 for trait in meta["traits"]}
    )
