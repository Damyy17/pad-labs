class TransactionCoordinator:
    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def prepare(self):
        votes = []
        for participant in self.participants:
            vote = participant.prepare()
            votes.append(vote)

        if all(vote == 'YES' for vote in votes):
            return 'COMMIT'
        else:
            return 'ABORT'

    def commit(self):
        for participant in self.participants:
            participant.commit()

    def abort(self):
        for participant in self.participants:
            participant.abort()
