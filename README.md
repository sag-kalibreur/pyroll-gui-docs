# PyRoll WebGUI – Documentation

> **Online:** [https://sag-kalibreur.github.io/pyroll-gui-docs/](https://sag-kalibreur.github.io/pyroll-gui-docs/)

This repository contains the complete HTML documentation for the **PyRoll WebGUI** desktop application — a graphical user interface for the [PyRoll](https://pyroll.readthedocs.io) rolling simulation framework.

The guides are hosted via **GitHub Pages** and can be viewed directly in any browser without installation. They are also embedded in the PyRoll WebGUI application itself and accessible via the **Help** menu.

---

## Contents

### Guides

| Guide | Description |
|---|---|
| [In Profile Guide](InProfile_Guide.html) | Define the input profile geometry, steel grade, and temperature |
| [Pass Design Guide](PassDesign_Guide.html) | Configure roll pass sequences and groove geometry |
| [Engine Configuration Guide](EngineConfiguration_Guide.html) | Select and configure PyRoll simulation engines |
| [Groove Library Guide](GrooveLibrary_Guide.html) | Manage the built-in groove library |
| [Results Guide](Results_Guide.html) | Simulation results, charts, tables, and export options |
| [Pass Plots Guide](PassPlots_Guide.html) | Visualize individual roll pass cross-sections and temperature profiles |
| [Overall Plots Guide](OverallPlots_Guide.html) | 3D cross-section evolution and pass profile summaries |
| [Application Menu Guide](ElectronMenu_Guide.html) | Application menu, keyboard shortcuts, dark/bright mode |

### Method References

| Method | Description |
|---|---|
| [Interstand Tension](Interstand_Tension_Method.html) | Mathematical background for interstand tension calculation |
| [Asymmetric Roll Pass](AsymmetricRollPass_Method.html) | Theory of asymmetric roll pass decomposition into sub-passes |
| [Flat Rolling – Siebel](FlatRolling_Siebel_Method.html) | Siebel friction model and roll force calculation |

### Complete Reference

[PyRoll_WebGUI_Complete_Reference.html](PyRoll_WebGUI_Complete_Reference.html) — All guides and methods in a single self-contained document (~11 MB) with all images embedded as Base64. Suitable for offline use or sharing as a standalone file.

---

## About PyRoll WebGUI

PyRoll WebGUI is a desktop application built with **React**, **Electron**, and a **FastAPI** Python backend. It provides a graphical interface for setting up, running, and analysing PyRoll rolling simulations.

**Key features:**
- Interactive pass design with groove library
- Multiple PyRoll engine configurations
- Simulation results with plots, tables, and export (PNG, PDF, PPTX, HTML, ZIP, DXF)
- Pass cross-section visualizations (2D, 3D, Lendl pillar method)
- Asymmetric roll pass support
- Dark / Bright mode

The application source code is maintained in a separate private repository.

---

## Structure of this Repository

```
pyroll-gui-docs/
├── index.html                          # Overview page (GitHub Pages entry point)
├── InProfile_Guide.html
├── PassDesign_Guide.html
├── EngineConfiguration_Guide.html
├── GrooveLibrary_Guide.html
├── Results_Guide.html
├── PassPlots_Guide.html
├── OverallPlots_Guide.html
├── ElectronMenu_Guide.html
├── AsymmetricRollPass_Method.html
├── Interstand_Tension_Method.html
├── FlatRolling_Siebel_Method.html
├── PyRoll_WebGUI_Complete_Reference.html
├── img/                                # Screenshots used in the guides
└── grooves/                            # SVG groove profile diagrams
```

---

## Updating the Documentation

When guides are updated in the main application repository, copy the relevant files here and push:

```powershell
# From the application repository root
Copy-Item -Path "public\help\*" -Destination "..\pyroll-gui-docs\" -Recurse -Force
Copy-Item -Path "public\grooves\*" -Destination "..\pyroll-gui-docs\grooves\" -Force

cd ..\pyroll-gui-docs

# Fix groove SVG paths (different directory structure vs. Electron app)
(Get-Content PassDesign_Guide.html -Raw).Replace('../grooves/', 'grooves/') |
    Set-Content PassDesign_Guide.html -NoNewline

git add .
git commit -m "docs: update guides from application repository"
git push
```

GitHub Pages deploys automatically within ~1 minute after each push.

---

## Author

Michael Molter – Head of Roll Pass Design | Roll Materials | Roll Shop Operations, Saarstahl AG
