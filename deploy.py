from cs102_autolab.report2 import Report2
from unitgrade_private.hidden_create_files import setup_grade_file_report
from snipper.snip_dir import snip_dir

if __name__ == "__main__":

    setup_grade_file_report(Report2)
    snip_dir("./", "../../students/cs102", clean_destination_dir=True, exclude=['*.token', 'deploy.py'])
    pass