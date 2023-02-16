* Start from main:
  git checkout main

* Show around the code: functions, tests, conventions.

* Run pytest to show what happens:
  pytest some_code.py

* Generate a coverage report:
  pytest --cov-report xml:cobertura.xml --cov=. *.py

* Check out the coverage report.

* Upload the coverage report to Codacy for the main branch:
  export CODACY_PROJECT_TOKEN=<TOKEN>
    get TOKEN at https://app.codacy.com/gh/nicklem/test-python/settings/coverage
  bash <(curl -Ls https://coverage.codacy.com/get.sh)
    it's a shorthand for bash <(curl -Ls https://coverage.codacy.com/get.sh) report -r cobertura.xml

* Check that the UI on Codacy shows the new report.

* Create a new branch
  * git checkout -b some-changes

* Explain how branches work
  git checkout main 
  echo "some content" > some_file
  git add some_file
  git commit -m "a change"
    Show the Git tab on Pycharm.
  git reset --hard HEAD~1
  git checkout some-changes

* Change the test results (for example, by adding an untested function)

* Upload the coverage report to Codacy
  bash <(curl -Ls https://coverage.codacy.com/get.sh) report -r cobertura.xml
  bash <(curl -Ls https://coverage.codacy.com/get.sh)

* Check that the UI on Codacy shows the new report but missing commit

* Commit & push the change
  git add some_code.py
  git commit -m change
  git push

* Open the PR on GitHub, wait for Codacy to detect the PR.

* This line is here just to trigger a Codacy warning. You can ignore it.
