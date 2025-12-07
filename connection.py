def connect(self, other):
    truth_value = self.truth + other.truth
    emotional_state = self.state & other.state
    return {
        'truth': truth_value,
        'state': emotional_state
    }
