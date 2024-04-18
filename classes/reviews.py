import json
import time, random
import hrequests


def make_reviews_request(id):

    url = f"https://www.vivino.com/api/wines/{id}/reviews?per_page=4&year=2015"

    payload = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.vivino.com/BE/en/penfolds-grange/w/1136930?year=2015&price_id=35098180",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Cookie": "first_time_visit=nhEBt4Z7LMxQd6dqfkA82QCLuP3XSiZNIz1R4Kc^%^2B^%^2BDVpnSa6cWJXICjByS5l25n2HQmd3^%^2FIdL6^%^2FHEcChICw6x^%^2BS76ZZSfYItut07Zbkq54neoeKDC^%^2BJVTOAsFdzRD7QhD4Q^%^3D--zETTaXjLIbPj46vz--Qqaxgxgub^%^2BL2y7IJVy^%^2F2TQ^%^3D^%^3D; anonymous_tracking_id=AiQqXnm46ZAJfz8u5MSFKVnIEcFBlAZkxvY2HPJuzhhYGNPIdXf^%^2BQ^%^2BwUo^%^2F58OM6OpjA8bfTS4ArZm8NQdTE^%^2Fg^%^2FIxXqorrsQim9dal2x^%^2Br0vF1CgC6zQehFZwXKQie4IISzf8DBJrx5F2DHTtFT6GJgPpDvcQv6CpkQoMbfPnPfV0Ozk^%^2B2^%^2BC3MiYCnskJRDZrZneJ--kgy^%^2FI^%^2BCR1sC0WFkW--nGdTDIEqiHxtkESD5or6^%^2BQ^%^3D^%^3D; client_cache_key=EZ^%^2Bxz^%^2BYVANw0pGTQKuHT1nuxLB4^%^2BxHzE8AVqMHDnEqFmDrmBk17xz6oKkH2pSXFzZdXTO8qWBqkPsdn8yB43X8P1kv8b3IJVXeFi^%^2FDntB5Jc3OXwe3swmCg9j^%^2BksBfBZmIZ^%^2BAAG49UA2Et8BPMsniLRc--jZ2xv66ZdHLBAHiL--c7ixiTn6OjZdgfbJyJjMmw^%^3D^%^3D; csrf_token=DKuYkgMzISF8QcMsrwTPEYLxIlUXdhoC2SWtiI2uzNrEyo9JfxzCkp1C60omcbAkMYzbyFq6QZfnIuo1z4emCQ; _ruby-web_session=z1z^%^2FTPdOotO5dAorRoN5ORApA3EfH7R99aVPFVrtyedLIpr9Zp3TZtbPZy9WgjP6TdLD9I7xVrCcCQsGCnPIc4BKa0lo0aXUvndpUMPjE8^%^2Bg0iOggcGWF12x6lmAXN^%^2BE0me4db0cbZ^%^2FNoFjQ2kA7BXGLconmPwIk4Ac^%^2FKCitk50Gn8iTHHU5hHK0h8XvP5O^%^2BHbqSr9eA2bOubBzZRdRqw2YTlbMBRkk7JO^%^2B^%^2FopVjSDQ26SLQhWxMLGa6HlhYgXVG6221DpGnjUvCphfmCcq^%^2BAblNcMpZ9ptKbsElMONlgQ2IMgQbX^%^2BNKCPR4Nd96YkfXk0TiRWKjRYLIUms^%^2BQ^%^2BMArwsIWxZSlA6D07jhlzD0ItYJTCPE7Qqb4kRH5HIdY0^%^2B4U7ASPYdt1qXF5KPRtsKjwCTva4b6eSf3^%^2FAbVNVesN0bk8FnGiaoWFdYbbYv0LDgRMaD5wLvCMXUVNaZ5Gso4rLldMflAxDYcRnYG1LKfAVMTsPfv^%^2Fjw7SK2tW12p0JtDy8vFccW3WSqx^%^2BjQ^%^3D--JOn0R77qfOA0cTBf--OcEFoKJVWOirLZWzhlQBhQ^%^3D^%^3D; eeny_meeny_personalized_upsell_module_v2=fsd^%^2BuG3OjZ8RSsmMqhXHmzvGIsoXTP^%^2FrsGe9Xc^%^2BqqnYiY9v7NRLUJhl6jGORrdVhx10Kiv^%^2B9hcmJXkT0EG0a1w^%^3D^%^3D; didomi_token=eyJ1c2VyX2lkIjoiMThlZTVjOTgtZmU3Yi02ODk2LWIxNmItZGY0YTUzZjQ1ODRiIiwiY3JlYXRlZCI6IjIwMjQtMDQtMTZUMDc6MjI6NTUuODQ3WiIsInVwZGF0ZWQiOiIyMDI0LTA0LTE2VDA3OjIyOjU3LjAzOVoiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImFtYXpvbiIsImM6bWl4cGFuZWwiLCJjOmltcGFjdCIsImM6c3RlZWwtaG91c2UtbWVkaWEiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiJdfSwicHVycG9zZXMiOnsiZGlzYWJsZWQiOlsiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyIsImdlb2xvY2F0aW9uX2RhdGEiXX0sInZlbmRvcnNfbGkiOnsiZGlzYWJsZWQiOlsiZ29vZ2xlIiwiYzptaXhwYW5lbC0zMnFpRVlEcCIsImM6aGVhcC15N0VKcnpraSJdfSwicHVycG9zZXNfbGkiOnsiZGlzYWJsZWQiOlsiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyIsImdlb19hZHMiXX0sInZlcnNpb24iOjIsImFjIjoiQUFBQS5BQUFBIn0=; euconsent-v2=CP9KXsAP9KXsAAHABBENAwEgAAAAAAAAAAZQAAAAAAAA.YAAAAAAAAAAA; recently_viewed=^%^2B9jtRo11uO4ZZV7Wfcmd99d1K0aEnO8JxHqrZ0x8AuDAEyeBAay1HT1h0wZExv9t3fg2i2zFS4LF^%^2BzqD7^%^2BUeVNariphWF8QTNjWzJqZwVO0^%^2FzdOF2^%^2BM7asv2aDmPxaEEQ70QBnkv8CYSPK5WvtAY^%^2BP5JZyITHp2hDVagIonjwJT0twwWyoP8LGa02oyeekM7uNum6ryfJ7ox4N2aEIafBxfUVP5Wqsj2HLdcz8MyCEw2wTPaKw4pFv^%^2Fg64RvuoYVdJcOnFQRVhEk8MjTPbipVw5r^%^2BOBj6gL8fENDwyuEDWwtFDVyGQ2EhIpNI^%^2FSevHyuo7NspyKPEEWyES6x1zoyjTswHakHkfBiM8d9R7Fcj2ZILQyn36q0lIZ^%^2BLtAv5MBg^%^2Fb9EWrdp7wQgDokTDD^%^2FXrh9Knb4JuzZiY2tPO4HghZPZL3kRhiLSv1MJO4Fbd3ZCIoqONQW^%^2BUZZEiRSu^%^2BQ2aedCzbZg7AA6Sph45aiYS46ZJi7rmUqg7a7dTrUTKoGzi79wPmGOaZajFxU^%^2Fgj3Rd6Z8^%^3D--lcP7msbDKwxteLVv--dlaChPq0OLFe9prva^%^2BwsXw^%^3D^%^3D; _ruby-web_session=4rc68FvV5ko4owebIXdc2o%2B7bFopldEqh0r%2Bi5VvNGKU7QGC26PVeaO9BwKXdK4%2FntGnXjklcT3TgB4ZQPL06PSpALsKdQ6ldF1q98eCnL74ievpaHt3vbcoGH0%2BPbHWYyG9BaxAK4UyHj7bYiV2l5nEAIsi0joTYv3JCnl42irmYhSL2Y583vRvlyujJvlphx4LKskvefiquLB3VPZTngDn3Ojf3QDU4rvcvYvbpSZy1dyZ1FXcb4Y%2FV7bIKaSvE9s%2F0gWJhEaXxwKjBz7tkDMLrIaB6sckLTWFIjd2ZsAkO792h3Bsdvsa1jEvrl%2FxnPzdg8CKU%2B3n2qWSN4OT1ANXRzLDbFbr2qnb56HBO0wODU4VMnE4camWBlNGSSx65JgkHQhSR9pLgaR6%2FnIfa2E01g%3D%3D--AGs77D2CGwBM5Bz8--niocrV8anCNDBgnzfT4NMg%3D%3D; csrf_token=1nITvLCpYWFuuqJdRBM6UtqCkY08rI0znh2_GpUPpoXJn6DXZk55jK2sbOCxkM9pIMOXfmJejzXrzGkUky7uag",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "DNT": "1",
        "Sec-GPC": "1",
        "If-None-Match": "W/e65aa655e926cbe6ea978a80185aca10",
        "TE": "trailers",
    }

    response = hrequests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    if response.status_code == 200:
        # The request was successful, process the response
        response_text = response.text
        print(response_text)
        return response.text
    elif response.status_code == 429:
        # We've hit the rate limit
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            # The 'Retry-After' header is present, pause execution for the specified number of seconds
            time.sleep(int(retry_after))
            # Retry the request
            return make_reviews_request(url, headers, payload)
    else:
        # The request failed for some other reason
        raise Exception(f"Request failed with status code {response.status_code}")


def get_ids():
    # read the json file
    with open("wine.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # load the reviews.json file and extract the ids
    with open("reviews.json", "a+", encoding="utf-8") as reviews_file:
        reviews_file.seek(0)  # Go to the start of the file to read its contents
        try:
            reviews_data = json.load(reviews_file)
        except json.JSONDecodeError:
            reviews_data = []

    reviews_ids = [item["id"] for item in reviews_data if json.loads(item["response"])["reviews"]]

    # return all ids that are not in the reviews.json file and where reviews are empty
    return [
        region["id"] for region in data["regions"] 
        if region["id"] not in reviews_ids or not json.loads(region["response"])["reviews"]
    ]


ids = get_ids()

for i in ids:
    response = make_reviews_request(i)
    response_data = {"id": i, "response": response}

    # Read the existing data
    with open("reviews.json", "a+", encoding="utf-8") as f:
        f.seek(0)  # Go to the start of the file to read its contents
        try:
            existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []

    # Append the new response
    existing_data.append(response_data)

    # Write everything back
    with open("reviews.json", "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

    # pause for a random amount of time between 1 and 5 seconds
    # time.sleep(random.uniform(1, 5))
    # time.sleep(2)
