#!/usr/bin/env python3

import json
from lxml import etree
from typing import List, Optional, Dict, Any
from datetime import date
import requests
import re

# Paths
VERSIONS_JSON = "./static/versions.json"
VERSION_TXT = "./static/version.txt"
KLEI_DST_VERSION = "https://forums.kleientertainment.com/game-updates/dst/"

RE_NUM = re.compile("\d+")


class DstVersion:
    version: int
    release_date: date
    is_release: bool
    is_hotfix: bool
    is_pinned: bool

    def __str__(self) -> str:
        return f"version: {self.version} date: {self.release_date} is_release: {self.is_release}"

    # Released 12/19/23...
    def __init__(self, num: int, release_date: str, is_release: bool) -> None:
        lst: List[str] = RE_NUM.findall(release_date)
        self.version = num
        self.is_release = is_release
        self.release_date = date(int(lst[2]) + 2000, int(lst[0]), int(lst[1]))
        self.is_hotfix = False
        self.is_pinned = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": self.version,
            "release_date": self.release_date.isoformat(),
            "is_release": self.is_release,
            "is_hotfix": self.is_hotfix,
            "is_pinned": self.is_pinned,
        }


def get_version_lst(url: str) -> List[DstVersion]:
    """
    sorted by version reverse=True
    """
    res_lst: List[DstVersion] = []

    text = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
        },
        timeout=10,
    ).text

    html: etree._Element = etree.HTML(text)
    h3_lst: List[etree._Element] = html.xpath(
        "//h3[@class='ipsType_sectionHead ipsType_break']"
    )

    for h3 in h3_lst:
        num_s: str = h3.text
        num = int(num_s.strip())

        # check is release
        is_release = "Release" in list(h3)[0].text

        # check is pinned
        h3_next: Optional[etree._Element] = h3.getnext()
        if h3_next is not None:
            lst = list(h3_next)
            if len(lst) > 0:
                is_pinned = "span" in lst[0].tag
            else:
                is_pinned = False
        else:
            is_pinned = False

        # check is hotfix
        h3_p: Optional[etree._Element] = h3.getprevious()

        is_hotfix = h3_p is not None

        # get release date
        release_date = list(h3.itersiblings("div"))[-1].text.strip()

        res = DstVersion(num, release_date, is_release)
        res.is_hotfix = is_hotfix
        res.is_pinned = is_pinned

        res_lst.append(res)

    # sort lst
    lst = sorted(res_lst, key=lambda v: v.version, reverse=True)

    return lst


# def read_version_txt() -> int:
#     with open(VERSION_TXT, "r", encoding="utf-8") as f:
#         return int(f.read().strip())


# def read_version_json() -> Union[List[Dict[str, Any]], Any]:
#     with open(VERSIONS_JSON, "r", encoding="utf-8") as f:
#         return json.load(f)


def save_to_version_txt(version_num: int):
    with open(VERSION_TXT, "w", encoding="utf-8") as f:
        f.write(str(version_num))


def save_to_versions_json(value):
    with open(VERSIONS_JSON, "w", encoding="utf-8") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)


def latest_version(lst: List[DstVersion], release_only: bool) -> int:
    latest = 0

    for v in lst:
        if release_only and not v.is_release:
            continue

        latest = max(v.version, latest)

    return latest


def dst_version_serializable(lst: List[DstVersion]) -> list:
    return list(map(lambda v: v.to_dict(), lst))


if __name__ == "__main__":
    dst_version = get_version_lst(KLEI_DST_VERSION)
    save_to_versions_json(dst_version_serializable(dst_version))
    latest_release = latest_version(dst_version, True)
    latest_all = latest_version(dst_version, False)
    save_to_version_txt(latest_release)
    print(f"latest release: {latest_release}")
    print(f"latest version: {latest_all}")
