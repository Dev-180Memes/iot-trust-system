import json
import os


class TrustScoreCalculator:
    def __init__(self, device_id):
        self.device_id = device_id
        self.transaction_history = []
        self.security_incidents = []

    def load_activity_data(self):
        try:
            with open(f"device_logs/device_{self.device_id}_log.json", "r") as log_file:
                self.transaction_history = [json.loads(line) for line in log_file]
        except FileNotFoundError:
            print(f"No data found for device {self.device_id}")

    def calculate_trust_score(self):
        success_count = sum(1 for activity in self.transaction_history if activity["transaction"] == "success")
        failure_count = len(self.transaction_history) - success_count
        incident_count = len([activity for activity in self.transaction_history if activity["security_incident"]])

        if not self.transaction_history:
            return 0

        success_rate = success_count / len(self.transaction_history)
        incident_penalty = incident_count / len(self.transaction_history)
        trust_score = success_rate - incident_penalty

        return max(0, trust_score * 100)

    def get_trust_score(self):
        self.load_activity_data()
        return self.calculate_trust_score()
