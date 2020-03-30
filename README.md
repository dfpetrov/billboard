# billboard
<ol>
<li>Запустить redis на localhost</li>
<li>Запустить mongodb на localhost</li>
<li>Установить все из requirements.txt</li>
<li>Запустить приложение app.py</li>
</ol>

<p>- список всех объявлений: GET http://127.0.0.1:5000/</p>
<p>- добавление нового объявления: POST http://127.0.0.1:5000/ad<br>
Тело запроса JSON:<br>
<pre>
{
    "title": "Новое объявление3",
    "tags": ["тэг1"],
    "comments": ["коммент1"]
}
</pre></p>
<p>- получение существующего объявления (с тегами и комментариями) по ID: GET http://127.0.0.1:5000/ad/id_объявления</p>
<p>- добавление тега к существующему объявлению: POST http://127.0.0.1:5000/addtag/id_объявления<br>
Тело запроса JSON:<br>
<pre>
{
    "title": "Новое объявление3",
    "tags": ["тэг1"],
    "comments": ["коммент1"]
}</pre></p>

<p>- добавление комментария к существующему объявлению: POST http://127.0.0.1:5000/addcomm/id_объявления<br>
Тело запроса JSON:<br>
<pre>
{
    "title": "Новое объявление3",
    "tags": ["тэг1"],
    "comments": ["коммент1"]
}</pre></p>
<p>- статистика для данного объявления: GET http://127.0.0.1:5000/stat/id_объявления</p>
<p>- очистить кэш: GET http://127.0.0.1:5000/clear</p>

