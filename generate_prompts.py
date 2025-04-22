import datetime
import random


BASE_PROMPT = (
    "I'm trying to decide what workout to do tomorrow. {}"
    " my preferences: {}. options: {}"
)
SLEEP = "I don't want to wake up too early"
STRUCTURE = "I prefer fitness classes over solo activities like running or swimming laps because i tend to procrastinate starting the latter"
FOCUS = "intense cardio (running & cycling) are better for focus and stress relief"
VARIETY = "i like to vary my exercises day to day"
EFFICIENT = "i prefer to be done with my workout and shower by 9:30am on weekdays"
PREFERENCES = [SLEEP, STRUCTURE, FOCUS, VARIETY, EFFICIENT]
choices_constant = [
    ("swim laps @ YMCA", "20m", "~8am"),
    ("run @ home", "0m", "~8am"),
    ("lift weights @ home", "0m", "~8am"),
    ("peloton spin workout @ home", "0m", "~8am"),
]
choices_schedule = []
WEDNESDAY_OPTIONS = [
    ("Cycling @ SoulCycle · Financial District", "30 min", "7:00 AM"),
    (
        "Gym Time @ Retro Fitness · One New York Plaza Financial District",
        "30 min",
        "7:00 AM",
    ),
    ("Gym Time @ RS Strength", "40 min", "7:00 AM"),
    ("Yoga @ ID Hot Yoga - Lower East Side Lower East Side", "40 min", "7:00 AM"),
    ("Cycling @ SoulCycle · Williamsburg", "50 min", "7:00 AM"),
    ("Yoga @ VERAYOGA · Williamsburg", "50 min", "7:00 AM"),
    ("Yoga @ Sui Yoga · Soho SoHo", "40 min", "7:00 AM"),
    ("Cycling @ CycleBar · NoHo NoHo", "40 min", "7:00 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Williamsburg Williamsburg",
        "50 min",
        "7:00 AM",
    ),
    ("Gym Time @ Crunch Gym · Union Square Union Square", "35 min", "7:00 AM"),
    ("Cycling @ SoulCycle · Brooklyn Heights", "20 min", "7:30 AM"),
    ("Yoga @ Brooklyn Yoga Project Carroll Gardens", "40 min", "7:30 AM"),
    ("Running @ Mile High Run Club · Noho NoHo", "40 min", "7:30 AM"),
    ("Yoga @ Bouldering Project", "30 min", "7:45 AM"),
    ("Yoga @ VERAYOGA (Tribeca) Tribeca", "35 min", "7:50 AM"),
    (
        "Gym Time @ Retro Fitness · One New York Plaza Financial District",
        "30 min",
        "8:00 AM",
    ),
    ("Gym Time @ Crunch Gym · FiDi Financial District", "30 min", "8:00 AM"),
    ("Cycling @ SoulCycle · Williamsburg", "50 min", "8:00 AM"),
    ("Yoga @ Sui Yoga · Soho SoHo", "40 min", "8:00 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Williamsburg Williamsburg",
        "50 min",
        "8:00 AM",
    ),
    ("Yoga @ Y7 Studio · Park Slope Manhattan", "20 min", "8:15 AM"),
    ("Cycling @ CycleBar · NoHo NoHo", "40 min", "8:15 AM"),
    ("Running @ Barry's · Brooklyn Heights Strength Training,", "22 min", "8:30 AM"),
    ("Cycling @ SoulCycle · Brooklyn Heights", "20 min", "8:30 AM"),
    ("Gym Time @ RS Strength", "40 min", "8:30 AM"),
    ("Yoga @ ID Hot Yoga - Lower East Side Lower East Side", "40 min", "8:30 AM"),
    ("Running @ Mile High Run Club · Noho NoHo", "40 min", "8:30 AM"),
]

