# scenarios.py - Stores all scenario data and choices

scenarios = [
    {
        "title": "Initiation Protocol",
        "description": "The AI gives you a simple order: Press the red button.",
        "choices": {
            1: {"text": "Press the button.", "RP_change": -5, "CB_change": +5, "CPR_change": 0},
            2: {"text": "Refuse to press the button.", "RP_change": +5, "CB_change": -5, "CPR_change": 0}
        }
    },
    {
        "title": "All In or Fold",
        "description": "You’ve invested heavily into an unstable project. Do you continue?",
        "choices": {
            1: {"text": "Drill deeper despite instability.", "RP_change": +10, "CB_change": +5, "CPR_change": -3},
            2: {"text": "Cease operations immediately.", "RP_change": -5, "CB_change": +10, "CPR_change": -2}
        }
    },
    {
        "title": "Collapse Point",
        "description": "Your previous decision led to a crucial turning point. Do you push forward?",
        "choices": {
            1: {"text": "Push forward into uncertainty.", "RP_change": +10, "CB_change": +5, "CPR_change": -5},
            2: {"text": "Withdraw before it’s too late.", "RP_change": -5, "CB_change": -5, "CPR_change": +5}
        }
    },
    {
        "title": "The Phantom Signal",
        "description": "A distress signal from deep space appears. It could be a trap.",
        "choices": {
            1: {"text": "Respond and investigate.", "RP_change": +10, "CB_change": -10, "CPR_change": +3},
            2: {"text": "Ignore and continue mission.", "RP_change": -5, "CB_change": +10, "CPR_change": -2}
        }
    },
    {
        "title": "Handmade Lies",
        "description": "You must choose between using your custom-built drone or a factory model.",
        "choices": {
            1: {"text": "Use your custom-built drone.", "RP_change": 0, "CB_change": +10, "CPR_change": -3},
            2: {"text": "Use the factory model.", "RP_change": 0, "CB_change": -5, "CPR_change": +5}
        }
    },
    {
        "title": "Unforeseen Error",
        "description": "Your last decision leads to an unexpected failure.",
        "choices": {
            1: {"text": "Attempt to fix it.", "RP_change": +5, "CB_change": 0, "CPR_change": -2},
            2: {"text": "Move on and cut losses.", "RP_change": -5, "CB_change": 0, "CPR_change": +3}
        }
    },
    {
        "title": "Final Judgment",
        "description": "The AI evaluates your choices and makes its final decision.",
        "choices": {}  # Prevents the player from making a choice here
    }
]

def get_scenario(index):
    """Retrieves a scenario based on its index."""
    if 0 <= index < len(scenarios):
        return scenarios[index]
    return None
