# 🔧 Website: Инструкция по запуску

Следуйте этой инструкции для настройки и запуска проекта **WebSite**. Все команды выполняются в терминале.  
**Важно:** Убедитесь, что у вас установлены `Python` и `pip`.

---

## 💻 Запуск проекта


### 1️⃣ Клонируйте проект:

#### Для Windows:
```bash
git clone https://github.com/124476/DjangoExmple-Prerelease/
```

#### Для macOS/Linux:
```bash
git clone https://github.com/124476/DjangoExmple-Prerelease/
```

---

### 2️⃣ Перейдите в папку проекта:

#### Для Windows:
```bash
cd web
```

#### Для macOS/Linux:
```bash
cd web
```

---

### 3️⃣ Создайте файл окружения `.env` на основе `env.example`:

#### Для Windows:
```bash
copy env.example .env
```

#### Для macOS/Linux:
```bash
cp env.example .env
```

---

### 4️⃣ Настройте файл `.env`:

Откройте файл `.env` в любом текстовом редакторе и настройте параметры:  

- **DJANGO_DEBUG**: `true` для разработки, `false` для продакшн.
- **DJANGO_SECRET_KEY**: Уникальный секретный ключ.
- **DJANGO_ALLOWED_HOSTS**: Разрешенные хосты, разделенные запятыми (например, `127.0.0.1,localhost`).

---

### 5️⃣ Создайте и активируйте виртуальное окружение:

#### Для Windows:
1. Создание виртуального окружения:
   ```bash
   python -m venv venv
   ```
2. Активация виртуального окружения:
   ```bash
   venv\Scripts\activate
   ```

#### Для macOS/Linux:
1. Создание виртуального окружения:
   ```bash
   python3 -m venv venv
   ```
2. Активация виртуального окружения:
   ```bash
   source venv/bin/activate
   ```

---

### 6️⃣ Установите зависимости:

#### Для Windows:
```bash
pip install -r requirements.txt
```

#### Для macOS/Linux:
```bash
pip install -r requirements.txt
```

---

### 7️⃣ Примените миграции:

#### Для Windows:
```bash
python manage.py migrate
```

#### Для macOS/Linux:
```bash
python3 manage.py migrate
```

---

### 8️⃣ Запустите сервер разработки:

#### Для Windows:
```bash
python manage.py runserver
```

#### Для macOS/Linux:
```bash
python3 manage.py runserver
```

---

### 9️⃣ Откройте сайт:
Перейдите по адресу:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

> **Важно:** Не закрывайте терминал, пока сервер работает.

---

## ⚙ Настройка файла `.env`

Файл `.env` содержит конфигурацию вашего проекта. Вы можете создать его на основе `env.example` и изменить параметры, если это необходимо.  
Пример содержимого `env.example`:

```env
DJANGO_DEBUG=true
DJANGO_SECRET_KEY=secret_key
DJANGO_ALLOWED_HOSTS=127.0.0.1
```

### Описание параметров `.env`:

- `DJANGO_DEBUG` - Включение режима отладки (True/False).
- `DJANGO_SECRET_KEY` - Секретный ключ Django.
- `DJANGO_ALLOWED_HOSTS` - Список разрешённых хостов, разделённых запятыми.

---

## ⚠ Возможные ошибки запуска

### 🛠 Ошибка при активации `venv\Scripts\activate` (Windows):
Решение:
1. Откройте PowerShell **от имени администратора**.
2. Выполните команду:
   ```bash
   Set-ExecutionPolicy RemoteSigned
   ```
3. Подтвердите, введя `A`.
4. Повторите активацию виртуального окружения.

### 🛠 Ошибка при загрузке `requirements.txt`:
Если на вашем устройстве установлено несколько версий Python, укажите путь к конкретной версии.  

#### Пример для Windows:
```bash
C:\path\to\python3.8\python.exe -m venv venv
```

#### Пример для macOS/Linux:
```bash
python3.8 -m venv venv
```

---

💡 **Совет:** Если у вас возникнут вопросы, создайте Issue в репозитории GitHub.
