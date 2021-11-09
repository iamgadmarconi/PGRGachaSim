if __name__ == "__main__":
    from copies import Copies
    ans = input("Enter the number of copies: ")
    cur = input("Pick the currency (CHF/EUR): ")
    sim = Copies(ans)
    sim.averageprice(cur)
    print(sim.__str__())
