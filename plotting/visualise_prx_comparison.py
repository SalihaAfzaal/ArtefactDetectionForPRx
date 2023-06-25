import matplotlib.pyplot as plt

def plot_comparison(pr1, pr2, pr3):
    """
        Vykresluje srovnání různých metod dokončení pro data PRx.

        Args:
            pr1 (seznam): Seznam dat PRx vyplněný pomocí prahové metody.
            pr2 (seznam): Seznam dat PRx vyplněný pomocí lineární interpolace.
            pr3 (seznam): Seznam dat PRx vyplněný pomocí polynomiální interpolace druhého řádu.

        Vrácení:
            Žádný

        Poznámka:
            Tato funkce využívá knihovnu Matplotlib ke generování grafu různých PRx dat a jejich příslušných metod dokončení.
        """
    plt.figure(figsize=(25,8))
    plt.rcParams.update({'font.size': 25})
    plt.title("Porovnání doplňovacích metod")

    plt.plot(pr1[0:420], color="violet", label="Prahovací metoda", linewidth=2)
    plt.plot(pr2[0:420], color="olive", label="Linearní interpolace", linewidth=3)
    plt.plot(pr3[0:420],'--', color="orange", label="Interpolace polynomem 2. řádu", linewidth=3)
    plt.plot(0,60)
    plt.ylim(-1.2,1.2)
    plt.xlabel("Čas(min)")
    plt.ylabel("PRx")
    plt.legend()
    # plt.savefig("Porovnani_prx.png", dpi=300)
    plt.show()
