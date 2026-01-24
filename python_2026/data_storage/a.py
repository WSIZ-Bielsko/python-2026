import json

from python_2026.data_storage.basics import Message

if __name__ == '__main__':
    messages = []
    with open('support.json', "r", encoding="utf-8") as f:
        ln = f.readline()
        # ...
        dd = json.loads(ln)
        for d in dd:
            messages.append(Message(**d))

    print(messages)
