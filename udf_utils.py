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
    try:
        salary_pattern = r'\$(\d{1,3}(?:,\d{3})+).+?to.+\$(\d{1,3}(?:,\d{3})+)(?:\s+and\s+\$(\d{1,3}(?:,\d{3})+)\s+to\s+\$(\d{1,3}(?:,\d{3})+))?'
        salary_match = re.search(salary_pattern, file_content)

        if salary_match:
            salary_start = float(salary_match.group(1).replace(',', ''))
            salary_end = float(salary_match.group(4).replace(',', '')) if salary_match.group(4) \
                else float(salary_match.group(2).replace(',', ''))
        else:
            salary_start, salary_end = None, None

        return salary_start, salary_end
    
    except Exception as e:
        raise ValueError(f'Error extracting salary: {str(e)}')

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
    try:
        requirements_match = re.search(r'(REQUIREMENTS?/\s?MINIMUM QUALIFICATIONS?)(.*)(NOTES?)', file_content, re.DOTALL)
        requirements = requirements_match.group(2).strip() if requirements_match else None
        return requirements
    except Exception as e:
        raise ValueError(f'Requirements not found: {e}')

def extract_notes(file_content):
    try:
        notes_match = re.search(r'(NOTES?)(.*)(?=DUTIES)', file_content, re.DOTALL | re.IGNORECASE)
        notes = notes_match.group(2).strip() if notes_match else None
        return notes
    except Exception as e:
        raise ValueError(f'Notes not found: {e}')

def extract_duties(file_content):
    try:
        duties_match = re.search(r'(DUTIES)(.*)(?=SELECTION PROCEDURE)', file_content, re.DOTALL | re.IGNORECASE)
        duties = duties_match.group(2).strip() if duties_match else None
        return duties
    except Exception as e:
        raise ValueError(f'Duties not found: {e}')

def extract_selection(file_content):
    try:
        selection_match = re.search(r'(SELECTION PROCEDURE)(.*)(?=BENEFITS)', file_content, re.DOTALL | re.IGNORECASE)
        selection = selection_match.group(2).strip() if selection_match else None
        return selection
    except Exception as e:
        raise ValueError(f'Selection not found: {e}')

def extract_experience_length(file_content):
    try:
        experience_length_match = re.search(r'(EXPERIENCE)(.*)(?=JOB TYPE)', file_content, re.DOTALL | re.IGNORECASE)
        experience_length = experience_length_match.group(2).strip() if experience_length_match else None
        return experience_length
    except Exception as e:
        raise ValueError(f'Experience Length not found: {e}')

def extract_job_type(file_content):
    try:
        job_type_match = re.search(r'(JOB TYPE)(.*)(?=EDUCATION)', file_content, re.DOTALL | re.IGNORECASE)
        job_type = job_type_match.group(2).strip() if job_type_match else None
        return job_type
    except Exception as e:
        raise ValueError(f'Job Type not found: {e}')

def extract_education_length(file_content):
    try:
        education_length_match = re.search(r'(EDUCATION)(.*)(?=SCHOOL TYPE)', file_content, re.DOTALL | re.IGNORECASE)
        education_length = education_length_match.group(2).strip() if education_length_match else None
        return education_length
    except Exception as e:
        raise ValueError(f'Education Length not found: {e}')

def extract_school_type(file_content):
    try:
        school_type_match = re.search(r'(SCHOOL TYPE)(.*)(?=APPLICATION)', file_content, re.DOTALL | re.IGNORECASE)
        school_type = school_type_match.group(2).strip() if school_type_match else None
        return school_type
    except Exception as e:
        raise ValueError(f'School Type not found: {e}')

def extract_application_location(file_content):
    try:
        application_location_match = re.search(r'(APPLICATIONS?)(.*)(?=AN EQUAL EMPLOYMENT OPPORTUNITY EMPLOYER)', file_content, re.DOTALL | re.IGNORECASE)
        application_location = application_location_match.group(2).strip() if application_location_match else None
        return application_location
    except Exception as e:
        raise ValueError(f'Application Location not found: {e}')


