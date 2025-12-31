# build.py
import shutil, os
# Очищаем папку build (если есть)1
shutil.rmtree('build', ignore_errors=True)
os.makedirs('build')
# Копируем и изменяем HTML
with open('src/index.html', 'r') as f:
    html = f.read()
# Добавляем метку о сборке
html = html.replace('</body>', '<p>✅ Built by CI/CD</p>\n</body>')
with open('build/index.html', 'w') as f:
    f.write(html)
# Копируем CSS
shutil.copy('src/style.css', 'build/style.css')
print("Build completed.")
