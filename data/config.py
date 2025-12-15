"""
Configuration for using downloaded data.

Borders can be downloaded from https://www.geoboundaries.org/countryDownloads.html.
The "features" keys are a subset of features identified by (shapeID, shapeName).
These are mostly cities but can also be districts or provinces.
The shapeID alone should be used as a unique identifier.

Sometimes when the shapeName was duplicated an index as added e.g. Mirpur-1 for Bangladesh.
This was before the shapeID was used as the unique identifier.

Rasters can be downloaded from https://hub.worldpop.org/geodata/listing?id=78
"""

CONFIG = {}

### Bangladesh

CONFIG["Bangladesh"] = {
    "geojson filepath": 'geoBoundaries-BGD-ADM3-all/geoBoundaries-BGD-ADM3.geojson',
    "raster filepath": 'bgd_ppp_2020_constrained.tif',
    "features": {
        "Dhaka": [
            ("5055444B49102485932636", "Adabor"),
            ("5055444B32230680322744", "Badda"),
            ("5055444B3033227423351", "Bangshal"),
            ("5055444B57714745100095", "Biman Bandar"),
            ("5055444B56407900252664", "Cantonment"),
            ("5055444B54932712585204", "Dakshinkhan"),
            ("5055444B58026692506241", "Darus Salam"),
            ("5055444B14528909504793", "Demra"),
            ("5055444B44526348177341", "Dhanmondi"),
            ("5055444B38357461991586", "Gendaria"),
            ("5055444B56461784969328", "Gulshan"),
            ("5055444B79082430711641", "Hazaribagh"),
            ("5055444B25595964672870", "Jatrabari"),
            ("5055444B98895982185439", "Kadamtali"),
            ("5055444B63983691041165", "Kafrul"),
            ("5055444B44586905762707", "Kalabagan"),
            ("5055444B25875561692739", "Kamrangir Char"),
            ("5055444B61701169401467", "Khilgaon"),
            ("5055444B65231246155988", "Khilkhet"),
            ("5055444B96747808832933", "Kotwali"),
            ("5055444B37083431015696", "Lalbagh"),
            ("5055444B1093476169518", "Mirpur-1"),
            ("5055444B96237484517929", "Mohammadpur"),
            ("5055444B92723626214353", "Motijheel"),
            ("5055444B9752476477947", "New Market"),
            ("5055444B7396550141885", "Pallabi"),
            ("5055444B25185864846738", "Paltan"),
            ("5055444B66987540891927", "Ramna"),
            ("5055444B30627422876303", "Rampura"),
            ("5055444B47617762942552", "Sabujbagh"),
            ("5055444B88449011386405", "Shah Ali"),
            ("5055444B26697181188091", "Shahbagh"),
            ("5055444B71144810702424", "Sher-e-bangla Nagar"),
            ("5055444B82614645252879", "Shyampur"),
            ("5055444B49503871645568", "Sutrapur"),
            ("5055444B91995345267504", "Tejgaon"),
            ("5055444B57500985162038", "Tejgaon Ind. Area"),
            ("5055444B30733148378014", "Turag"),
            ("5055444B65870568835453", "Uttar Khan"),
            ("5055444B45163668529800", "Uttara"),
        ]
    }
}

### Egypt

