class Step():
    def init(self, name):
        self.name = name
        self.duration = TASK_DURATION + 1 - ord('A') + ord(name)
        self.done = False
        self.available = True
        self.time_spent = 0
        self.in_progress = False
        self.prereqs = []

    def start(self):
        self.in_progress = True
        self.available = False

    def do_work(self):
        self.time_spent += 1
        if self.time_spent == self.duration:
            self.done = True
            self.in_progress = False

    def add_prereq(self, req):
        self.prereqs.append(req)
        self.available = False

    def prereq_completed(self, req):
        if req in self.prereqs:
            self.prereqs.remove(req)
            if len(self.prereqs) == 0:
                self.available = True

    def available_list(self):
        if self.available:
            return [self.name]
        return []

    def __iter__(self):
        return self.name

    def __str__(self):
        return "%s:%r" % (self.name, self.prereqs)

