import operator
import re
from datetime import datetime

with open('input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

class Event(object):
    pass

class Guard(object):
    pass

def parse_input():
    events = []
    for line in data:
        m = re.match(r'^\[(.+)\]\s(.+)$', line)
        e = Event()
        e.timestamp = datetime.strptime(m.group(1), '%Y-%m-%d %H:%M')
        e.text = m.group(2)
        events.append(e)
    events.sort(key=lambda e: e.timestamp)
    return events

def create_schedule(events):
    schedule = {}
    guard_id = None
    for e in events:
        date = e.timestamp.date()
        if date not in schedule:
            guard = Guard()
            guard.id = None
            guard.asleep = [0] * 60
            schedule[date] = guard
        else:
            guard = schedule[date]

        if 'begins shift' in e.text:
            m = re.match(r'Guard #(\d+) begins shift', e.text)
            guard_id = int(m.group(1)) # ID might be for today or next day (before or after midnight)
        elif 'falls asleep' in e.text:
            guard.asleep[e.timestamp.time().minute] = 1
            guard.id = guard_id # Now set ID, all sleeps are between 00:00 and 00:59
        elif 'wakes up' in e.text:
            last_idx = len(guard.asleep) - 1 - guard.asleep[::-1].index(1)
            idx = e.timestamp.time().minute
            guard.asleep[last_idx:idx] = [1] * (idx - last_idx)

    return schedule

def calc_guard_most_minutes_asleep_total(schedule):
    sleep_schedule = {}
    for date, guard in schedule.items():
        minutes_asleep = len([x for x in guard.asleep if x == 1])
        if guard.id not in sleep_schedule:
            sleep_schedule[guard.id] = 0
        sleep_schedule[guard.id] += minutes_asleep

    guard_id, minutes_asleep = max(sleep_schedule.items(), key=operator.itemgetter(1))
    return guard_id, minutes_asleep

def calc_minute_most_asleep(schedule, guard_id, minutes_asleep):
    asleep_total = [0] * 60
    for date, guard in schedule.items():
        if guard.id == guard_id:
            asleep_total = [x + y for x, y in zip(guard.asleep, asleep_total)]

    minute_most_asleep = asleep_total.index(max(asleep_total))
    return minute_most_asleep

def calc_guard_most_freq_asleep_same_minute(schedule):
    asleep_total_by_guard = {}
    for date, guard in schedule.items():
        if guard.id not in asleep_total_by_guard:
            asleep_total_by_guard[guard.id] = [0] * 60
        asleep_total_by_guard[guard.id] = [x + y for x, y in zip(guard.asleep, asleep_total_by_guard[guard.id])]

    highscore_max = 0
    highscore_guard_id = None
    for guard_id, score in asleep_total_by_guard.items():
        highscore = max(score)
        if highscore > highscore_max:
            highscore_max = highscore
            highscore_guard_id = guard_id

    most_freq_asleep_minute = asleep_total_by_guard[highscore_guard_id].index(highscore_max)
    return highscore_guard_id, most_freq_asleep_minute

events = parse_input()
schedule = create_schedule(events)
guard_id, minutes_asleep = calc_guard_most_minutes_asleep_total(schedule)
minute_most_asleep = calc_minute_most_asleep(schedule, guard_id, minutes_asleep)
print('Part 1:', guard_id * minute_most_asleep)

guard_id, most_freq_asleep_minute = calc_guard_most_freq_asleep_same_minute(schedule)
print('Part 2:', guard_id * most_freq_asleep_minute)