cairo_giza_districts = [
    ("37247803B10880133914548", "Abdin"),
    ("37247803B66210800118153", "Ain Shams"),
    ("37247803B56780050438943", "Al-Aguza"),
    ("37247803B9687639154335", "Al-Ahram"),
    ("37247803B6267278220516", "Al Azbakiyya"),
    ("37247803B66957331642315", "Al Darb al-Ahmar"),
    ("37247803B15392203431980", "Al Khalifa"),
    ("37247803B27962965783351", "Al Matariyya"),
    ("37247803B54164801772616", "Al Sahil"),
    ("37247803B59541002076203", "Al Salam"),
    ("37247803B22012205190656", "Al Sharabiyya"),
    ("37247803B46837021628067", "Al Wayli"),
    ("37247803B28746183260819", "Al Zahir"),
    ("37247803B62499095418831", "Al Zaytun"),
    ("37247803B16391777329697", "Auseem"),
    ("37247803B36275264085145", "Bab Al-Shariyya"),
    ("37247803B92056872151518", "Basatin"),
    ("37247803B29547542469056", "Bulaq"),
    ("37247803B34210539192827", "Bulaq Al-DakrUr"),
    ("37247803B46347292779018", "DuqqI"),
    ("37247803B35159038955302", "Gamaliyya-1"),
    ("37247803B55829024150134", "Giza-1"),
    ("37247803B1921003738807", "Hadaiq Al-Qubba"),
    ("37247803B14597497558400", "Imbaba-1"),
    ("37247803B74669546915316", "Kardasa"),
    ("37247803B74269871636707", "Khsos"),
    ("37247803B60267904610722", "Madinat Nasr-2"),
    ("37247803B51665438591487", "Marg"),
    ("37247803B62139513677683", "Minshat Nasir"),
    ("37247803B70915432571750", "Misr al-Gadida"),
    ("37247803B34541492244214", "Misr Al-Qadima"),
    ("37247803B88500614059504", "Muski"),
    ("37247803B64528254011318", "Nasr City"),
    ("37247803B21469576264473", "Nuzha"),
    ("37247803B52731964573716", "Qasr Al-Nile"),
    ("37247803B92272311463105", "Rud Al-Farag"),
    ("37247803B41278628102289", "Sayyida Zainab"),
    ("37247803B2980274366801", "Shubra"),
    ("37247803B87868406017087", "Shubra Al-Khayma 1"),
    ("37247803B84983151070332", "Shubra Al-Khayma 2"),
    ("37247803B30889137034133", "Umraniyya"),
    ("37247803B78325352338503", "Waraq"),
    ("37247803B72756565577460", "Zamalik"),
    ("37247803B37865224267935", "Zawiyya Al-Hamra"),
]

CONFIG["Egypt"] = {
    "geojson filepath": 'geoBoundaries-EGY-ADM2-all/geoBoundaries-EGY-ADM2.geojson',
    "raster filepath": 'egy_ppp_2020_constrained.tif',
    "features": {
        "Greater Cairo": cairo_giza_districts
    }
}

### France

CONFIG["France"] = {
    "geojson filepath": 'geoBoundaries-FRA-ADM2-all/geoBoundaries-FRA-ADM2.geojson',
    "raster filepath": 'fra_ppp_2020_constrained.tif',
    "features": {
        "Paris": [
            ("29444166B33792924009837", "Paris"),
            ("29444166B3280539319107", "Hauts-de-Seine"),
            ("29444166B11945742862669", "Seine-Saint-Denis"),
            ("29444166B83164575229799", "Val-de-Marne"),
        ]
    }
}


### Gaza

CONFIG["Gaza"] = {
    "geojson filepath": 'geoBoundaries-PSE-ADM2-all/geoBoundaries-PSE-ADM2.geojson',
    "raster filepath": 'pse_ppp_2020_constrained.tif',
    "features": {
        "Gaza": [
            ("87354302B11532502248212", "Rafah"),
            ("87354302B69236118899353", "North Gaza"),
            ("87354302B92317438543703", "Gaza"),
            ("87354302B21422506618890", "Khan Yunis"),
            ("87354302B22339434669936", "Deir Al Balah"),
        ]
    }
}

### India

CONFIG["India"] = {
    "geojson filepath": 'geoBoundaries-IND-ADM3-all/geoBoundaries-IND-ADM3.geojson',
    "raster filepath": 'ind_ppp_2020_constrained.tif',
    "features": {
        "Kolkata": [
            ("7132399B51822200806842", "Chanditala - I"),
            ("7132399B49310456347554", "Barasat - I"),
            ("7132399B84767188509372", "Amdanga"),
            ("7132399B24084234700227", "Barrackpur - I"),
            ("7132399B20977881911793", "Singur"),
            ("7132399B80803675257723", "Serampur Uttarpara"),
            ("7132399B61821868380391", "Thakurpukur Mahestola"),
            ("7132399B96129768514696", "Domjur"),
            ("7132399B50374631153904", "Bally Jagachha"),
            ("7132399B59861308195071", "Rajarhat"),
            ("7132399B49723217617281", "Barrackpur - Ii"),
            ("7132399B15579509596825", "Budge Budge - I"),
            ("7132399B81201704905333", "Chanditala - Ii"),
            ("7132399B81607080685719", "Sankrail-2"),
            ("7132399B12066186320957", "Kolkata"),
        ],
        "Mumbai": [
            ("7132399B61909415886633", "Mumbai Suburban"),
            ("7132399B37347557660936", "Mumbai"),
        ]
    }
}

### Phillipines

