from flask import Blueprint, render_template, request

echo_app = Blueprint('echo', __name__, template_folder='echo/templates',)

@echo_app.route('/')
def main():
    return render_template(f'echo/main.html')

@echo_app.route('/run')
def echo():
    text = request.args.get('text') or 'Nope'
    return render_template(f'echo/main.html', text = text)
