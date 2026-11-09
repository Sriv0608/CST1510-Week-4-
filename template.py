"""
RECORD CHECK  -  my version
===========================

Name  :  Srivatsa
Lane  :  AI / Cyber / IT      (delete two)
Date  :  18 October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here

def check(value,limit):
    """this does the difference and percentage calculation"""
    difference=value-limit
    percentage=(value/limit)*100
    return difference,percentage

def print_report(label,value,limit,difference,percent,status):

    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference:.2f}")
    print(f"Percent: {percent:.2f}%")
    print(f"Status: {status}")
    print("=" * 34)

records = [
    {"label": "R-001", "value": 86, "limit": 100},
    {"label": "R-002", "value": 97, "limit": 100},
    {"label": "R-003", "value": 65, "limit": 100}
]

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.



# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here

for record in records:
    value = record["value"]
    limit = record["limit"]
    label = record["label"]
    
    difference, percentage = check(value, limit)
    
    if percentage > 100:
        status = "OVER LIMIT"
    else:
        status = "OK"
    
    print_report(label, value, limit, difference, percentage, status)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
