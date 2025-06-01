!pip install anvil-uplink numpy pillow tensorflow keras

import anvil.server
import io
import numpy as np
from PIL import Image
from keras.models import load_model

# Sambungkan ke Anvil project Anda dengan Uplink key (ganti dengan Uplink key Anda)
ANVIL_UPLINK_KEY = "server_75PXBMV26UWHAY5GP3NURKGY-OYPOUP4XBOVQZ7GO"
anvil.server.connect(ANVIL_UPLINK_KEY)

# Load model sekali saat start
model = load_model('WDaun.h5')

label_kelas = ['Dikotil', 'Monokotil']

@anvil.server.callable
def klasifikasi_gambar(file):
    try:
        print(f"Menerima file: {file.name}")
        image_bytes = file.get_bytes()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB").resize((128,128))
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0).astype('float32')

        prediction = model.predict(img_array)[0]
        kelas = label_kelas[np.argmax(prediction)]
        print(f"Hasil prediksi: {kelas}")
        return kelas
    except Exception as e:
        print(f"Error di uplink: {e}")
        return "Error pada klasifikasi"

# Jalankan agar Uplink tetap aktif dan menerima event
anvil.server.wait_forever()
