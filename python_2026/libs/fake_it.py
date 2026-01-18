from faker import Faker

if __name__ == '__main__':
    # Polish locale
    fake_pl = Faker('pl_PL')
    # Korean locale
    fake_ko = Faker('ko_KR')
    # Danish locale
    fake_dn = Faker('da_DK')

    print("=== POLISH DATA ===")
    for i in range(300):
        print(f"{i + 1}. Name: {fake_pl.name()}")
        # print(f"   Address: {fake_pl.address()}")
        # print(f"   Person ID (PESEL): {fake_pl.pesel()}")
        print()

    # print("\n=== KOREAN DATA ===")
    # for i in range(10):
    #     print(f"{i + 1}. Name: {fake_ko.name()}")
    #     print(f"   Address: {fake_ko.address()}")
    #     print(f"   Person ID (SSN): {fake_ko.ssn()}")
    #     print()
    #
    # print("\n=== DANISH DATA ===")
    # for i in range(10):
    #     print(f"{i + 1}. Name: {fake_dn.name()}")
    #     print(f"   Address: {fake_dn.address()}")
    #     print(f"   Person ID (SSN): {fake_dn.ssn()}")
    #     print()
