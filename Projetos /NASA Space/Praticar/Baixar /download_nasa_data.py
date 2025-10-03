import earthaccess
import os

# --- 1. LOGIN ---
earthaccess.login()

# --- 2. CONFIGURAÇÃO GLOBAL ---
DOWNLOAD_DIR = "climate_data"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Período (últimos 3 meses)
TEMPORAL_RANGE = ("2025-07-01", "2025-10-01")

# --- 3. LISTA DE PRODUTOS ---
# Cada entrada = (Categoria, Short Name, Descrição)
PRODUCTS = [
    # Atmosféricos
    ("Atmosfera", "AIRS3STD", "Temperatura/Umidade do ar (AIRS - Aqua)"),
    ("Atmosfera", "M2I3NPASM", "Pressão atmosférica (MERRA-2)"),
    ("Atmosfera", "ASCATA-L2-25km", "Vento oceânico (ASCAT)"),
    ("Atmosfera", "MOD08_D3", "Nuvens/Aerossóis (MODIS Terra)"),
    ("Atmosfera", "CERES_EBAF_Ed4.2", "Radiação Terra-Sol (CERES)"),

    # Terrestres
    ("Terra", "SMAP_L3_SM_P_E", "Umidade do solo (SMAP)"),
    ("Terra", "MOD13Q1", "NDVI Vegetação (MODIS Terra)"),
    ("Terra", "MOD11A1", "Temperatura da superfície terrestre (MODIS)"),
    ("Terra", "ATL06", "Altura do gelo (ICESat-2)"),

    # Oceânicos
    ("Oceano", "SMAP_L3_SSS_P_E", "Salinidade da superfície do mar (SMAP)"),
    ("Oceano", "S6A_L2_NRT_NTC_F07", "Altimetria oceânica (Sentinel-6)"),
    ("Oceano", "MODISA_L3m_CHL", "Cor do oceano (Clorofila-a, MODIS Aqua)"),
]

# --- 4. LOOP DE DOWNLOAD ---
for category, short_name, desc in PRODUCTS:
    print(f"\n=== {category.upper()} → {desc} ({short_name}) ===")

    # Pasta por categoria
    save_path = os.path.join(DOWNLOAD_DIR, category)
    os.makedirs(save_path, exist_ok=True)

    try:
        results = earthaccess.search_data(
            short_name=short_name,
            temporal=TEMPORAL_RANGE
        )
        if not results:
            print("⚠ Nenhum dado encontrado nesse período.")
            continue

        print(f"Encontrados {len(results)} arquivos. Baixando...")
        files = earthaccess.download(results, local_path=save_path)
        print(f"✅ Download concluído! {len(files)} arquivos salvos em {save_path}")

    except Exception as e:
        print(f"❌ Erro ao baixar {short_name}: {e}")
    except Exception as e:
        print(f"❌ Erro ao baixar {short_name}: {e}")
