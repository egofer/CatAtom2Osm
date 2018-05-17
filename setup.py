# -*- coding: utf-8 -*-
"""Application preferences"""
from __future__ import unicode_literals
from builtins import range, str
import six
import sys, os, locale
import csv
import gettext

app_name = 'CatAtom2Osm'
app_version = '1.1.7dev'
app_author = str(u'Javier Sánchez Portero')
app_copyright = u'2017, Javier Sánchez Portero'
app_desc = 'Tool to convert INSPIRE data sets from the Spanish Cadastre ATOM Services to OSM files'
app_tags = ''

MIN_QGIS_VERSION_INT = 21001
MIN_QGIS_VERSION = '2.10.1'
MIN_GDAL_VERSION_INT = 11103
MIN_GDAL_VERSION = '1.11.3'

def winenv():
    global eol, encoding
    eol = '\n'
    if platform.startswith('win'):
        eol = '\r\n'
        if os.getenv('LANG') is None:
            os.environ['LANG'] = language

locale.setlocale(locale.LC_ALL, '')
language, encoding = locale.getdefaultlocale()
app_path = os.path.dirname(__file__)
localedir = os.path.join(app_path, 'locale', 'po')
platform = sys.platform
winenv()

if six.PY2:
    gettext.install(app_name.lower(), localedir=localedir, unicode=1)
else:
    gettext.install(app_name.lower(), localedir=localedir)
gettext.bindtextdomain('argparse', localedir)
gettext.textdomain('argparse')

log_level = 'INFO' # Default log level
log_file = 'catatom2osm.log'
log_format = '%(asctime)s - %(levelname)s - %(message)s'

fn_prefix = 'A.ES.SDGC' # Inspire Atom file name prefix

silence_gdal = False

delimiter = '\t'
dup_thr = 0.012 # Distance in meters to merge nearest vertexs.
                # 0.011 is about 1E-7 degrees in latitude
dist_thr = 0.02 # Threshold in meters for vertex simplification and topological points.
straight_thr = 2 # Threshold in degrees from straight angle to delete a vertex
acute_thr = 10 # Remove vertices with an angle smaller than this value
min_area = 0.05 # Delete geometries with an area smaller than this value
addr_thr = 10 # Distance in meters to merge address node with building footprint
acute_inv = 5 # Remove geometries/rings that result invalid after removing any vertex with an angle smaller than this value
dist_inv = 0.1 # Threshold in meters to filter angles for zig-zag and spikes
entrance_thr = 0.4 # Minimum distance in meters from a entrance to the nearest corner
warning_min_area = 1 # Area in m2 for small area warning
warning_max_area = 30000 # Area in m2 for big area warning

changeset_tags = {
    'comment': "#Spanish_Cadastre_Buildings_Import",
    'source': u"Dirección General del Catastro",
    'type': 'import',
    'url': "https://wiki.openstreetmap.org/wiki/Spanish_Cadastre/Buildings_Import" 
}

base_url = {
    "BU": "http://www.catastro.minhap.es/INSPIRE/buildings/",
    "AD": "http://www.catastro.minhap.es/INSPIRE/addresses/",
    "CP": "http://www.catastro.minhap.es/INSPIRE/CadastralParcels/"
}

serv_url = {
    "BU": base_url['BU'] + "ES.SDGC.BU.atom.xml",
    "AD": base_url['AD'] + "ES.SDGC.AD.atom.xml",
    "CP": base_url['CP'] + "ES.SDGC.CP.atom.xml"
}

prov_url = {
    "BU": base_url['BU'] + "{code}/ES.SDGC.bu.atom_{code}.xml",
    "AD": base_url['AD'] + "{code}/ES.SDGC.ad.atom_{code}.xml",
    "CP": base_url['CP'] + "{code}/ES.SDGC.CP.atom_{code}.xml"
}

cadastre_doc_url = 'http://ovc.catastro.meh.es/OVCServWeb/OVCWcfLibres/OVCFotoFachada.svc/RecuperarFotoFachadaGet?ReferenciaCatastral={}'

valid_provinces = ["%02d" % i for i in range(2,57) if i not in (20, 31, 48)]

no_number = 'S-N' # Regular expression to match addresses without number