CONFIG["Phillipines"] = {
    "geojson filepath": 'geoBoundaries-PHL-ADM2-all/geoBoundaries-PHL-ADM2.geojson',
    "raster filepath": 'phl_ppp_2020_constrained.tif',
    "features": {
        "Manila": [
            ("2640588B65314213268917", "NCR, City of Manila, First District"),
            ("2640588B20861121251971", "NCR, Fourth District"),
            ("2640588B12869096786612", "NCR, Second District"),
            ("2640588B11276327116073", "NCR, Third District"),
        ]
    }
}

### South Africa


CONFIG["South Korea"] = {
    "geojson filepath": 'geoBoundaries-ZAFKOR-ADM2-all/geoBoundaries-ZAF-ADM2.geojson',
    "raster filepath": 'zaf_ppp_2020_constrained.tif',
    "features": {
        "Eastern Cape": [
            ("47623444B30321887561170", "Alfred Nzo"),
            ("47623444B36505680523289", "Amathole"),
            ("47623444B85184421345333", "Buffalo City"),
            ("47623444B84929106525656", "Cacadu"),
            ("47623444B97098873518332", "Chris Hani"),
            ("47623444B23123045321242", "Joe Gqabi"),
            ("47623444B28857154592205", "Nelson Mandela Bay"),
            ("47623444B2401151093158", "O.R.Tambo"),
        ],
        "Free State": [
            ("47623444B21501715606105", "Fezile Dabi"),
            ("47623444B29116896592790", "Lejweleputswa"),
            ("47623444B22599792684232", "Mangaung"),
            ("47623444B5552574832417", "Thabo Mofutsanyane"),
            ("47623444B92402502391318", "Xhariep"),
        ],
        "Gauteng": [
            ("47623444B15418766532839", "City of Johannesburg"),
            ("47623444B80921072750836", "City of Tshwane"),
            ("47623444B61881803671589", "Ekurhuleni"),
            ("47623444B84489694859974", "Sedibeng"),
            ("47623444B6623169143942", "West Rand"),
        ],
        "KwaZulu-Natal": [
            ("47623444B66034573524186", "Amajuba"),
            ("47623444B60178842862169", "eThekwini"),
            ("47623444B69150070479938", "iLembe"),
            ("47623444B12889843225205", "Sisonke"),
            ("47623444B80915190121590", "Ugu"),
            ("47623444B82303823139799", "Umgungundlovu"),
            ("47623444B87808740966359", "Umkhanyakude"),
            ("47623444B41861303399053", "Umzinyathi"),
            ("47623444B45932738864801", "Uthukela"),
            ("47623444B51210648784187", "Uthungulu"),
            ("47623444B26591670939926", "Zululand"),
        ],
        "Limpopo": [
            ("47623444B39961875100415", "Capricorn"),
            ("47623444B84816538378710", "Mopani"),
            ("47623444B21298621424908", "Sekhukhune"),
            ("47623444B95982048670815", "Vhembe"),
            ("47623444B68910643198214", "Waterberg"),
        ],
        "Mpumalanga": [
            ("47623444B37290189898198", "Ehlanzeni"),
            ("47623444B27645248540404", "Gert Sibande"),
            ("47623444B64302501149239", "Nkangala"),
        ],
        "North West": [
            ("47623444B85240549790840", "Bojanala"),
            ("47623444B93741575558004", "Dr Kenneth Kaunda"),
            ("47623444B1265322146951", "Dr Ruth Segomotsi Mompati"),
            ("47623444B28912463422483", "Ngaka Modiri Molema"),
        ],
        "Northern Cape": [
            ("47623444B47551800403987", "Frances Baard"),
            ("47623444B84629172160693", "John Taolo Gaetsewe"),
            ("47623444B2552562251298", "Namakwa"),
            ("47623444B63696254381244", "Pixley ka Seme"),
            ("47623444B49450251729649", "Z F Mgcawu"),
        ],
        "Western Cape": [
            ("47623444B8262601395586", "Cape Winelands"),
            ("47623444B66747201173997", "Central Karoo"),
            ("47623444B95865124382580", "City of Cape Town"),
            ("47623444B71894478343084", "Eden"),
            ("47623444B61406186088349", "Overberg"),
            ("47623444B37444115609272", "West Coast"),
        ]
    }
}

### South Korea

