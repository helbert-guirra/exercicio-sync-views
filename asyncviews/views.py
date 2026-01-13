import asyncio
import httpx
from time import sleep
from django.http import HttpResponse


# =========================================================
# FUNÇÃO ASSÍNCRONA (NON-BLOCKING)
# =========================================================
async def http_call_async():
    for num in range(5, 0, -1):
        await asyncio.sleep(1)
        print(f"Async contador regressivo: {num}")

    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org")
        print("Async status code:", response.status_code)



# =========================================================
# FUNÇÃO SÍNCRONA (BLOCKING)
# =========================================================
def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(f"Sync contador: {num}")
    response = httpx.get("https://httpbin.org")
    print("Sync status code:", response.status_code)


# =========================================================
# VIEW ASSÍNCRONA (NON-BLOCKING)
# =========================================================
async def async_view(request):
    asyncio.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request (ASYNC)")



# =========================================================
# VIEW SÍNCRONA (BLOCKING)
# =========================================================
def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request (SYNC)")
