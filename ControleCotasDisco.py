def converte_bytes_megabytes(tamanho_bytes):
    # Converte bytes para megabytes
    return round(tamanho_bytes / (1024 * 1024), 2)

def calcula_percentual_uso(tamanho_megabytes, total_megabytes):
    # Calcula o percentual de uso
    return round((tamanho_megabytes / total_megabytes) * 100, 2)

# Solicita ao usuário o número de entradas que deseja exibir
n = int(input("Quantos usuários você deseja ver no relatório? "))

# Lê o arquivo de usuários e armazena os dados em um dicionário
usuarios_dict = {}
with open('usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        usuario_dados = linha.split()
        usuarios_dict[usuario_dados[0]] = int(usuario_dados[1])

# Calcula o total de espaço ocupado por todos os usuários em megabytes
total_megabytes = converte_bytes_megabytes(sum(usuarios_dict.values()))

# Calcula o espaço médio ocupado
media_megabytes = round(total_megabytes / len(usuarios_dict), 2)

# Cria uma lista com os usuários e seus dados, incluindo o percentual de uso
usuarios_com_percentual = []
for usuario, tamanho_bytes in usuarios_dict.items():
    tamanho_megabytes = converte_bytes_megabytes(tamanho_bytes)
    percentual_uso = calcula_percentual_uso(tamanho_megabytes, total_megabytes)
    usuarios_com_percentual.append((usuario, tamanho_megabytes, percentual_uso))

# Ordena a lista de usuários com base no percentual de uso (do maior para o menor)
usuarios_com_percentual.sort(key=lambda x: x[2], reverse=True)

# Limita a lista aos n primeiros usuários
usuarios_com_percentual = usuarios_com_percentual[:n]

# Gera o relatório em formato TXT
with open('relatório.txt', 'w') as relatorio_txt:
    relatorio_txt.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    relatorio_txt.write("--------------------------------------------------------------\n")
    relatorio_txt.write(f"Mostrando os {n} usuários que mais consomem espaço:\n\n")
    relatorio_txt.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")
    
    for i, (usuario, tamanho_megabytes, percentual_uso) in enumerate(usuarios_com_percentual, start=1):
        relatorio_txt.write(f"{i:<4} {usuario:<15} {tamanho_megabytes:>10.2f} MB          {percentual_uso:>6.2f}%\n")

    # Adiciona os campos do espaço total e médio ocupado
    relatorio_txt.write("\n--------------------------------------------------------------\n")
    relatorio_txt.write(f"Espaço total ocupado: {total_megabytes:>10.2f} MB\n")
    relatorio_txt.write(f"Espaço médio ocupado: {media_megabytes:>10.2f} MB\n")

print("Relatório TXT gerado com sucesso!")

# Gera o relatório em formato HTML
with open('relatório.html', 'w') as relatorio_html:
    relatorio_html.write("<html>\n<head>\n<title>Relatório de Uso de Disco</title>\n</head>\n<body>\n")
    relatorio_html.write("<h1>ACME Inc. - Uso do espaço em disco pelos usuários</h1>\n")
    relatorio_html.write("<table border='1' style='width:50%; text-align:left;'>\n")
    relatorio_html.write("<tr><th>Nr.</th><th>Usuário</th><th>Espaço utilizado (MB)</th><th>% do uso</th></tr>\n")
    
    for i, (usuario, tamanho_megabytes, percentual_uso) in enumerate(usuarios_com_percentual, start=1):
        relatorio_html.write(f"<tr><td>{i}</td><td>{usuario}</td><td>{tamanho_megabytes:.2f}</td><td>{percentual_uso:.2f}%</td></tr>\n")
    
    relatorio_html.write("</table>\n")
    
    # Adiciona os campos do espaço total e médio ocupado
    relatorio_html.write("<p><strong>Espaço total ocupado:</strong> {:.2f} MB</p>\n".format(total_megabytes))
    relatorio_html.write("<p><strong>Espaço médio ocupado:</strong> {:.2f} MB</p>\n".format(media_megabytes))
    
    relatorio_html.write("</body>\n</html>")

print("Relatório HTML gerado com sucesso!")