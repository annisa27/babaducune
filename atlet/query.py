def sql_get_pelatih_atlet(id):
    return f""" 
    SELECT M.nama
    FROM ATLET_PELATIH AP
        JOIN PELATIH P ON P.ID = AP.ID_Pelatih
        JOIN ATLET A ON A.ID = AP.ID_ATLET
        JOIN MEMBER M ON P.ID = M.ID
    WHERE A.ID = '{id}';
    """



def sql_get_status_kualifikasi(id):
    return f"""
    SELECT 
        K.World_Rank,
        K.World_Tour_Rank,
        CASE
            WHEN K.ID_Atlet IS NOT NULL THEN 'Qualified'
            ELSE 'Not Qualified'
        END AS status_kualifikasi
    FROM ATLET A
    LEFT JOIN ATLET_KUALIFIKASI K ON K.ID_Atlet = A.ID
    LEFT JOIN ATLET_NON_KUALIFIKASI N ON N.ID_Atlet = A.ID
    WHERE A.ID = '{id}';
    """

def sql_get_total_point(id):
    return f"""
    SELECT 
        SUM(total_point) as total_point
    FROM ATLET A
    JOIN POINT_HISTORY PH ON PH.ID_Atlet = A.ID
    WHERE A.ID = '{id}';
    """