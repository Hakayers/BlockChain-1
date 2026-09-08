from blockchain import Blockchain


blockchain = Blockchain()


# Simulasi Smart Contract
# Aturan pembagian royalti:
# - Kreator/Penyanyi = 60%
# - Produser = 20%
# - Penulis Lagu = 15%
# - Platform Musik = 5%

def smart_contract_royalti(song_id, judul, total_royalti):

    pembagian = {
        "Kreator/Penyanyi": 0.60,
        "Produser": 0.20,
        "Penulis Lagu": 0.15,
        "Platform Musik": 0.05
    }

    for actor, persen in pembagian.items():

        jumlah = total_royalti * persen

        blockchain.add_block({
            "song_id": song_id,
            "judul": judul,
            "actor": actor,
            "jenis_transaksi": "Distribusi Royalti",
            "persentase": f"{persen * 100:.0f}%",
            "jumlah_royalti": jumlah,
            "status": "Berhasil"
        })


# Contoh transaksi royalti lagu
smart_contract_royalti(
    song_id="MUSIC-001",
    judul="Langit Digital",
    total_royalti=1000000
)


for block in blockchain.chain:

    print("=" * 60)
    print("INDEX :", block.index)
    print("DATA  :", block.data)
    print("PREV  :", block.previous_hash)
    print("HASH  :", block.hash)


print("\nBlockchain valid:", blockchain.is_valid())