import threading
import time

import requests


def heartbeat_loop(
    registry_url: str,
    service_id: str,
    interval: int = 3
):

    while True:

        try:

            requests.post(
                f"{registry_url}/heartbeat",
                json={
                    "service_id": service_id
                },
                timeout=5
            )

        except Exception as e:

            print(
                f"[HEARTBEAT ERROR] "
                f"{service_id}: {e}"
            )

        time.sleep(interval)


def start_heartbeat(
    registry_url: str,
    service_id: str
):

    thread = threading.Thread(
        target=heartbeat_loop,
        args=(
            registry_url,
            service_id
        ),
        daemon=True
    )

    thread.start()