Kurulum

    Bu depoyu klonlayın veya indirin.

    bash

git clone https://github.com/kabin-guvenligi-sistemi.git

Anaconda veya benzeri bir sanal ortamda bir ortam oluşturun ve aktif hale getirin.

lua

conda create --name kabin-guvenligi-sistemi python=3.8
conda activate kabin-guvenligi-sistemi

Gerekli kütüphaneleri yükleyin.

pip install -r requirements.txt

Verileri indirin ve ön işlem yapın.

python data_preparation.py

Modeli eğitin.

python train_model.py

Model performansını test edin.

    python test_model.py

Not: İlgili veri dosyaları, eğitim, test veri setleri, eğitilmiş model dosyaları ve kaynak kodlar depoda mevcuttur.