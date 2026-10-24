# Portfolyo Botu

Discord üzerinden kişisel projelerinizi ekleyip yönetebileceğiniz, SQLite tabanlı bir Discord botu. Her kullanıcı yalnızca kendi projelerini görüntüleyebilir, güncelleyebilir ve silebilir.

## Özellikler

- Kullanıcıya özel proje listesi
- Proje adı, bağlantı ve durum bilgisi ile proje ekleme
- Projelere yetenek (skill) ekleme
- Proje bilgilerini güncelleme
- Proje silme
- Hazır durum ve yetenek listeleri
- SQLite ile kalıcı veri saklama

## Komutlar

| Komut | Açıklama |
| --- | --- |
| `!start` | Botu başlatır ve komut özetini gösterir. |
| `!info` | Kullanılabilir komutları listeler. |
| `!new_project` | Yeni bir proje ekler. |
| `!projects` | Kullanıcının projelerini listeler. |
| `!skills` | Seçilen projeye yetenek ekler. |
| `!update_projects` | Seçilen projenin bilgilerini günceller. |
| `!delete` | Seçilen projeyi siler. |

## Kurulum

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/kagan-u/PortfolioBot.git
   cd PortfolioBot
   ```

2. Sanal ortam oluşturup etkinleştirin:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Bağımlılıkları yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

4. `config.py` dosyasında Discord bot token'ınızı ve veritabanı yolunu ayarlayın:

   ```python
   DATABASE = "portfolyo.db"
   TOKEN = "DISCORD_BOT_TOKEN"
   ```

   > `TOKEN` değerini asla herkese açık bir depoya eklemeyin. Gerçek token'ı ortam değişkeni veya yerel bir yapılandırma dosyası üzerinden yönetmeniz önerilir.

5. Veritabanını ilk kez oluşturun:

   ```bash
   python logic.py
   ```

   Bu komut `projects`, `skills`, `project_skills` ve `status` tablolarını oluşturur ve varsayılan yetenek/durum kayıtlarını ekler. `portfolyo.db` dosyası zaten mevcutsa bu adımı atlayın.

6. Botu çalıştırın:

   ```bash
   python bot.py
   ```

## Proje Yapısı

| Dosya | Açıklama |
| --- | --- |
| `bot.py` | Discord botu ve komutlar. |
| `logic.py` | SQLite veritabanı işlemleri. |
| `config.py` | Veritabanı yolu ve bot token ayarları. |
| `modal.py` | Discord modal/buton kullanımına dair örnek. |
| `requirements.txt` | Python bağımlılıkları. |

## Veritabanı Şeması

- **projects**: `project_id`, `user_id`, `project_name`, `description`, `url`, `status_id`
- **skills**: `skill_id`, `skill_name`
- **project_skills**: `project_id`, `skill_id`
- **status**: `status_id`, `status_name`

## Gereksinimler

- Python 3.8+
- `discord.py`