CONFIG["South Korea"] = {
    "geojson filepath": 'geoBoundaries-KOR-ADM2-all/geoBoundaries-KOR-ADM2.geojson',
    "raster filepath": 'kor_ppp_2020_constrained.tif',
    "features": {
        "Seoul": [
            ("91817680B75936691302089", "Gangseo-gu-2"),
            ("91817680B8309013283439", "Gangdong-gu"),
            ("91817680B10131618900015", "Songpa-gu"),
            ("91817680B5725333816693", "Seocho-gu"),
            ("91817680B53321453404308", "Gangnam-gu"),
            ("91817680B6950995223857", "Nowon-gu"),
            ("91817680B55050579859044", "Dobong-gu"),
            ("91817680B92844029998138", "Gangbuk-gu"),
            ("91817680B66829558888986", "Jungnang-gu"),
            ("91817680B53616587081026", "Eunpyeong-gu"),
            ("91817680B55576639555152", "Jongno-gu"),
            ("91817680B19736947579274", "Seongbuk-gu"),
            ("91817680B25965069984368", "Dongdaemun-gu"),
            ("91817680B49246193334347", "Gwangjin-gu"),
            ("91817680B63185877293812", "Seongdong-gu"),
            ("91817680B29418542168397", "Jung-gu [Central District]-5"),
            ("91817680B50347392057391", "Yongsan-gu"),
            ("91817680B72690271662871", "Dongjak-gu"),
            ("91817680B65126245655882", "Seodaemun-gu"),
            ("91817680B14643286354390", "Mapo-gu"),
            ("91817680B5490200958143", "Yeongdeungpo-gu"),
            ("91817680B99536699865294", "Gwanak-gu"),
            ("91817680B1968034056748", "Guro-gu"),
            ("91817680B8017156108400", "Yangcheon-gu"),
            ("91817680B69479464976516", "Geumcheon-gu"),
        ]
    }
}

### United Kingdom

CONFIG["United Kingdom"] = {
    "geojson filepath": 'geoBoundaries-GBR-ADM2-all/geoBoundaries-GBR-ADM2.geojson',
    "raster filepath": 'gbr_ppp_2020_constrained.tif',
    "features": {
        "London": [
            ("9080712B97999030763342", "City of London"),
            ("9080712B32800787628045", "Barking and Dagenham"),
            ("9080712B71536097625899", "Barnet"),
            ("9080712B42809460048540", "Bexley"),
            ("9080712B99403255709140", "Brent"),
            ("9080712B62294642180343", "Bromley"),
            ("9080712B44623990435361", "Camden"),
            ("9080712B54972646687738", "Croydon"),
            ("9080712B48606994457952", "Ealing"),
            ("9080712B27244151555615", "Enfield"),
            ("9080712B64588414247228", "Greenwich"),
            ("9080712B81123650494794", "Hackney"),
            ("9080712B6991151074246", "Hammersmith and Fulham"),
            ("9080712B98331752183955", "Haringey"),
            ("9080712B85229688010924", "Harrow"),
            ("9080712B13607306368601", "Havering"),
            ("9080712B45194275403121", "Hillingdon"),
            ("9080712B85959270461063", "Hounslow"),
            ("9080712B49045247202114", "Islington"),
            ("9080712B39473788331099", "Kensington and Chelsea"),
            ("9080712B89177385119631", "Kingston upon Thames"),
            ("9080712B40540283796062", "Lambeth"),
            ("9080712B25883423000924", "Lewisham"),
            ("9080712B31505825113523", "Merton"),
            ("9080712B98999290586969", "Newham"),
            ("9080712B26905607212870", "Redbridge"),
            ("9080712B29790766461311", "Richmond upon Thames"),
            ("9080712B52245663238426", "Southwark"),
            ("9080712B3334907750367", "Sutton"),
            ("9080712B53792364084436", "Tower Hamlets"),
            ("9080712B6382316371033", "Waltham Forest"),
            ("9080712B56158297313901", "Wandsworth"),
            ("9080712B54935279696040", "Westminster"),
        ],
        "London Inner City": [
            ("9080712B44623990435361", "Camden"),
            ("9080712B81123650494794", "Hackney"),
            ("9080712B49045247202114", "Islington"),
            ("9080712B40540283796062", "Lambeth"),
            ("9080712B52245663238426", "Southwark"),
            ("9080712B53792364084436", "Tower Hamlets"),
            ("9080712B54935279696040", "Westminster"),
        ]
    }
}

## United States

CONFIG["United States"] = {
    "geojson filepath": 'geoBoundaries-USA-ADM2-all/geoBoundaries-USA-ADM2.geojson',
    "raster filepath": 'usa_ppp_2020_constrained.tif',
    "features": {
        "New York": [
            ("52423323B86897144494159", "Queens"),
            ("52423323B38635571773884", "Richmond-2"),
            ("52423323B44038614744637", "Bronx"),
            ("52423323B42930074476451", "Kings-2"),
            ("52423323B68557587713523", "New York"),
        ]
    }
}
