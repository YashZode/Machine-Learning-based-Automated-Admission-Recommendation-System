# --------------------------------------------
# File: score_sop_lor.py
# Description: Provides continuous scoring functions for SOP and LOR summaries
#              by scaling the density of detected keywords to a 1.0–5.0 range.
# --------------------------------------------

TECHNICAL_KEYWORDS_SOP = [
    "Java", "Python", "C++", "API", "Spring Boot", "Docker", "SQL", "Machine Learning",
    "Android", "Web application", "Web development", "Software engineering", "Software development",
    "Cloud", "Microservices", "RESTful", "DevOps", "Deployment", "CI/CD", "Project", "Internship",
    "Agile", "Data Structures", "Algorithm", "Cybersecurity", "Database", "Thingworx", "Networking",
    "Cyber security", "Kubernetes", "Version control", "Git", "JIRA", "Postman", "Automation", "SpringBoot"
]

TECHNICAL_KEYWORDS_LOR = [
    "performance", "project", "skills", "academic", "internship", "teamwork", "leadership",
    "machine learning", "communication", "problem-solving", "research", "dedicated",
    "technical", "programming", "recommend", "knowledge", "collaboration", "presentation",
    "adaptability", "initiative"
]

def score_sop(summary: str) -> float:
    """
    Assigns a continuous score (1.0–5.0) to the SOP summary by scaling the count of
    detected technical keywords relative to the total keyword set.

    Returns:
        float: SOP score rounded to one decimal place.
    """
    summary_lower = summary.lower()
    detected = [kw for kw in TECHNICAL_KEYWORDS_SOP if kw.lower() in summary_lower]
    print("✅ Detected SOP Keywords:", detected)
    count = len(detected)
    max_count = len(TECHNICAL_KEYWORDS_SOP)
    score = 1.0 + 4.0 * (count / max_count)
    return round(min(score, 5.0), 1)


def score_lor(summary: str) -> float:
    """
    Assigns a continuous score (1.0–5.0) to the LOR summary by scaling the count of
    detected strength keywords relative to the total keyword set.

    Returns:
        float: LOR score rounded to one decimal place.
    """
    summary_lower = summary.lower()
    detected = [kw for kw in TECHNICAL_KEYWORDS_LOR if kw.lower() in summary_lower]
    print("✅ Detected LOR Keywords:", detected)
    count = len(detected)
    max_count = len(TECHNICAL_KEYWORDS_LOR)
    score = 1.0 + 4.0 * (count / max_count)
    return round(min(score, 5.0), 1)
