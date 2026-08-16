# The Duplicate Spy Detector 

# 1. THE BRUTE-FORCE WAY (Compares every ID with every other ID)
def check_brute_force(agent_ids):
    for i in range(len(agent_ids)):
        for j in range(i + 1, len(agent_ids)):
            if agent_ids[i] == agent_ids[j]:
                return True  
    return False

# 2. THE OPTIMIZED WAY (Uses a set as a fast checklist)
def check_optimized(agent_ids):
    seen = set()
    for item in agent_ids:
        if item in seen:
            return True 
        seen.add(item)
    return False

# --- TESTING THE CODE ---
# A sample list of agent IDs with a hidden duplicate (the number 5)
spy_list = [1, 2, 3, 4, 5, 6, 5]

print("--- Testing Brute-Force ---")
found_brute = check_brute_force(spy_list)
print("Duplicate found?", found_brute)

print("\n--- Testing Optimized Set ---")
found_optimized = check_optimized(spy_list)
print("Duplicate found?", found_optimized)