print("--- 📖 MEU DIÁRIO PYTHON ---")

while True:
    print("\nMENU:")
    print("1 - Escrever no diário")
    print("2 - Ler diário completo")
    print("3 - Sair")

    try:
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            texto = input("\nO que você está pensando? ")
            # Abrimos o arquivo no modo 'a' (append/acrescentar)
            with open("diario.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(texto + "\n")
            print("✅ Pensamento salvo com sucesso!")

        elif opcao == 2:
            print("\n📜 RELEMBRANDO SEUS PENSAMENTOS:")
            try:
                # Abrimos no modo 'r' (read/ler)
                with open("diario.txt", "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                    if not conteudo:
                        print("O diário ainda está vazio.")
                    else:
                        print(conteudo)
            except FileNotFoundError:
                print("⚠️ O arquivo ainda não existe. Escreva algo no seu diário!")

        elif opcao == 3:
            print("Fechando diário... Até amanhã!")
            break

        else:
            print("⚠️ Opção inválida!")

    except ValueError:
        print("❌ Erro: Digite apenas números (1, 2 ou 3).")
