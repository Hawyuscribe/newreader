#!/usr/bin/env python3
"""Fix indentation in case_bot_enhanced.py"""

# Read the file
with open('django_neurology_mcq/mcq/case_bot_enhanced.py', 'r') as f:
    lines = f.readlines()

# Find the line where we need to start indenting
start_indent = None
for i, line in enumerate(lines):
    if 'try:' in line and 'if request.method' in lines[i+1]:
        start_indent = i + 2  # Start after the return statement
        break

# Find the except block that should match the try
end_indent = None
for i, line in enumerate(lines):
    if 'except Exception as e:' in line and 'Global exception handler' in lines[i+1]:
        end_indent = i
        break

if start_indent and end_indent:
    # Add 4 spaces to all lines between start and end
    for i in range(start_indent + 3, end_indent):
        if lines[i].strip():  # Don't indent empty lines
            lines[i] = '    ' + lines[i]
    
    # Write back
    with open('django_neurology_mcq/mcq/case_bot_enhanced.py', 'w') as f:
        f.writelines(lines)
    
    print(f"Fixed indentation from line {start_indent} to {end_indent}")
else:
    print("Could not find the correct lines to fix")