# src/challenges.py
from collections import deque


def count_evidence(evidence: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}

    for item in evidence:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


def first_repeated_id(ids: list[str]) -> str | None:
    seen: set[str] = set()

    for case_id in ids:
        if case_id in seen:
            return case_id
        seen.add(case_id)

    return None


def valid_tags(tags: str) -> bool:
    stack: list[str] = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in tags:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if len(stack) == 0:
                return False

            if stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


def lookup_alias(aliases: dict[str, str], alias: str) -> str | None:
    return aliases.get(alias)


def process_reports(reports: list[str]) -> list[str]:
    queue: deque[str] = deque(reports)
    result: list[str] = []

    while queue:
        result.append(queue.popleft())

    return result


def largest_time_gap(times: list[int]) -> int:
    if len(times) < 2:
        return 0

    sorted_times = sorted(times)
    largest_gap = 0

    for i in range(1, len(sorted_times)):
        gap = sorted_times[i] - sorted_times[i - 1]

        if gap > largest_gap:
            largest_gap = gap

    return largest_gap
