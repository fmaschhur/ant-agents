

class Initiator(object):
    def __init__(self, job):
        self.deals = None
        self.job = job

    def answer(self):
        if self.deals:
            bids = sorted(self.deals, key=lambda x: x.time)
            if bids[0].is_pre_accepted:
                bids[0].set_definitive_accept()
                self.job.status = 2
                for deal in bids[1:]:
                    deal.set_definitive_reject()
                return 1  # Information fü die welt
            bids[0].set_pre_accept()
            for deal in bids[1:]:
                deal.set_pre_reject()
            return 0
        return 0