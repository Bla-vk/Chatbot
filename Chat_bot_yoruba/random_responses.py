import random


def random_string():
    random_list = [
        "Jọwọ gbiyanju kikọ nkan diẹ sapejuwe.",
        "Oh! O dabi pe o kọ nkan ti Emi ko loye sibẹsibẹ",
        "Ṣe o lokan lati gbiyanju lati tun pe?",
        "Ma binu gidigidi, emi ko gba iyẹn rara.",
        "Nko le dahun yen sibe, jowo gbiyanju lati beere nkan miran.",
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
