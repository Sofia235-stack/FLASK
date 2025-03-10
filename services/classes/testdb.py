import psycopg2

try:
    conn = psycopg2.connect("dbname='gestion_etablisseement' user='postgres' password='passer' host='localhost'")
    print("Connexion réussie !")
except Exception as e:
    print("Erreur de connexion :", e)
