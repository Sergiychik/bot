# Как работать с GitHub

 * git clone [вставить ссылку, взятую под зеленой кнопкой Code в репозитарии] (произойдет клонирование репозитария)
 * Закройте окно git bash
 * Перейдите в созданную папку (имя - совпадает с именем склонированного репозитария
 * Откройте git bash в этой папке
 * Произведите изменения в папке
 * Далее - в git bash напишите
 * git add .
 * git commit -m first_commit

# Как работать с Gheroku

 * Ставим Heroku cli
 * Логинемся на Heroku login
 * Создаем файлы Procfile , requirements.txt, runtime.txt
 * git init
 * git add .
 * git comit -m first
 * heroku create app_name
 * git remote -v
 * git push heroku master
 * heroku ps
 * heroku ps:scale worker=1
