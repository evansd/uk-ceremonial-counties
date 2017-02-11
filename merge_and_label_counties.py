#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import sys

# From https://en.wikipedia.org/wiki/List_of_English_districts
# Tweaked in a couple of places to make the names match
ENGLISH_MAPPING_TEXT = """
Adur	West Sussex
Allerdale	Cumbria
Amber Valley	Derbyshire
Arun	West Sussex
Ashfield	Nottinghamshire
Ashford	Kent
Aylesbury Vale	Buckinghamshire
Babergh	Suffolk
Barking and Dagenham	Greater London
Barnet	Greater London
Barnsley	South Yorkshire
Barrow-in-Furness	Cumbria
Basildon	Essex
Basingstoke and Deane	Hampshire
Bassetlaw	Nottinghamshire
Bath and North East Somerset	Somerset
Bedford	Bedfordshire
Bexley	Greater London
Birmingham	West Midlands
Blaby	Leicestershire
Blackburn with Darwen	Lancashire
Blackpool	Lancashire
Bolsover	Derbyshire
Bolton	Greater Manchester
Boston	Lincolnshire
Bournemouth	Dorset
Bracknell Forest	Berkshire
Bradford	West Yorkshire
Braintree	Essex
Breckland	Norfolk
Brent	Greater London
Brentwood	Essex
Brighton and Hove	East Sussex
Bristol	Bristol
Broadland	Norfolk
Bromley	Greater London
Bromsgrove	Worcestershire
Broxbourne	Hertfordshire
Broxtowe	Nottinghamshire
Burnley	Lancashire
Bury	Greater Manchester
Calderdale	West Yorkshire
Cambridge	Cambridgeshire
Camden	Greater London
Cannock Chase	Staffordshire
Canterbury	Kent
Carlisle	Cumbria
Castle Point	Essex
Central Bedfordshire	Bedfordshire
Charnwood	Leicestershire
Chelmsford	Essex
Cheltenham	Gloucestershire
Cherwell	Oxfordshire
Cheshire East	Cheshire
Cheshire West and Chester	Cheshire
Chesterfield	Derbyshire
Chichester	West Sussex
Chiltern	Buckinghamshire
Chorley	Lancashire
Christchurch	Dorset
Colchester	Essex
Copeland	Cumbria
Corby	Northamptonshire
Cornwall	Cornwall
Cotswold	Gloucestershire
Coventry	West Midlands
Craven	North Yorkshire
Crawley	West Sussex
Croydon	Greater London
Dacorum	Hertfordshire
Darlington	Durham
Dartford	Kent
Daventry	Northamptonshire
Derby	Derbyshire
Derbyshire Dales	Derbyshire
Doncaster	South Yorkshire
Dover	Kent
Dudley	West Midlands
County Durham	Durham
Ealing	Greater London
East Cambridgeshire	Cambridgeshire
East Devon	Devon
East Dorset	Dorset
East Hampshire	Hampshire
East Hertfordshire	Hertfordshire
East Lindsey	Lincolnshire
East Northamptonshire	Northamptonshire
East Riding of Yorkshire	East Riding of Yorkshire
East Staffordshire	Staffordshire
Eastbourne	East Sussex
Eastleigh	Hampshire
Eden	Cumbria
Elmbridge	Surrey
Enfield	Greater London
Epping Forest	Essex
Epsom and Ewell	Surrey
Erewash	Derbyshire
Exeter	Devon
Fareham	Hampshire
Fenland	Cambridgeshire
Forest Heath	Suffolk
Forest of Dean	Gloucestershire
Fylde	Lancashire
Gateshead	Tyne and Wear
Gedling	Nottinghamshire
Gloucester	Gloucestershire
Gosport	Hampshire
Gravesham	Kent
Great Yarmouth	Norfolk
Greenwich	Greater London
Guildford	Surrey
Hackney	Greater London
Halton	Cheshire
Hambleton	North Yorkshire
Hammersmith and Fulham	Greater London
Harborough	Leicestershire
Haringey	Greater London
Harlow	Essex
Harrogate	North Yorkshire
Harrow	Greater London
Hart	Hampshire
Hartlepool	Durham
Hastings	East Sussex
Havant	Hampshire
Havering	Greater London
Herefordshire	Herefordshire
Hertsmere	Hertfordshire
High Peak	Derbyshire
Hillingdon	Greater London
Hinckley and Bosworth	Leicestershire
Horsham	West Sussex
Hounslow	Greater London
Kingston upon Hull	East Riding of Yorkshire
Huntingdonshire	Cambridgeshire
Hyndburn	Lancashire
Ipswich	Suffolk
Isle of Wight	Isle of Wight
Isles of Scilly	Cornwall
Islington	Greater London
Kensington and Chelsea	Greater London
Kettering	Northamptonshire
King's Lynn and West Norfolk	Norfolk
Kingston upon Thames	Greater London
Kirklees	West Yorkshire
Knowsley	Merseyside
Lambeth	Greater London
Lancaster	Lancashire
Leeds	West Yorkshire
Leicester	Leicestershire
Lewes	East Sussex
Lewisham	Greater London
Lichfield	Staffordshire
Lincoln	Lincolnshire
Liverpool	Merseyside
City of London	City of London
Luton	Bedfordshire
Maidstone	Kent
Maldon	Essex
Malvern Hills	Worcestershire
Manchester	Greater Manchester
Mansfield	Nottinghamshire
Medway	Kent
Melton	Leicestershire
Mendip	Somerset
Merton	Greater London
Mid Devon	Devon
Mid Suffolk	Suffolk
Mid Sussex	West Sussex
Middlesbrough	North Yorkshire
Milton Keynes	Buckinghamshire
Mole Valley	Surrey
Newark and Sherwood	Nottinghamshire
Newcastle-under-Lyme	Staffordshire
Newcastle upon Tyne	Tyne and Wear
New Forest	Hampshire
Newham	Greater London
North Devon	Devon
North Dorset	Dorset
North East Derbyshire	Derbyshire
North East Lincolnshire	Lincolnshire
North Hertfordshire	Hertfordshire
North Kesteven	Lincolnshire
North Lincolnshire	Lincolnshire
North Norfolk	Norfolk
North Somerset	Somerset
North Tyneside	Tyne and Wear
North Warwickshire	Warwickshire
North West Leicestershire	Leicestershire
Northampton	Northamptonshire
Northumberland	Northumberland
Norwich	Norfolk
Nottingham	Nottinghamshire
Nuneaton and Bedworth	Warwickshire
Oadby and Wigston	Leicestershire
Oldham	Greater Manchester
Oxford	Oxfordshire
Pendle	Lancashire
Peterborough	Cambridgeshire
Plymouth	Devon
Poole	Dorset
Portsmouth	Hampshire
Preston	Lancashire
Purbeck	Dorset
Reading	Berkshire
Redbridge	Greater London
Redcar and Cleveland	North Yorkshire
Redditch	Worcestershire
Reigate and Banstead	Surrey
Ribble Valley	Lancashire
Richmond upon Thames	Greater London
Richmondshire	North Yorkshire
Rochdale	Greater Manchester
Rochford	Essex
Rossendale	Lancashire
Rother	East Sussex
Rotherham	South Yorkshire
Rugby	Warwickshire
Runnymede	Surrey
Rushcliffe	Nottinghamshire
Rushmoor	Hampshire
Rutland	Rutland
Ryedale	North Yorkshire
St Albans	Hertfordshire
St Edmundsbury	Suffolk
St Helens	Merseyside
Salford	Greater Manchester
Sandwell	West Midlands
Scarborough	North Yorkshire
Sedgemoor	Somerset
Sefton	Merseyside
Selby	North Yorkshire
Sevenoaks	Kent
Sheffield	South Yorkshire
Shepway	Kent
Shropshire	Shropshire
Slough	Berkshire
Solihull	West Midlands
South Bucks	Buckinghamshire
South Cambridgeshire	Cambridgeshire
South Derbyshire	Derbyshire
South Gloucestershire	Gloucestershire
South Hams	Devon
South Holland	Lincolnshire
South Kesteven	Lincolnshire
South Lakeland	Cumbria
South Norfolk	Norfolk
South Northamptonshire	Northamptonshire
South Oxfordshire	Oxfordshire
South Ribble	Lancashire
South Somerset	Somerset
South Staffordshire	Staffordshire
South Tyneside	Tyne and Wear
Southampton	Hampshire
Southend-on-Sea	Essex
Southwark	Greater London
Spelthorne	Surrey
Stafford	Staffordshire
Staffordshire Moorlands	Staffordshire
Stevenage	Hertfordshire
Stockport	Greater Manchester
Stoke-on-Trent	Staffordshire
Stratford-on-Avon	Warwickshire
Stroud	Gloucestershire
Suffolk Coastal	Suffolk
Sunderland	Tyne and Wear
Surrey Heath	Surrey
Sutton	Greater London
Swale	Kent
Swindon	Wiltshire
Tameside	Greater Manchester
Tamworth	Staffordshire
Tandridge	Surrey
Taunton Deane	Somerset
Teignbridge	Devon
Telford and Wrekin	Shropshire
Tendring	Essex
Test Valley	Hampshire
Tewkesbury	Gloucestershire
Thanet	Kent
Three Rivers	Hertfordshire
Thurrock	Essex
Tonbridge and Malling	Kent
Torbay	Devon
Torridge	Devon
Tower Hamlets	Greater London
Trafford	Greater Manchester
Tunbridge Wells	Kent
Uttlesford	Essex
Vale of White Horse	Oxfordshire
Wakefield	West Yorkshire
Walsall	West Midlands
Waltham Forest	Greater London
Wandsworth	Greater London
Warrington	Cheshire
Warwick	Warwickshire
Watford	Hertfordshire
Waveney	Suffolk
Waverley	Surrey
Wealden	East Sussex
Wellingborough	Northamptonshire
Welwyn Hatfield	Hertfordshire
West Berkshire	Berkshire
West Devon	Devon
West Dorset	Dorset
West Lancashire	Lancashire
West Lindsey	Lincolnshire
Westminster	Greater London
West Oxfordshire	Oxfordshire
West Somerset	Somerset
Weymouth and Portland	Dorset
Wigan	Greater Manchester
Wiltshire	Wiltshire
Winchester	Hampshire
Windsor and Maidenhead	Berkshire
Wirral	Merseyside
Woking	Surrey
Wokingham	Berkshire
Wolverhampton	West Midlands
Worcester	Worcestershire
Worthing	West Sussex
Wychavon	Worcestershire
Wycombe	Buckinghamshire
Wyre	Lancashire
Wyre Forest	Worcestershire
York	North Yorkshire
"""

