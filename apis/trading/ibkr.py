"""IBKR api object."""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class IBApi(EWrapper, EClient):
    def __init__(self):
        """Init function."""
        EClient.__init__(self, self)
        self.data = []

    def error(self, reqId, errorCode, errorString):
        """Error function."""
        print("Error. Id: ", reqId, " Code: ", errorCode, " Msg: ", errorString)

    def historicalData(self, reqId, bar):
        """Append bar data to list."""
        self.data.append([bar.date, bar.close, bar.volume])

    def historicalDataEnd(self, reqId: int, start: str, end: str):
        """Reset list after data is called."""
        self.data = []

    def nextValidId(self, orderId: int):
        """Next valid id."""
        super().nextValidId(orderId)
        self.nextValidOrderId = orderId
