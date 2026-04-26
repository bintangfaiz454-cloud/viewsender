import requests
import time
import sys
import random

# WARNA PELANGI (ANSI)
B = '\033[1m'; G = '\033[92m'; Y = '\033[93m'; R = '\033[91m'; C = '\033[94m'; M = '\033[95m'; W = '\033[0m'
P = [C, M, R, Y, G, C]

def run_mata():
    # JUDUL ASCII MEGA (Sesuai permintaan lu!)
    # Pakai r"" (raw string) supaya \ tidak bikin error SyntaxWarning
    print(f"{P[0]}  __      _______ ________          __                   ")
    print(f"{P[1]}  \\ \\    / /_   _|  ____\\ \\        / /                   ")
    print(f"{P[2]}   \\ \\  / /  | | | |__   \\ \\  /\\  / /                    ")
    print(f"{P[3]}    \\ \\/ /   | | |  __|   \\ \\/  \\/ /                     ")
    print(f"{P[4]}     \\  /   _| |_| |____   \\  /\\  /                      ")
    print(f"{P[5]}   __\\/_ _|_____|______|___\\/__\\/__ _____               ")
    print(f"{P[0]}  / ____|  ____| \\ | |  __ \\|  ____|  __ \\              ")
    print(f"{P[1]} | (___ | |__  |  \\| | |  | | |__  | |__) |             ")
    print(f"{P[2]}  \\___ \\|  __| | . ` | |  | |  __| |  _  /              ")
    print(f"{P[3]}  ____) | |____| |\\  | |__| | |____| | \\ \\              ")
    print(f"{P[4]} |_____/|______|_|_\\_|_____/|______|_|__\\_\\_____ ______ ")
    print(f"{P[5]} \\ \\        / /  ____|  _ \\ / ____|_   _|__   __|  ____|")
    print(f"{P[0]}  \\ \\  /\\  / /| |__  | |_) | (___   | |    | |  | |__   ")
    print(f"{P[1]}   \\ \\/  \\/ / |  __| |  _ < \\___ \\  | |    | |  |  __|  ")
    print(f"{P[2]}    \\  /\\  /  | |____| |_) |____) |_| |_   | |  | |____ ")
    print(f"{P[3]}     \\/  \\/   |______|____/|_____/|_____|  |_|  |______|")
    print(f"{Y}{B}           >> VIEW SENDER WEBSITE BY BINTANG <<{W}\n")

    print(f"{C}{B}╔══════════════════════════════════════════════════════════╗")
    print(f"║              - VIEWSENDER WEBSITE -                                 ║")          
    print(f"║        Penambah Views Pada Website - By Bintang.                    ║")
    print(f"║             Simple | Cepat | Work 100%                              ║")
    print(f"╚══════════════════════════════════════════════════════════╝{W}")

    target = input(f"\n{B}┌─[MASUKKAN URL TARGET]\n└────► {W}")
    try:
        views = int(input(f"{B}┌─[MASUKKAN JUMLAH VIEWS]\n└────► {W}"))
    except:
        views = 10

    print(f"\n{Y}══════════════════════════════════════════════════════════")
    print(f" TARGET: {target}\n TOTAL VIEWS: {views}")
    print(f"══════════════════════════════════════════════════════════{W}")

    # LOADING BAR (Super Fast)
    print(f"\n⏳ MENYIAPKAN MATA SERVER...", end="")
    for i in range(30):
        sys.stdout.write(f"{P[i%6]}█{W}"); sys.stdout.flush(); time.sleep(0.02)
    print(f" {C}100%{W}\n")

    success, fail = 0, 0
    session = requests.Session()
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)"
    ]

    for i in range(1, views + 1):
        try:
            # METODE TINGKAT DEWA: Hit Langsung URL + UserAgent Random
            headers = {'User-Agent': random.choice(user_agents)}
            response = session.get(target, headers=headers, timeout=5)
            
            if response.status_code == 200:
                print(f"{G}✅ VIEW {i}/{views} BERHASIL{W}")
                success += 1
            else:
                print(f"{R}❌ VIEW {i}/{views} GAGAL (Code: {response.status_code}){W}")
                fail += 1
        except:
            print(f"{R}❌ VIEW {i}/{views} GAGAL (Timeout/Lag){W}")
            fail += 1
        time.sleep(0.01)

    print(f"\n{Y}══════════════════════════════════════════════════════════")
    print(f" PROSES SELESAI!")
    print(f"{G}✅ BERHASIL : {success} views{W}")
    print(f"{R}❌ GAGAL    : {fail} views{W}")
    print(f" TARGET   : {target}")
    print(f"══════════════════════════════════════════════════════════{W}")

if __name__ == "__main__":
    run_mata()
