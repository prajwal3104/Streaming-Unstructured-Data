import re
from datetime import datetime

def extract_file_name(file_content):
    file_content = file_content.strip()
    position = file_content.split('\n')[0]
    return position

def extract_position(file_content):
    file_content = file_content.strip()
    position = file_content.split('\n')[0]
    return position

def extract_class_code(file_content):
    try:
        class_code_match = re.search(r'(Class Code:)\s+ (\d+)', file_content)
        class_code = class_code_match.group(2) if class_code_match else None
        return class_code
    except Exception as e:
        raise ValueError('Class code not found: {e}')

def extract_salary(file_content):
    pass

def extract_start_date(file_content):
    try:
        start_date_match = re.search(r'(Start [Dd]ate:)\s+(\d\d-\d\d-\d\d)', file_content)
        start_date = datetime.strptime(start_date_match.group(2), '%m-%d-%y') if start_date_match else None
        return start_date
    except Exception as e:
        raise ValueError(f'Start Date not found: {e}')

def extract_end_date(file_content):
    try:
        end_date_match = re.search(
            r'(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s(\d{1,2},\s\d{4})', file_content)
        end_date = end_date_match.group() if end_date_match else None
        end_date = datetime.strptime(end_date, '%B %d, %Y') if end_date else None
        return end_date
    except Exception as e:
        raise ValueError(f'End Date not found: {e}')


def extract_requirements(file_content):
    pass

def extract_notes(file_content):
    pass

def extract_duties(file_content):
    pass

def extract_selection(file_content):
    pass

def extract_experience_length(file_content):
    pass

def extract_job_type(file_content):
    pass

def extract_education_length(file_content):
    pass

def extract_school_type(file_content):
    pass

def extract_application_location(file_content):
    pass