# Based on the advice given here and tweaked slightly to make the names
# match:
# https://github.com/mysociety/mapit/wiki/UK-Ceremonial-Counties
REST_OF_GB_MAPPING_TEXT = """
Scottish Borders
Scottish Borders

Central
Clackmannanshire, Falkirk, Stirling

Dumfries and Galloway
Dumfries and Galloway

Fife
Fife

Grampian
Aberdeenshire, Banff and Buchan, Gordon, Kincardine and Deeside, Aberdeen City, Moray

Highland
Highland

Lothian
West Lothian, City of Edinburgh, Midlothian, East Lothian

Orkney Islands
Orkney Islands

Strathclyde
Argyll and Bute, North Ayrshire, East Ayrshire, South Ayrshire, South Lanarkshire, Inverclyde, Renfrewshire, West Dunbartonshire, East Dunbartonshire, Glasgow City, East Renfrewshire, North Lanarkshire

Shetland Islands
Shetland Islands

Tayside
Angus, Dundee City, Perth and Kinross

Eilean Siar
Na h-Eileanan Siar

Gwent
Caerphilly, Blaenau Gwent, Torfaen, Monmouthshire, Newport

South Glamorgan
Cardiff, Vale of Glamorgan

Mid Glamorgan
Merthyr Tydfil, Bridgend, Rhondda Cynon Taf

West Glamorgan
Neath Port Talbot, Swansea

Dyfed
Carmarthenshire, Ceredigion, Pembrokeshire

Powys
Powys

Gwynedd
Gwynedd, Isle of Anglesey

Clwyd
Wrexham, Flintshire, Denbighshire, Conwy
"""

