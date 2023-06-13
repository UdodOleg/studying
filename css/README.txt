Тут викладені завдання та вирішення їх за темою "CSS". Для більш комфортного перегляду перейдіть у "Readme.pdf" для перегляду умов завдання!
Завдання №1 
Опис завдання: 
Відформатувати блоки тексту як в прикладі
Приклад 
 
Для виконання завдання скопіюйте шаблон в робочу область та замініть коментарі на Вашу реалізацію:
<!DOCTYPE html><html><head><meta charset="UTF-8" /><title>Вивчаємо CSS</title>
        <style>
            /* присвойте кожному блоку CSS правил відповідний селектор */

            /* замініть коментар на звернення за id */{
                font-weight: bold;
            }

            /* замініть коментар на звернення за класом */{
                text-decoration: underline;
            }

            /* замініть коментар на звернення за тегом */{
                text-align: right;
            }
        </style>
    </head>

    <body>
        <p id="select_by_id">HTML - стандартна мова розмітки веб-сторінок в Інтернеті. Більшість веб-сторінок створюються за допомогою мови HTML. Документ HTML оброблюється браузером та відтворюється на екрані у звичному для людини вигляді.</p>

        <p class="select_by_class">HTML - стандартна мова розмітки веб-сторінок в Інтернеті. Більшість веб-сторінок створюються за допомогою мови HTML. Документ HTML оброблюється браузером та відтворюється на екрані у звичному для людини вигляді.</p>

        <p>HTML - стандартна мова розмітки веб-сторінок в Інтернеті. Більшість веб-сторінок створюються за допомогою мови HTML. Документ HTML оброблюється браузером та відтворюється на екрані у звичному для людини вигляді.</p>
    </body>
</html>

Завдання №2 
Опис завдання: 
Відформатувати блоки тексту як в прикладі
Приклад 
 
Для виконання завдання скопіюйте шаблон в робочу область та замініть коментарі на Вашу реалізацію:
<!DOCTYPE html><html><head><meta charset="UTF-8" /><title>Вивчаємо CSS</title>
        <style>
          body {
            font-family: Arial;
            font-size: 16px;
            line-height: 1.2em;
          }
          .paragraf1 {
            /* додайте стилі тут */
          }
          .paragraf2 {
            border-width: 2px;
            border-style: solid;
            border-color: blue;
            /* додайте стилі тут */
          }
          .paragraf3 {
            /* додайте стилі тут */
          }
        </style>
    </head>

    <body>
        <!-- Відформатуйте текст, наведений нижче-->
        
        <p class="paragraf1">HTML - стандартна мова розмітки веб-сторінок в Інтернеті. Більшість веб-сторінок створюються за допомогою мови HTML. Документ HTML оброблюється браузером та відтворюється на екрані у звичному для людини вигляді.</p>

        <p class="paragraf2">HTML - стандартна мова розмітки веб-сторінок в Інтернеті. Більшість веб-сторінок створюються за допомогою мови HTML. Документ HTML оброблюється браузером та відтворюється на екрані у звичному для людини вигляді.</p>

        <p class="paragraf3">HTML - стандартна мова розмітки веб-сторінок в Інтернеті. Більшість веб-сторінок створюються за допомогою мови HTML. Документ HTML оброблюється браузером та відтворюється на екрані у звичному для людини вигляді.</p>
    </body>
</html>

Завдання №3 
Опис завдання: 
Створити горизонтальне меню. Параметр float: left або float: right не використовувати.
Зразок 
 
Для виконання завдання скопіюйте шаблон в робочу область та замініть коментарі на Вашу реалізацію:
<!DOCTYPE html><html><head><meta charset="UTF-8" /><title>Вивчаємо CSS</title>
        <style>
            body{
                padding: 30px;
            }
            nav {
                background: -webkit-linear-gradient(red, blue); /* For Safari 5.1 to 6.0 */
                background: -o-linear-gradient(red, blue); /* For Opera 11.1 to 12.0 */
                background: -moz-linear-gradient(red, blue); /* For Firefox 3.6 to 15 */
                background: linear-gradient(red, blue); /* Standard syntax (must be last) */
                display: inline-block;
            }
            ul, li{
                margin: 0;
                padding: 0;
            }
            a{
                color: white;
                font-weight: bold;
            }
            li {
                list-style-type: none;
                padding: 10px;
                border: 1px solid white;
                /* додайте стилі тут */
            }
        </style>
    </head>

    <body>
        <nav>
            <ul>
                <li><a href="#">Текст</a></li>
                <li><a href="#">Текст</a></li>
                <li><a href="#">Текст</a></li>
                <li><a href="#">Текст</a></li>
                <li><a href="#">Текст</a></li>
            </ul>
        </nav>
    </body>
