messages = []
message = {}
message["userName"] = "Rusal"
message["timeStamp"] = "19:12 12.10.2022"
message["text"] = "Привет"
message["sex"] = "male"
messages.append(message)
message = {}
message["userName"] = "Рита"
message["timeStamp"] = "19:13 12.10.2022"
message["text"] = "Добрый вечер"
messages.append(message)
message = {}
message["userName"] = "Rusal"
message["timeStamp"] = "19:14 12.10.2022"
message["text"] = "Правда что препод душный?"
messages.append(message)
message = {}
message["userName"] = "Рита"
message["timeStamp"] = "19:14 12.10.2022"
message["text"] = "Нет пока всё нормально"
messages.append(message)
print(messages)
for item in messages:
    print(f"{item['timeStamp']}-<{item['userName']}>: {item['text']}")