NORTH_YORKSHIRE_WARDS = set("""
E05001538
E05001539
E05001540
E05001548
E05001550
E05001552
""".strip().splitlines())

DURHAM_WARDS = set("""
E05001527
E05001528
E05001529
E05001530
E05001531
E05001532
E05001533
E05001534
E05001535
E05001536
E05001537
E05001541
E05001542
E05001543
E05001544
E05001545
E05001546
E05001547
E05001549
E05001551
""".strip().splitlines())

NI_COUNTIES = set("""
Tyrone
Armagh
Down
Londonderry
Antrim
Fermanagh
""".strip().splitlines())

def parse_rest_of_gb_mapping_text(text):
    lines = text.strip().splitlines()
    mapping = {}
    for i in range(0, len(lines), 3):
        county = lines[i]
        for authority in lines[i+1].split(','):
            mapping[authority.strip()] = county
    return mapping


def parse_english_mapping_text(text):
    return {
            line.split('\t')[0]: line.split('\t')[1]
            for line in text.strip().splitlines()}


COUNTY_MAPPING = parse_rest_of_gb_mapping_text(REST_OF_GB_MAPPING_TEXT)
COUNTY_MAPPING.update(parse_english_mapping_text(ENGLISH_MAPPING_TEXT))


def main(filenames, out_stream):
    #print json.dumps(COUNTY_MAPPING, indent=2)
    #sys.exit()
    features = []
    output_data = {
        'type': 'FeatureCollection',
        'features': features}
    for filename in filenames:
        with open(filename, 'rb') as f:
            data = json.load(f)
        for feature in data['features']:
            feature['properties'] = transform_properties(feature['properties'])
            features.append(feature)
    json.dump(output_data, out_stream, indent=2)


def transform_properties(props):
    return {
        'county': get_ceremonial_county(props),
        'area': props.get('st_areashape', props.get('AREA'))}


def get_ceremonial_county(props):
    name_tag = props.get('NAME_TAG')
    # Irish counties
    if name_tag:
        if name_tag in NI_COUNTIES:
            return name_tag
        else:
            # We treat all RoI counties as None so they get
            # merged into one continuous body
            return None
    if props['lad15cd'].startswith('E090000'):
        return 'Greater London'
    ward = props['wd15cd']
    if ward in DURHAM_WARDS:
        return 'Durham'
    elif ward in NORTH_YORKSHIRE_WARDS:
        return 'North Yorkshire'
    authority = props['lad15nm']
    authority = authority.split(',')[0]
    authority = authority.replace('St. ', 'St ')
    return COUNTY_MAPPING[authority]


if __name__ == '__main__':
    main(sys.argv[1:], sys.stdout)
