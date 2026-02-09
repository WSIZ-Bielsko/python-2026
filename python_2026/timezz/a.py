import sys
from datetime import datetime, timedelta, UTC
from zoneinfo import ZoneInfo

from loguru import logger

logger.remove()
logger.add(level='DEBUG',sink=sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss!UTC} | {level} | {message}")

if __name__ == '__main__':
    t1 = datetime.now(tz=ZoneInfo('Europe/Warsaw'))
    t1 = datetime.now()
    print(t1)
    print(t1.year)
    print(t1.month)
    print(t1.day)
    print(t1.hour)
    print(t1.minute)
    print(t1.second)
    print(t1.microsecond)

    print(t1.tzinfo)
    if t1.tzinfo is None:
        logger.warning('t1.tzinfo is None')

    logger.info('starting loop around time zone change ')

    tz = datetime(year=2026, month=3, day=29, hour=1, minute=0, second=0,tzinfo=ZoneInfo('Europe/Warsaw'))
    uz = datetime(year=2026, month=3, day=29, hour=1, minute=0, second=0,tzinfo=UTC)
    logger.info(f'tz={tz}, uz={uz}')

    ptz = tz
    puz = uz
    for _ in range(30):
        logger.debug(f'iteration {_}')
        tz = tz + timedelta(minutes=30)
        uz = uz + timedelta(minutes=30)
        print(tz, tz.astimezone(UTC),  uz)
        print(f'diff1={tz-ptz}, diff2={uz-puz}')
        ptz = tz
        puz = uz

