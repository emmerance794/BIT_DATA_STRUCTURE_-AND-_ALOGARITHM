# integers
incident_counts=[5,10,15,20,25]
total_incidents=sum(incident_counts)
average_incidents=total_incidents/len(incident_counts)
minimum_incidents=min(incident_counts)
maximum_incidents=max(incident_counts)
print("integers")
print(f"total incidents: {total_incidents}")
print(f"average incidents: {average_incidents}")
print(f"minimum incidents: {minimum_incidents}")
print(f"maximum incidents: {maximum_incidents}")

# strings
report=(f"security incident report\n"
        f"total incidents recorded: {total_incidents}\n"
        f"average incidents per log: {average_incidents:0.3f}\n"
        f"highest recorded incidents: {maximum_incidents}\n"
f"lowest recorded incidents: {maximum_incidents}\n")
print("strings")
print(report)

# booleans
threshold=10
status=""
if average_incidents> threshold and maximum_incidents> threshold: # compound condition
    status= "above standard"
    print(f"{status}")
else:
    status= "below standard"
    print("booleans")
    print(f"threshold check: {status}")
    print(f"status check: {status}")
    print()
    
    # Lists Section
# -----------------------------
incident_list = ["Phishing", "Malware", "Unauthorized Access", "Data Breach"]

print("=== Lists ===")
print("Original List:", incident_list)

# Add a new incident
incident_list.append("Stolen Device")

# Remove based on condition (remove if incident name has 'Malware')
incident_list = [i for i in incident_list if "Malware" not in i]

# Sort list
incident_list.sort()

print("Modified List:", incident_list)
print()

# Arrays Section
from array import array
# -----------------------------
incident_array = array('i', [5, 12, 7, 9, 15])
array_sum = sum(incident_array)
list_sum = sum(incident_counts)

print("=== Arrays ===")
print("Array sum:", array_sum)
print("List sum :", list_sum)
print("Array sum equals List sum? ->", array_sum == list_sum)
print()

# Dictionaries Section
# -----------------------------
incident_dicts = [
    {"id": 1, "name": "Phishing", "value": 5},
    {"id": 2, "name": "Malware", "value": 12},
    {"id": 3, "name": "Unauthorized Access", "value": 7},
]

print("=== Dictionaries ===")
print("Original Records:", incident_dicts)

# Update one record (change value of Malware to 15)
incident_dicts[1]["value"] = 15

# Delete another record (remove Unauthorized Access)
