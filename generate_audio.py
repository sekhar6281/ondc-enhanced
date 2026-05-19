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
    'te_05': "నాగాలాండ్ యొక్క Ilandlo ప్రభుత్వ యాప్ ONDC లో లైవ్‌గా ఉంది, ప్రతి లావాదేవీ నుండి ప్లాట్‌ఫామ్ ఫీజులు వసూలు చేస్తోంది. AP కి నాగాలాండ్ కంటే 50 రెట్లు జనాభా, 80 రెట్లు GDP మరియు చాలా అభివృద్ధి చెందిన డిజిటల్ మౌలిక సదుపాయం ఉంది. నాగాలాండ్ చేయగలిగితే, AP చేయకపోవడానికి ఎటువంటి కారణం లేదు.",
    'en_06': "ONDC's national network is in its highest-growth phase today. Early state participants set the governance standards, claim the market share, and establish infrastructure that latecomers must then integrate with. AP's window to be a founding participant, not a follower, is open now.",
    'te_06': "ONDC యొక్క జాతీయ నెట్‌వర్క్ ఈ రోజు అత్యధిక వృద్ధి దశలో ఉంది. తొలి రాష్ట్ర పాల్గొనేవారు పాలన ప్రమాణాలు నిర్ణయిస్తారు, మార్కెట్ వాటా స్వాధీనం చేసుకుంటారు మరియు తదుపరి వచ్చేవారు అనుసరించాల్సిన మౌలిక సదుపాయాన్ని స్థాపిస్తారు. AP అనుచరుడు కాదు, వ్యవస్థాపక పాల్గొనేవారిగా ఉండే అవకాశం ఇప్పుడు తెరిచి ఉంది.",
    'en_07': "This table quantifies the exact revenue AP currently cedes to private platforms across 8 sectors — food, tickets, services, GI products, grocery, MSME, agri, and government procurement — derived from publicly available national transaction data, not projection.",
    'te_07': "ఈ పట్టిక AP ప్రస్తుతం 8 రంగాలలో ప్రైవేట్ ప్లాట్‌ఫామ్‌లకు వదిలేస్తున్న ఖచ్చితమైన ఆదాయాన్ని లెక్కిస్తుంది. ఆహారం, టికెట్లు, సేవలు, GI ఉత్పత్తులు, కిరాణా, MSME, వ్యవసాయం మరియు ప్రభుత్వ సేకరణ. అంచనా కాదు, బహిరంగంగా అందుబాటులో ఉన్న జాతీయ లావాదేవీ డేటా నుండి తీసుకోబడింది.",
    'en_08': "APCS is governed in three clean layers. Government of AP sets policy and earns revenue. Zian operates as the Nodal Agency accountable to the state. And eight commerce verticals run on top. Each layer has defined responsibilities, defined metrics, and defined consequences for underperformance.",
    'te_08': "APCS మూడు స్పష్టమైన పొరలలో పరిపాలించబడుతుంది. AP ప్రభుత్వం విధానాలు నిర్ణయిస్తుంది మరియు ఆదాయం సంపాదిస్తుంది. Zian రాష్ట్రానికి జవాబుదారీగా నోడల్ ఏజెన్సీగా నిర్వహిస్తుంది. ఎనిమిది వాణిజ్య వర్టికల్‌లు పైన నడుస్తాయి. ప్రతి పొరకు నిర్వచించిన బాధ్యతలు, కొలతలు మరియు పనితీరు తగ్గినపుడు పరిణామాలు ఉన్నాయి.",
    'en_09': "Eight verticals — Food, Tickets, My Services, Brand Andhra GI, Grocery, MSME, Agri, and Government Procurement — are each designed to capture a specific market currently dominated by private platforms, with AP earning a fee on every transaction across all eight.",
    'te_09': "ఎనిమిది వర్టికల్‌లు — ఆహారం, టికెట్లు, నా సేవలు, బ్రాండ్ ఆంధ్ర GI, కిరాణా, MSME, వ్యవసాయం మరియు ప్రభుత్వ సేకరణ — ప్రతి ఒక్కటి ప్రస్తుతం ప్రైవేట్ ప్లాట్‌ఫామ్‌లు ఆధిపత్యం చేస్తున్న నిర్దిష్ట మార్కెట్‌ను స్వాధీనం చేసుకోవడానికి రూపొందించబడ్డాయి, AP అన్ని ఎనిమిదింటిలో ప్రతి లావాదేవీపై ఫీజు సంపాదిస్తుంది.",
    'en_10': "BookMyShow earns hundreds of crores annually from AP cinema-goers with zero revenue share to the state. APCS's Ticket vertical reclaims that revenue for AP's treasury while adding forensic watermarking-based anti-piracy enforcement — a direct benefit to AP's 12,000 crore rupee film industry.",
    'te_10': "BookMyShow రాష్ట్రానికి సున్నా రెవెన్యూ షేర్‌తో AP సినిమా ప్రేమికుల నుండి ప్రతి సంవత్సరం వందల కోట్లు సంపాదిస్తుంది. APCS యొక్క టికెట్ వర్టికల్ ఆ ఆదాయాన్ని AP ఖజానాకు తిరిగి పొందుతూ ఫోరెన్సిక్ వాటర్‌మార్కింగ్-ఆధారిత యాంటీ-పైరసీ అమలును జోడిస్తుంది. AP యొక్క 12,000 కోట్ల చలనచిత్ర పరిశ్రమకు ప్రత్యక్ష ప్రయోజనం."
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
