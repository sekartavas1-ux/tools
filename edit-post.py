import requests

# Ganti dengan data Anda
POST_ID = "1234567890_987654321"
ACCESS_TOKEN = "Masukkan_Token_Anda_Di_Sini"
NEW_MESSAGE = "Ini adalah pesan yang sudah diperbarui menggunakan API."

url = f"https://graph.facebook.com/v19.0/{POST_ID}"

payload = {
    'message': NEW_MESSAGE,
    'access_token': ACCESS_TOKEN
}

try:
    response = requests.post(url, data=payload)
    response.raise_for_status()  # Angkat pengecualian untuk kode status HTTP yang buruk (4xx atau 5xx)

    if response.status_code == 200:
        print("✅ Post berhasil diperbarui!")
        print("Respons:", response.json())
    else:
        print(f"❌ Gagal memperbarui. Kode Status: {response.status_code}")
        print("Detail Error:", response.json())

except requests.exceptions.HTTPError as errh:
    print(f"Error HTTP: {errh}")
except requests.exceptions.RequestException as err:
    print(f"Error Lainnya: {err}")