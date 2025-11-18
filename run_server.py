from waitress import serve
from mysite_proj.wsgi import application  # myproject ko apne project folder name se replace karo

serve(application, host='0.0.0.0', port=8000)
