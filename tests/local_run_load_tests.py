import sys
import os
import shutil
import subprocess
from pathlib import Path

MY_DJANGO_NEWS_TESTS = Path(__file__).parent.parent
MY_DJANGO_NEWS_WEBSITE = Path(__file__).parent.parent.parent / "my_django_news_website"
BASE_URL = "http://localhost:8000"

def main():
    DATA_BASE = MY_DJANGO_NEWS_WEBSITE / "mysite" / "db.sqlite3"
    COPY_DATA_BASE = MY_DJANGO_NEWS_TESTS / "tests" / "db_copy.sqlite3"
    MYSITE = MY_DJANGO_NEWS_WEBSITE / "mysite"
    if len(sys.argv) < 2:
        print("Error: Please specify test load file")
        print("Usage: python local_run_load_tests.py")
        sys.exit(1)
    test_file = sys.argv[1]

    #Copy database
    print("Copying database")
    if not DATA_BASE.exists():
        print("Error: You should add path to data_base value")
        sys.exit(1)
    shutil.copy2(DATA_BASE, COPY_DATA_BASE)
    print(f"Copied to {DATA_BASE}")

    #Start Django
    print("\nStart Django website")
    django_process = subprocess.Popen(
        ['python', 'manage.py', 'runserver', "0.0.0.0:8000"],
        cwd=MYSITE,
        stdin=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
    )
    print(f"Django started PID: {django_process.pid}")

    #Wait django start
    import time
    for i in range(30):
        try:
            response = subprocess.run(
                    ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', BASE_URL],
                    capture_output=True,
                    text=True,
                    timeout= 5
            )
            if response.stdout == '200':
                print(f"Website is ready!")
                break
        except:
            pass
        time.sleep(1)
    else:
        print("Django failed to start")
        django_process.terminate()
        os.remove(COPY_DATA_BASE)
        sys.exit(1)

    #Running k6 tests
    print(f"\nStarting k6 test file: {test_file}")
    os.environ['BASE_URL'] = BASE_URL
    result = subprocess.run(['k6', 'run', test_file])

    #Cleanup database
    print(f"\nCleaning up processes and database")
    django_process.terminate()
    django_process.wait()
    COPY_DATA_BASE.unlink()
    print(f"Cleanup complited")
    sys.exit(result)
        
main()