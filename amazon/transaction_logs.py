from typing import List


def process_logs(logs: List[str], threshold: int) -> List[str]:
    frq = {}
    for s in logs:
        tx = s.split(" ")
        if len(tx) != 3:
            continue
        sender = tx[0]
        receiver = tx[1]
        print("sender: ", sender, " receiver: ", receiver)
        frq[sender] = frq.get(sender, 0) + 1
        if receiver != sender:
            frq[receiver] = frq.get(receiver, 0) + 1

    print(frq)

    users = [int(k) for k, v in frq.items() if v >= threshold]

    users.sort()
    return users


if __name__ == "__main__":
    print(process_logs(["88 99 200", "88 99 300", "99 32 100", "12 12 15"], 2))
