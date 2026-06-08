import httpx


class ProxyService:

    async def forward(
        self,
        method,
        url,
        headers,
        params,
        body
    ):

        async with httpx.AsyncClient() as client:

            response = await client.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                content=body,
                timeout=10
            )

            return response