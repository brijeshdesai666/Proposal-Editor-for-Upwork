# Proposal-Editor-for-Upwork

A small Python/HTML utility collection originally intended for Upwork proposal workflows.

## Contents

    Proposal-Editor-for-Upwork/
    └── VS/
        ├── AU.py                  (automated browsing simulator — see note below)
        └── text-editor-app.html    (simple text editor, likely for drafting proposals)

## AU.py

This script uses pyautogui and keyboard to simulate human-like browsing behavior on a webpage (mouse movement with randomized timing, scrolling, clicking, then navigating back), running in repeated cycles. It can be stopped at any time via the Esc key.

## Important Note

This script is designed to mimic organic human browsing patterns rather than simply automate a repetitive task. If used against a real platform account (e.g. Upwork), this kind of behavior is the type of thing bot-detection systems are built to catch, and could risk account suspension. Use with caution and only on accounts/situations where this is acceptable.

## text-editor-app.html

A basic HTML text editor, likely intended as a simple interface for drafting and editing proposal text.

## Tech Stack

- Python (pyautogui, keyboard)
- HTML/JavaScript
