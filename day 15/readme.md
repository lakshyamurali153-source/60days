# 🕵️‍♂️ The Duplicate Spy Detector

**Day 15 of the Algorithmic Thinking Phase**

## Mission Brief
A secret agency intercepted a suspicious list of agent IDs. This project detects whether any duplicate IDs exist before spies can infiltrate the system. 

## The Solutions

### 1. Brute-Force Checker
* **How it works:** Uses nested loops to compare every single ID against every other ID in the list.
* **Time Complexity:** $O(N^2)$ - As the dataset grows, the number of operations increases quadratically.
* **Space Complexity:** $O(1)$ - Requires no extra memory.

### 2. Optimized Checker (Sets)
* **How it works:** Utilizes a Hash Set to keep track of IDs we have already seen. Hash Sets allow for constant-time lookups. 
* **Time Complexity:** $O(N)$ - We only need to iterate through the list of IDs a single time. 
* **Space Complexity:** $O(N)$ - Requires extra memory to store the set of seen IDs.

## Performance Comparison (Scaling to 1 Million IDs)
When tested with a large dataset, the difference in scaling is massive:
* The **Brute-Force** approach becomes entirely unusable for 1,000,000 IDs. Because $1,000,000^2$ results in 1 trillion operations, it would take a standard computer hours (or even days) to process.
* The **Optimized** approach using a Hash Set processes 1,000,000 IDs in just a few milliseconds. 

**Conclusion:** Trading memory $O(N)$ for speed $O(N)$ is necessary for real-world applications like fraud prevention and transaction validation.
