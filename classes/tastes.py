import hrequests
import json
import time, random


def make_tastes_request(id):
    url = f"https://www.vivino.com/api/wines/{id}/tastes?language=en"

    payload = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.vivino.com/BE/en/w/2353",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Cookie": "first_time_visit=nhEBt4Z7LMxQd6dqfkA82QCLuP3XSiZNIz1R4Kc^%^2B^%^2BDVpnSa6cWJXICjByS5l25n2HQmd3^%^2FIdL6^%^2FHEcChICw6x^%^2BS76ZZSfYItut07Zbkq54neoeKDC^%^2BJVTOAsFdzRD7QhD4Q^%^3D--zETTaXjLIbPj46vz--Qqaxgxgub^%^2BL2y7IJVy^%^2F2TQ^%^3D^%^3D; anonymous_tracking_id=AiQqXnm46ZAJfz8u5MSFKVnIEcFBlAZkxvY2HPJuzhhYGNPIdXf^%^2BQ^%^2BwUo^%^2F58OM6OpjA8bfTS4ArZm8NQdTE^%^2Fg^%^2FIxXqorrsQim9dal2x^%^2Br0vF1CgC6zQehFZwXKQie4IISzf8DBJrx5F2DHTtFT6GJgPpDvcQv6CpkQoMbfPnPfV0Ozk^%^2B2^%^2BC3MiYCnskJRDZrZneJ--kgy^%^2FI^%^2BCR1sC0WFkW--nGdTDIEqiHxtkESD5or6^%^2BQ^%^3D^%^3D; client_cache_key=EZ^%^2Bxz^%^2BYVANw0pGTQKuHT1nuxLB4^%^2BxHzE8AVqMHDnEqFmDrmBk17xz6oKkH2pSXFzZdXTO8qWBqkPsdn8yB43X8P1kv8b3IJVXeFi^%^2FDntB5Jc3OXwe3swmCg9j^%^2BksBfBZmIZ^%^2BAAG49UA2Et8BPMsniLRc--jZ2xv66ZdHLBAHiL--c7ixiTn6OjZdgfbJyJjMmw^%^3D^%^3D; csrf_token=BU1glx9_weK_3-bPFm57X0PzEP5vbc13n77Aq-Ig3p_NLHdMY1AiUV7czqmfGwRq8I7pYyKhluKhuYcWoAm0TA; _ruby-web_session=^%^2Bff1mOM7u7He3zE0Lcuw19EcSCzYOjdwgQC6ZZcxlocEWwbkH5IzHt0PgHnjeJCqSy22LDisru^%^2FP6X6dCEJzUFujmlwwRcneHyeh3Z5erJrbCVdI8RKBdcQRcD68ttsOwZ7yCDIDrGZbj5NIAM2U4Nsx^%^2BugIDxyDCN^%^2FlcslSgDwaBnSUpsCKB4c3k1hgQa07kWUM4cvgnOg97DkeDcXKDV4InNEkx4PhzPE7SMSQE4MLys7n0cIT2PGOW7nydNIO0riOAdPlV^%^2Fo8oQ2r1^%^2FySZ^%^2BrkZfL3I75AW5VSk2XdYpkEQOQdTGTmDhmdh9vosQ1VkRVFhazUlRmWxE^%^2BnjpqNMQ4md0sJFOZBt4y0rnEE2a28Bu088KUCgv0XMMxAOsEkrVmFxysu^%^2BcKdHhM3tCAAqhqeuVRO9me1481^%^2BJ8K5S9lzlXr6GLbuZWFDilIrVwVKgRYTV0LTEnqIW7BEiinOBir3BZJoHXGcOMJDJ0vxyZTyxMnA8U9MKDHen^%^2B2D03ejGvILTTzLWNpDMfg^%^3D--3ufHOI9nRcIoFkyG--SG1OM062kAO02UiinQkGJA^%^3D^%^3D; eeny_meeny_personalized_upsell_module_v2=fsd^%^2BuG3OjZ8RSsmMqhXHmzvGIsoXTP^%^2FrsGe9Xc^%^2BqqnYiY9v7NRLUJhl6jGORrdVhx10Kiv^%^2B9hcmJXkT0EG0a1w^%^3D^%^3D; didomi_token=eyJ1c2VyX2lkIjoiMThlZTVjOTgtZmU3Yi02ODk2LWIxNmItZGY0YTUzZjQ1ODRiIiwiY3JlYXRlZCI6IjIwMjQtMDQtMTZUMDc6MjI6NTUuODQ3WiIsInVwZGF0ZWQiOiIyMDI0LTA0LTE2VDA3OjIyOjU3LjAzOVoiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImFtYXpvbiIsImM6bWl4cGFuZWwiLCJjOmltcGFjdCIsImM6c3RlZWwtaG91c2UtbWVkaWEiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiJdfSwicHVycG9zZXMiOnsiZGlzYWJsZWQiOlsiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyIsImdlb2xvY2F0aW9uX2RhdGEiXX0sInZlbmRvcnNfbGkiOnsiZGlzYWJsZWQiOlsiZ29vZ2xlIiwiYzptaXhwYW5lbC0zMnFpRVlEcCIsImM6aGVhcC15N0VKcnpraSJdfSwicHVycG9zZXNfbGkiOnsiZGlzYWJsZWQiOlsiZGV2aWNlX2NoYXJhY3RlcmlzdGljcyIsImdlb19hZHMiXX0sInZlcnNpb24iOjIsImFjIjoiQUFBQS5BQUFBIn0=; euconsent-v2=CP9KXsAP9KXsAAHABBENAwEgAAAAAAAAAAZQAAAAAAAA.YAAAAAAAAAAA; recently_viewed=fKCWa6^%^2F8QC3yxPf1BdlDvECk2TzsKiNDtmBKrMPMI3BJdKjLNqmw0O1O46Hcoa^%^2Bd1I5It9rlRDmyCgCpZCcVshPD2FoMt7rZ3Mihl7gGFC9ZSZhqy^%^2FeHowu^%^2BYSVL2yRV3^%^2F^%^2Bm0hWv8rUZMU01LD13SnY9nvCoBRtNyL2GnnvHLwvlU9wQeRbvnbmOCet5DNtgZuOAl0PXLGoBOK8BpnpN^%^2BL9rc92hT38lAY38^%^2B4Ap^%^2FuVlBu6z9KWs5cVzkI4D4wgyVBjmsXBWI4Ofvm62WRJLgglXQ2WDeZq01ca26q8nHzhjd^%^2F^%^2BJCrzHwqY5iLcnDeDcXwrLOgQ3VdvsUQNbhINHl9HwkIB3OTBlRahSbjk5LsREjhwqPSU^%^2B^%^2Bg2OlNOC8A0QNR^%^2BWuEltl2QCC^%^2F3B1I^%^2FgdmFxdm^%^2BwBazHZyAx^%^2BU0A5cTwwNU1IsLUn9^%^2FcR^%^2BP1qfJ3ClY1gjOxFvR7Wb8ivcl6MbvEr34qufTuTfh01BHQpL1TgPVw0s5i1YgZPWXOHefawOE2s7hNbC6JeKX3B3^%^2FlkpI^%^3D--5YmBqcYHcfSn^%^2Bneh--f42cU3a3LEhO7M3kHXHL3Q^%^3D^%^3D; _ruby-web_session=hlS1xpeugTuRJhBPDmcQdisbLcdrQOZKiYchopF7N8IgMBDmPhqW4dJ06IoLpg%2FWjRcZNhOXxQze2TgsHIpOl5MnF5Gy03QDEyZKumobdTXo7jYttha24PMhHdF1RIeKZFl4aD%2BSd8KIwjqXIkP7SwcnAtFTQXRDuYJGf5TgR3HkvYEzGgG7Lgr2r62OiVjgnfDR7PFY4ottKviMKBQx1JtNELbfT4rymy94%2FhJttF3At%2FcfMUC6yFFcZfY4h2AaBSrvUNVL7zd%2FpY%2BtXocYAiv74z%2FOhdPBfOIHQIjalmNedc9ofQmyTpeBIQrzAhipFxxxEZMtlCILDDiUZn%2FFrhSxMdOdDDpIXqFVauaIUfSozBFjP3R7nExVALQD%2FUfodqUKqukwAEGYDznl7pwQjMAh491Q9HPUKsB8IBCBWaFPjV%2BP6zHe--pa03IT%2BazJD2Ua86--9ESDLu3deT36ylF%2BQvxFQw%3D%3D; csrf_token=vecL6_w4Rr6pJyauSiGR7A3ggKaAvoKsDfIpL-TF1-LcylC_WX78ZMoeRP1x27k0vCDSk48C8hNVurZ7RFTM6A",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "DNT": "1",
        "Sec-GPC": "1",
        "If-None-Match": "W/a31344f78b03f0283e113d63859c221c",
        "TE": "trailers",
    }

    response = hrequests.request("GET", url, headers=headers, data=payload)

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
            return make_tastes_request(url, headers, payload)
    else:
        # The request failed for some other reason
        raise Exception(f"Request failed with status code {response.status_code}")


