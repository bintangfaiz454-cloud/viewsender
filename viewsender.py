import requests
import time
import sys
import random

# WARNA PELANGI
B = '\033[1m'; G = '\033[92m'; Y = '\033[93m'; R = '\033[91m'; C = '\033[94m'; M = '\033[95m'; W = '\033[0m'
P = [C, M, R, Y, G, C]

def run_mata():
    # ASCII MEGA FIX
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

    target = input(f"{B}┌─[TARGET URL] └────► {W}")
    try:
        views = int(input(f"{B}┌─[JUMLAH VIEW] └────► {W}"))
    except:
        views = 10

    print(f"\n{Y}🚀 STARTING VIEW SENDER...{W}\n")

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
            headers = {'User-Agent': random.choice(user_agents)}
            # Hit langsung URL target (Metode paling cepat)
            response = session.get(target, headers=headers, timeout=5)
            
            if response.status_code == 200:
                print(f"{G}✅ VIEW {i} BERHASIL{W} ➔ {C}Total nambah {success + 1} view{W}")
                success += 1
            else:
                print(f"{R}❌ VIEW {i} GAGAL{W}")
                fail += 1
        except:
            print(f"{R}❌ VIEW {i} GAGAL (Lag){W}")
            fail += 1
        time.sleep(0.01)

    # RESPONS AKHIR YANG LU MAU
    print(f"\n{Y}══════════════════════════════════════════════════════════")
    print(f" RESULT: {G}{success} VIEW BERTAMBAH{W} (Gagal: {fail})")
    print(f" TARGET: {target}")
    print(f"══════════════════════════════════════════════════════════{W}\n")

if __name__ == "__main__":
    run_mata()
