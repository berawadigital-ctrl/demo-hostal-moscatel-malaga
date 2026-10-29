# Contenido de la demo Hostal Moscatel (Málaga) (es/ca/en/fr). Hechos de hostalmoscatel.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble con bañera de hidromasaje','Doble superior','Twin'],'ca':['Doble amb banyera d\'hidromassatge','Doble superior','Twin'],'en':['Double with whirlpool bath','Superior double','Twin'],'fr':['Double avec baignoire balnéo','Double supérieure','Twin']}
RD={
'es':['Amplia y luminosa, con pequeño balcón al patio andaluz, cama doble de 150 cm, cafetera Nespresso y bañera de hidromasaje. Unos 20 m².','Cama doble extragrande de 180 cm. Ideal para largas estancias.','Dos camas individuales de 90 cm para dos personas.'],
'ca':['Àmplia i lluminosa, amb petit balcó al pati andalús, llit doble de 150 cm, cafetera Nespresso i banyera d\'hidromassatge. Uns 20 m².','Llit doble extragran de 180 cm. Ideal per a estades llargues.','Dos llits individuals de 90 cm per a dues persones.'],
'en':['Spacious and bright, with a small balcony onto the Andalusian patio, a 150 cm double bed, a Nespresso machine and a whirlpool bath. About 20 m².','Extra-large 180 cm double bed. Ideal for long stays.','Two 90 cm single beds for two people.'],
'fr':['Spacieuse et lumineuse, avec un petit balcon sur le patio andalou, un lit double de 150 cm, une machine Nespresso et une baignoire balnéo. Environ 20 m².','Très grand lit double de 180 cm. Idéale pour les longs séjours.','Deux lits simples de 90 cm pour deux personnes.']}
ART={
'hero':('waves',9201,['#1d4e63','#f2c487','#f8e2bd','#2f6f86','#1d4e63','#123341']),
'intro':('arches',9202,['#f4ede2','#e7c08f','#c9733a','#1d4e63','#123341']),
'r1':('arches',9211,['#f2ebe0','#e4bc8a','#c46f37','#1d4e63','#123341']),
'r2':('columns',9212,['#edf1f3','#f6f8f9','#c9733a','#1d4e63','#123341']),
'r3':('hills',9213,['#e6eef0','#f2ecd6','#f0c27f','#a9c2a4','#7fa28a','#567a68']),
'g1':('waves',9221,['#22566c','#f0c083','#f7dfb8','#33738a','#22566c','#143a49']),
'g2':('arches',9222,['#f1e9dc','#e1b886','#c06b34','#1d4e63','#123341']),
'g3':('skyline',9223,['#1d4e63','#e9a865','#f8d9a4','#1b4a5e','#163d4e','#0f2b37']),
'g4':('waves',9224,['#1f526a','#eebd7f','#f6ddb4','#30708a','#1f526a','#133746']),
'g5':('columns',9225,['#ebeff1','#f5f7f8','#c6703a','#1d4e63','#123341']),
'g6':('hills',9226,['#e4ecef','#f0e9d2','#eebf7b','#a6bf9f','#7c9f86','#537764'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal Moscatel · Hostal de 2 estrellas en Pedregalejo, Málaga',see_rooms='Ver habitaciones',hero_k='Málaga · Pedregalejo',hero_t='Tu casa en Málaga, junto al mar de Pedregalejo',hero_s='Casa típica andaluza convertida en hostal familiar de 10 habitaciones, entre calles tranquilas y arboladas del antiguo barrio de pescadores.',
 intro_t='Pedregalejo, esencia marinera',intro_p1='Un barrio con paseo marítimo, chiringuitos y restaurantes, a unos 5 km del centro histórico y a 15 minutos en autobús.',
 intro_p2='Hoteleros de segunda y tercera generación que quieren ofrecerte un lugar acogedor y tranquilo para desconectar.',
 stats=['2 estrellas','10 habitaciones','Pet friendly','Playa de Pedregalejo'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Ocho tipos de habitación, de la individual a la doble con bañera de hidromasaje.',
 svcs=['Wifi','Aire acondicionado y calefacción','Se aceptan mascotas (ver normas)','Traslado desde el aeropuerto (bajo petición)','Gestión de coche de alquiler','Kit de playa: sombrilla y esterilla','Check-in tardío','Parking privado cercano'],
 loc_p='Calle Conde de las Navas, 9 · 29017 Málaga (Pedregalejo). Atención: lunes a jueves 9:30–17:00; viernes a domingo 10:30–15:00.',
 chips=['¿Qué habitaciones tiene?','¿Dónde está?','¿Cómo llego al centro?','¿Cómo se reserva?']),
'ca':dict(title='Hostal Moscatel · Hostal de 2 estrelles a Pedregalejo, Màlaga',see_rooms='Veure habitacions',hero_k='Màlaga · Pedregalejo',hero_t='La teva casa a Màlaga, al costat del mar de Pedregalejo',hero_s='Casa típica andalusa convertida en hostal familiar de 10 habitacions, entre carrers tranquils i arbrats de l\'antic barri de pescadors.',
 intro_t='Pedregalejo, essència mariner',intro_p1='Un barri amb passeig marítim, xiringuitos i restaurants, a uns 5 km del centre històric i a 15 minuts amb autobús.',
 intro_p2='Hotelers de segona i tercera generació que volen oferir-te un lloc acollidor i tranquil per desconnectar.',
 stats=['2 estrelles','10 habitacions','Pet friendly','Platja de Pedregalejo'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Vuit tipus d\'habitació, de la individual a la doble amb banyera d\'hidromassatge.',
 svcs=['Wifi','Aire condicionat i calefacció','S\'accepten mascotes (veure normes)','Trasllat des de l\'aeroport (sota petició)','Gestió de cotxe de lloguer','Kit de platja: para-sol i estora','Check-in tardà','Pàrquing privat a prop'],
 loc_p='Calle Conde de las Navas, 9 · 29017 Màlaga (Pedregalejo). Atenció: dilluns a dijous 9:30–17:00; divendres a diumenge 10:30–15:00.',
 chips=['Quines habitacions té?','On és?','Com arribo al centre?','Com es reserva?']),
'en':dict(title='Hostal Moscatel · 2-star hostal in Pedregalejo, Málaga',see_rooms='See the rooms',hero_k='Málaga · Pedregalejo',hero_t='Your home in Málaga, by the sea at Pedregalejo',hero_s='A typical Andalusian house turned into a family-run hostal with 10 rooms, among quiet tree-lined streets of the old fishing quarter.',
 intro_t='Pedregalejo, seafaring spirit',intro_p1='A district with a seafront promenade, beach bars and restaurants, about 5 km from the historic centre and 15 minutes by bus.',
 intro_p2='Second- and third-generation hoteliers who want to offer you a cosy, quiet place to unwind.',
 stats=['2 stars','10 rooms','Pet friendly','Pedregalejo beach'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Eight room types, from the single to the double with whirlpool bath.',
 svcs=['Wifi','Air conditioning and heating','Pets welcome (see rules)','Airport transfer (on request)','Car rental arranged','Beach kit: umbrella and mat','Late check-in','Private car park nearby'],
 loc_p='Calle Conde de las Navas, 9 · 29017 Málaga (Pedregalejo). Opening hours: Monday to Thursday 9:30–17:00; Friday to Sunday 10:30–15:00.',
 chips=['What rooms does it have?','Where is it?','How do I get to the centre?','How do I book?']),
'fr':dict(title='Hostal Moscatel · Hostal 2 étoiles à Pedregalejo, Malaga',see_rooms='Voir les chambres',hero_k='Malaga · Pedregalejo',hero_t='Votre maison à Malaga, au bord de la mer à Pedregalejo',hero_s='Maison andalouse typique devenue un hostal familial de 10 chambres, dans les rues calmes et arborées de l\'ancien quartier de pêcheurs.',
 intro_t='Pedregalejo, l\'esprit marin',intro_p1='Un quartier avec promenade maritime, paillotes et restaurants, à environ 5 km du centre historique et à 15 minutes en bus.',
 intro_p2='Des hôteliers de deuxième et troisième génération qui veulent vous offrir un lieu accueillant et calme pour décrocher.',
 stats=['2 étoiles','10 chambres','Animaux acceptés','Plage de Pedregalejo'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Huit types de chambre, de l\'individuelle à la double avec baignoire balnéo.',
 svcs=['Wifi','Climatisation et chauffage','Animaux acceptés (voir règles)','Transfert depuis l\'aéroport (sur demande)','Location de voiture organisée','Kit plage : parasol et natte','Arrivée tardive','Parking privé à proximité'],
 loc_p='Calle Conde de las Navas, 9 · 29017 Malaga (Pedregalejo). Accueil : du lundi au jeudi 9:30–17:00 ; du vendredi au dimanche 10:30–15:00.',
 chips=['Quelles chambres a-t-il ?','Où est-il ?','Comment aller au centre ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://reserva.hostalmoscatel.com/'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':RES,'fr':RES})
D=dict(name='Hostal Moscatel',ac='#1d4e63',ac2='#c9733a',ac2_a11y='#8a4a1e',book=BOOK,around=[],foot=FOOT,
 address='Calle Conde de las Navas, 9 · 29017 Málaga',phones=['+34 952 293 218'],emails=['info@hostalmoscatel.com'],maps='Hostal Moscatel, Calle Conde de las Navas 9, Málaga',t=T)
META=dict(repo='demo-hostal-moscatel-malaga',name='Hostal Moscatel',legal_name='Hostal Moscatel Salitre Málaga, S.L.',registry_ids=['CIF B93494961'],
 url='https://www.hostalmoscatel.com/',domain='hostalmoscatel.com',municipality='Málaga',province='Málaga',sector='hostal familiar de 2 estrellas en Pedregalejo (Málaga)',
 read_at='2026-10-29T13:08:00+01:00',created_at='2026-10-29T13:05:00+01:00',built_at='2026-10-29T13:20:00+01:00',audit_date='2026-10-29T12:52:40+01:00',
 rating=dict(value=4.2,coincide=['telefono','web'],date='2026-10-29T10:22:59+01:00',url='https://www.google.com/maps/place/Hostal+Moscatel/@36.7230583,-4.3664167,17z/data=!4m9!3m8!1s0xd725837fa35c76f:0xa0ee851c96f07918!5m2!4m1!1i2!8m2!3d36.7230583!4d-4.3664167!16s%2Fg%2F1q5bmz0nh'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas real del hostal (reserva.hostalmoscatel.com, el destino de su boton «Reservas»); la demo no construye ningun motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Hay habitación con bañera de hidromasaje?','K02'),('¿Dónde está?','K03'),('¿Cómo llego al centro?','K04'),('¿Cómo llego desde el aeropuerto?','K05'),('¿A qué hora es el check-in?','K06'),('¿Admiten mascotas?','K07'),('¿Qué servicios tiene?','K08'),('¿Cuál es el horario de atención?','K09'),('¿Cómo reservo?','K10'),('¿Quién es el titular?','K11'),('¿Está cerca de la playa?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Tienen gimnasio?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Hi ha habitació amb banyera d\'hidromassatge?','K02'),('On és?','K03'),('Com arribo al centre?','K04'),('Com hi arribo des de l\'aeroport?','K05'),('A quina hora és el check-in?','K06'),('Admeteu mascotes?','K07'),('Quins serveis té?','K08'),('Quin és l\'horari d\'atenció?','K09'),('Com reservo?','K10'),('Qui és el titular?','K11'),('És a prop de la platja?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Teniu gimnàs?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('Is there a room with a whirlpool bath?','K02'),('Where is it?','K03'),('How do I get to the centre?','K04'),('How do I get there from the airport?','K05'),('What time is check-in?','K06'),('Are pets allowed?','K07'),('What services are there?','K08'),('What are the opening hours?','K09'),('How do I book?','K10'),('Who is the owner?','K11'),('Is it close to the beach?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Do you have a gym?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Y a-t-il une chambre avec baignoire balnéo ?','K02'),('Où est-il ?','K03'),('Comment aller au centre ?','K04'),('Comment venir depuis l\'aéroport ?','K05'),('À quelle heure est le check-in ?','K06'),('Les animaux sont-ils admis ?','K07'),('Quels services propose-t-il ?','K08'),('Quels sont les horaires d\'accueil ?','K09'),('Comment réserver ?','K10'),('Qui est le titulaire ?','K11'),('Est-il près de la plage ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None)]}
