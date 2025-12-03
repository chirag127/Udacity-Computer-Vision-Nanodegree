# CVND-Udacity-Computer-Vision-Nanodegree-Archive

[![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/CVND-Udacity-Computer-Vision-Nanodegree-Archive/ci.yml?label=Build&style=flat-square)](https://github.com/chirag127/CVND-Udacity-Computer-Vision-Nanodegree-Archive/actions/workflows/ci.yml)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/CVND-Udacity-Computer-Vision-Nanodegree-Archive?style=flat-square)](https://codecov.io/gh/chirag127/CVND-Udacity-Computer-Vision-Nanodegree-Archive)
[![Language](https://img.shields.io/github/languages/top/chirag127/CVND-Udacity-Computer-Vision-Nanodegree-Archive?style=flat-square)](https://github.com/chirag127/CVND-Udacity-Computer-Vision-Nanodegree-Archive)
[![License](https://img.shields.io/github/license/chirag127/CVND-Udacity-Computer-Vision-Nanodegree-Archive?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/CVND-Udacity-Computer-Vision-Nanodegree-Archive?style=social)](https://github.com/chirag127/CVND-Computer-Vision-Nanodegree-Archive/stargazers)

***

## Vision Statement

This repository serves as a definitive, professionally structured archive of the Udacity Computer Vision Nanodegree (CVND) curriculum and completed projects. It is preserved as a high-fidelity technical reference for educational replication and historical study of deep learning and computer vision milestones up to the 2024/2025 standard.

## 🏛️ Project Artifact Context

This repository, while archival, is maintained under the **Apex Technical Authority** mandate. All internal documentation (READMEs, CI/CD definitions) has been elevated to reflect modern best practices, even though the core content (Jupyter Notebooks) reflects the curriculum timelines.

## 🏗️ Architectural Overview

The primary artifact structure for this archival repository follows a simple, navigable format optimized for conceptual retrieval.

mermaid
graph TD
    A[Root Repository] --> B(Curriculum_Materials/);
    A --> C(Projects/);
    A --> D(Documentation/);
    C --> C1(Project_01_Object_Detection);
    C --> C2(Project_05_Segmentation);
    D --> D1(AGENTS.md);
    D --> D2(LICENSE);


## 📚 Table of Contents

1.  [Vision Statement](#vision-statement)
2.  [Project Artifact Context](#-project-artifact-context)
3.  [Architectural Overview](#-architectural-overview)
4.  [Table of Contents](#--table-of-contents)
5.  [Technology Stack & Maintenance Context](#-technology-stack--maintenance-context)
6.  [🤖 AI Agent Directives (Mandatory Alignment)](#-ai-agent-directives-mandatory-alignment)
7.  [Accessing Curricular Content](#accessing-curricular-content)
8.  [Archival & Re-Use License](#archival--re-use-license)

## ⚙️ Technology Stack & Maintenance Context

Although the core deliverables are primarily **Jupyter Notebooks** (`.ipynb`) utilizing **PyTorch** for deep learning tasks, the *maintenance framework* adheres to 2026 standards.

*   **Core Language Reference:** Python 3.10+ (Implicit in Notebook environments).
*   **Deep Learning Framework:** PyTorch.
*   **Documentation Standard:** GitHub Actions, Ruff Linter (applied to any configuration files), CC BY-NC License.
*   **Linting/Testing:** Not applicable to raw `.ipynb` files, but required for any adjacent configuration or tooling (e.g., CI definitions).

## 🤖 AI Agent Directives (Mandatory Alignment)

<details><summary><strong>📜 View Apex Agent Alignment Protocol (December 2025)</strong></summary>

### 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

### 2. INPUT PROCESSING & COGNITION
*   **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    *   **Context:** User inputs may contain phonetic errors (homophones, typos).
    *   **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. You must **INFER** technical intent based on the project context.
    *   **Logic Anchor:** Treat the `README.md` as the **Single Source of Truth (SSOT)**.
*   **MANDATORY MCP INSTRUMENTATION:**
    *   **No Guessing:** Do not hallucinate APIs. This project relies on established CV/DL libraries.
    *   **Research First:** Use `linkup`/`brave` to search for **PyTorch 2.x best practices** and **CV Model efficiency benchmarks (2025)**.
    *   **Validation:** Use `docfork` to verify *every* library import signature (e.g., ensuring `torchvision` paths are current).
    *   **Reasoning:** Engage `clear-thought-two` to architect complex data augmentation flows *before* modifying notebook cells.

### 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** Detect the project type and apply the corresponding **Apex Toolchain**.

*   **PRIMARY SCENARIO: DATA / SCRIPTS / AI (Jupyter/PyTorch)**
    *   **Stack:** This project necessitates adherence to **PyTorch 2.x** standards. While configuration files are minimal, agents must assume an environment capable of running modern CUDA operations (if hardware is available).
    *   **Architecture:** The structure is **Conceptual Modularization** enforced by notebook organization. Ensure dependencies within notebooks are self-contained or explicitly referenced from the original curriculum structure.
    *   **Data Flow:** Focus on verifying data loading paths (`/data` directory structure) and ensuring deterministic execution across different PyTorch versions where possible.

### 4. VERIFICATION COMMANDS (Conceptual)
Since this is an archive of educational material, verification focuses on successful execution rather than unit testing of the notebooks themselves.

*   **Environment Check:** `conda env create -f environment.yml` (or equivalent Pip/uv setup).
*   **Notebook Execution Audit (Conceptual):** Execute notebooks sequentially using `nbconvert` or equivalent tooling to confirm cell outputs align with expected CV results.
*   **Deep Learning Sanity Check:** Verify PyTorch and CUDA visibility: `python -c "import torch; print(torch.cuda.is_available())"` should return `True` in a capable environment.

</details>

## 🚀 Accessing Curricular Content

The primary educational assets are located within the `/Projects` directory, categorized by the Nanodegree module structure.

| Module Title | Primary Technology | Location |
| :--- | :--- | :--- |
| Introduction to CV/DL | NumPy, Matplotlib | `/Curriculum_Materials/Intro` |
| Object Detection | PyTorch, CNNs | `/Projects/Project_01_Object_Detection` |
| Image Segmentation | U-Net Architectures | `/Projects/Project_05_Segmentation` |
| Advanced Topics | GANs, Style Transfer | `/Curriculum_Materials/Advanced` |

## 📜 Archival & Re-Use License

This project is governed by the **Creative Commons Attribution-NonCommercial 4.0 International License**.

**ATTRIBUTION REQUIRED:** While derived from Udacity materials, this structure and maintenance effort are governed by the CC BY-NC license, acknowledging the original source while protecting future derivative educational work under these specific terms.

[View Full License](LICENSE)