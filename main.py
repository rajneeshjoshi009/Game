# main.py - AI-PURGE Main Game Loop

import time
from stats import update_stats, get_stats
from scenarios import get_scenario
from ai_logic import immediate_response, cpr_based_response, final_AI_judgment
from ui_effects import glitch_text, redacted_text, fake_time_lapse, type_effect

def play_scenario(index):
    """
    Runs a single scenario, allowing the player to make a choice.
    """
    scenario = get_scenario(index)
    if not scenario:
        return

    glitch_text(f"\nSCENARIO {index+1}: {scenario['title']}")
    type_effect(redacted_text(scenario['description']))

    print("\nChoices:")
    for key, choice in scenario["choices"].items():
        print(f"{key}: {choice['text']}")

    choice = input("\nEnter 1 or 2: ").strip()
    while choice not in ["1", "2"]:
        choice = input("Invalid choice. Enter 1 or 2: ").strip()

    # Apply the choice's effect on stats
    choice_data = scenario["choices"][choice]
    update_stats(choice_data["RP_change"], choice_data["CB_change"], choice_data["CPR_change"])

    # AI Response
    print("\nAI RESPONSE:")
    fake_time_lapse()
    type_effect(immediate_response(choice_data["RP_change"], choice_data["CB_change"]))

def main():
    """
    Runs the entire game loop for all scenarios.
    """
    glitch_text("CONNECTION ESTABLISHED... SUBJECT ANALYSIS INITIATED.")

    for i in range(7):  # Loop through all 7 scenarios
        play_scenario(i)

    # Final AI Judgment
    print("\nFINAL AI JUDGMENT:")
    fake_time_lapse()
    type_effect(cpr_based_response())
    time.sleep(1)
    type_effect(final_AI_judgment())

if __name__ == "__main__":
    main()
