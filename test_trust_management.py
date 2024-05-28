import json
import time
import threading
from iot_device import start_reporting
from trust_manager import TrustManager
from access_control import ResourceAccessControl


def generate_activity(device_id, activities):
    device_log_path = f"device_logs/device_{device_id}_log.json"
    with open(device_log_path, "w") as log_file:
        for activity in activities:
            log_file.write(json.dumps(activity) + "\n")


def test_trust_score():
    # Generate specific activities for device 1
    activities = [
        {"device_id": 1, "timestamp": time.time(), "status": "active", "transaction": "success",
         "security_incident": None},
        {"device_id": 1, "timestamp": time.time(), "status": "active", "transaction": "failure",
         "security_incident": "malware_detected"},
        {"device_id": 1, "timestamp": time.time(), "status": "active", "transaction": "success",
         "security_incident": None},
    ]
    generate_activity(1, activities)

    trust_manager = TrustManager()
    trust_manager.update_trust_scores()
    trust_manager.enforce_policies()

    assert trust_manager.device_trust_scores[1] < 75, "Trust score should be lower due to security incident"

    access_control = ResourceAccessControl(trust_manager)
    access_control.control_access()

    assert 1 not in access_control.resources["resource3"], "Device 1 should not have access to resource3"


if __name__ == "__main__":
    test_trust_score()
