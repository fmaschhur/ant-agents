

class Initiator(object):
    def __init__(self, job):
        self.deals = None   # abgegebene angebote
        self.job = job      # job für den der initiator zuständig ist

    # Nimmt alle eingegangenen Deals. Gibt dem besten ein preaccept oder ein definitive accept, je nachdem ob es vorher ein preaccept gab. dem rest pre reject.
    # wenn es ein preaccept gab ändere den job status auf 2 und gib eine 1 zurück.
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