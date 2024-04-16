import requests
import json


def get_id(json_name):
    # read the json file
    with open(json_name, "r") as file:
        data = json.load(file)
    return data["regions"][0]["id"]


def construct_url(id):
    base_url = "https://www.vivino.com/BE/en/w/"
    full_url = str(base_url) + str(id)
    return full_url


print(construct_url(2978))

# url = "https://www.vivino.com/api/prices/35283752/subtotal?language=en"

# payload = {}
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
#     "Accept": "application/json",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://www.vivino.com/BE/en/bodegas-vilano-castilla-and-leon-terra-incognita-ribera-del-duero/w/3721052?year=2020&price_id=35283752",
#     "X-Requested-With": "XMLHttpRequest",
#     "Content-Type": "application/json",
#     "Connection": "keep-alive",
#     "Cookie": "first_time_visit=nhEBt4Z7LMxQd6dqfkA82QCLuP3XSiZNIz1R4Kc^%^2B^%^2BDVpnSa6cWJXICjByS5l25n2HQmd3^%^2FIdL6^%^2FHEcChICw6x^%^2BS76ZZSfYItut07Zbkq54neoeKDC^%^2BJVTOAsFdzRD7QhD4Q^%^3D--zETTaXjLIbPj46vz--Qqaxgxgub^%^2BL2y7IJVy^%^2F2TQ^%^3D^%^3D; anonymous_tracking_id=AiQqXnm46ZAJfz8u5MSFKVnIEcFBlAZkxvY2HPJuzhhYGNPIdXf^%^2BQ^%^2BwUo^%^2F58OM6OpjA8bfTS4ArZm8NQdTE^%^2Fg^%^2FIxXqorrsQim9dal2x^%^2Br0vF1CgC6zQehFZwXKQie4IISzf8DBJrx5F2DHTtFT6GJgPpDvcQv6CpkQoMbfPnPfV0Ozk^%^2B2^%^2BC3MiYCnskJRDZrZneJ--kgy^%^2FI^%^2BCR1sC0WFkW--nGdTDIEqiHxtkESD5or6^%^2BQ^%^3D^%^3D; client_cache_key=EhoESEutgrS7raucfZI8G^%^2FpOZ1NhceMJ8cAEWogzCLHjrJwyAdvXZCOjHPDf3FoiN^%^2BpVpgibiARoKJKqvu^%^2FHtFEYXAwciCrQGgYdK^%^2F1EIl4glArlKRk^%^2F2eHQmeExhfPkVanP1p910CEOHsekX8HpXxSE--BcZ0E1mxsGCDVefg--msDvnqlP2ODfxAwUltsmOA^%^3D^%^3D; csrf_token=2S_euVJDqOz3N-azSNbve_bbgxxX00Pk912xPMNBQqERTsliLmxLXxY0ztXBo5BORaZ6gRofGHHJWvaBgWgocg; _ruby-web_session=0D^%^2BRyczyf9fvYFLHhEPQOs5kUY6kZAJs4^%^2BCsbybhUnJasDtWhxxshFML9YfwNoHT^%^2FdMDpsaYNL7ip^%^2FmKpXt13yfNhKRSWpXVxcKHcXDM2CpSClTEadZUPt^%^2FFwDgbDICKsMoqoRt4dxrMe7pKtYwo1Sd07ylR1FP^%^2FtKVRArqaZNVFQaKnpaq1NiIxpnbbltwVQAASJLOFUo8GD2ani7y1WOnDXhtx8932wzggS5hv2dL3YtSB8CUimmA1u7m4l1NFUTrFivFi10VhVVoVokCOLdn1QOP651tUkfwusxxepOSHhHGqK3^%^2F2bUWkBVjvVsqWPLr9FqsOgZjYp^%^2BIQ8RQAHMRHxOt4dkTH0uzjFaa84MEFj^%^2BNeSKbhIkYKbcrDqkbbAQZJopOd9houkaomK50l182ngy4O4Euk43XeMBN^%^2BCgqy^%^2FuNoAN8I--QaBh^%^2BH1IaudEe8N6--CZPtM3MTxUAgX6xE^%^2B4L8vQ^%^3D^%^3D; eeny_meeny_personalized_upsell_module_v2=fsd^%^2BuG3OjZ8RSsmMqhXHmzvGIsoXTP^%^2FrsGe9Xc^%^2BqqnYiY9v7NRLUJhl6jGORrdVhx10Kiv^%^2B9hcmJXkT0EG0a1w^%^3D^%^3D; didomi_token=eyJ1c2VyX2lkIjoiMThlZTVjOTgtZmU3Yi02ODk2LWIxNmItZGY0YTUzZjQ1ODRiIiwiY3JlYXRlZCI6IjIwMjQtMDQtMTZUMDc6MjI6NTUuODQ3WiIsInVwZGF0ZWQiOiIyMDI0LTA0LTE2VDA3OjIyOjU3LjAzOVoiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImFtYXpvbiIsImM6bWl4cGFuZWwiLCJjOmltcGFjdCIsImM6c3RlZWwtaG91c2UtbWVkaWEiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiJdfSwicHVycG9zZXMiOnsiZGlzYWJsZWQiOlsiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyIsImdlb2xvY2F0aW9uX2RhdGEiXX0sInZlbmRvcnNfbGkiOnsiZGlzYWJsZWQiOlsiZ29vZ2xlIiwiYzptaXhwYW5lbC0zMnFpRVlEcCIsImM6aGVhcC15N0VKcnpraSJdfSwicHVycG9zZXNfbGkiOnsiZGlzYWJsZWQiOlsiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyIsImdlb19hZHMiXX0sInZlcnNpb24iOjIsImFjIjoiQUFBQS5BQUFBIn0=; euconsent-v2=CP9KXsAP9KXsAAHABBENAwEgAAAAAAAAAAZQAAAAAAAA.YAAAAAAAAAAA; recently_viewed=YFsTNuuoJgggkqaTZsAoWUOi84JAJ9oAF3gLGbMxNOhmopvfrG^%^2FIZg2uVPSvjZtteL7qpb9vdBNQh5B3pT3ONuXvrw^%^2FFWdo0bWi8N1QwNqUDpsiPhjesZeCI0EtS5N8vHv^%^2BE94tIlkAOOoUNPLLcypH1DMEe^%^2FYtgQfN^%^2B6IgT4FyBwNcVjFnMSQImqxy^%^2BHNsePOeB2yqoycnd6uCxzdENzfjtO42Jd0ETrENdiDt19gIWqi8M5UwY2qojrPRbI0HSHXjdwuNNfVKOiLC^%^2F3qbqJIKWp7dkZ6jWa6qabBe5pRFH7OZ^%^2BfGCbRMEgHd7Nx1CaylEeECbVnnViCPGLPPYJx66gUPB2Lyhc^%^2BP7CFSM^%^2FjV5tKn3o4BQyKHrLuVTQ4QrxPTEeTFZLILUOJgl^%^2BsjwMIOwQ7Q9C3LEBP7EHNcxvQzqRssseWVsKr6sdgBhSmdHfXoNm^%^2BOxz0MXk7SeYJYQWZww8cxgIpeDBxGhOE8dammjsRFE^%^2FH5SPQcSVtSQ0S4mewxM4MAT3kuKWkTyz9bMapz0^%^3D--o7t0CRRiGL2UbeoF--1v1v1w9dwvM9s9nyLoJTsw^%^3D^%^3D; _ruby-web_session=M0X65cIpokvswJOq7Z32dTYsa6UKYPo2qLd3EjaUJ3zGHR%2FcrALj%2B6iEvxbRK0oN6c3W9iZwwlZQMWDpkLlYviP1bV4gr%2BUXNINE3bqmaurRgvMe9wPwKx0jmIasS49qz4PaxLOe1lhr9%2BotQ5qqvGS5jB3N6S0XjNFjL1IdMTWfL0IyHpq3q9ec37GblpV4JkfsggZ0rxgZaCUSqGkkVo%2BbCMp0y4EG7%2FPdFNcggF70BQw64i9oyGSiZincOva1UnZ0jSVOAJxa6BHccCmq1wLBV6tVURxwMV%2F%2FCgpjPMYga1iCJQU4bNahg24iSFRKIvP1tg1V99TbS2d6%2Ft03FalHVf3Hz5RgC53rSWwMsZMtazAnWEyCjQSLjltxyjsYX7Qo8w7vxJV1hUFYGXo8--Nzoj0uInKJzpCveU--v1znfiMq7qfosCGgEM%2BChw%3D%3D; csrf_token=N_3LysYNU86UxNlFHEvWhWTZVX2yeufZxfyHom-pSRS-zbiXp4L6D8cq6teFWgmOKcbhjUMcXz7dm7EqVkCoZw",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "DNT": "1",
#     "Sec-GPC": "1",
#     "If-None-Match": "W/a9a7404f3d2c7fcbbf513abf7cfe2481",
#     "TE": "trailers",
# }

# response = requests.request("GET", url, headers=headers, data=payload)
