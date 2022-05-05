import sys
import logging
from pysitemap import crawler
from asyncio import events, windows_events


if __name__ == '__main__':
    if '--iocp' in sys.argv:
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)

    root_url = 'https://stackoverflow.com'
    crawler(root_url, out_file= 'stackoverflow.xml', exclude_urls=[".pdf", ".jpg", ".zip"])
