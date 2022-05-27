from unitgrade_private.autolab.autolab import new_deploy_assignment
from unitgrade_private.docker_helpers import download_docker_images
from unitgrade_private.docker_helpers import compile_docker_image

if __name__ == "__main__":
    ## Step 1. Deploy the report file.
    from report2 import Report2
    from unitgrade_private.hidden_create_files import setup_grade_file_report
    from snipper.snip_dir import snip_dir
    from unitgrade import version
    print("version", version.__version__)
    # Set up the instructor _grade script and all files needed for the tests.
    setup_grade_file_report(Report2, with_coverage=False)
    snip_dir("./", "../../students/cs102_autolab", clean_destination_dir=True, exclude=['*.token', 'deploy_autolab.py', '*_grade.py', 'tmp', '*.tar'])

    # Step 1: Download and compile docker grading image. You only need to do this once.  #!s=a
    download_docker_images("../docker") # Download docker images from gitlab (only do this once).
    dockerfile = f"../docker/docker_tango_python/Dockerfile"
    autograde_image = 'tango_python_tue2'  # Tag given to the image in case you have multiple images.
    compile_docker_image(Dockerfile=dockerfile, tag=autograde_image, no_cache=False)  # Compile docker image. #!s

    # Step 2: Create the cs102.tar file from the grade scripts. #!s=b
    instructor_base = f"."
    student_base = f"../../students/cs102_autolab"

    from report2 import Report2
    # INSTRUCTOR_GRADE_FILE =
    output_tar = new_deploy_assignment("cs105g",  # Autolab name of assignment (and name of .tar file)
                                   INSTRUCTOR_REPORT_CLASS=Report2,
                                   INSTRUCTOR_BASE=instructor_base,
                                   INSTRUCTOR_GRADE_FILE=f"{instructor_base}/report2_grade.py",
                                   STUDENT_BASE=student_base,
                                   STUDENT_GRADE_FILE=f"{instructor_base}/report2.py",
                                   autograde_image_tag=autograde_image,
                                   student_should_upload_token=False,
                                    homework_file="homework1.py") #!s

    # What can you do? Get a report class from the .token file?


