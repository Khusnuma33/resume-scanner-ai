def match_skills(resume_text, required_skills):
    matched = []
    resume_text_lower = resume_text.lower()
    for skill in required_skills:
        if skill.lower() in resume_text_lower:
            matched.append(skill.lower())
    return matched


