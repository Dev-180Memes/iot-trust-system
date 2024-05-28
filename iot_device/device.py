import random
import time
import json
import threading


class IOTDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "active"
        self.transaction_history = []
        self.security_incidents = []

    def report_activity(self):
        while True:
            activity = {
                "device_id": self.device_id,
                "timestamp": time.time(),
                "status": self.status,
                "transaction": random.choice(["success", "failure"]),
                "security_incident": random.choice([None, "malware", "unauthorized_access"])
            }
            self.transaction_history.append(activity)
            if activity["security_incident"]:
                self.security_incidents.append(activity["security_incident"])
            self.send_report(activity)
            time.sleep(random.randint(1, 5))

    def send_report(self, activity):
        with open(f"device_logs/device_{self.device_id}_log.json", "a") as log_file:
            log_file.write(json.dumps(activity) + "\n")


def start_reporting(device_id):
    device = IOTDevice(device_id)
    device.report_activity()


if __name__ == "__main__":
    device_threads = [threading.Thread(target=start_reporting, args=(i,)) for i in range(1, 6)]
