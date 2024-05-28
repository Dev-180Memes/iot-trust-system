from iot_device import start_reporting
from trust_manager import TrustManager
from access_control import ResourceAccessControl
import threading
import time


if __name__ == "__main__":
    device_threads = [threading.Thread(target=start_reporting, args=(i,)) for i in range(1, 6)]
    for thread in device_threads:
        thread.start()

    trust_manager = TrustManager()
    trust_manager.update_trust_scores()
    trust_manager.enforce_policies()

    access_control = ResourceAccessControl(trust_manager)
    access_control.control_access()
