from trust_score import TrustScoreCalculator


class TrustManager:
    def __init__(self):
        self.device_trust_scores = {}

    def update_trust_scores(self):
        for device_id in range(1, 6):
            calculator = TrustScoreCalculator(device_id)
            self.device_trust_scores[device_id] = calculator.get_trust_score()

    def enforce_policies(self):
        for device_id, trust_score in self.device_trust_scores.items():
            if trust_score > 75:
                self.grant_access(device_id)
            elif trust_score > 50:
                self.limit_access(device_id)
            else:
                self.restrict_access(device_id)

    @staticmethod
    def grant_access(device_id):
        print(f"Device {device_id} granted full access.")

    @staticmethod
    def limit_access(device_id):
        print(f"Device {device_id} granted limited access.")

    @staticmethod
    def restrict_access(device_id):
        print(f"Device {device_id} access restricted.")
