# <blockquote>👾208itc бот</blockquote>

###  Чат-бот для группы университета

### <blockquote>Что бот умеет?</blockquote>

- Отправлять расписание
- Редактировать расписание
- Записывать и присылать кабинеты
- Отправлять список преподавателей
- Присылать погоду с утра
- Осуществлять контроль над пользователями
- Реагировать на сообщения в группе

### <blockquote>Установка и запуск</blockquote>

- Заполните поля в <code>.env</code>
- Выполните комманду <code>pip install -r requirements.txt</code>
- Выполните комманду <code>python main.py</code>


### <blockquote>Роли</blockquote>
### <code>Администратор 🔐</code> 

- Доступны все возможности бота.

### <code>Староста 👨‍🏫</code> 

- Позволяет добавлять и удалять занятия

### <code>Редактор 📝</code>

- Позволяет добавлять и удалять занятия

### <code>Уровень 3️</code>

- _В разработке.._

### <code>Одногруппник 👨‍</code>

- Позволяет добавлять и просматривать кабинеты

### <code>Пользователь 👤‍</code>

- Обычный пользователь

### <code>Заблокирован 🚫</code>

- Закрывает доступ к общим командам

### <blockquote>Команды бота</blockquote>

### <code>/start</code> 

- _Отправляет приветственное сообщение._

### <code>/help</code>

- _Присылает список команд._

### <code>/roles</code> 

- _Присылает список ролей._

### <code>/schedule или /s</code> 

- _Присылает расписание занятий._

### <code>/add</code> 

- _Вызывает меню добавления занятий._

### <code>/remove</code> 

- _Вызывает меню удаления занятий._

### <code>/teacher или /t</code> 

- _Вызывает меню поиска преподавателя._

### <code>/cabinets или /c или каб</code> 

- _Присылает или добавляет кабинеты._


### <code>/weather или /w</code> 

- _Присылает текущую погоду в городе Минск_

### <code>/random или /r (элемент1) (элемент..)</code> 

- _Выбирает один из переданных элементов._

### <code>/admin</code> 

- _Отправляет список команд администратора._

### <blockquote>Режим администратора</blockquote>
#### Создан для проверки возможностей определенной роли.

<code>True</code>: _Администратору открыты все возможности._

<code>False</code>: _Администратор обладает правами присвоеной ему роли._

**Для переключения используйте <code>/am</code>**

### <blockquote>Комманды администратора</blockquote>

### <code>/read</code> 

- _Осуществляет чтение расписание из **.txt** файла._

### <code>/drop</code> 

- _Очищает базу расписания._

### <code>/set (telegram ID или username) (уровень)</code> 

- _Устанавливает роль для пользователя._

### <code>/perm (telegram ID или username</code> 

- _Показывает роль пользователя._

### <code>/id</code> 

- _Показывает telegram ID пользователя и группы._

### <blockquote>Требования</blockquote>

- `pytz==2023.3.post1`
- `pyTelegramBotAPI==4.15.2`
- `requests==2.31.0`
- `environs==10.3.0`

### <blockquote>Контакты</blockquote>
    
## Email: me.yarmolovich@gmail.com
## [Telegram](https://t.me/naitmag)
