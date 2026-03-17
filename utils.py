from typing import List

def extract_skills(job_description: str) -> List[str]:
    keywords = [
        "python", "sql", "machine learning", "nlp", "aws",
        "azure", "data engineering", "spark", "streamlit",
        "api", "docker", "langchain"
    ]
    found = []
    jd_lower = job_description.lower()
    for keyword in keywords:
        if keyword in jd_lower:
            found.append(keyword)
    return found if found else ["python", "sql", "machine learning"]

def retrieve_portfolio_links(skills: List[str]) -> List[str]:
    portfolio_db = {
        "python": "https://github.com/yourusername/python-project",
        "sql": "https://github.com/yourusername/sql-project",
        "machine learning": "https://github.com/yourusername/ml-project",
        "nlp": "https://github.com/yourusername/nlp-project",
        "spark": "https://github.com/yourusername/spark-project",
        "api": "https://github.com/yourusername/api-project",
        "docker": "https://github.com/yourusername/docker-project",
        "langchain": "https://github.com/yourusername/cold-email-generator"
    }
    links = []
    for skill in skills:
        if skill in portfolio_db:
            links.append(portfolio_db[skill])
    return list(dict.fromkeys(links))[:4]

def generate_email(job_description: str, skills: List[str], links: List[str]) -> str:
    skill_text = ", ".join(skills)
    link_text = "\n".join(links) if links else "Portfolio available upon request."

    return f"""Subject: Application for Relevant Opportunity

Hi Hiring Team,

I came across the role and noticed the need for experience in {skill_text}. My background includes building AI-driven applications, backend systems, and data workflows using technologies aligned with these requirements.

I have worked on projects involving machine learning, APIs, and scalable application development. A few relevant portfolio links are included below:

{link_text}

I would love the opportunity to discuss how my skills can contribute to your team.

Best regards,
Sushmanth Reddy
"""
