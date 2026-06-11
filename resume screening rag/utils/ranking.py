def rank_resume(resume_text, job_description):

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())

    score = len(resume_words.intersection(jd_words))

    return score