graph = {
             'Anggi home': ['Subang'],
             'Subang': ['Jalan Cagak'],
             'Jalan Cagak': ['Ciater'],
             'Ciater': ['Cikole'],
             'Cikole': ['Lembang'],
             'Lembang': ['Setiabudhi'],
             'Setiabudhi': ['Gegerkalong'],
             'Gegerkalong': ['Sariasih'],
             'Sariasih': ['Sarijadi'],
             'Sarijadi': ['Poltekpos'],
             'Poltekpos': ['Sarijadi','Sariasih']
        }

def mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[]):
        jalur = jalur + [jalanawal]
        if jalanawal == jalantujuan:
            return jalur
            if not graph.has_key(jalanawal):
                    return None
        jalurpendek = None
        for node in graph[jalanawal]:
            if node not in jalur:
                newjalur = mencari_jalur_terpendek(graph, node, jalantujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Jalan Raya Dari Anggi Homes Sampai Kampus Politeknik Pos Indonesia")
print("(Anggi Homes, Subang, Jalan Cagak, Ciater, Cikole, Lembang)")
print("(Setiabudhi, Gegerkalong, Sariasih, Sarijadi, Poltekpos)")
print("\n")
jalanawal = raw_input("Masukan jalanawal : ")
jalantujuan = raw_input("Masukan jalantujuan : ")
hasil = mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[])
print "Jalur Terpendek", hasil