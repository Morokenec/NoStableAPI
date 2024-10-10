from flask import Flask, render_template, request, redirect, url_for
import time
import services

SETTINGS_FILE = 'tabels.json'

app = Flask(__name__)

@app.route('/')
def root():
    ip_address = request.remote_addr
    settings = services.load_settings()

    for setting in settings:
        if setting['error_count'] != 0 and ip_address == setting['ip']:
            time.sleep(setting['timeout'])
            setting['error_count'] -= 1
            services.save_settings(settings)
            return "<h1 style='text-align: center'>Bad Request 502</h1><a href = '/settings'>Настройки</a>", 502
        

    setting['error_count'] = setting['limit_error']
    services.save_settings(settings)
    return { 
        "message" : "Hello user!",
        "ip" : ip_address,
        "settings": "/settings"
    }
    
@app.route("/settings", methods=['GET', 'POST'])
def settings():

    if request.method == 'POST':
        settings = services.load_settings()

        ip = request.remote_addr
        limit_error = request.form.get('limit_error')
        timeout = request.form.get('timeout')

        for setting in settings:
            if setting['ip'] == ip:
                setting['error_count'] = int(limit_error)
                setting['limit_error'] = int(limit_error)
                setting['timeout'] = int(timeout)
                services.save_settings(settings)
                return redirect(url_for('root'))
        
        new_setting = {
            'ip': ip,
            'limit_error': int(limit_error),
            'timeout': int(timeout),
            'error_count': 0 
        }

        settings.append(new_setting)
        services.save_settings(settings)
        return redirect(url_for('root'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '80')