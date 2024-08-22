import os
import csv

fieldnames = [
    '_id', 'attendance_status', 'attendanee_id', 'company_name', 'contact_name', 
    'created_date', 'email', 'event_name', 'is_member', 'is_sent', 
    'job_title', 'members_number', 'paid', 'phone', 'price', 'idofuser'
]

def addAtt(data):
    with open('att.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        file_is_empty = file.tell() == 0
        if file_is_empty:
            writer.writeheader()
        
        if isinstance(data, list):
            writer.writerows(data)
        else:
            writer.writerow(data)

def parseID(input_string):
    scanned_text = ""
    for char in input_string:
        if char == '_':
            break
        scanned_text += char

    return int(scanned_text)


