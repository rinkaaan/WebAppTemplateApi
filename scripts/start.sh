WORKPLACE="$HOME/workplace/WebAppTemplate"

(
  cd "$WORKPLACE/WebAppTemplateApi"
  uvicorn api.app:app --port 8080
)
