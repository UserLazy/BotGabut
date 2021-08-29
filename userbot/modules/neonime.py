"""
 Scrape neonime.site, samehadaku.vip, kusonime.com, lendrive.web.id
 Feature
           Show new update anime
           Scrape link download
 Update By : t.me/erruuu
 Improve By : t.me/RxyMX
"""

import requests
from bs4 import BeautifulSoup as bs
import re
from userbot import CMD_HELP
from userbot.events import register



@register(outgoing=True, pattern=r"^\.neo ?(.*)")
async def _neonime(event):
    await event.edit('`please wait...`')
    url = 'https://neonime.site/episode/'
    ht_ = requests.get(url).text
    _bs = bs(ht_, "html.parser")
    bd_ = _bs.findAll('td', class_='bb')
    out = "<b>➲ Neonime > New Episode:</b>\n═════════════════\n"
    for kntl_ in bd_:
        _lucu = kntl_.find('a')
        if not _lucu:
            _lucu = 'none'
        else:  # FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
            tt_ = _lucu.get_text()
            _tt = re.sub(r'\s+Subtitle\s+Indonesia\s+Season.\d+', '', tt_)
            link = _lucu['href']
            out += f"➣ <a href='{link}'>{_tt}</a>\n"
            if len(out) > 1000:
                break
            await event.edit(out, parse_mode="html")


@register(outgoing=True, pattern=r"^\.ks ?(.*)")
async def _neonime(event):
    await event.edit('`please wait...`')
    url = 'https://kusonime.com/'
    ht_ = requests.get(url).text
    _bs = bs(ht_, "html.parser")
    bd_ = _bs.findAll('h2', class_='episodeye')
    out = "<b>➲ Kusonime > New Batch:</b>\n═════════════════\n"
    for kntl_ in bd_:
        _lucu = kntl_.find('a')
        if not _lucu:
            _lucu = 'none'
        else:  # FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
            tt_ = _lucu.get_text()
            _tt = re.sub(r'\s+Subtitle\s+Indonesia\s+Season.\d+', '', tt_)
            link = _lucu['href']
            out += f"➣ <a href='{link}'>{_tt}</a>\n"
            if len(out) > 1000:
                break
            await event.edit(out, parse_mode="html")
            
@register(outgoing=True, pattern=r"^\.wb ?(.*)")
async def _neonime(event):
    await event.edit('`please wait...`')
    url = 'https://wibudesu.com/'
    ht_ = requests.get(url).text
    _bs = bs(ht_, "html.parser")
    bd_ = _bs.findAll('h2', class_='episodeye')
    out = "<b>➲ Wibudesu > New Batch:</b>\n═════════════════\n"
    for kntl_ in bd_:
        _lucu = kntl_.find('a')
        if not _lucu:
            _lucu = 'none'
        else:  # FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
            tt_ = _lucu.get_text()
            _tt = re.sub(r'\s+Subtitle\s+Indonesia\s+Season.\d+', '', tt_)
            link = _lucu['href']
            out += f"➣ <a href='{link}'>{_tt}</a>\n"
            if len(out) > 1000:
                break
            await event.edit(out, parse_mode="html")


@register(outgoing=True, pattern=r"^\.nk ?(.*)")
async def _neonime(event):
    await event.edit('`please wait...`')
    url = 'https://nekonime.vip/'
    ht_ = requests.get(url).text
    _bs = bs(ht_, "html.parser")
    bd_ = _bs.findAll('div', class_='col-md-4 col-sm-4')
    out = "<b>➲ Nekonime > New Episode:</b>\n═════════════════\n"
    for kntl_ in bd_:
        _lucu = kntl_.find('a')
        if not _lucu:
            _lucu = 'none'
        else:  # FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
            tt_ = _lucu.get_text()
            _tt = re.sub(r'\s+Subtitle\s+Indonesia\s+Season.\d+', '', tt_)
            link = _lucu['href']
            out += f"➣ <a href='{link}'>{_tt}</a>\n"
            
            await event.edit(out, parse_mode="html")


@register(outgoing=True, pattern=r"^\.sm ?(.*)")
async def _neonime(event):
    await event.edit('`please wait...`')
    url = 'https://samehadaku.vip/'
    ht_ = requests.get(url).text
    _bs = bs(ht_, "html.parser")
    bd_ = _bs.findAll('div', class_='animposx')
    out = "<b>➲ Samehadaku > New Episode:</b>\n═════════════════\n"
    for kntl_ in bd_:
        _lucu = kntl_.find('a')
        if not _lucu:
            _lucu = 'none'
        else:  # FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
            tt_ = _lucu.get_text()
            _tt = re.sub(r'\s+TV\s+Ongoing\s+Season.\d+', '', tt_)
            link = _lucu['href']
            out += f"➣ <a href='{link}'>{_tt}</a>\n"
            if len(out) > 1000:
                break
            await event.edit(out, parse_mode="html")
            
            
