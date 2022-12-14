"""
Filename    : Recall.py
Description : 
"""
class Recall():
    def __init__(self, data):
        self.manufacturer = data["Manufacturer"]
        self.campaignNum = data["NHTSACampaignNumber"]
        self.parkIt = data["parkIt"]
        self.parkOutside = data["parkOutSide"]
        self.reportReceiveDate = data["ReportReceivedDate"]
        self.component = data["Component"]
        self.summary = data["Summary"]
        self.consequence = data["Consequence"]
        self.remedy = data["Remedy"]
        self.notes = data["Notes"]

    def __repr__(self) -> str:
        return f"{self.campaignNum}"