lowcase_words = [ # Words to exclude from the general Title Case rule for highway names
    'DE', 'DEL', 'EL', 'LA', 'LOS', 'LAS', 'Y', 'AL', 'EN',
    'A LA', 'A EL', 'A LOS', 'DE LA', 'DE EL', 'DE LOS', 'DE LAS',
    'ELS', 'LES', "L'", "D'", "N'", "S'", "NA", "DE NA", "SES", "DE SES",
    "D'EN", "D'EL", "D'ES", "DE'N", "DE'L", "DE'S"
]

highway_types_es = { 
    'AG': str(u'Agregado'),
    'AL': str(u'Aldea/Alameda'),
    'AR': str(u'Área/Arrabal'),
    'AU': str(u'Autopista'),
    'AV': str(u'Avenida'),
    'AY': str(u'Arroyo'),
    'BJ': str(u'Bajada'),
    'BO': str(u'Barrio'),
    'BR': str(u'Barranco'),
    'CA': str(u'Cañada'),
    'CG': str(u'Colegio/Cigarral'),
    'CH': str(u'Chalet'),
    'CI': str(u'Cinturón'),
    'CJ': str(u'Calleja/Callejón'),
    'CL': str(u'Calle'),
    'CM': str(u'Camino/Carmen'),
    'CN': str(u'Colonia'),
    'CO': str(u'Concejo/Colegio'),
    'CP': str(u'Campa/Campo'),
    'CR': str(u'Carretera/Carrera'),
    'CS': str(u'Caserío'),
    'CT': str(u'Cuesta/Costanilla'),
    'CU': str(u'Conjunto'),
    'CY': str(u'Caleya'),
    'DE': str(u'Detrás'),
    'DP': str(u'Diputación'),
    'DS': str(u'Diseminados'),
    'ED': str(u'Edificios'),
    'EM': str(u'Extramuros'),
    'EN': str(u'Entrada/Ensanche'),
    'ER': str(u'Extrarradio'),
    'ES': str(u'Escalinata'),
    'EX': str(u'Explanada'),
    'FC': str(u'Ferrocarril/Finca'),
    'FN': str(u'Finca'),
    'GL': str(u'Glorieta'),
    'GR': str(u'Grupo'),
    'GV': str(u'Gran Vía'),
    'HT': str(u'Huerta/Huerto'),
    'JR': str(u'Jardines'),
    'LD': str(u'Lado/Ladera'),
    'LG': str(u'Lugar'),
    'MC': str(u'Mercado'),
    'ML': str(u'Muelle'),
    'MN': str(u'Município'),
    'MS': str(u'Masías'),
    'MT': str(u'Monte'),
    'MZ': str(u'Manzana'),
    'PB': str(u'Poblado'),
    'PD': str(u'Partida'),
    'PJ': str(u'Pasaje/Pasadizo'),
    'PL': str(u'Polígono'),
    'PM': str(u'Páramo'),
    'PQ': str(u'Parroquia/Parque'),
    'PR': str(u'Prolongación/Continuación'),
    'PS': str(u'Paseo'),
    'PT': str(u'Puente'),
    'PZ': str(u'Plaza'),
    'QT': str(u'Quinta'),
    'RB': str(u'Rambla'),
    'RC': str(u'Rincón/Rincona'),
    'RD': str(u'Ronda'),
    'RM': str(u'Ramal'),
    'RP': str(u'Rampa'),
    'RR': str(u'Riera'),
    'RU': str(u'Rúa'),
    'SA': str(u'Salida'),
    'SD': str(u'Senda'),
    'SL': str(u'Solar'),
    'SN': str(u'Salón'),
    'SU': str(u'Subida'),
    'TN': str(u'Terrenos'),
    'TO': str(u'Torrente'),
    'TR': str(u'Travesía/Transversal'),
    'UR': str(u'Urbanización'),
    'VR': str(u'Vereda'),
    'AC': str(u'Acceso'),
    'AD': str(u'Aldea'),
    'BV': str(u'Bulevar'),
    'CZ': str(u'Calzada'),
    'PA': str(u'Paralela'),
    'PC': str(u'Placeta/Plaça'),
    'PG': str(u'Polígono'),
    'PO': str(u'Polígono'),
    'SB': str(u'Subida'),
    'SC': str(u'Sector'),
    'CALLEJON': str(u'Callejón'), 'CANTON': str(u'Cantón'),
    'CIRCUNVALACION': str(u'Circunvalación'), 'GENERICA': str(u'Genérica'),
    'JARDIN': str(u'Jardín'), 'MALECON': str(u'Malecón'), 'RINCON': str(u'Rincón'),
    'PROLONGACION': str(u'Prolongación'), 'TRANSITO': str(u'Tránsito'),
    'TRAVESIA': str(u'Travesía'), 'VIA': str(u'Vía')
}