</html>

Деякі задачі мають такі варіанти , як збереження, скидання, підказки або показ відповіді. Ці варіанти слідують кнопці Надіслати. 
Завдання №4 
Опис завдання: 
Створити горизонтальне меню, яке реагує на наведення курсору. Колір тексту повинен змінюватись на червоний (red), а також повинно з'являтися підкреслення тексту.
Зразок 
 
Для виконання завдання скопіюйте шаблон в робочу область та замініть коментарі на Вашу реалізацію:
<!DOCTYPE html><html><head><meta charset="UTF-8" /><title>Вивчаємо CSS</title>
        <style>
            body{
                padding: 30px;
                color: white;
            }
            nav {
                background: -webkit-linear-gradient(red, blue); /* For Safari 5.1 to 6.0 */
                background: -o-linear-gradient(red, blue); /* For Opera 11.1 to 12.0 */
                background: -moz-linear-gradient(red, blue); /* For Firefox 3.6 to 15 */
                background: linear-gradient(red, blue); /* Standard syntax (must be last) */
                display: inline-block;
            }
            ul, li{
                margin: 0;
                padding: 0;
            }
            li {
                list-style-type: none;
                padding: 10px;
                border: 1px solid white;
                display: inline-block;
            }
            a {
                color: white;
                text-decoration: none;
            }

            li:hover a {
                /* додайте стилі тут */
            }
        </style>
    </head>

    <body>
        <nav>
            <ul>
                <li><a href="#">Текст</a></li>
                <li><a href="#">Текст</a></li>
                <li><a href="#">Текст</a></li>
                <li><a href="#">Текст</a></li>
                <li><a href="#">Текст</a></li>
            </ul>
        </nav>
    </body>
</html>

Завдання №5 
Опис завдання: 
Розмістити на сторінці 5 блоків так, щоб при зміні ширини браузера вони теж змінювати ширину. Відповідь ховається в задачі про меню. Параметр float: left або float: right не використовувати.
Зразок
Початковий вигляд
 
Вигляд після масштабування
 
Для виконання завдання скопіюйте шаблон в робочу область та замініть коментарі на Вашу реалізацію:
<!DOCTYPE html><html><head><meta charset="UTF-8" /><title>Вивчаємо CSS</title>
        <style>
        div {
            border: 2px dashed blue;
            background-color: yellow;
            height: 100px;
            box-sizing:border-box;
            /* додайте стилі тут */
        }
        </style>
    </head>

    <body>
        <div></div><div></div><div></div><div></div><div></div>
    </body>
</html>

Завдання №6 
Опис завдання: 
Додати 3 вкладених списка з різними позначками перед <li> елементом. Як в прикладі. Дотримуйтесь послідовності.
Приклад 
 
Для виконання завдання скопіюйте шаблон в робочу область та замініть коментарі на Вашу реалізацію:
<!DOCTYPE html><html><head><meta charset="UTF-8" /><title>Вивчаємо CSS</title>
        <style>
            .list1 li {
                /* додайте стилі тут */
            }
            .list2 li {
                /* додайте стилі тут */
            }
            .list3 li {
                /* додайте стилі тут */
            }
        </style>
    </head>

    <body>
    <ol>
        <li>Заголовок 1
            <ul class="list1">
                <li>Текст</li>
                <li>Текст</li>
                <li>Текст</li>
            </ul>
        </li>
        <li>Заголовок 2
            <ul class="list2">
                <li>Текст</li>
                <li>Текст</li>
                <li>Текст</li>
            </ul>
        </li>
        <li>Заголовок 3
            <ul class="list3">
                <li>Текст</li>
                <li>Текст</li>
                <li>Текст</li>
            </ul>
        </li>
    </ol>
    </body>
</html>

Завдання №7 
Опис завдання: 
Розмістіть блоки як на малюнку, використовуючи відносне та абсолютне позиціонування. Синій блок прив'язати до правого нижнього кута. 
*Підказка: для прив`язки використовуйте параметри bottom та right 
Приклад 
 
Для виконання завдання скопіюйте шаблон в робочу область та замініть коментарі на Вашу реалізацію:
<!DOCTYPE html><html><head><meta charset="UTF-8" /><title>Вивчаємо CSS</title>
        <style>
            .parent {
                width: 200px;
                height: 200px;
                background-color: yellow;
                margin: 20px auto;
                /* додайте стилі тут */
            }

            .child {
                width: 50px;
                height: 50px;
                background-color: blue;
                /* додайте стилі тут */
            }
        </style>
    </head>

    <body>
    <div class="parent">
        <div class="child"></div>
    </div>
    </body>
</html>
