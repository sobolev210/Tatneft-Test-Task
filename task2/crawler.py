import os
import asyncio
from datetime import datetime

import aiofiles
from aiohttp import ClientSession, ClientConnectionError, ClientResponseError


class PageRequestException(Exception):
    pass


async def add_entry_to_crawling_history(page_url: str, result_message: str = "Success", additional_content: str = ""):
    entry = (f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
             f"Page url: {page_url}\nResult: {result_message}\n{additional_content}\n")
    async with aiofiles.open("crawling_history.txt", "a") as f:
        await f.write(entry)


async def fetch_page_content(page_url: str, session: ClientSession) -> str:
    try:
        async with session.get(page_url, raise_for_status=True) as resp:
            return await resp.text()
    except ClientConnectionError as e:
        raise PageRequestException(f"Connection error: {e}")
    except ClientResponseError as e:
        raise PageRequestException(f"Unsuccessful status code. Status: {e.status}. Request info: {e.request_info}")


async def write_page_content_to_disk(page_url: str, page_content: str):
    page_url_hash = hash(page_url)
    filename = f"page_{hash(page_url)}.html" if page_url_hash > 0 else f"page_n{abs(hash(page_url))}.html"
    async with aiofiles.open(os.path.join("pages", filename), "w") as f:
        await f.write(page_content)
    await add_entry_to_crawling_history(page_url, additional_content=f"Filename: {filename}\n")


async def load_web_page_to_disk(page_url: str, session: ClientSession):
    try:
        page_content = await fetch_page_content(page_url, session)
    except PageRequestException as e:
        await add_entry_to_crawling_history(page_url, result_message=str(e))
        return
    await write_page_content_to_disk(page_url, page_content)


async def main(pages_urls):
    async with ClientSession() as session:
        await asyncio.gather(*[load_web_page_to_disk(url, session) for url in pages_urls])


if __name__ == "__main__":
    some_pages_urls = [
        "https://random-site_wwertere/recordings/upload",
        "https://fastapi.tiangolo.com/about/",
        "https://en.wikipedia.org/wiki/Cat",
        "https://github.com/",
        "https://fastapi.tiangolo.com/",
        "https://docs.djangoproject.com/en/5.0/",
        # "https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component",
        # "https://pypi.org/project/aiohttp/",
        # "https://docs.aiohttp.org/en/stable/client_quickstart.html",
        # "https://pypi.org/project/aiofiles/",
        # "https://www.coursera.org/career-academy?utm_medium=sem&utm_source=gg&utm_campaign=B2C_EMEA__coursera_FTCOF_career-academy_pmax-multiple-audiences-country-multi&campaignid=20858198824&adgroupid=&device=c&keyword=&matchtype=&network=x&devicemodel=&adposition=&creativeid=&hide_mobile_promo&gad_source=1&gclid=CjwKCAiAibeuBhAAEiwAiXBoJIBPnFdVuOJyDAah4HFptNs4Wh3MzVxX10zwkWSwgwLADxMiYw0UPxoC1tIQAvD_BwE",
        # "https://www.udemy.com/?utm_source=adwords&utm_medium=udemyads&utm_campaign=Generic-Exact_la.EN_cc.ROW&utm_content=deal4584&utm_term=_._ag_86841139896_._ad_535632329484_._kw_online%20training%20free%20courses_._de_c_._dm__._pl__._ti_kwd-296200660279_._li_1028595_._pd__._&matchtype=b&gad_source=1&gclid=CjwKCAiAibeuBhAAEiwAiXBoJBvPewQkfCS-k45t3SX_JnZTCAsPg6CujFsc3tUYA5hLQtTji5TNcRoC2voQAvD_BwE",
        # "https://www.edx.org/",
        # "https://pll.harvard.edu/catalog/free",
        # "https://www.reed.co.uk/courses/",
        # "https://www.futurelearn.com/",
        # "https://www.linkedin.com/learning/",
        # "https://www.domestika.org/en/courses",
        # "https://www.open.edu/openlearn/free-courses",
        # "https://online.stanford.edu/free-courses",
        # "https://ocw.mit.edu/",
        # "https://en.wikipedia.org/wiki/Course_(education)",
        # "https://www.netacad.com/courses/all-courses",
        # "https://nationalcareers.service.gov.uk/find-a-course",

    ]
    asyncio.run(main(some_pages_urls))