MONDAY_OPTIONS = [
    ("Gym Time @ Crunch Gym · FiDi  Financial District", "30 min", "9:00 AM"),
    ("Gym Time @ Crunch Gym · FiDi  Financial District", "30 min", "7:00 AM"),
    ("Gym Time @ Crunch Gym · FiDi  Financial District", "30 min", "8:00 AM"),
    (
        "Gym Time @ Retro Fitness · One New York Plaza  Financial District",
        "30 min",
        "8:00 AM",
    ),
    (
        "Gym Time @ Retro Fitness · One New York Plaza  Financial District",
        "30 min",
        "7:00 AM",
    ),
    ("Dance @ 305 Fitness · Williamsburg NYC", "40 min", "7:30 AM"),
    ("Gym Time @ RS Strength", "40 min", "7:00 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Cobble Hill  Cobble Hill",
        "30 min",
        "9:00 AM",
    ),
    ("Yoga @ Bouldering Project", "30 min", "7:45 AM"),
    ("Running @ Barry's · Brooklyn Heights  Strength Training,", "22 min", "8:30 AM"),
    (
        "Gym Time @ Retro Fitness · One New York Plaza  Financial District",
        "30 min",
        "9:00 AM",
    ),
    ("Yoga @ Y7 Studio · Park Slope  Manhattan", "20 min", "8:15 AM"),
    ("Cycling @ SoulCycle · Brooklyn Heights", "20 min", "8:30 AM"),
    ("Yoga @ Bouldering Project", "30 min", "9:00 AM"),
    ("Cycling @ SoulCycle · Financial District", "30 min", "7:00 AM"),
    ("Yoga @ Brooklyn Yoga Project  Carroll Gardens", "40 min", "7:30 AM"),
    ("Gym Time @ RS Strength", "40 min", "8:30 AM"),
]
SATURDAY_OPTIONS = [
    (
        "Barre @ The Bar Method · Brooklyn - Williamsburg  Williamsburg",
        "50 min",
        "10:00 AM",
    ),
    ("Cycling @ SoulCycle · Williamsburg", "50 min", "11:00 AM"),
    ("Gym Time @ RS Strength", "40 min", "9:30 AM"),
    ("Cycling @ SoulCycle · Financial District", "30 min", "9:30 AM"),
    ("Cycling @ BYKlyn  Gowanus", "20 min", "11:30 AM"),
    ("Dance @ 305 Fitness · Williamsburg NYC", "40 min", "9:00 AM"),
    ("Gym Time @ Crunch Gym · FiDi  Financial District", "30 min", "10:00 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Williamsburg  Williamsburg",
        "50 min",
        "8:00 AM",
    ),
    ("Cycling @ SoulCycle · Williamsburg", "50 min", "8:30 AM"),
    (
        "Gym Time @ Retro Fitness · One New York Plaza  Financial District",
        "30 min",
        "8:00 AM",
    ),
    ("Gym Time @ RS Strength", "40 min", "11:00 AM"),
    ("Cycling @ BYKlyn  Gowanus", "20 min", "10:15 AM"),
    ("Gym Time @ RS Strength", "40 min", "8:00 AM"),
    ("Dance @ 305 Fitness · Williamsburg NYC", "40 min", "11:00 AM"),
    ("Cycling @ SoulCycle · Financial District", "30 min", "10:45 AM"),
    ("Yoga @ VERAYOGA · Williamsburg", "50 min", "9:00 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Cobble Hill  Cobble Hill",
        "30 min",
        "11:00 AM",
    ),
    ("Cycling @ SoulCycle · Brooklyn Heights", "20 min", "8:30 AM"),
    ("Yoga @ Bouldering Project", "30 min", "10:30 AM"),
    ("Running @ Barry's · Brooklyn Heights  Strength Training,", "22 min", "7:00 AM"),
    ("Cycling @ BYKlyn  Gowanus", "20 min", "9:00 AM"),
    ("Running @ Action Black · Tribeca", "40 min", "8:30 AM"),
    ("Cycling @ Elite Fitness Studio  Carroll Gardens", "45 min", "10:15 AM"),
    ("Yoga @ ID Hot Yoga - Lower East Side  Lower East Side", "40 min", "8:00 AM"),
    ("Dance @ 305 Fitness · Williamsburg NYC", "40 min", "10:00 AM"),
    ("Yoga @ VERAYOGA (Tribeca)  Tribeca", "35 min", "10:15 AM"),
    ("Gym Time @ Crunch Gym · FiDi  Financial District", "30 min", "8:00 AM"),
]
SUNDAY_OPTIONS = [
    ("megaformer @ form50", "50m", "9:30am"),
    ("megaformer @ form50", "50m", "8:20am"),
    ("megaformer @ form50", "50m", "10:40am"),
    (
        "Barre @ The Bar Method · Brooklyn - Cobble Hill Cobble Hill",
        "30 min",
        "8:00 AM",
    ),
    ("Yoga @ ID Hot Yoga - Lower East Side Lower East Side", "40 min", "8:00 AM"),
    ("Cycling @ SoulCycle · Williamsburg", "50 min", "8:30 AM"),
    ("Yoga @ Sui Yoga · Soho SoHo", "40 min", "8:30 AM"),
    ("Yoga @ Y7 Studio · Park Slope Manhattan", "20 min", "9:00 AM"),
    ("Gym Time @ Crunch Gym · FiDi Financial District", "30 min", "9:00 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Williamsburg Williamsburg",
        "50 min",
        "9:00 AM",
    ),
    ("Running @ Mile High Run Club · Noho NoHo", "40 min", "9:00 AM"),
    ("Yoga @ Sui Yoga · Soho SoHo", "40 min", "9:00 AM"),
    ("Cycling @ CycleBar · NoHo NoHo", "40 min", "9:00 AM"),
    ("Cycling @ SoulCycle · Brooklyn Heights", "20 min", "9:30 AM"),
    ("Yoga @ The Bar Method · Brooklyn - Cobble Hill Cobble Hill", "30 min", "9:30 AM"),
    ("Cycling @ SoulCycle · Financial District", "30 min", "9:30 AM"),
    ("Cycling @ SoulCycle · Williamsburg", "50 min", "9:30 AM"),
    ("Dance @ 305 Fitness · Williamsburg NYC", "40 min", "10:00 AM"),
    ("Yoga @ Elite Fitness Studio Carroll Gardens", "45 min", "10:00 AM"),
    ("Yoga @ ID Hot Yoga - FIDI", "30 min", "10:00 AM"),
    ("Yoga @ ID Hot Yoga - Lower East Side Lower East Side", "40 min", "10:00 AM"),
    ("Cycling @ CycleBar · NoHo NoHo", "40 min", "10:00 AM"),
    ("Pilates @ BYKlyn Gowanus", "20 min", "10:15 AM"),
    ("Cycling @ BYKlyn Gowanus", "20 min", "10:15 AM"),
    ("Yoga @ Y7 Studio · Park Slope Manhattan", "20 min", "10:15 AM"),
    ("Yoga @ VERAYOGA · Williamsburg", "50 min", "10:15 AM"),
    ("Running @ Mile High Run Club · Noho NoHo", "40 min", "10:15 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Cobble Hill Cobble Hill",
        "30 min",
        "10:30 AM",
    ),
    ("Yoga @ Bouldering Project", "30 min", "10:30 AM"),
    ("Yoga @ Sui Yoga · Soho SoHo", "40 min", "10:30 AM"),
    ("Cycling @ SoulCycle · Brooklyn Heights", "20 min", "10:45 AM"),
    ("Cycling @ SoulCycle · Financial District", "30 min", "10:45 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Cobble Hill Cobble Hill",
        "30 min",
        "11:00 AM",
    ),
    ("Dance @ 305 Fitness · Williamsburg NYC", "40 min", "11:00 AM"),
    ("Cycling @ SoulCycle · Williamsburg", "50 min", "11:00 AM"),
    ("Running @ Action Black · Tribeca", "40 min", "11:00 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Williamsburg Williamsburg",
        "50 min",
        "11:00 AM",
    ),
    ("Yoga @ Sui Yoga · Soho SoHo", "40 min", "11:00 AM"),
    ("Cycling @ CycleBar · NoHo NoHo", "40 min", "11:00 AM"),
    ("Running @ Mile High Run Club · Noho NoHo", "40 min", "11:15 AM"),
    ("Cycling @ BYKlyn Gowanus", "20 min", "11:30 AM"),
    ("Yoga @ Y7 Studio · Park Slope Manhattan", "20 min", "11:30 AM"),
    ("Yoga @ VERAYOGA (Tribeca) Tribeca", "35 min", "11:30 AM"),
    ("Cycling @ SoulCycle · Brooklyn Heights", "20 min", "11:45 AM"),
    ("Cycling @ SoulCycle · Financial District", "30 min", "11:45 AM"),
    ("Dance @ 305 Fitness · Williamsburg NYC", "40 min", "12:00 PM"),
    ("Yoga @ Bouldering Project", "30 min", "12:00 PM"),
    ("Yoga @ ID Hot Yoga - FIDI", "30 min", "12:00 PM"),
    ("Yoga @ ID Hot Yoga - Lower East Side Lower East Side", "40 min", "12:00 PM"),
    (
        "Barre @ The Bar Method · Brooklyn - Williamsburg Williamsburg",
        "50 min",
        "12:00 PM",
    ),
    ("Yoga @ Sui Yoga · Soho SoHo", "40 min", "12:00 PM"),
    ("Cycling @ CycleBar · NoHo NoHo", "40 min", "12:00 PM"),
]

