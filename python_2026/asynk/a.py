from asyncio import run, sleep, create_task, gather
from loguru import logger


async def prepare_tea() -> str:
    logger.info('prepare_tea - enter')
    logger.info('prepare_tea - get water')
    await sleep(0.5)
    water_temp = 22
    while water_temp < 90:
        logger.info(f'prepare_tea - warm up water (current temperature is {water_temp})')
        await sleep(0.5)
        water_temp = water_temp + 17
    logger.info(f'prepare_tea - dop tea bag')
    await sleep(1.5)
    logger.info('prepare_tea - complete')
    return f'tea {water_temp}C'


async def prepare_toast() -> str:
    logger.info('prepare_toast - enter')
    await sleep(0.5)
    logger.info('prepare_toast - start-toasting')
    await sleep(0.5)
    logger.info('prepare_toast - complete')
    return 'toast'


async def main():
    logger.info('in main')
    t1 = create_task(prepare_tea())
    t2 = create_task(prepare_toast())

    # while True:
    #     await sleep(0.2)  # oczekiwanie 0.1s = 100ms, w tym czasie program może robić co innego
    #     logger.info('in sleep')
    #     if t1.done() and t2.done():
    #         break
    logger.info('in main - before gather')
    await gather(t1, t2)
    logger.info('in main - after gather')

    logger.info('in main - complete')
    print(t1.result(), t2.result())


if __name__ == '__main__':
    run(main())
