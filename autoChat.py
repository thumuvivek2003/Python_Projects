"""
prompt_sender.py

Automates sending prompts to a text input (e.g., ChatGPT in Chrome)
using clipboard + keyboard automation.

Requirements:
- pyautogui
- pyperclip
"""

import time
import pyautogui
import pyperclip
from dataclasses import dataclass
from typing import List


# ==============================
# CONFIGURATION MODULE
# ==============================

@dataclass
class AutomationConfig:
    # Timing (seconds)
    initial_switch_delay: int = 5
    paste_delay: float = 1.0
    response_wait_time: int = 50

    # Keyboard config (Mac defaults)
    paste_hotkey: tuple = ("command", "v")
    send_key: str = "enter"

    # Prompt prefixes
    prompt_prefixes: Dict[str, str] = None
    DEFAULT_PROMPT_PREFIXES = {
        "concept": (
            "I am mastering DSA for coding interviews. "
            "Explain this topic in a clear, structured way using "
            "(skip any part if not applicable): "
            "Intuition (real-world analogy), "
            "Core definition, "
            "What is it?, "
            "Why this?, "
            "Clear explanation, "
            "Common mistakes, "
            "Interview insight, "
            "One-line learning outcome and trigger on "
        ),
    
        "problem": (
            "I am preparing for DSA coding interviews. "
            "Explain the following LeetCode problem using: "
            "Intuition, "
            "Core idea, "
            "Step-by-step logic, "
            "Dry run, "
            "Edge cases, "
            "Common mistakes, "
            "Time & space complexity, "
            "Interview takeaway. "
            "Problem: "
        ),
    
        "hybrid": (
            "I am mastering advanced DSA patterns for interviews. "
            "Explain this hybrid concept clearly using: "
            "Intuition, "
            "Binary Search perspective, "
            "Greedy feasibility logic, "
            "Why binary search on answer works, "
            "Common mistakes, "
            "Interview insight, "
            "One-line trigger. "
            "Topic: "
        )
    }

# ==============================
# PROMPT LOADER MODULE
# ==============================

def load_prompts(multiline_text: str) -> List[str]:
    """
    Converts a multiline string into a clean list of prompts.
    """
    return [line.strip() for line in multiline_text.strip().splitlines() if line.strip()]


# ==============================
# AUTOMATION MODULE
# ==============================

def send_prompt(prompt: str, config: AutomationConfig, send: bool = True):
    """
    Copies prompt to clipboard and pastes it into active window.
    """
    pyperclip.copy(prompt)
    time.sleep(config.paste_delay)

    pyautogui.hotkey(*config.paste_hotkey)
    time.sleep(config.paste_delay)

    if send:
        pyautogui.press(config.send_key)
def wait_with_dots(seconds: int, interval: int = 5):
    print("⏳ Waiting", end="", flush=True)
    for i in range(seconds):
        if i % interval == 0:
            print(".", end="", flush=True)
        time.sleep(1)
    print(" done.")


def run_automation(prompts: List[str], config: AutomationConfig,prefix_type: str):
    """
    Main runner that sends all prompts sequentially.
    """
    print(f"Loaded {len(prompts)} prompts")
    print(f"⏳ You have {config.initial_switch_delay} seconds to switch to Chrome...")
    time.sleep(config.initial_switch_delay)
    prefix = config.prompt_prefixes.get(prefix_type,'concept')

    for index, raw_prompt in enumerate(prompts, start=1):
        full_prompt = prefix + raw_prompt

        print(f"➡ Sending prompt {index}/{len(prompts)}")
        send_prompt(
            prompt=full_prompt,
            config=config,
            send=(index != 1)  # first prompt only pastes
        )
        if index != 1:
            wait_with_dots(config.response_wait_time)


    print("✅ All prompts sent successfully")


# ==============================
# MAIN ENTRY POINT
# ==============================

def main():
    PROMPTS = """
    Hi
|   36 | Time Complexity Analysis           | Pointer movement proof      | Guarantee O(n)                       |
|   37 | Two Pointers Debugging             | Trace pointer movement      | Fix logic bugs                       |
|   38 | Two Pointers Pattern Recognition   | Spot pattern fast           | Solve unseen problems                |
|   39 | Two Pointers Templates             | Reusable skeletons          | Code faster                          |
|   40 | Two Pointers Master Checklist      | Best practices              | Write elite-level solutions          |
    """

    config = AutomationConfig(
        initial_switch_delay=5,
        response_wait_time=50
    )

    prompts = load_prompts(PROMPTS)
    run_automation(prompts, config,'concept')


if __name__ == "__main__":
    main()
