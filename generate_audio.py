import asyncio, edge_tts, os

os.makedirs('audio', exist_ok=True)

scripts = {
    'en_01': "AP's residents spend an estimated 8,000 plus crore rupees every year on private commerce platforms. Every rupee of that commission leaves the state. AP Commerce Stack is the proposal that brings it home.",
    'te_01': "AP నివాసులు ప్రతి సంవత్సరం ప్రైవేట్ కామర్స్ ప్లాట్‌ఫామ్‌లపై అంచనా 8,000 కోట్లు పైగా ఖర్చు చేస్తున్నారు. ఆ కమీషన్ ప్రతి రూపాయి రాష్ట్రం విడిచి వెళ్తోంది. AP Commerce Stack దాన్ని తిరిగి తీసుకొచ్చే ప్రతిపాదన.",
    'en_02': "AP citizens spend thousands of crores annually on Swiggy, Zomato, BookMyShow, and Meesho. Every rupee of that platform commission leaves the state. AP Commerce Stack exists to stop that permanently and redirect that revenue to the state exchequer.",
    'te_02': "AP పౌరులు Swiggy, Zomato, BookMyShow, మరియు Meesho లో వేల కోట్లు ఖర్చు చేస్తున్నారు. ఆ ప్లాట్‌ఫామ్ కమీషన్ ప్రతి రూపాయి రాష్ట్రం విడిచి వెళ్తోంది. AP Commerce Stack దాన్ని శాశ్వతంగా ఆపి ఆ ఆదాయాన్ని రాష్ట్ర ఖజానాకు మళ్లించడానికి ఉద్దేశించబడింది.",
    'en_03': "Just as NPCI built UPI and collects a fee on every digital payment in India, AP can build APCS and collect a fee on every digital commerce transaction in the state. The legal framework through ONDC already exists. What is needed is the political will to act.",
    'te_03': "NPCI, UPI ని నిర్మించి భారతదేశంలో ప్రతి డిజిటల్ చెల్లింపుపై ఫీజు వసూలు చేసినట్లే, AP కూడా APCS ని నిర్మించి రాష్ట్రంలో ప్రతి డిజిటల్ వాణిజ్య లావాదేవీపై ఫీజు వసూలు చేయవచ్చు. ONDC ద్వారా చట్టపరమైన చట్రం ఇప్పటికే ఉంది. అవసరమైనది రాజకీయ సంకల్పం మాత్రమే.",
    'en_04': "ONDC is the Government of India's open commerce protocol that decouples buyers from platforms. AP can enter as a Buyer-Side Network Operator today, exactly the way Nagaland's Ilandlo and Magicpin have, and begin earning from every transaction AP residents place on the network.",
    'te_04': "ONDC అనేది భారత ప్రభుత్వం యొక్క ఓపెన్ కామర్స్ ప్రోటోకాల్, ఇది కొనుగోలుదారులను ప్లాట్‌ఫామ్‌ల నుండి వేరు చేస్తుంది. నాగాలాండ్ Ilandlo మరియు Magicpin చేసినట్లే, AP ఈ రోజు బయ్యర్-సైడ్ నెట్‌వర్క్ ఆపరేటర్‌గా ప్రవేశించి, AP నివాసులు నెట్‌వర్క్‌లో చేసే ప్రతి లావాదేవీ నుండి సంపాదించడం ప్రారంభించవచ్చు.",
    'en_05': "Nagaland's Ilandlo government app is live on ONDC, collecting platform fees from every transaction. AP has 50 times Nagaland's population, 80 times its GDP, and a far more developed digital infrastructure. If Nagaland could do it, AP has no reason not to.",
    'te_05': "నాగాలాండ్ యొక్క Ilandlo ప్రభుత్వ యాప్ ONDC లో లైవ్‌గా ఉంది, ప్రతి లావాదేవీ నుండి ప్లాట్‌ఫామ్ ఫీజులు వసూలు చేస్తోంది. AP కి నాగాలాండ్ కంటే 50 రెట్లు జనాభా, 80 రెట్లు GDP మరియు చాలా అభివృద్ధి చెందిన డిజిటల్ మౌలిక సదుపాయం ఉంది. నాగాలాండ్ చేయగలిగితే, AP చేయకపోవడానికి ఎటువంటి కారణం లేదు."
}

voices = { 'en': 'en-IN-PrabhatNeural', 'te': 'te-IN-MohanNeural' }

async def generate(key, text):
    lang = key[:2]
    out  = f'audio/{key}.mp3'
    await edge_tts.Communicate(text, voices[lang]).save(out)
    print(f'OK {out}')

async def main():
    await asyncio.gather(*[generate(k, v) for k, v in scripts.items()])

asyncio.run(main())
