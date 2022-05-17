from bidding.models import Bid


class BiddingInteractions:
    def __init__(self, **repositories):
        self._database_repository = repositories["database_repository"]
        self._pubsub_repository = repositories["pubsub_repository"]

    def list(self):
        return [m.to_dict() for m in self._database_repository.list_models()]

    def create(self, data):
        bid = Bid(
            price=data["price"],
            status=data["status"],
            bid_accepted=data["bid_accepted"],
            price_accepted=data["price_accepted"],
        )

        return self._database_repository.create_bid(bid).to_dict()

    def get(self, data):
        return self._database_repository.get_bid(data)

    def update(self, id, data):
        price=data["price"],
        status=data["status"],
        bid_accepted=data["bid_accepted"],
        price_accepted=data["price_accepted"],
        return self._database_repository.update_bid(id, price, status, bid_accepted, price_accepted)

    def delete(self, d_id):
        return self._database_repository.delete_bid(d_id)