from trust_manager import TrustManager


class ResourceAccessControl:
    def __init__(self, trust_manager):
        self.trust_manager = trust_manager
        self.resources = {"resource1": [], "resource2": [], "resource3": []}

    def control_access(self):
        for device_id, trust_score in self.trust_manager.device_trust_scores.items():
            if trust_score > 75:
                self.grant_resource_access(device_id, ["resource1", "resource2", "resource3"])
            elif trust_score > 50:
                self.grant_resource_access(device_id, ["resource1", "resource2"])
            else:
                self.deny_resource_access(device_id)

    def grant_resource_access(self, device_id, resources):
        for resource in resources:
            self.resources[resource].append(device_id)
        print(f"Device {device_id} granted access to {', '.join(resources)}.")

    def deny_resource_access(self, device_id):
        for resource in self.resources:
            if device_id in self.resources[resource]:
                self.resources[resource].remove(device_id)
        print(f"Device {device_id} denied access to all resources.")
