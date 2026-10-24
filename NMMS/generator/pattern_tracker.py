"""
NMMS Pattern History & Least-Recently-Used (LRU) Recency Tracker
Maintains persistent record of which question and diagram patterns have been used
across successive test papers and regenerations, ensuring rich variety and preventing duplicates.
"""

import os
import json
import time
import random
from typing import List, Optional, Dict, Any

HISTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pattern_history.json')

def load_history() -> Dict[str, Dict[str, Dict[str, Any]]]:
    """Loads pattern usage history from disk, or initializes default schema."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {
        'paper_folding': {},
        'venn_geometric': {},
        'venn_survey': {}
    }

def save_history(data: Dict[str, Dict[str, Dict[str, Any]]]) -> None:
    """Safely saves pattern usage history to disk."""
    try:
        temp_file = HISTORY_FILE + '.tmp'
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
        os.rename(temp_file, HISTORY_FILE)
    except Exception as e:
        print(f"Warning: Failed to save pattern history: {e}")

def get_least_recently_used_patterns(
    category: str,
    all_pattern_ids: List[str],
    count: int = 1,
    current_test_num: int = 0,
    exclude: Optional[List[str]] = None
) -> List[str]:
    """
    Selects `count` pattern IDs from `all_pattern_ids` that have been used
    least recently (lowest last_used_test, then lowest usage_count, with random tie-breaking).
    Automatically records their usage and saves history.
    """
    history = load_history()
    cat_data = history.setdefault(category, {})

    exclude_set = set(exclude or [])
    candidates = [pid for pid in all_pattern_ids if pid not in exclude_set]
    if not candidates:
        candidates = list(all_pattern_ids)

    # Decorate with sort keys: (last_used_test, usage_count, random_jitter)
    scored = []
    for pid in candidates:
        info = cat_data.get(pid, {'last_used_test': -1, 'usage_count': 0, 'last_time': 0})
        # Unused patterns get lowest priority score
        last_test = info.get('last_used_test', -1)
        usage = info.get('usage_count', 0)
        jitter = random.random()
        scored.append(((last_test, usage, jitter), pid))

    scored.sort(key=lambda x: x[0])
    selected = [pid for _, pid in scored[:count]]

    # Record usage
    now = time.time()
    for pid in selected:
        info = cat_data.setdefault(pid, {'last_used_test': 0, 'usage_count': 0, 'last_time': 0})
        info['last_used_test'] = current_test_num
        info['usage_count'] = info.get('usage_count', 0) + 1
        info['last_time'] = now

    save_history(history)
    return selected

def record_pattern_usage(category: str, pattern_ids: List[str], current_test_num: int = 0) -> None:
    """Manually records pattern usage in history."""
    history = load_history()
    cat_data = history.setdefault(category, {})
    now = time.time()
    for pid in pattern_ids:
        info = cat_data.setdefault(pid, {'last_used_test': 0, 'usage_count': 0, 'last_time': 0})
        info['last_used_test'] = current_test_num
        info['usage_count'] = info.get('usage_count', 0) + 1
        info['last_time'] = now
    save_history(history)
