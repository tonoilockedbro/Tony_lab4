# Tony_lab4  
# geometry-demo

**geometry-demo** is a lightweight Python package created as part of *Lab 4 — Fundamentals of Software Packaging & Testing* in the BU RISE Practicum (June 2025). The objective was to gain hands-on experience with creating Python packages, writing testable and reusable code, and practicing modern development tools including `pytest`, `setuptools`, and version control with Git.

---

## 🔧 Key Features

- Abstract base class `Shape` built with Python’s `abc` module  
- Two concrete shape implementations: `Square` and `Circle`, each featuring an `area()` method  
- Utility function `area_stats()` that calculates summary statistics over multiple shape areas  
- Public interface neatly organized and exposed through `__init__.py`  
- Full test coverage with `pytest` and installable in editable mode for development  

---

## 📦 Installation

To get started, clone the repo and install the package in editable mode:

```bash
git clone https://github.com/<your-username>/geometry-demo.git
cd geometry-demo
pip install -e .
