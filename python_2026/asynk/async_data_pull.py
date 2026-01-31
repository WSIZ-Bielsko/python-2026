from asyncio import run, create_task, gather

import httpx
from loguru import logger
from pydantic import BaseModel

from python_2026.common import ts


class ToDoItem(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool


BASE_URL = "https://jsonplaceholder.typicode.com"


async def get_todo_item(item_number: int) -> ToDoItem:
    logger.info(f"pulling {item_number}")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/todos/{item_number}")
        return ToDoItem(**response.json())


async def fast_fetch(client, item_number: int) -> ToDoItem:
    response = await client.get(f"{BASE_URL}/todos/{item_number}")
    return ToDoItem(**response.json())


async def pull_todos_fast(items: list[int]) -> list[ToDoItem]:
    res = []
    for item in items:
        res.append(create_task(get_todo_item(item)))
    await gather(*res)
    res = [r.result() for r in res]
    # 19 requests/second
    return res


async def pull_todos_fastest(items: list[int]) -> list[ToDoItem]:
    res = []
    async with httpx.AsyncClient() as client:
        for item in items:
            res.append(create_task(fast_fetch(client, item)))
        await gather(*res)
    res = [r.result() for r in res]
    # 27 requests/second
    return res


async def main():
    logger.info('in main')
    st = ts()
    # val = await get_todo_item(8)
    items = await pull_todos_fastest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    en = ts()
    items_per_second = len(items) / (en - st)
    logger.info(f"items_per_second: {items_per_second:.2f}")
    for v in items:
        logger.debug(f'item: {v}')


if __name__ == '__main__':
    run(main())
