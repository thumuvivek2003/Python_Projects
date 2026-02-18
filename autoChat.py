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
    # prompt_prefixes  = {
    #     "concept": (
    #         "I am mastering DSA for coding interviews. "
    #         "Explain this topic in a clear, structured way using "
    #         "(skip any part if not applicable): "
    #         "Intuition (real-world analogy), "
    #         "Core definition, "
    #         "What is it?, "
    #         "Why this?, "
    #         "Clear explanation, "
    #         "Where it breaks (limitations), "
    #         "Common mistakes, "
    #         "Interview insight, "
    #         "One-line learning outcome and trigger on "
    #     ),
    
    #     "problem": (
    #         "I am preparing for DSA coding interviews. "
    #         "Explain the following LeetCode problem using: "
    #         "Intuition, "
    #         "Core idea, "
    #         "Step-by-step logic, "
    #         "Dry run, "
    #         "Edge cases, "
    #         "Alternative approaches (why rejected), "
    #         "Common mistakes, "
    #         "Time & space complexity, "
    #         "Interview takeaway. "
    #         "Problem: "
    #     ),
    
    #     "hybrid": (
    #         "I am mastering advanced DSA patterns for interviews. "
    #         "Explain this hybrid concept clearly using: "
    #         "Intuition, "
    #         "Binary Search perspective, "
    #         "Greedy feasibility logic, "
    #         "Why binary search on answer works, "
    #         "Common mistakes, "
    #         "Interview insight, "
    #         "One-line trigger. "
    #         "Topic: "
    #     ),
    #     "strategy_concept": """I am learning Business Strategy to think like a strategist. 
    #         Explain this concept in a clear, structured way using:
    #         Intuition (real-world analogy),
    #         Core definition,
    #         What is it?,
    #         Why this matters in business?,
    #         Clear explanation with examples,
    #         Common misunderstandings,
    #         Strategic insight,
    #         One-line takeaway and trigger.
    #         Concept: """

    # }

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




# ==============================
# MAIN ENTRY POINT
# ==============================


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
    prompt_prefixes  = {
        "concept": (
            "I am mastering DSA for coding interviews. "
            "Explain this topic in a clear, structured way using "
            "(skip any part if not applicable): "
            "Intuition (real-world analogy), "
            "Core definition, "
            "What is it?, "
            "Why this?, "
            "Clear explanation, "
            "Where it breaks (limitations), "
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
            "Alternative approaches (why rejected), "
            "Common mistakes, "
            "Time & space complexity, "
            "Interview takeaway. "
            "Problem: "
        ),
        "amazon_concepts":'''Hey  I am preparing for Amazon SDE OA explain clear  explaination , tips & tricks , main things to learn before interview currently learning  ''',
        "amazon_lc":'''Hey I am preparing for Amazon OA, explain clearly intuition, template, edge cases, complexities, trigger clearly. I am currently at''',
        "amazon_ws":'''Hey I am preparing for Amazon OA Workstyles Assessment, explain clearly why , what , how ,clear explain ,  sample questions perfect answers . I am currently at''',
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
        ),
        "strategy_concept": """I am learning Business Strategy to think like a strategist. 
            Explain this concept in a clear, structured way using:
            Intuition (real-world analogy),
            Core definition,
            What is it?,
            Why this matters in business?,
            Clear explanation with examples,
            Common misunderstandings,
            Strategic insight,
            One-line takeaway and trigger.
            Concept: """

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
        if index != len(prompts) and index != 1:
            wait_with_dots(config.response_wait_time)


    print("✅ All prompts sent successfully")


# ==============================
# MAIN ENTRY POINT
# ==============================

