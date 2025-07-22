# 🎓 Smart Student Agent (Gemini-Compatible)

This project is a subject-based AI assistant designed to guide students with study tips and support across different academic areas.
It was built using the OpenAI Agent SDK and configured to run with Gemini’s free API (with limited support for tools and handoffs).

---

## 💡 Project Goal

The agent simulates a helpful assistant that can:
- Provide subject-specific study tips
- Guide students through simple, personalized queries
- Run directly via terminal (CLI)

---

## ⚙️ How It Works

Due to **Gemini Free API limitations**, the project:
- **Does not use `@function_tool` decorators**
- **Avoids automatic `handoffs`**
- Instead, each agent is manually triggered using `Runner.run_sync(...)`.

---

## 🧠 Agents Used

| Agent         | Description                                 |
|---------------|---------------------------------------------|
| `MathAgent`     | Shares math study advice                   |
| `ScienceAgent`  | Offers science concept tips                |
| `GeneralAgent`  | Gives general study strategies             |
| `MainAgent`     | Coordinator (handoff logic not active)     |

---

## 🔧 tools.py

Custom logic is defined manually instead of using function tools:

```python
def get_study_tips(subject: str) -> str:
    tips = {
        "math": "Practice problems daily. Focus on understanding formulas.",
        "science": "Understand concepts, use diagrams and revise frequently.",
        "english": "Read regularly, improve vocabulary, and practice writing.",
    }
    return tips.get(subject.lower(), "No tips available for this subject.")
