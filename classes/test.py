import requests
import json


# This function prints out all the keys found in a nested dictionary in a recursive way.
def extract_keys(val, keys_set=None):
    if keys_set is None:
        keys_set = set()

    if isinstance(val, dict):
        for key in val.keys():
            keys_set.add(key)
            extract_keys(val[key], keys_set)
    elif isinstance(val, list):
        for item in val:
            extract_keys(item, keys_set)

    return keys_set


# Make the request to the hidden api.
url = "https://www.vivino.com/api/regions?cache_key=446940327868b531465e78484b883dd2dddb7fe41e7644a1d54c&language=en"

payload = {}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NTBQS660dXJVS7Z1DQ1SKwDKpqfZliUWZaaWJOao5Rel2KakFier5SdV2ialFpfEF2QmZxerlZdExwKVgikjCGUMoUwglDlUzgQALX0lDQ^%^3D^%^3D",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/json",
    "Alt-Used": "www.vivino.com",
    "Connection": "keep-alive",
    "Cookie": "first_time_visit=38Tmwio2VBRJ2tIfD3n23P8n7yhaXOU1tx^%^2FWpAHZnHcxZqnz3dP7RevKJTCDBjr8oe^%^2FwUPjEMF37EUlf3DdcQSNWYTH4^%^2FoepCcSrSZAXiFzaRSyzH^%^2BJeYTh8HAMW7KjLAcA^%^3D--31^%^2BsMNZKfe7PMrld--YXG66heDIgXVpfhxbkGyGw^%^3D^%^3D; anonymous_tracking_id=2gQtDW4a110zkQKgNT0x3tCMhWBpGnJTjmEZEdT6NCdTkIbd6EGaXPAYiNrv8tLi^%^2B7kBiNdZQPLfyQE7i0GlrQpZK7V^%^2FbhhBTR4siKwW4tammN0TLNBXplLrOVm5LydD5GGx^%^2FmKBmtaQMUdDSxEQpQNyxdHy96FFXL8aYoSaCTUinoFXiwHj5eBoL4F1^%^2BlSxHMnH--DQ^%^2FON8hZp52che0n--n1QJEVQuC2pJuRJYh9Ck^%^2BQ^%^3D^%^3D; client_cache_key=lMZIAP1zy8TgpOqAYHUIwyfNf^%^2FPmHEdZjPkKC^%^2BU2prvVHLLIGa0Uqr7hktVCL^%^2FQnxE^%^2BgvgqOdL7YGA8XvZDIf9j82vj^%^2FumfsY3E5uNRM9Hn7BxBYTmBT16YebKBaCwHHISSf2zgtgKtSFuLnnMpu47Vw--QvYvdJzw7DNCGIxL--6JHrpCgjAv8HsMvte4hqbA^%^3D^%^3D; csrf_token=d9JZgZCbikbzzo3D2R0H9okplF39eSK09ESttjdOoEABfv04ZytMpPxZSlIQFDT7Ep8xYfjE4kB3OH26CTLy3w; _ruby-web_session=sidtgEe^%^2FCFLmc9dRiQ^%^2BEkrJQigG0Dw9uC4dSmy6SstOFVQHCBAXah49rKxFzrm^%^2Fq^%^2BRCBu3PVZX8auV1O4eBzMQT68x4cz0P1fJIO8rDC3dKxGJeP4Eg5NfS^%^2FQUt6Vf1iCT5YsPFbIOQE7MtPI99dxjd2BFYo6d7FhEh47SEAPwlfdBI4bvsW1N5^%^2Fkh^%^2FkYb^%^2B9ZEpUxeQfqnNYnOUkZlWBI5UOQJZkwvhoyhr8QAtspP6^%^2Ff5hwu07^%^2BIQTjA^%^2FrUzYn78T6yYyHVyeyZCcb54gh0PpDC^%^2B7X7idnLThkWnoqjTmbmlYdQ7rLR^%^2FTSEuTy5nZrGT7dlvkCWbc0uW65OT^%^2FcQw^%^2BXoYS30b9nAaN1qODc^%^2B9Ifa^%^2Bz6v7ZaMSFxAYRYM6tzHqKDfekihZx4X5qqr5lBvfLW5bp^%^2FgDbqKvqX3VrETq^%^2FHIXcw^%^3D--Q4nxh^%^2FHKr6JthcPQ--9Tfus5yEyHTleUovX7Y^%^2BKA^%^3D^%^3D; eeny_meeny_personalized_upsell_module_v2=ytfRyykU09EQE3cY3KGPXVpH5onaIKjR5m^%^2F29EOEHxseyCTuk2^%^2FDKWmBrOID^%^2B2QswT5pAc^%^2BarC^%^2B248ihJGc6gw^%^3D^%^3D; didomi_token=eyJ1c2VyX2lkIjoiMThlZTEwYjUtMWMwYi02N2JiLWI3NjQtMDAzODViNzVkZmY1IiwiY3JlYXRlZCI6IjIwMjQtMDQtMTVUMDk6MTY6MzkuMjMyWiIsInVwZGF0ZWQiOiIyMDI0LTA0LTE1VDA5OjE2OjQyLjUwNFoiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImFtYXpvbiIsImM6bWl4cGFuZWwiLCJjOmltcGFjdCIsImM6c3RlZWwtaG91c2UtbWVkaWEiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiJdfSwicHVycG9zZXMiOnsiZGlzYWJsZWQiOlsiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyIsImdlb2xvY2F0aW9uX2RhdGEiXX0sInZlbmRvcnNfbGkiOnsiZGlzYWJsZWQiOlsiZ29vZ2xlIiwiYzptaXhwYW5lbC0zMnFpRVlEcCIsImM6aGVhcC15N0VKcnpraSJdfSwicHVycG9zZXNfbGkiOnsiZGlzYWJsZWQiOlsiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyIsImdlb19hZHMiXX0sInZlcnNpb24iOjIsImFjIjoiQUFBQS5BQUFBIn0=; euconsent-v2=CP9HEwAP9HEwAAHABBENAvEgAAAAAAAAAAZQAAAAAAAA.YAAAAAAAAAAA; recently_viewed=yLZjKKcLuBSidvhr9D1OIIEoM7jMoNMT^%^2Fsln7tNe82F2HdPM68cjr6^%^2BhXCAIvmTAUOFaCZgSZPaGSY0pTq2FV7w596snmXtw0jLG^%^2FF6NWr5jCJBiehY3D22nR3kSnGi7QaH5vuLo0RlYKThILO3Xw2^%^2FzIYSNcFcV5DMA5tBKEIQuN^%^2BXvPevpNu7N9R8Z09kolbC34r75kNkT4yuUNKETVo^%^2ByNDcvZn34tbDo5bKyV1bMN3V5P1wpxPRf2g4Fu^%^2F4BLEwd9a3PA1M8trpme6N5e6wRfTlIbYu2WSjcpDjQNWASurtikRo^%^2FZ^%^2Bvt2p5KbE6f^%^2FyxxZhQPN8EfZMBtqPnIG0gbGey89K5m^%^2BtSipPMHXUPRNSmmf9^%^2F5AX9D4ROAV5GJbunco3O1Yf^%^2FgcHwAsOogJI3V1GDMeZ^%^2Fht4e0OMIPa33o7aLCKAKVeS3uQ1AeA2CCtADg^%^2BmQzfr33VxYK^%^2BAfjTYhhPXcW6drZ9Mw0YMEM^%^2BLmjCDpMpZj7K9NbLG5HzPKsg1bcXlNTpBNXtzgZ^%^2Bhb4Oxg^%^3D--ARuxgIhvkMC6mAVq--mE8eHg4oJoD^%^2F1V7CN0aaZw^%^3D^%^3D; _ruby-web_session=i3E%2B7%2BQGDyQFvb18wE0KYqm8T2FuUUohO7jWmXZdFbxNeDf4sLZ2F%2B8DOcX9xSnMROhZ6U92V%2FXEca5oHNLsHdeA6a7X%2FCHJArNp4t2hh2jddRz%2FMr5%2B9R97KeU5KzlEPJpEsRbZZbFDROMKEV%2F2xUmtIZJgIppnCzLYhN7Fa6nCYajPHxrLK2SP2c9pfVOF0oxexqsbyBbAZmLGJOCf8OXqAnr5x4ygaT%2BjZQPx%2BwkhJldkeLUnrQVZft87iELrKOE1K9DiAszO7AAkIXv4GgavF5k9S5dM0qrVRLLMqjiT39LNwCryNUCggJwpsWOKQqQGd410kMx6ZbIgQRjwVTCsNmW7PClZ8vo2TFpdrhqb64hkuzt%2BOKsQcUPkF63gxjV4SpT4EKWYQ%2Fo%3D--CPTZ33Lsus95PJMm--ds95H6wPlaXTXVokTQv5VA%3D%3D; anonymous_tracking_id=jb1qRxZgoAK4uSDztkfT0yy8SMt9DAgrSDtFdx3uEy7WG7TAauyXCNwLtHoUvKwyMv6ymCxwPTMrRqTxyE0gDaeF5FX2t6gwa8i0RDgF%2B4lqryw6XbI811pmgS9TRwdVBTq7oGOsuGv6F89dildZU8NDzFd0AhR5BMyRULJs5XWfF3QmLgIfwl7Gt4aE9ap%2FEpBY--%2FvRb2KXPtvRCTQfe--S5xC09sxWK7PROP2S8FesQ%3D%3D; client_cache_key=PI6I1E0h8wGevBhIio664X5IbvDM%2Fw8lTs6H5upAuO4YOjippd%2BNdqGDTH6Yt%2F73z%2B7tV0gwWhUBjYvw%2F4suHOl%2FZ4PmDqEyW01mLzfVlqMGYw%2F8O31uxgD%2Bk2013DQklLc4OVfvROqFo8Vu6xoiS2%2B%2B--HAinzTPQaxq%2FxRku--ovxLRFcI8kqNxaaR1v99eQ%3D%3D; csrf_token=nFeYypzveID7PR8pdLmYSObeZQyLOZW66jjFxryujMxmtt1cgm13h1OAQeScX9BQTaYIU8NAiJ9BzJyIA92NGQ; eeny_meeny_personalized_upsell_module_v2=APMFYVwXN2Zx0oLHisMQvRLVCywNJoOa2SAD51xzB%2F2M0G%2BoNCLLdYajQ%2BnhAELCsGCGirmJ6L%2Baz0QlYVyOsg%3D%3D; first_time_visit=GiBIZABJmCWPVYxB60HySFKnn%2F8a4Hwx8a7iD4VRYY1DVrJqZA%2BMHlBZnZIe36avMkgT2zCBt1XiEkbT2tmvV7%2FrtvqQhRanM%2BtTMtDFYF9RzpX1XtM3%2FfxvDeiz3MJ9CPw%3D--iq%2FzCRwd1BCMu9x7--uh5qIFGbcabKHHeurS%2FDtw%3D%3D",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Sec-GPC": "1",
    "If-None-Match": "W/8e2611eb5423e6d95087e34ef9d2061d",
    "TE": "trailers",
}

response = requests.request("GET", url, headers=headers, data=payload)

print(extract_keys(json.loads(response.text)))

# save the response to a json file
with open("wine.json", "w", encoding="utf-8") as f:
    f.write(response.text)
