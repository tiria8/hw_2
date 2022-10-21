import json

"""
- `load_candidates_from_json(path)` – возвращает список всех кандидатов
- `get_candidate(candidate_id)` – возвращает одного кандидата по его id
- `get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
- `get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку
"""

def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

def get_candidate(candidate_id, path):
    data = load_candidates_from_json(path)
    candidate = data[candidate_id-1]
    return candidate

def get_candidates_by_name(candidate_name, path):
    data = load_candidates_from_json(path)
    candidates = []
    for candidate in data:
        if candidate_name.lower() in candidate['name'].lower():
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill_name, path):
    data = load_candidates_from_json(path)
    candidates = []
    for candidate in data:
        if skill_name.lower() in candidate["skills"].lower().split(', '):
            candidates.append(candidate)
    return candidates


