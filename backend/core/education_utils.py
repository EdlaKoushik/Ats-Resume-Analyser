#education_utils.py
EDU_NORMALIZATION = {
    "btech": "bachelor",
    "b.tech": "bachelor",
    "be": "bachelor",
    "b.e": "bachelor",
    "bachelor": "bachelor",
    "ug": "bachelor",

    "mtech": "master",
    "m.tech": "master",
    "me": "master",
    "m.e": "master",
    "master": "master",
    "pg": "master",
}


def normalize_education(text: str) -> set:
    text = text.lower()
    found = set()

    for key, normalized in EDU_NORMALIZATION.items():
        if key in text:
            found.add(normalized)

    return found
