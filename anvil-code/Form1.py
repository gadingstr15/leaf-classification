from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.gambar = None
    self.label_hasil.text = "Silakan upload gambar daun."

  def file_loader_1_change(self, file, **event_args):
    if file is None:
      self.label_hasil.text = "Silakan upload gambar terlebih dahulu."
      return
    self.gambar = file
    self.image_1.source = file
    self.label_hasil.text = "Gambar berhasil diupload, silakan klik Klasifikasi."

  def button_klasifikasi_click(self, **event_args):
    if not self.gambar:
      self.label_hasil.text = "Silakan upload gambar terlebih dahulu."
      return
    try:
      self.label_hasil.text = "Sedang klasifikasi..."
      # Kirim media file ke backend uplink
      hasil = anvil.server.call('klasifikasi_gambar', self.gambar)
      self.label_hasil.text = f"Hasil Klasifikasi: {hasil}"
    except Exception as e:
      self.label_hasil.text = f"Terjadi error: {e}"
      print(f"Error di UI: {e}")
