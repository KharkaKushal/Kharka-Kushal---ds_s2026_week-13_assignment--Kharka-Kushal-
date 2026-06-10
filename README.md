[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cm6PS4yt)
# Week 1 Homework: Evidence Desk Patterns

## Student Name

Kharka Kushal

## Summary

This homework practices fundamental data structures and algorithms patterns used in evidence processing:
- **Frequency counting** with dictionaries to count evidence items
- **Duplicate detection** with sets to find first repeated suspect IDs
- **Stack-based validation** with lists to check balanced evidence tags
- **Dictionary lookup** for alias-to-real-name resolution
- Optional challenges: processing reports in order and finding largest time gaps

## How to Run Tests

From the repository root, run:

```bash
pytest -q
```

To run one test file:

```bash
pytest -q tests/test_challenges.py
```

## Required Problems

Complete these functions in `src/challenges.py`:

1. `count_evidence`
2. `first_repeated_id`
3. `valid_tags`
4. `lookup_alias`

## Optional Challenges

These are extra practice unless your instructor tells you otherwise:

1. `process_reports`
2. `largest_time_gap`

Optional tests are skipped by default. To run them, remove the `@pytest.mark.skip(...)` line above the optional test you want to check.

---

# Problem Notes

## 1. Evidence Counter

### Pattern

Frequency Counting / Hash Map Counting

### Data Structure

Dictionary (Hash Map)

### Approach

- Step 1: Initialize an empty dictionary to store counts
- Step 2: Iterate through each evidence item in the input list
- Step 3: For each item, increment its count in the dictionary (or initialize to 1 if not present)

### Complexity

- Time: `O(n)` where n is the number of evidence items
- Space: `O(k)` where k is the number of unique evidence types

Explain briefly:
We use a dictionary to maintain counts of each evidence type. As we iterate through the list, we either increment an existing count or add a new entry. This gives us O(1) average lookup/insertion per item.

### Edge Cases Checked

- [x] Empty list
- [x] One item
- [x] Repeated items
- [x] Different labels
- [x] Case sensitivity

---

## 2. Repeat Suspect ID

### Pattern

Seen Set / Duplicate Detection

### Data Structure

Set (Hash Set)

### Approach

- Step 1: Initialize an empty set to track seen IDs
- Step 2: Iterate through each ID in the input list
- Step 3: If the ID is already in the set, return it immediately (first duplicate); otherwise add it to the set

### Complexity

- Time: `O(n)` where n is the number of IDs
- Space: `O(n)` in worst case (no duplicates)

Explain briefly:
We maintain a set of seen IDs. As we iterate, the first ID we encounter that's already in the set is the first duplicate. Set operations (add/check) are O(1) average.

### Edge Cases Checked

- [x] Empty list
- [x] No repeated IDs
- [x] First two IDs match
- [x] Multiple repeated IDs

---

## 3. Evidence Tag Validator

### Pattern

Stack-based Bracket Matching

### Data Structure

List used as Stack

### Approach

- Step 1: Initialize an empty stack and a mapping of closing to opening brackets
- Step 2: Iterate through each character in the string
- Step 3: If it's an opening bracket, push to stack; if closing, check stack not empty and top matches corresponding opening bracket

### Complexity

- Time: `O(n)` where n is the length of the input string
- Space: `O(n)` in worst case (all opening brackets)

Explain briefly:
We use a stack to track opening brackets. For each closing bracket, we verify it matches the most recent unclosed opening bracket (stack top). Non-bracket characters are ignored. Valid if stack is empty at end.

### Edge Cases Checked

- [x] Empty string
- [x] Correctly nested tags
- [x] Mismatched tags
- [x] Closing tag before opening tag
- [x] Unclosed opening tag
- [x] Non-bracket characters

---

## 4. Alias Directory

### Pattern

Dictionary Lookup / Hash Map Lookup

### Data Structure

Dictionary (Hash Map)

### Approach

- Step 1: Use the dictionary's `.get()` method with the alias as key
- Step 2: Return the value (real name) if found, or None if not found

### Complexity

- Time: `O(1)` average case
- Space: `O(1)` additional

Explain briefly:
Direct dictionary lookup using `.get()` method which returns the value for a key or None if key doesn't exist. This is the idiomatic Python way to do safe dictionary lookups.

### Edge Cases Checked

- [x] Known alias
- [x] Unknown alias
- [x] Empty dictionary

---

# Assistance & Sources

## AI Used?

- [x] Yes
- [ ] No

## If yes, what did AI help with?

- Helped with understanding the problem requirements and patterns
- Assisted in writing clean, efficient Python implementations
- Helped structure the README documentation

## Other Sources

None
