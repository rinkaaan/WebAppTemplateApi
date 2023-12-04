WORKPLACE="$HOME/workplace/WebAppTemplate"

(
  cd "$WORKPLACE/PythonUtils"
  pip install .
  rm -rf build
)