def get_ids(json_name):
    # read the json file
    with open(json_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    # load the tastes.json file and extract the ids
    with open("tastes.json", "a+", encoding="utf-8") as tastes_file:
        tastes_file.seek(0)  # Go to the start of the file to read its contents
        try:
            tastes_data = json.load(tastes_file)
        except json.JSONDecodeError:
            tastes_data = []

    tastes_ids = [item["id"] for item in tastes_data]

    # get all ids that are not in the tastes.json file or have null structure and flavor
    ids = [
        region["id"] for region in data["regions"] 
        if region["id"] not in tastes_ids or 
        (region.get('response') and json.loads(region['response']).get('tastes', {}).get('structure') is None and 
        json.loads(region['response']).get('tastes', {}).get('flavor') is None)
    ]

    # print the ids and their count
    print(f"Number of IDs: {len(ids)}")

    return ids


ids = get_ids("wine.json")

for i in ids:
    response = make_tastes_request(i)
    response_data = {"id": i, "response": response}

    # Read the existing data
    with open("tastes.json", "a+", encoding="utf-8") as f:
        f.seek(0)  # Go to the start of the file to read its contents
        try:
            existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []

    # Append the new response
    existing_data.append(response_data)

    # Write everything back
    with open("tastes.json", "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

    # pause for a random amount of time between 1 and 5 seconds
    # time.sleep(random.uniform(1, 5))
    # time.sleep(2)