def main():
    PROMPTS = """
    Hi
|   27 | Lazy Deletion              | Delayed removals                | Handle updates            |
|   28 | Indexed Heap               | Decrease-key support            | Advanced updates          |
|   29 | Min-Max Heap               | Dual extremes                   | Advanced variant          |
|   30 | Heap on Custom Objects     | Struct/class storage            | Complex data              |
|   31 | Heap vs Sorting            | log n vs n log n                | Choose wisely             |
|   32 | Heap vs Deque              | Window problems                 | Pick right tool           |
|   33 | Debugging Heaps            | Trace heapify                   | Fix subtle bugs           |
|   34 | Pattern Recognition        | Spot heap use                   | Solve unseen problems     |
|   35 | Heap Templates             | Reusable code                   | Implement faster          |
|   36 | Competitive Constraints    | When heaps TLE                  | Smart choices             |
|   37 | Advanced Heap Variants     | Fibonacci/Binomial              | Theory overview           |
|   38 | Memory & Cache Behavior    | Practical performance           | Optimization insight      |
|   39 | Common Heap Mistakes       | Comparator/index bugs           | Avoid WA                  |
|   40 | Heap / PQ Master Checklist | Best practices                  | Write elite heap code     |
"""



    PROMPTS = """
    Hi
|   23 | Coin Change                   | Counting & min coins                | Learn order sensitivity        |
|   24 | Target Sum DP                 | + / – assignments                   | Transform into subset DP       |
|   25 | DP on Grid                    | 2D movement                         | Paths, obstacles               |
|   26 | DP on Matrix                  | Multi-directional DP                | Gold mine, maximal square      |
|   27 | DP on Trees                   | Post-order DP                       | Solve subtree problems         |
|   28 | Tree Rerooting DP             | Change root efficiently             | Advanced tree DP               |
|   29 | DP on Graphs                  | DAG-based DP                        | Longest path, topo DP          |
|   30 | Interval DP                   | Break range into parts              | Matrix chain multiplication    |
|   31 | DP on Subsequences (Advanced) | Multi-state DP                      | Palindrome subsequences        |
|   32 | Bitmask DP                    | State compression                   | Handle small n efficiently     |
|   33 | Digit DP                      | DP on digits                        | Count numbers with constraints |
|   34 | DP with Probability           | Expected value DP                   | Randomized processes           |
|   35 | DP Optimization Techniques    | Knuth, Divide & Conquer             | Speed up heavy DP              |
|   36 | DP with Monotonic Stack       | Optimize transitions                | Advanced range DP              |
|   37 | DP with Binary Search         | Optimize LIS-like DP                | Combine paradigms              |
|   38 | DP with Greedy                | Hybrid problems                     | Choose correct approach        |
|   39 | DP Debugging Techniques       | Visual tables                       | Fix wrong transitions          |
|   40 | DP Pattern Recognition        | Identify DP category                | Solve unseen problems          |
|   41 | Converting DP ↔ Recursion     | Bidirectional thinking              | Master top-down & bottom-up    |
|   42 | Memory & Constraints Handling | Stack vs heap                       | Avoid MLE/TLE                  |
|   43 | Competitive DP Strategy       | When DP is overkill                 | Choose wisely                  |
|   44 | DP Master Checklist           | Best practices                      | Write clean DP code            |
"""


    PROMPTS = """
    Hi
| 4    | Profit vs Growth          | Difference between scaling and profitability | Avoid wrong growth decisions     |
| 5    | Unit Economics            | Revenue – cost per customer                  | Judge business sustainability    |
| 6    | Value Proposition         | Why customers pay                            | Connect product to pain          |
| 7    | Customer Segments         | Buyer vs user                                | Understand decision-makers       |
| 8    | Enterprise Sales Basics   | Long sales cycles, stakeholders              | Understand B2B dynamics          |
"""













    config = AutomationConfig(
        initial_switch_delay=5,
        response_wait_time=45
    )

    prompts = load_prompts(PROMPTS)
    run_automation(prompts, config,'amazon_concepts')
    # run_automation(prompts, config,'amazon_lc')


if __name__ == "__main__":
    main()
