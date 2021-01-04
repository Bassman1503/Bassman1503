import PySimpleGUI as sg
import re

layout=[ 
    [sg.Column([
        [sg.Frame('Guitar:',
            [[sg.Text('category:', size=(22,1), justification='right'), sg.Combo(['acoustic', 'electric', 'semi-acoustic'], default_value= 'electric', key='category', size=(23,1))],
             [sg.Text('brand:', size = (22,1), justification='right'), sg.Combo(['Fodera', 'Fender', 'Ibanez', 'Gretsch', 'Cort', 'Music Man', 'Taylor', 'Takamine', 'Hofner', 'Epiphone'], default_value = 'Ibanez', key='brand', size=(23,1))],
        
             [sg.Text('model:', size=(22,1), justification='right'),  sg.Input(key='model', size=(23,1))],
        
             [sg.Text('is-signature:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'no', key='is-signature', size=(23,1))],
             [sg.Text('number-of-strings:', size=(22,1), justification='right'), sg.Combo(['4', '5', '6'], default_value = 4, key='number-of-strings', size=(23,1))],
             [sg.Text('price:', size=(22,1), justification='right'), sg.Input(key='price', size=(23,1))],
             [sg.Text('hand:', size=(22,1), justification='right'), sg.Combo(['right', 'left'], default_value = 'right', key='hand', size=(23,1))],
             [sg.Text('quality-end:', size=(22,1), justification='right'), sg.Combo(['low', 'mid-low', 'mid', 'mid-high', 'high', 'elite'], key='quality-end', size=(23,1))]])],

        [sg.Frame('Strings:',
            [[sg.Text('factory-strings:', size=(22,1), justification='right'), sg.Combo(['DAddario EXP PBB190GS', 'DAddario® EXL156', 'DAddario® ECB81 Flatwound', 'DAddario® ECB81-5 Flatwound', 'DAddario® EXL170-5SL', 'Elixir Optiweb', '	Elixir NANOWEB Coating', 'DAddario® EXL165 + .130', 'DAddario® EXL165', 'Fender 7250M Nickel Plated Steel Roundwound', 'Fender USA 7250-5M Nickel Plated Steel', 'Fender® 5250XL Nickel Plated Steel Roundwound'], key='factory-strings', size=(23,1))],
             [sg.Text('string-gauge:', size=(22,1), justification='right'), sg.Combo(['.040/.060/.080/.095', '.040/.065/.080/.100', '.045/.065/.085/.105', '.045/.060/.080/.100', '.045/.065/.080/.100', '.050/.070/.085/.105','.050/.075/.090/.110', '.060/.080/.0100/.120', '.040/.060/.080/.100/.128', '045/.065/.080/.100/.130', '045/.065/.080/.100/.132', '.045/.065/.085/.105/.135', '.045/.065/.085/.105/.125', '.045/.065/.085/.105/.130', '.032/.045/.065/.085/.105/.130', '.032/.045/.065/.080/.100/.130', '.024/.034/.044/.056/.072/.084'], default_value = '.045/.065/.085/.105', key='string-gauge', size=(23,1))]])],
        
        [sg.Frame('Neck:',
            [[sg.Text('neck-material:', size=(22,1), justification='right'), sg.Combo(['Panga-Panga', 'Oak', 'Sapele', 'Alder','Ebony', 'Koa', 'Bubinga', 'Purpleheart', 'Rosewood', 'Wenge', 'Jatoba', 'Ash', 'Maple', 'Alder', 'Mahogany', ], default_value = 'Jatoba', key='neck-material', size=(23,1))],
             [sg.Text('neck-scale-length:', size=(22,1), justification='right'), sg.Combo(['short', 'medium', 'long', 'extra-long'], default_value = 'long', key='neck-scale-length', size=(23,1))],
             [sg.Text('neck-profile:', size=(22,1), justification='right'), sg.Combo(['C', 'D', 'U', 'V', 'LP', 'SRV', 'unknown'], default_value = 'D', key='neck-profile', size=(23,1))]])],
        
        [sg.Frame('Fretboard:',
            [[sg.Text('fretboard-radius:', size=(22,1), justification='right'), sg.Combo(['compound-radius', '6in', '7.25in', '9.45in', '9.5in', '10in', '11.5in', '12in', '15.75in ', '16in', '19.685in', '20in', '37.40in'], default_value = '12in', key='fretboard-radius', size=(23,1))],
             [sg.Text('fretboard-scale-type:', size=(22,1), justification='right'), sg.Combo(['normal', 'multiscale'], default_value = 'normal', key='fretboard-scale-type', size=(23,1))],
             [sg.Text('fret-size:', size=(22,1), justification='right'), sg.Combo(['vintage-tall', 'narrow-tall', 'no-fret', 'small', 'medium', 'medium-jumbo', 'jumbo', 'large'], default_value = 'medium', key='fret-size', size=(23,1))],
             [sg.Text('fretboard-is-fretted:', size=(22,1), justification='right'), sg.Combo(['fretted', 'fretless'], default_value = 'fretted', key='fretboard-is-fretted', size=(23,1))],
             [sg.Text('fretboard-material:', size=(22,1), justification='right'), sg.Combo(['Panga-Panga', 'Pau-Ferro', 'Alder','Ebony', 'Koa', 'Bubinga', 'Purpleheart', 'Rosewood', 'Wenge', 'Jatoba', 'Ash', 'Maple', 'Alder', 'Mahogany'], default_value = 'Panga-Panga', key='fretboard-material', size=(23,1))],
             [sg.Text('number-of-frets:', size=(22,1), justification='right'), sg.Combo(['0', '18', '19', '20', '21', '22', '23', '24', '25'], default_value = '24', key='number-of-frets', size=(23,1))]])]
             
             ]
                 ),
    sg.Column([
        [sg.Frame('Preamp:',
            [[sg.Text('preamp-type:', size=(22,1), justification='right'), sg.Combo(['active', 'passive', 'active-piezo', 'passive-with-active-bass-boost'], default_value = 'active', key='preamp-type', size=(23,1))],
             [sg.Text('preamp-model:', size=(22,1), justification='right'), sg.Combo(['Fodera/Pope 3-band standard preamp', 'Fodera/Pope 3-band preamp', 'Fodera standard passive preamp', 'Fodera Standard 3-band Preamp', 'Ibanez Custom Passive', 'Vari-mid 3-band EQ', 'Phat II EQ', 'Piezo active tone control', 'Ibanez Custom Electronics 2-band EQ ', 'Ibanez Custom Electronics 3-band EQ', 'Fender Pro Passive 2', 'Fender Pro Passive 4', 'Fender Pro Active 5-Knobs', 'Bartolini EQMK-5 Active Preamp', 'Fishman Isys Plus Preamp', 'Gretsch Pro Handmade', 'DiMarzio Aggro-pro CH3', 'Seymour Duncan OP-45', 'Takamine ClassicBass 45', 'Aguilar OBP-3', 'FilterTron Custom Pro BA-3', 'Hofner HandMade Pro-7'], default_value = 'Ibanez Custom Electronics 3-band EQ', key='preamp-model', size=(50,1))],
             [sg.Text('have-tone-control:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'no', key='have-tone-control', size=(23,1))],
             [sg.Text('have-master-volume:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'yes', key='have-master-volume', size=(23,1))],
             [sg.Text('have-high-volume:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'yes', key='have-high-volume', size=(23,1))],
             [sg.Text('have-mid-volume:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'yes', key='have-mid-volume', size=(23,1))],
             [sg.Text('have-bass-volume:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'yes', key='have-bass-volume', size=(23,1))],
             [sg.Text('have-bridge-pickup-volume:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'no', key='have-bridge-pickup-volume', size=(23,1))],
             [sg.Text('have-neck-pickup-volume:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'no', key='have-neck-pickup-volume', size=(23,1))],
             [sg.Text('have-middle-pickup-volume:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'no', key='have-middle-pickup-volume', size=(23,1))],
             [sg.Text('have-active-bass-boost:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'no', key='have-active-bass-boost', size=(23,1))],
             [sg.Text('have-active-passive-switch:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'yes', key='have-active-passive-switch', size=(23,1))],
             [sg.Text('have-pickup-selector/balancer:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'yes', key='have-pickup-selector/balancer', size=(23,1))],
             [sg.Text('have-3-way-mid-selector:', size=(22,1), justification='right'), sg.Combo(['yes', 'no'], default_value = 'yes', key='have-3-way-mid-selector', size=(23,1))]
            ])
        ],

        [sg.Frame('Bridge:',
            [[sg.Text('bridge model:', size=(22,1), justification='right'), sg.Input(key='bridge-model', size=(23,1))],
             [sg.Text('bridge-string-spacing:', size=(22,1), justification='right'), sg.Combo(['fixed', 'adjustable'], default_value = 'adjustable', key='bridge-string-spacing', size=(23,1))],
             [sg.Text('string-space:', size=(22,1), justification='right'), sg.Combo(['10.8mm', '16.5mm', '17mm', '17.5', '18mm', '19mm'], key='string-space', size=(23,1))]
            ])
        ],

        [sg.Frame('Body:',
            [[sg.Text('body-type:', size=(22,1), justification='right'), sg.Combo(['full-body', 'semi-hollow', 'hollow'], default_value = 'full-body', key='body-type', size=(23,1))],
             [sg.Text('body-shape:', size=(22,1), justification='right'), sg.Combo(['no-cutaway', 'single-cutaway', 'double-cutaway', 'G-cut'], default_value = 'double-cutaway', key='body-shape', size=(23,1))],
             [sg.Text('body-finish:', size=(22,1), justification='right'), sg.Combo(['nitrocellulose', 'opaque', 'glossy'], default_value = 'glossy', key='body-finish', size=(23,1))],
             [sg.Text('body-materials:', size=(22,1), justification='right'), sg.Combo(['Poplar', 'Nyatoh', 'Okume', 'Walnut', 'Oak', 'Alder','Ebony', 'Koa', 'Bubinga', 'Purpleheart', 'Rosewood', 'Wenge', 'Ash', 'Maple', 'Alder', 'Mahogany', ], key='body-materials', size=(23,1))]
            ])
        ],
        
        
        [sg.Frame('Pickup:',
            [[sg.Text('pickups-model:', size=(22,1), justification='right'), sg.Combo(['Seymour Duncan Retrospective P', 'Seymour Duncan Single coil J pickup', 'Seymour Duncan Steve Harris Signature P-Bass SPB-4', 'Seymour Duncan Basslines SPB-3 Quarter Pound', 'Custom Vintage 59', 'Dual Coil Ceramic Noiseless Jazz', 'Seymour Duncan STKJ2B Jazz', 'Pure Vintage 58', 'Pure Vintage 63', 'V-mod', 'Tony Franklin', 'Vintage Style 50', 'Ultra Noiseless', 'Custom Seymour Duncan', 'Yosemite', 'Vintage Style', 'Vintage Style 60', 'Custom Noiseless', 'Player Series Alnico 5', 'Classic Elite Bass', 'Dynamix', 'Bartolini MK-1', 'Fender', 'Aguilar', 'Nordstrand', 'Fishman', 'FilterTron', 'EMG', 'DiMarzio', 'Seymour Duncan', 'Hofner', 'Takamine'], key='pickups-model', size=(50,1))],
             [sg.Text('pickup-type:', size=(22,1), justification='right'), sg.Combo(['P/J-pickup', 'J-pickup', 'split-coil', 'soap-bar', 'humbucker', 'piezo', 'single-coil', 'dual-coil'], default_value = 'soap-bar', key='pickup-type', size=(23,1))],
             [sg.Text('pickup-arrangement', size=(22,1), justification='right'), sg.Combo(['J-pickup/J-pickup', 'split-coil', 'split-coil/J-pickup', 'single-soap', 'double-soap', 'humbucker', 'double-humbucker', 'dual-coil/dual-coil', 'piezo-at-bridge', 'body-inside-piezo', 'double-soap/piezo-at-bridge', 'unknown'], default_value = 'double-soap', key='pickup-arrangement', size=(23,1))],
             
            ])
        ]
        ])],
        [sg.Ok(size=(10,2)), sg.Exit(size=(10,2))]
]

window = sg.Window('Bass Model Creator',layout, element_justification='center')

while True:
    event, values = window.read()
    
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break

    basso = ["\t(bass-guitar\n"]

    for data in [('category', 'SYMBOL'),
                ('brand', 'STRING'),
                ('model', 'STRING'),
                ('is-signature', 'SYMBOL'),
                ('number-of-strings','INTEGER'),
                ('price', 'NUMBER'),
                ('hand', 'SYMBOL'),
                ('quality-end', 'SYMBOL'),
                None,
                ('factory-strings', 'STRING'),
                ('string-gauge', 'SYMBOL'),
                None,
                ('neck-material', 'SYMBOL'),
                ('neck-scale-length', 'SYMBOL'),
                ('neck-profile', 'SYMBOL'),
                None,
                ('fretboard-radius', 'SYMBOL'),
                ('fretboard-scale-type', 'SYMBOL'),
                ('fret-size', 'SYMBOL'),                
                ('fretboard-is-fretted', 'SYMBOL'),
                ('fretboard-material', 'SYMBOL'),
                ('number-of-frets','INTEGER'),                
                None,
                ('preamp-type', 'SYMBOL'),
                ('preamp-model', 'STRING'),
                ('have-tone-control', 'SYMBOL'),
                ('have-master-volume', 'SYMBOL'),
                ('have-high-volume', 'SYMBOL'),
                ('have-mid-volume', 'SYMBOL'),
                ('have-bass-volume', 'SYMBOL'),
                ('have-bridge-pickup-volume', 'SYMBOL'),
                ('have-neck-pickup-volume', 'SYMBOL'),
                ('have-middle-pickup-volume', 'SYMBOL'),
                ('have-active-bass-boost','SYMBOL'),
                ('have-active-passive-switch', 'SYMBOL'),
                ('have-pickup-selector/balancer', 'SYMBOL'),
                ('have-3-way-mid-selector', 'SYMBOL'),
                None,
                ('bridge-model', 'STRING'),
                ('bridge-string-spacing', 'SYMBOL'),
                ('string-space', 'SYMBOL'),
                None,
                ('body-type', 'SYMBOL'),
                ('body-shape', 'SYMBOL'),
                ('body-finish', 'SYMBOL'),
                ('body-materials', 'SYMBOL'),
                None,
                ('pickups-model', 'STRING'),
                ('pickup-type', 'SYMBOL'),
                ('pickup-arrangement', 'SYMBOL')]:
        if data == None:
            basso.append('\n')
        elif values[data[0]]:
            basso.append('\t\t(')
            basso.append(data[0])
            basso.append(' ')
            if data[1] == 'STRING':
                basso.append('"')
            basso.append(values[data[0]])
            if data[1] == 'STRING':
                basso.append('"')
            basso.append(")\n")
    basso.append("\n\t)")
    basso = "".join(basso)
    basso = re.sub(r'\n\n+', '\n\n', basso)
    sg.Window("Ecco il tuo basso",[[sg.Multiline(basso, size=(100,40))],[sg.Ok(size=(10,2))]]).read(close=True)
window.close()