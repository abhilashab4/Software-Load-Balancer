import requests


def register_service(
    registry_url: str,
    service_id: str,
    service_url: str
):

    try:

        response = requests.post(
            f"{registry_url}/register",
            json={
                "service_id": service_id,
                "url": service_url
            },
            timeout=5
        )

        response.raise_for_status()

        print(
            f"[REGISTERED] "
            f"{service_id}"
        )

    except Exception as e:

        print(
            f"[REGISTER FAILED] "
            f"{service_id}: {e}"
        )