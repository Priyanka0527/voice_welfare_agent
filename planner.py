def planner(memory):
    missing = memory.missing()

    if "age" in missing:
        return "ASK_AGE"
    if "income" in missing:
        return "ASK_INCOME"
    if "occupation" in missing:
        return "ASK_OCCUPATION"
    if "category" in missing:
        return "ASK_CATEGORY"

    return "RUN_ELIGIBILITY"
