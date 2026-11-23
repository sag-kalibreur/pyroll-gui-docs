# PyRoll WebGUI Documentation – Notes for Claude

This repository is **public** (GitHub Pages). It holds the online help of the PyRoll WebGUI.
The full working rules and the roadmap live in the application repository next to this one: `../pyroll-gui-costum/CLAUDE.md` and `../pyroll-gui-costum/ROADMAP.md`. Read them before working here. Do not put internal information (roadmap, open questions, branches) into this repository.

## Rules for this repository
- Commit and push only when the user explicitly asks. Never `git checkout -- .`, never `git reset --hard`, never `git push --force`. No `Co-Authored-By` lines.
- The content is identical to `../pyroll-gui-costum/public/help`. The only difference is the frame: every page here keeps the **PyRoll favicon** and the **backlinks to the main menu** (`index.html`).
- **Never overwrite pages 1:1** from the application repository (including the `Copy-Item -Force` from the README). Transfer only the changed content sections and keep favicon and backlinks. Check with a diff afterwards that only the head/nav block differs.
- Groove image paths: `../grooves/` in the app becomes `grooves/` here.
- Update the **creation date** in every changed page, in **header and footer** (e.g. `Date: November 2026` at the top, `… | November 2026` in the footer; position and format differ per page). Check with `grep -n -i -E "october|november" <file>` that no page shows two different months.
- `PyRoll_WebGUI_Complete_Reference.html` is self-contained (everything embedded for offline use). Regenerate it in the application repository with `scripts/build_combined_guide.py` and copy it here.
