from tools.eligibility import EligibilityEngine

engine = EligibilityEngine()

def executor(memory):
    return engine.check(memory.profile)
