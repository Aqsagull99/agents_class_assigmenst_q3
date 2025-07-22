# tool.py
def get_career_roadmap(career_name: str) -> str:
    roadmap = {
        "Web Developer": "HTML, CSS, JavaScript, React, APIs, Node.js",
        "Data Scientist": "Python, Pandas, NumPy, ML, SQL, Data Visualization",
        "AI Engineer": "Python, ML, Deep Learning, Transformers, MLOps"
    }
    return roadmap.get(career_name, "No roadmap found for this career.")
