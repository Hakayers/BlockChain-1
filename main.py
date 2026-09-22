from blockchain import Blockchain
from pow import proof_of_work
from pos import proof_of_stake


blockchain = Blockchain()


# Simulasi Smart Contract Royalti
def smart_contract_royalti(song_id, judul, total_royalti, difficulty):

    pembagian = {
        "Kreator/Penyanyi": 0.60,
        "Produser": 0.20,
        "Penulis Lagu": 0.15,
        "Platform Musik": 0.05
    }

    distribusi = {}

    for actor, persen in pembagian.items():
        jumlah = total_royalti * persen

        distribusi[actor] = {
            "persentase": f"{persen * 100:.0f}%",
            "jumlah_royalti": jumlah
        }

    # Membuat SATU block untuk seluruh distribusi royalti
    blockchain.add_block({
        "song_id": song_id,
        "judul": judul,
        "jenis_transaksi": "Distribusi Royalti",
        "distribusi": distribusi,
        "status": "Berhasil"
    })

    # Mengambil block terakhir
    block = blockchain.chain[-1]

    # Menambahkan nonce untuk PoW
    block.nonce = 0

    # Mining dilakukan SATU KALI
    proof_of_work(block, difficulty)


# =========================
# ATUR DIFFICULTY
# =========================

difficulty = 5

smart_contract_royalti(
    song_id="MUSIC-001",
    judul="Langit Digital",
    total_royalti=1000000,
    difficulty=difficulty
)


# Menampilkan blockchain
for block in blockchain.chain:

    print("=" * 60)
    print("INDEX :", block.index)
    print("DATA  :", block.data)
    print("PREV  :", block.previous_hash)
    print("HASH  :", block.hash)

    if hasattr(block, "nonce"):
        print("NONCE :", block.nonce)


print("\nBlockchain valid:", blockchain.is_valid())


# =========================
# SIMULASI PROOF OF STAKE
# =========================

validators = {
    "Kreator/Penyanyi": 70,
    "Produser": 10,
    "Penulis Lagu": 10,
    "Platform Musik": 10
}

for i in range(20):
    validator = proof_of_stake(validators)
    print("Simulasi", i + 1, ":", validator)

print("\nValidator PoS terpilih:", validator)