import anvil.server
import io
import numpy as np
from PIL import Image
from keras.models import load_model

# Load model sekali saat module di-load
model = load_model('WDaun.h5')

# Label kelas sesuai model Anda
label_kelas = ['Dikotil', 'Monokotil']

@anvil.server.callable
def klasifikasi_gambar(file):
  try:
    # Dapatkan bytes gambar dari file media Anvil
    image_bytes = file.get_bytes()
    # Buka dan resize gambar sesuai input model
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB").resize((128,128))
    # Preprocessing input sesuai model
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0).astype('float32')
    # Prediksi kelas
    prediction = model.predict(img_array)[0]
    kelas = label_kelas[np.argmax(prediction)]
    return kelas
  except Exception as e:
    print(f"Error saat klasifikasi: {e}")
    return "Error klasifikasi"