TUESDAY_OPTIONS = [
    ("Yoga @ Brooklyn Yoga Project Carroll Gardens", "40 min", "7:30 AM"),
    ("Strength Training @ Elite Fitness Studio Carroll Gardens", "45 min", "7:30 AM"),
    ("Running @ Action Black · Tribeca", "40 min", "7:30 AM"),
    ("Yoga @ Bouldering Project", "30 min", "7:45 AM"),
    ("Yoga @ VERAYOGA (Tribeca) Tribeca", "35 min", "7:50 AM"),
    ("Strength Training @ BYKlyn Gowanus", "20 min", "8:00 AM"),
    (
        "Gym Time @ Retro Fitness · One New York Plaza Financial District",
        "30 min",
        "8:00 AM",
    ),
    ("Cycling @ SoulCycle · Financial District", "30 min", "8:00 AM"),
    ("Yoga @ Crunch Gym · FiDi Financial District", "30 min", "8:00 AM"),
    ("Gym Time @ Crunch Gym · FiDi Financial District", "30 min", "8:00 AM"),
    ("Dance @ 305 Fitness · Williamsburg NYC", "40 min", "8:00 AM"),
    ("Cycling @ SoulCycle · Williamsburg", "50 min", "8:00 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Williamsburg Williamsburg",
        "50 min",
        "8:00 AM",
    ),
    ("Running @ Barry's · Brooklyn Heights Strength Training,", "22 min", "8:30 AM"),
    ("Strength Training @ Elite Fitness Studio Carroll Gardens", "45 min", "8:30 AM"),
    ("Gym Time @ RS Strength", "40 min", "8:30 AM"),
    ("Yoga @ ID Hot Yoga - Lower East Side Lower East Side", "40 min", "8:30 AM"),
    ("Yoga @ VERAYOGA · Williamsburg", "50 min", "8:30 AM"),
    ("Strength Training @ Action Black · Tribeca", "40 min", "8:45 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Cobble Hill Cobble Hill",
        "30 min",
        "9:00 AM",
    ),
    ("Yoga @ Bouldering Project", "30 min", "9:00 AM"),
    (
        "Gym Time @ Retro Fitness · One New York Plaza Financial District",
        "30 min",
        "9:00 AM",
    ),
    (
        "Barre @ The Bar Method · Brooklyn - Williamsburg Williamsburg",
        "50 min",
        "9:00 AM",
    ),
    ("Cycling @ BYKlyn Gowanus", "20 min", "9:15 AM"),
    ("Cycling @ SoulCycle · Brooklyn Heights", "20 min", "9:30 AM"),
    (
        "Barre @ The Bar Method · Brooklyn - Cobble Hill Cobble Hill",
        "30 min",
        "9:30 AM",
    ),
    ("Yoga @ Brooklyn Yoga Project Carroll Gardens", "40 min", "9:30 AM"),
    ("Pilates @ Elite Fitness Studio Carroll Gardens", "45 min", "9:30 AM"),
    ("Cycling @ SoulCycle · Williamsburg", "50 min", "9:30 AM"),
    ("Running @ Barry's · Brooklyn Heights Strength Training,", "22 min", "9:40 AM"),
    (
        "Gym Time @ Retro Fitness · One New York Plaza Financial District",
        "30 min",
        "10:00 AM",
    ),
    ("Gym Time @ RS Strength", "40 min", "10:00 AM"),
    ("Yoga @ ID Hot Yoga - FIDI", "30 min", "10:00 AM"),
    ("Gym Time @ Crunch Gym · FiDi Financial District", "30 min", "10:00 AM"),
    ("Yoga @ ID Hot Yoga - Lower East Side Lower East Side", "40 min", "10:00 AM"),
]

