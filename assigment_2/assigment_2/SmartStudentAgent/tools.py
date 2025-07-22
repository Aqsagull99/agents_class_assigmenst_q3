# tools.py
def get_study_tips(subject: str) -> str:
    tips = {
        "math": "Practice problems daily. Focus on understanding formulas.",
        "science": "Understand concepts, use diagrams and revise frequently.",
        "english": "Read regularly, improve vocabulary, and practice writing.",
    }
    return tips.get(subject.lower(), "No tips available for this subject.")