highway_types_cat = {
    'AG': str(u'Agregat'),
    'AL': str(u'Llogaret'),
    'AR': str(u'Àrea/Raval'),
    'AU': str(u'Autopista'),
    'AV': str(u'Avinguda'),
    'AY': str(u'Rierol'),
    'BJ': str(u'Baixada'),
    'BO': str(u'Barri'),
    'BR': str(u'Barranc'),
    'CA': str(u'Camí ramader'),
    'CG': str(u'Col·legi/Cigarral'),
    'CH': str(u'Xalet'),
    'CI': str(u'Cinturó/Ronda'),
    'CJ': str(u'Carreró'),
    'CL': str(u'Carrer'),
    'CM': str(u'Camí'),
    'CN': str(u'Colònia'),
    'CO': str(u'Ajuntament/Col·legi'),
    'CP': str(u'Camp'),
    'CR': str(u'Carretera'),
    'CS': str(u'Mas'),
    'CT': str(u'Costa/Rost'),
    'CU': str(u'Conjunt'),
    'CY': str(u'Carreró'),
    'DE': str(u'Darrere'),
    'DP': str(u'Diputació'),
    'DS': str(u'Disseminats'),
    'ED': str(u'Edificis'),
    'EM': str(u'Extramurs/Raval'),
    'EN': str(u'Entrada/Eixample'),
    'ER': str(u'Extraradi/Raval'),
    'ES': str(u'Escalinata'),
    'EX': str(u'Pla'),
    'FC': str(u'Ferrocarril'),
    'FN': str(u'Finca'),
    'GL': str(u'Rotonda/Plaça'),
    'GR': str(u'Grup'),
    'GV': str(u'Gran Via'),
    'HT': str(u'Hort'),
    'JR': str(u'Jardins'),
    'LD': str(u'Marge/Vessant'),
    'LG': str(u'Lloc'),
    'MC': str(u'Mercat'),
    'ML': str(u'Moll'),
    'MN': str(u'Municipi'),
    'MS': str(u'Masies'),
    'MT': str(u'Muntanya'),
    'MZ': str(u'Illa'),
    'PB': str(u'Poblat'),
    'PD': str(u'Partida'),
    'PJ': str(u'Passatge'),
    'PL': str(u'Polígon'),
    'PM': str(u'Erm'),
    'PQ': str(u'Parròquia/Parc'),
    'PR': str(u'Prolongació/Continuació'),
    'PS': str(u'Passeig'),
    'PT': str(u'Pont'),
    'PZ': str(u'Plaça'),
    'QT': str(u'Quinta'),
    'RB': str(u'Rambla'),
    'RC': str(u'Racó'),
    'RD': str(u'Ronda'),
    'RM': str(u'Branc'),
    'RP': str(u'Rampa'),
    'RR': str(u'Riera'),
    'RU': str(u'Rua'),
    'SA': str(u'Sortida'),
    'SD': str(u'Sender'),
    'SL': str(u'Solar'),
    'SN': str(u'Saló'),
    'SU': str(u'Pujada'),
    'TN': str(u'Terrenys'),
    'TO': str(u'Torrent'),
    'TR': str(u'Travessera'),
    'UR': str(u'Urbanització'),
    'VR': str(u'Sendera'),
    'AC': str(u'Accès'),
    'AD': str(u'Llogaret'),
    'BV': str(u'Bulevard'),
    'CZ': str(u'Calçada'),
    'PA': str(u'Paral·lel'),
    'PC': str(u'Placeta/plaça'),
    'PG': str(u'Polígon'),
    'PO': str(u'Polígon'),
    'SB': str(u'Pujada'),
    'SC': str(u'Sector'),
}

