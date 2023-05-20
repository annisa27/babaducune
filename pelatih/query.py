def sql_get_spesialisasi(id):
    return f"""
    SELECT Spesialisasi
    FROM SPESIALISASI S
    JOIN PELATIH_SPESIALISASI PS ON S.ID = PS.ID_Spesialisasi
    WHERE PS.ID_Pelatih = '{id}';
    """