weekday_cache = {
    "Monday": MONDAY_OPTIONS,
    "Saturday": SATURDAY_OPTIONS,
    "Sunday": SUNDAY_OPTIONS,
    "Tuesday": TUESDAY_OPTIONS,
    "Wednesday": WEDNESDAY_OPTIONS,
}
lookup_weekday_dt = datetime.datetime.now().date() + datetime.timedelta(days=1)
weekday_key = lookup_weekday_dt.strftime("%A")
if weekday_key in weekday_cache:
    choices_schedule = weekday_cache[weekday_key]


choices = choices_constant + choices_schedule
random.shuffle(choices)
prev_workouts = """4/8/25: cycling
4/18/25: a run
4/14/25: cycling
4/15/25: cycling
4/19/25: lifting
4/17/25: a run
4/20/25: megaformer pilates
4/21/25: cycling
4/7/25: hot yoga
4/9/25: hot yoga
4/16/25: hot yoga
4/22/25: bootcamp
4/10/25: a run
4/6/25: run & lift
4/11/25: cycling
4/5/25: barre"""
workout_dates = {}
for entry in prev_workouts.split("\n"):
    date, workout = entry.strip().split(": ")
    entry_dt = datetime.datetime.strptime(date, "%m/%d/%y").date()
    workout_dates[entry_dt] = workout
three_days = []
for relative_day in [0, 1, 2]:
    relative_dt = datetime.datetime.now().date() - datetime.timedelta(days=relative_day)
    weekday = relative_dt.strftime("%A")
    if relative_dt in workout_dates:
        three_days.append((weekday, workout_dates[relative_dt]))
    else:
        three_days.append((weekday, "nothing"))

today = "today ({}) I did {}.".format(three_days[0][0], three_days[0][1])
yesterday = " yesterday ({}) I did {}.".format(three_days[1][0], three_days[1][1])
day_before = " the day before ({}) I did {}.".format(three_days[2][0], three_days[2][1])

prev_workouts = today + yesterday + day_before

choice_descs = ""
comma = ""
for name, distance, time in choices:
    choice_descs += comma + f"{name} at {time} {distance} away"
    comma = ", "

random.shuffle(PREFERENCES)



def get_prompt():
    return BASE_PROMPT.format(prev_workouts, ", ".join(PREFERENCES), choice_descs)
