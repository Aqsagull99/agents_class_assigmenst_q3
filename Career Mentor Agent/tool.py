from agents import Agent , function_tool

 #  Define get_career_roadmap tool
@function_tool
def get_career_roadmap(career_name: str) -> str:
    print(f"[DEBUG] Tool called with career_name={career_name}")
    roadmap = {
        "Web Developer": "HTML, CSS, JavaScript, React, APIs, Node.js",
        "Data Scientist": "Python, Pandas, NumPy, ML, SQL, Data Visualization",
        "AI Engineer": "Python, ML, Deep Learning, Transformers, MLOps"
    }
    return roadmap.get(career_name, "No roadmap found for this career.")
print("Career roadmap tool is ready to use.")


# Define tool function for job search advice
@function_tool
def job_advice_tool(input: str) -> str:
    """
    Provides job search tips based on user's query.
    """
    print(f"[DEBUG] Tool called with job_advice_tool={input}")
    if "remote" in input.lower():
        return "Explore remote job boards like We Work Remotely, Remote OK, or FlexJobs. Tailor your resume for remote roles."
    elif "internship" in input.lower():
        return "For internships, target platforms like Internshala, LinkedIn, and AngelList. Customize your cover letter!"
    else:
        return "Use LinkedIn, Indeed, and networking to find jobs. Keep your resume tailored for each job you apply to."
print("Job advice tool is ready to use.")



# # Define tool function for skill development advice
@function_tool
def skill_development_tool(career: str) -> str:
    """
    Suggests skills based on career name.
"""
    print(f"[DEBUG] Tool called with skill_development_tool={career}")
    career = career.lower()
    if "developer" in career or "programmer" in career:
        return "Learn Git, HTML, CSS, JavaScript, TypeScript, React, and Node.js. Build projects on GitHub."
    elif "designer" in career:
        return "Master tools like Figma, Adobe XD, Photoshop. Understand UX principles and design systems."
    elif "data" in career:
        return "Focus on Python, SQL, data analysis with pandas, visualization with matplotlib/PowerBI, and machine learning basics."
    else:
        return "Explore soft skills, communication, and research tools relevant to your chosen field."

print("Skill development tool is ready to use.")