place_types_es = [
	'Agregado', 'Aldea', str(u'Área'), 'Barrio', 'Barranco', str(u'Cañada'), 'Colegio', 
	'Cigarral', 'Chalet', 'Concejo', 'Campa', 'Campo', str(u'Caserío'), 'Conjunto', 
	str(u'Diputación'), 'Diseminados', 'Edificios', 'Extramuros', 'Entrada', 
	'Ensanche', 'Extrarradio', 'Finca', 'Grupo', 'Huerta', 'Huerto', 
	'Jardines', 'Lugar', 'Mercado', 'Muelle', 'Municipio', str(u'Masías'), 'Monte', 
	'Manzana', 'Poblado', 'Partida', str(u'Polígono'), str(u'Páramo'), 'Parroquia', 'Solar', 
	'Terrenos', str(u'Urbanización'), 'Bulevar', 'Sector'
]
place_types_cat = [
    str(u'Agregat'), str(u'Llogaret'), str(u'Àrea'), str(u'Barri'), str(u'Barranc'), str(u'Camí ramader'),
    str(u'Col·legi/Cigarral'), str(u'Xalet'), str(u'Ajuntament/Col·legi'), str(u'Camp'), str(u'Mas'),
    str(u'Conjunt'), str(u'Diputació'), str(u'Disseminats'), str(u'Edificis'), str(u'Extramurs'), 
    str(u'Entrada'), str(u'Extraradi'), str(u'Finca'), str(u'Grup'), str(u'Hort'), str(u'Jardins'), str(u'Lloc'),
    str(u'Mercat'), str(u'Moll'), str(u'Municipi'), str(u'Masies'), str(u'Muntanya'), str(u'Illa'), str(u'Poblat'),
    str(u'Partida'), str(u'Polígon'), str(u'Erm'), str(u'Parròquia'), str(u'Solar'), str(u'Terrenys'),
    str(u'Urbanització'), str(u'Bulevard'), str(u'Sector')
]

# Dictionary for default 'highway_types.csv'
highway_types = highway_types_es

# List of highway types to translate as place addresses
place_types = place_types_es
remove_place_from_name = [place_types_es[26]]

# List of highway types not to be parsed
excluded_types = ['DS', 'ER']

# Dictionary of name and OSM boundary relation id for know municipalities
# wich fails in get_boundary method.
mun_fails = {
    '07032': [str(u'Maó'), '1809102'],
    '07040': [str(u'Palma'), '341321'],
    '11042': [str(u'Zahara'), '343140'],
    '16176': [str(u'Pozorrubio'), '347331'],
    '19178': [str(u'Humanes'), '341781'],
    '23043': [str(u'Hornos'), '344389'],
    '23086': [str(u'Torre del Campo'), '346324'],
    '26004': [str(u'Ajamil'), '348189'],
    '26093': [str(u'Mansilla de la Sierra'), '345202'],
    '28063': [str(u'Gargantilla del Lozoya y Pinilla de Buitrago'), '345009'],
    '29101': [str(u'Montecorto'), '7541639'],
    '35010': [str(u'Santa María de Guía de Gran Canaria'), '345440'],
    '37252': [str(u'Pereña de la Ribera'), '343095'],
    '37367': [str(u'Villarino de los Aires'), '340062'],
    '38023': [str(u'San Cristóbal de La Laguna'), '345393'],
    '38039': [str(u'Santa Úrsula'), '340717'],
    '39103': [str(u'Mancomunidad de Campoo-Cabuérniga'), '340042'],
    '44007': [str(u'Alba'), '345065'],
    '47047': [str(u'Castroponce'), '340763'],
    '47101': [str(u'Muriel'), '346973'],
    '47207': [str(u'Villafuerte'), '341197'],
    '50030': [str(u'Añón de Moncayo'), '342653'],
    '50049': [str(u'Biel'), '348008'],
    '51021': [str(u'Fuente-Álamo'), '341797'],
    '52024': [str(u'Gijón/Xixón'), '345576'],
}

aux_address = {'cdau': ['04', '11', '14', '18', '21', '23', '29', '41']}

