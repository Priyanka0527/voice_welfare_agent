class Memory:
    def __init__(self):
        self.profile = {}   # always fresh
        self.history = []

    def update(self, key, value):
        self.profile[key] = value

    def get(self, key):
        return self.profile.get(key)

    def missing(self):
        required = ["age", "income", "occupation", "category"]
        return [k for k in required if not self.profile.get(k)]
