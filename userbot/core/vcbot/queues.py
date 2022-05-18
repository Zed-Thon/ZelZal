# Zed - UserBot
# Copyright (c) 2022 ZelZal
# Credits: @Zed-Thon || https://github.com/Zed-Thon
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# t.me/zzzzl1l & t.me/Zed-Thon

QUEUE = {}


def add_to_queue(chat_id, songname, link, ref, type, quality):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append([songname, link, ref, type, quality])
        return int(len(chat_queue) - 1)
    QUEUE[chat_id] = [[songname, link, ref, type, quality]]


def get_queue(chat_id):
    if chat_id in QUEUE:
        return QUEUE[chat_id]
    return 0


def pop_an_item(chat_id):
    if chat_id not in QUEUE:
        return 0

    chat_queue = QUEUE[chat_id]
    chat_queue.pop(0)
    return 1


def clear_queue(chat_id: int):
    if chat_id not in QUEUE:
        return 0

    QUEUE.pop(chat_id)
    return 1
