import time
from threading import RLock


class ServiceRegistry:

    def __init__(self, timeout_seconds: int = 10):
        self.timeout_seconds = timeout_seconds
        self.services = {}
        self.lock = RLock()

    def register(self, service_id: str, url: str):

        with self.lock:
            self.services[service_id] = {
                "service_id": service_id,
                "url": url,
                "last_heartbeat": time.time()
            }

    def heartbeat(self, service_id: str):

        with self.lock:

            if service_id not in self.services:
                return False

            self.services[service_id][
                "last_heartbeat"
            ] = time.time()

            return True

    def get_healthy_services(self):

        now = time.time()

        healthy = []

        with self.lock:

            for service in self.services.values():

                if (
                    now - service["last_heartbeat"]
                    <= self.timeout_seconds
                ):
                    healthy.append({
                        "service_id":
                            service["service_id"],
                        "url":
                            service["url"]
                    })

        return healthy

    def remove_dead_services(self):

        now = time.time()

        with self.lock:

            dead = []

            for (
                service_id,
                service
            ) in self.services.items():

                if (
                    now - service["last_heartbeat"]
                    > self.timeout_seconds
                ):
                    dead.append(service_id)

            for service_id in dead:
                del self.services[service_id]