@register(outgoing=True, pattern=r"^\.mal ?(.*)")
async def _neonime(event):
    await event.edit('`please wait...`')
    url = 'https://myanimelist.net/news'
    ht_ = requests.get(url).text
    _bs = bs(ht_, "html.parser")
    bd_ = _bs.findAll('div', class_='news-list mt16 mr8')
    out = "<b>➲ Jurnal Otaku > New Information:</b>\n═════════════════\n"
    for kntl_ in bd_:
        _lucu = kntl_.find('a')
        if not _lucu:
            _lucu = 'none'
        else:  # FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
            tt_ = _lucu.get_text()
            _tt = re.sub(r'\s+TV\s+Ongoing\s+Season.\d+', '', tt_)
            link = _lucu['href']
            judul = _lucu['alt']
            out += f"➣ <a href='{link}'>{_tt}</a>\n"
            if len(out) > 1000:
                break
            await event.edit(out, parse_mode="html")


def get_html(url):
    tag_li = []
    req = requests.get(url)
    res = bs(req.text, "html.parser")
    box = res.find("div", class_="sbox").parent.find_all("li")
    if len(box) != 0:
        for clear in box:
            if clear.get_text() == 'MP4':
                box.remove(clear)
            elif clear.get_text() == 'MKV':
                box.remove(clear)
            else:
                pass
    for box_ in box:
        tag_li.append(box_)
    return {
        "html": tag_li
    }


def link_download(query, url):
    tag_label = []
    tag_href = []
    r = get_html(url)["html"]
    for k, v in enumerate(r[query].find_all("a")):
        tag_href.append({"server": v.get_text(strip=True), "link": v["href"]})
    for p, o in enumerate(r[query].find_all("label")):
        tag_label.append(o.get_text())
    return {
        "label": tag_label,
        "url": tag_href
    }


@register(outgoing=True, pattern=r"^\.nl ?(.*)")
async def _(event):
    url = event.pattern_match.group(1)
    if not url:
        await event.edit("Enter your episode url, see .help neonime")
    elif 'https://' not in url:
        await event.edit('Enter url')
        return
    else:
        await event.edit("`please wait..`")
        msg = "<b>➲ Link Download:</b>\n═════════════════\n"
        p = link_download(1, url)
        for label_name in p["label"]:
            msg += f"<b>↛ {label_name} ↚</b>\n"
        for server_link in p["url"]:
            server_name = server_link["server"]
            server_url = server_link["link"]
            msg += f"➣ <a href='{server_url}'>{server_name}</a>\n"

        p = link_download(2, url)
        for label_name in p["label"]:
            msg += f"\n<b>↛ {label_name} ↚</b>\n"
        for server_link in p["url"]:
            server_name = server_link["server"]
            server_url = server_link["link"]
            msg += f"➣ <a href='{server_url}'>{server_name}</a>\n"

        p = link_download(3, url)
        for label_name in p["label"]:
            msg += f"\n<b>↛ {label_name} ↚</b>\n"
        for server_link in p["url"]:
            server_name = server_link["server"]
            server_url = server_link["link"]
            msg += f"➣ <a href='{server_url}'>{server_name}</a>\n"

        p = link_download(4, url)
        for label_name in p["label"]:
            msg += f"\n<b>↛ {label_name} ↚</b>\n"
        for server_link in p["url"]:
            server_name = server_link["server"]
            server_url = server_link["link"]
            msg += f"➣ <a href='{server_url}'>{server_name}</a>\n"

        p = link_download(5, url)
        for label_name in p["label"]:
            msg += f"\n<b>↛ {label_name} ↚</b>\n"
        for server_link in p["url"]:
            server_name = server_link["server"]
            server_url = server_link["link"]
            msg += f"➣ <a href='{server_url}'>{server_name}</a>\n"

        p = link_download(6, url)
        for label_name in p["label"]:
            msg += f"\n<b>↛ {label_name} ↚</b>\n"
        for server_link in p["url"]:
            server_name = server_link["server"]
            server_url = server_link["link"]
            msg += f"➣ <a href='{server_url}'>{server_name}</a>\n"

        p = link_download(7, url)
        for label_name in p["label"]:
            msg += f"\n<b>↛ {label_name} ↚</b>\n"
        for server_link in p["url"]:
            server_name = server_link["server"]
            server_url = server_link["link"]
            msg += f"➣ <a href='{server_url}'>{server_name}</a>\n"

        p = link_download(8, url)
        for label_name in p["label"]:
            msg += f"\n<b>↛ {label_name} ↚</b>\n"
        for server_link in p["url"]:
            server_name = server_link["server"]
            server_url = server_link["link"]
            msg += f"➣ <a href='{server_url}'>{server_name}</a>\n"
        await event.edit(msg, parse_mode="html")


CMD_HELP.update({"neonime": "**neonime**"
                 "\n >`.neo`"
                 "\n  Usage: See Last Update."
                 "\n >`.nl` <`url episode`>"
                 "\n  Usage: Cari link download, Copy url episode dari `.neo` "
                 "\n Others : .ks | .nk | .sm | .mal | .wb"
})
