class EthicsFilter:
    def approve(self, intent):
        blocked = ["violence", "hate", "harm"]
        return not any(bad_word in intent["response"].lower() for bad_word in blocked)

