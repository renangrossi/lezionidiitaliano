#!/usr/bin/env python3
"""
Build levels/{level}.html: the hub page for one CEFR level — overview,
the ordered grid of lesson cards, a Test Yourself call-to-action, and a
compact Vocabulary section (two themed word tables with exercises).

Usage:
    python3 scripts/build_level_pages.py
"""
import json
import sys
from pathlib import Path
from string import ascii_uppercase

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REL = "../"

LEVEL_META = {
    "A1": ("Beginner", "Basic phrases and everyday expressions for immediate needs — greetings, gender, essere/avere, the present tense."),
    "A2": ("Elementary", "Simple, direct exchanges on familiar topics — irregular verbs, the passato prossimo, reflexive verbs, comparatives."),
    "B1": ("Intermediate", "Independent, everyday Italian — the imperfetto, indirect and combined pronouns, the future, conditional and imperative."),
    "B2": ("Upper Intermediate", "Fluent, spontaneous interaction — the subjunctive, hypothetical sentences, reported speech, the passive voice."),
    "C1": ("Advanced", "Flexible, effective language for professional and academic life — the full subjunctive system, gerund, register and connectors."),
    "C2": ("Proficient", "Precise, nuanced command of Italian — complex syntax, literary register, lexical nuance, and Italy's real linguistic variety."),
}

# Two compact vocabulary themes per level: (theme_title, [ (word, part_of_speech, meaning, italian_example, english_gloss), ... ])
VOCAB = {
    "A1": [
        ("La Famiglia (Family)", [
            ("la madre / la mamma", "noun", "mother / mom", "Mia madre lavora in ospedale.", "My mother works at a hospital."),
            ("il padre / il papà", "noun", "father / dad", "Mio padre cucina molto bene.", "My father cooks very well."),
            ("il fratello", "noun", "brother", "Ho un fratello più grande.", "I have an older brother."),
            ("la sorella", "noun", "sister", "Mia sorella vive a Torino.", "My sister lives in Turin."),
            ("i nonni", "noun", "grandparents", "I miei nonni abitano in campagna.", "My grandparents live in the countryside."),
            ("il/la figlio/a", "noun", "son / daughter", "Hanno due figli.", "They have two children."),
            ("marito / moglie", "noun", "husband / wife", "Mio marito è insegnante.", "My husband is a teacher."),
            ("sposato/a", "adjective", "married", "Sei sposata?", "Are you married?"),
        ]),
        ("Il Cibo di Tutti i Giorni (Everyday Food)", [
            ("il pane", "noun", "bread", "Compro il pane ogni mattina.", "I buy bread every morning."),
            ("l'acqua", "noun", "water", "Vorrei un bicchiere d'acqua.", "I'd like a glass of water."),
            ("la frutta", "noun", "fruit", "Mangio frutta ogni giorno.", "I eat fruit every day."),
            ("la verdura", "noun", "vegetables", "Non mi piace la verdura cotta.", "I don't like cooked vegetables."),
            ("il formaggio", "noun", "cheese", "Il parmigiano è un formaggio famoso.", "Parmesan is a famous cheese."),
            ("la carne", "noun", "meat", "Non mangio carne il venerdì.", "I don't eat meat on Fridays."),
            ("dolce / salato", "adjective", "sweet / salty", "Preferisco il salato al dolce.", "I prefer savory to sweet."),
            ("avere fame / sete", "expression", "to be hungry / thirsty", "Ho fame, mangiamo?", "I'm hungry, shall we eat?"),
        ]),
    ],
    "A2": [
        ("Viaggi (Travel)", [
            ("l'aeroporto", "noun", "airport", "Siamo arrivati in aeroporto in anticipo.", "We arrived at the airport early."),
            ("il biglietto", "noun", "ticket", "Ho comprato due biglietti per Roma.", "I bought two tickets to Rome."),
            ("la valigia", "noun", "suitcase", "La mia valigia è troppo pesante.", "My suitcase is too heavy."),
            ("il volo", "noun", "flight", "Il volo è stato cancellato.", "The flight was cancelled."),
            ("prenotare", "verb", "to book", "Ho prenotato l'albergo online.", "I booked the hotel online."),
            ("partire / arrivare", "verb", "to leave / to arrive", "Il treno parte alle nove.", "The train leaves at nine."),
            ("il passaporto", "noun", "passport", "Non dimenticare il passaporto!", "Don't forget your passport!"),
            ("la meta", "noun", "destination", "Napoli è la nostra prossima meta.", "Naples is our next destination."),
        ]),
        ("Al Ristorante (At the Restaurant)", [
            ("il menù", "noun", "menu", "Posso vedere il menù, per favore?", "Can I see the menu, please?"),
            ("il conto", "noun", "the bill", "Il conto, per favore.", "The bill, please."),
            ("prenotare un tavolo", "expression", "to book a table", "Ho prenotato un tavolo per due.", "I booked a table for two."),
            ("il cameriere / la cameriera", "noun", "waiter / waitress", "Il cameriere è molto gentile.", "The waiter is very kind."),
            ("consigliare", "verb", "to recommend", "Cosa mi consiglia?", "What do you recommend?"),
            ("il primo / il secondo", "noun", "first / second course", "Come primo prendo la pasta.", "For my first course I'll have pasta."),
            ("il contorno", "noun", "side dish", "Come contorno vorrei insalata.", "As a side I'd like salad."),
            ("il conto è sbagliato", "expression", "the bill is wrong", "Scusi, credo che il conto sia sbagliato.", "Excuse me, I think the bill is wrong."),
        ]),
    ],
    "B1": [
        ("Il Lavoro (Work)", [
            ("il colloquio", "noun", "job interview", "Ho un colloquio domani mattina.", "I have a job interview tomorrow morning."),
            ("assumere", "verb", "to hire", "L'azienda ha assunto tre persone.", "The company hired three people."),
            ("licenziare / licenziarsi", "verb", "to fire / to quit", "Si è licenziato dopo dieci anni.", "He quit after ten years."),
            ("lo stipendio", "noun", "salary", "Lo stipendio è aumentato quest'anno.", "My salary went up this year."),
            ("la scadenza", "noun", "deadline", "La scadenza del progetto è venerdì.", "The project deadline is Friday."),
            ("il collega", "noun", "colleague", "I miei colleghi sono molto simpatici.", "My colleagues are very nice."),
            ("fare straordinari", "expression", "to work overtime", "Ho fatto straordinari tutta la settimana.", "I worked overtime all week."),
            ("la carriera", "noun", "career", "Vuole fare carriera in questo settore.", "She wants to advance her career in this field."),
        ]),
        ("La Salute (Health)", [
            ("il medico / il dottore", "noun", "doctor", "Devo andare dal medico oggi.", "I have to go to the doctor today."),
            ("la febbre", "noun", "fever", "Ho la febbre da ieri sera.", "I've had a fever since last night."),
            ("il mal di testa", "noun", "headache", "Ho un forte mal di testa.", "I have a bad headache."),
            ("la ricetta", "noun", "prescription", "Il medico mi ha dato una ricetta.", "The doctor gave me a prescription."),
            ("guarire", "verb", "to recover, heal", "Spero di guarire presto.", "I hope to recover soon."),
            ("il pronto soccorso", "noun", "emergency room", "Siamo andati al pronto soccorso.", "We went to the emergency room."),
            ("fare male", "expression", "to hurt", "Mi fa male la schiena.", "My back hurts."),
            ("la farmacia", "noun", "pharmacy", "La farmacia è aperta fino a tardi.", "The pharmacy is open until late."),
        ]),
    ],
    "B2": [
        ("I Media (Media)", [
            ("la notizia", "noun", "news item", "Questa notizia mi ha sorpreso.", "This news surprised me."),
            ("il quotidiano", "noun", "daily newspaper", "Leggo il quotidiano ogni mattina.", "I read the daily paper every morning."),
            ("l'opinione pubblica", "noun", "public opinion", "L'opinione pubblica è divisa.", "Public opinion is divided."),
            ("diffondere", "verb", "to spread, broadcast", "La notizia si è diffusa rapidamente.", "The news spread quickly."),
            ("la fonte", "noun", "source", "Bisogna verificare la fonte.", "You need to verify the source."),
            ("i social media", "noun", "social media", "I social media influenzano l'opinione pubblica.", "Social media influences public opinion."),
            ("un articolo di approfondimento", "expression", "an in-depth article", "Ho letto un ottimo articolo di approfondimento.", "I read an excellent in-depth article."),
            ("l'attendibilità", "noun", "reliability, credibility", "Bisogna valutare l'attendibilità della fonte.", "You have to assess the source's reliability."),
        ]),
        ("L'Ambiente (Environment)", [
            ("il riscaldamento globale", "noun", "global warming", "Il riscaldamento globale preoccupa gli scienziati.", "Global warming worries scientists."),
            ("sostenibile", "adjective", "sustainable", "Cerchiamo soluzioni più sostenibili.", "We're looking for more sustainable solutions."),
            ("le energie rinnovabili", "noun", "renewable energy", "Investono nelle energie rinnovabili.", "They're investing in renewable energy."),
            ("l'inquinamento", "noun", "pollution", "L'inquinamento dell'aria è un problema serio.", "Air pollution is a serious problem."),
            ("ridurre", "verb", "to reduce", "Dobbiamo ridurre i rifiuti.", "We need to reduce waste."),
            ("il riciclaggio", "noun", "recycling", "Il riciclaggio è obbligatorio qui.", "Recycling is mandatory here."),
            ("l'impronta ecologica", "expression", "ecological footprint", "Vuole ridurre la sua impronta ecologica.", "She wants to reduce her ecological footprint."),
            ("tutelare l'ambiente", "expression", "to protect the environment", "Le nuove leggi tutelano l'ambiente.", "The new laws protect the environment."),
        ]),
    ],
    "C1": [
        ("Espressioni Idiomatiche (Idiomatic Expressions)", [
            ("in bocca al lupo", "expression", "good luck (lit. \"in the wolf's mouth\")", "In bocca al lupo per l'esame!", "Good luck on the exam!"),
            ("avere le mani in pasta", "expression", "to be involved/have connections", "Ha le mani in pasta in molti settori.", "He has fingers in many pies."),
            ("prendere due piccioni con una fava", "expression", "to kill two birds with one stone", "Così prendiamo due piccioni con una fava.", "That way we kill two birds with one stone."),
            ("essere al verde", "expression", "to be broke", "Non posso uscire, sono al verde.", "I can't go out, I'm broke."),
            ("fare orecchie da mercante", "expression", "to turn a deaf ear", "Fa sempre orecchie da mercante.", "He always turns a deaf ear."),
            ("rompere il ghiaccio", "expression", "to break the ice", "Una battuta può rompere il ghiaccio.", "A joke can break the ice."),
            ("avere la testa fra le nuvole", "expression", "to have one's head in the clouds", "Oggi ha proprio la testa fra le nuvole.", "He really has his head in the clouds today."),
            ("essere un pesce fuor d'acqua", "expression", "to be a fish out of water", "In quell'ambiente mi sentivo un pesce fuor d'acqua.", "I felt like a fish out of water in that environment."),
        ]),
        ("Registro Professionale (Professional Register)", [
            ("il quadro normativo", "noun", "regulatory framework", "Il quadro normativo è cambiato di recente.", "The regulatory framework recently changed."),
            ("in merito a", "expression", "regarding, concerning", "In merito alla Sua richiesta...", "Regarding your request..."),
            ("prendere atto di", "expression", "to take note of", "Prendiamo atto delle Sue osservazioni.", "We take note of your observations."),
            ("conformemente a", "expression", "in accordance with", "Conformemente alla normativa vigente...", "In accordance with current regulations..."),
            ("l'interlocutore", "noun", "the other party (in a discussion)", "Il nostro interlocutore ha proposto un'alternativa.", "The other party proposed an alternative."),
            ("il riscontro", "noun", "feedback, response", "Attendiamo un Suo riscontro.", "We await your response."),
            ("in allegato", "expression", "attached, enclosed", "In allegato trova il documento richiesto.", "Please find the requested document attached."),
            ("porgere distinti saluti", "expression", "to extend best regards (formal closing)", "Porgo distinti saluti.", "Best regards."),
        ]),
    ],
    "C2": [
        ("Sfumature Astratte (Abstract Nuance)", [
            ("l'ambivalenza", "noun", "ambivalence", "Prova una certa ambivalenza verso la decisione.", "He feels a certain ambivalence toward the decision."),
            ("il paradosso", "noun", "paradox", "È un vero paradosso della modernità.", "It's a real paradox of modernity."),
            ("intrinseco", "adjective", "intrinsic", "Il valore intrinseco dell'opera è indiscutibile.", "The work's intrinsic value is undeniable."),
            ("la sfumatura", "noun", "nuance, shade of meaning", "Ogni parola ha le sue sfumature.", "Every word has its nuances."),
            ("l'incongruenza", "noun", "inconsistency", "C'è un'incongruenza nel suo ragionamento.", "There's an inconsistency in his reasoning."),
            ("preminente", "adjective", "preeminent, foremost", "È una figura preminente nel suo campo.", "He's a preeminent figure in his field."),
            ("il retaggio", "noun", "legacy, heritage", "Il retaggio culturale della città è immenso.", "The city's cultural legacy is immense."),
            ("emblematico", "adjective", "emblematic", "È un caso emblematico del problema.", "It's an emblematic case of the problem."),
        ]),
        ("Il Linguaggio Letterario (Literary Language)", [
            ("l'ordito", "noun", "the underlying structure/plot (lit. \"weft\")", "L'ordito narrativo è complesso.", "The narrative structure is complex."),
            ("evocare", "verb", "to evoke", "Il testo evoca immagini vivide.", "The text evokes vivid images."),
            ("la metafora", "noun", "metaphor", "Usa spesso metafore marine.", "He often uses sea metaphors."),
            ("il registro", "noun", "register (of language)", "Il registro cambia da capitolo a capitolo.", "The register shifts from chapter to chapter."),
            ("malinconico", "adjective", "melancholic", "Il finale ha un tono malinconico.", "The ending has a melancholic tone."),
            ("la prosa", "noun", "prose", "La sua prosa è densa e precisa.", "Her prose is dense and precise."),
            ("l'incipit", "noun", "the opening lines (of a text)", "L'incipit del romanzo è memorabile.", "The novel's opening lines are memorable."),
            ("permeare", "verb", "to permeate", "Un senso di nostalgia permea tutto il libro.", "A sense of nostalgia permeates the whole book."),
        ]),
    ],
}

# Reading passage, listening script, writing prompt, speaking prompts per level.
READING = {
    "A1": ("Una Giornata di Marco", "<p>Mi chiamo Marco e vivo a Bologna. Ogni mattina mi sveglio alle sette e faccio colazione con un caffè e un cornetto. Poi vado al lavoro in bicicletta, perché non è lontano da casa mia.</p><p>A mezzogiorno mangio con i miei colleghi in un piccolo bar vicino all'ufficio. La sera, dopo il lavoro, mi piace fare una passeggiata o guardare un film con mia moglie. Andiamo a letto verso le undici.</p>"),
    "A2": ("Un Weekend a Firenze", "<p>Il weekend scorso sono andata a Firenze con due amiche. Siamo partite venerdì sera e siamo arrivate tardi, ma non importava: eravamo troppo emozionate! Sabato mattina abbiamo visitato il Duomo e poi abbiamo passeggiato lungo l'Arno.</p><p>Nel pomeriggio pioveva, quindi siamo entrate in un piccolo museo che non conoscevamo. La sera abbiamo mangiato una bistecca alla fiorentina in una trattoria consigliata da un'amica del posto. Domenica, prima di tornare a casa, abbiamo comprato un po' di souvenir al mercato.</p>"),
    "B1": ("Cambiare Lavoro a Trent'anni", "<p>Quando avevo ventotto anni, lavoravo in banca. Era un lavoro sicuro, ben pagato, ma non mi rendeva felice. Ogni mattina mi svegliavo con un peso sullo stomaco. Un giorno, dopo una lunga riflessione, ho deciso di licenziarmi e di seguire la mia vera passione: la fotografia.</p><p>I miei genitori erano preoccupati, e all'inizio anche io avevo paura di aver fatto la scelta sbagliata. Tuttavia, dopo due anni di lavoro duro, sono riuscita a costruirmi una piccola clientela. Oggi non guadagno quanto guadagnavo in banca, ma mi sveglio felice.</p>"),
    "B2": ("Il Dibattito sullo Smart Working", "<p>Da quando molte aziende italiane hanno adottato lo smart working in modo permanente, il dibattito pubblico si è concentrato su vantaggi e svantaggi di questa trasformazione. Da un lato, i sostenitori sottolineano la maggiore flessibilità, la riduzione dei tempi di spostamento e un migliore equilibrio tra vita privata e professionale.</p><p>Dall'altro, i critici fanno notare che il lavoro da remoto può indebolire i legami tra colleghi e rendere più difficile la formazione dei nuovi assunti. Inoltre, non tutte le professioni si prestano a questo modello: chi lavora nel settore manifatturiero o sanitario, ad esempio, non ha la stessa possibilità di scelta. Il vero equilibrio, secondo molti esperti, sta in un modello ibrido, capace di coniugare autonomia e collaborazione diretta.</p>"),
    "C1": ("La Memoria e le Lingue", "<p>Chi impara una lingua straniera in età adulta sviluppa spesso una relazione singolare con la propria memoria linguistica. Alcuni ricercatori sostengono che ogni lingua che parliamo attivi, in un certo senso, una versione leggermente diversa di noi stessi: il tono, i riferimenti culturali, persino l'umorismo cambiano a seconda dell'idioma utilizzato.</p><p>Non sorprende, dunque, che molti bilingui riferiscano di sentirsi \"più diretti\" in una lingua e \"più cauti\" in un'altra, o che certe emozioni risultino più facili da esprimere in una lingua acquisita piuttosto che in quella materna — quasi che la distanza linguistica offrisse una sorta di protezione emotiva.</p>"),
    "C2": ("Sul Tempo e sulla Lentezza", "<p>Vi è, nella cultura contemporanea, una silenziosa nostalgia per ciò che un tempo si chiamava semplicemente \"il tempo\" — non inteso come risorsa da ottimizzare, bensì come dimensione da abitare. La retorica della produttività, così pervasiva nel discorso pubblico odierno, sembra aver eroso la possibilità stessa di un'esperienza non finalizzata: leggere senza uno scopo dichiarato, camminare senza una destinazione precisa, conversare senza un ordine del giorno.</p><p>Non è un caso che movimenti come lo \"slow living\" abbiano trovato, negli ultimi anni, un'eco tanto ampia: essi non propongono, in fondo, nulla di rivoluzionario, ma il recupero di un ritmo che l'uomo ha conosciuto per la quasi totalità della propria storia, e che solo di recente ha iniziato a percepire come un lusso anziché come una normalità.</p>"),
}

LISTENING = {
    "A1": ("Al Bar", "<p><strong>Barista:</strong> Buongiorno! Cosa prende?<br><strong>Cliente:</strong> Buongiorno. Vorrei un cappuccino e un cornetto, per favore.<br><strong>Barista:</strong> Subito. Vuole anche dell'acqua?<br><strong>Cliente:</strong> No, grazie, va bene così. Quant'è?<br><strong>Barista:</strong> Sono tre euro e cinquanta.<br><strong>Cliente:</strong> Ecco a Lei. Grazie, arrivederci!<br><strong>Barista:</strong> Grazie a Lei, buona giornata!</p>"),
    "A2": ("Prenotare un Tavolo per Telefono", "<p><strong>Ristorante:</strong> Ristorante Da Luigi, buonasera.<br><strong>Cliente:</strong> Buonasera, vorrei prenotare un tavolo per stasera, se possibile.<br><strong>Ristorante:</strong> Certo, per quante persone?<br><strong>Cliente:</strong> Per quattro persone, verso le otto.<br><strong>Ristorante:</strong> Perfetto, abbiamo un tavolo libero. A che nome, scusi?<br><strong>Cliente:</strong> A nome Bianchi.<br><strong>Ristorante:</strong> Bene, signor Bianchi, l'aspettiamo alle otto.</p>"),
    "B1": ("Un Colloquio di Lavoro", "<p><strong>Selezionatrice:</strong> Allora, mi parli un po' della sua esperienza precedente.<br><strong>Candidato:</strong> Ho lavorato tre anni come assistente marketing in un'azienda di Milano. Mi occupavo soprattutto dei social media e delle campagne pubblicitarie.<br><strong>Selezionatrice:</strong> Interessante. E perché ha deciso di lasciare quel lavoro?<br><strong>Candidato:</strong> Cercavo nuove sfide, e questa posizione mi sembra più in linea con i miei obiettivi a lungo termine.<br><strong>Selezionatrice:</strong> Capisco. Ha domande per me?<br><strong>Candidato:</strong> Sì, volevo chiedere come è strutturato il team.</p>"),
    "B2": ("Un Podcast sul Traffico in Città", "<p><strong>Conduttore:</strong> Oggi parliamo di un tema che riguarda molti di noi: il traffico nelle grandi città. Con me c'è un'esperta di mobilità urbana.<br><strong>Esperta:</strong> Grazie per l'invito. Il punto centrale è che le città italiane, storicamente, non sono state progettate per il traffico automobilistico attuale.<br><strong>Conduttore:</strong> Quindi, secondo lei, qual è la soluzione?<br><strong>Esperta:</strong> Non credo esista un'unica soluzione. Bisognerebbe investire di più nei trasporti pubblici e, allo stesso tempo, incentivare l'uso della bicicletta, specialmente nei centri storici.<br><strong>Conduttore:</strong> E i cittadini sarebbero disposti a rinunciare alla macchina?<br><strong>Esperta:</strong> Con le giuste infrastrutture, credo proprio di sì.</p>"),
    "C1": ("Un'Intervista su Un Nuovo Romanzo", "<p><strong>Giornalista:</strong> Il suo ultimo romanzo affronta temi piuttosto complessi: la memoria, l'identità, l'esilio. Da dove nasce questa scelta?<br><strong>Autrice:</strong> In realtà nasce da una domanda molto personale: cosa resta di noi quando lasciamo il luogo in cui siamo cresciuti? Non volevo scrivere un saggio, ma raccontare questa domanda attraverso una storia.<br><strong>Giornalista:</strong> C'è un elemento autobiografico?<br><strong>Autrice:</strong> Certamente, anche se ho preferito trasfigurarlo attraverso la finzione. Credo che la narrativa permetta di dire certe verità più liberamente della saggistica.</p>"),
    "C2": ("Una Conferenza sull'Evoluzione della Lingua", "<p><strong>Relatore:</strong> Quello che spesso si tende a dimenticare, parlando di \"purezza\" linguistica, è che ogni lingua viva è, per definizione, in perenne trasformazione. L'italiano stesso, quale lo conosciamo oggi, è il risultato di secoli di contaminazioni, prestiti, riadattamenti.<br><strong>Moderatrice:</strong> Alcuni sostengono però che l'influenza dell'inglese, in particolare, rappresenti una minaccia specifica...<br><strong>Relatore:</strong> È una posizione comprensibile, ma storicamente poco fondata. Ogni epoca ha avuto la propria lingua \"minacciosa\" — il francese nell'Ottocento, ad esempio. La lingua, semmai, va osservata, non difesa come fosse un monumento immobile.</p>"),
}

WRITING = {
    "A1": "Write 5-6 simple sentences introducing yourself: your name, where you're from, your age, your family, and one thing you like. Use essere, avere, and the present tense of at least two regular verbs.",
    "A2": "Write a short paragraph (6-8 sentences) about your last vacation, using the passato prossimo. Mention where you went, what you did, and how you felt — try to use at least one essere verb and one avere verb.",
    "B1": "Write a short narrative (8-10 sentences) about something unexpected that happened to you. Use both the passato prossimo and the imperfetto — remember, the imperfetto sets the scene, the passato prossimo moves the story forward.",
    "B2": "Write a short opinion paragraph (10-12 sentences) about a topic you care about (technology, the environment, remote work...). Use at least two subjunctive triggers (penso che, è importante che, dubito che) and one hypothetical sentence.",
    "C1": "Write a formal email (10-12 sentences) requesting information from a company or institution. Use appropriate formal register throughout, at least one advanced connector (tuttavia, dato che, di conseguenza), and a proper formal opening and closing.",
    "C2": "Write a short argumentative paragraph (12-15 sentences) taking a position on a debated topic. Structure it with a clear thesis, a concession to the opposing view (è vero che...), and a rebuttal (tuttavia...). Aim for varied, cohesive sentence structure — avoid repeating the same noun phrase twice in a row.",
}

SPEAKING = {
    "A1": ["Describe yourself in one minute: name, age, nationality, family, and what you do.", "Ask a partner three questions using question words (dove, quando, come, perché)."],
    "A2": ["Tell a partner about your typical week using frequency adverbs (sempre, spesso, a volte).", "Describe your last vacation using the passato prossimo."],
    "B1": ["Discuss what you would do if you won the lottery, using the condizionale.", "Give a partner directions and instructions using the imperative, both informal and formal."],
    "B2": ["Debate a current issue with a partner, using subjunctive triggers to express opinion and doubt.", "Describe a hypothetical situation (\"If I could change one thing about my city...\") using the periodo ipotetico."],
    "C1": ["Give a short persuasive talk (2 minutes) on a topic of your choice, using advanced connectors.", "Role-play a formal complaint and its polite, hedged response."],
    "C2": ["Debate a nuanced topic, deliberately using hedging expressions (sembra che, non sono del tutto d'accordo) to soften your claims.", "Summarize a short article or news story aloud in under a minute, using your own words."],
}


def esc(s):
    import html
    return html.escape(s, quote=False)


def lesson_cards(level_slug, nav_list):
    cards = []
    for i, entry in enumerate(nav_list):
        idx = ascii_uppercase[i] if i < 26 else str(i + 1)
        lesson = json.loads((REPO_ROOT / "curriculum" / level_slug / f"{entry['slug']}.json").read_text(encoding="utf-8"))
        cards.append(f"""<article class="lesson-card">
            <span class="lesson-card__index" aria-hidden="true">{idx}</span>
            <h3><a class="lesson-card__title-link" href="{level_slug}/{entry['slug']}.html">{esc(lesson['title'])}</a></h3>
            <p>{esc(lesson['subtitle'])}</p>
        </article>""")
    return "".join(cards)


def vocab_section(level_code):
    themes = VOCAB.get(level_code, [])
    blocks = []
    for ti, (theme_title, words) in enumerate(themes):
        rows = "".join(
            f"<tr><td><strong>{esc(w)}</strong></td><td class=\"text-muted\">{esc(pos)}</td><td>{esc(meaning)}</td><td><em>{esc(it_ex)} &mdash; {esc(en_ex)}</em></td></tr>"
            for w, pos, meaning, it_ex, en_ex in words
        )
        opts = [w for w, *_ in words][:6]
        items = []
        for i, (w, pos, meaning, it_ex, en_ex) in enumerate(words[:4]):
            items.append({
                "id": f"{level_code.lower()}v{ti}i{i}",
                "prompt": f"Which word means “{meaning}”?",
                "options": opts if w in opts else opts + [w],
                "answerIndex": (opts if w in opts else opts + [w]).index(w),
                "explanation": f"{w} means {meaning}.",
            })
        ex_block = {"id": f"{level_code.lower()}-vocab-{ti}-mc", "type": "multiple-choice", "title": "Match the Meaning", "items": items}
        blocks.append(f"""<div class="card" style="margin-bottom:var(--space-lg);">
            <h3>{esc(theme_title)}</h3>
            <div class="table-scroll">
                <table class="ref-table">
                    <thead><tr><th>Word</th><th>Type</th><th>Meaning</th><th>Example</th></tr></thead>
                    <tbody>{rows}</tbody>
                </table>
            </div>
            <div style="margin-top:var(--space-md);"><div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(ex_block, ensure_ascii=False)}</script></div></div>
        </div>""")
    return f"""<section id="vocabulary" class="section section--tight" aria-labelledby="vocabulary-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code}</p>
                <h2 id="vocabulary-heading">Vocabulary</h2>
                <p>Themed word groups for real situations, each with example sentences and a quick check.</p>
            </div>
            {"".join(blocks)}
        </div>
    </section>"""


def reading_section(level_code):
    title, passage = READING[level_code]
    ex = {
        "id": f"{level_code.lower()}-reading-mc", "type": "true-false", "title": "Comprehension Check",
        "instructions": "Based on the passage above, mark each statement true or false.",
        "items": [
            {"id": f"{level_code.lower()}rd1", "statement": "The passage is written in the first person.", "answer": True, "explanation": "The narrator speaks about their own experience using io-forms."},
        ],
    }
    return f"""<section id="reading" class="section section--surface" aria-labelledby="reading-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code} &middot; Reading</p>
                <h2 id="reading-heading">{esc(title)}</h2>
            </div>
            <div class="card"><div class="prose">{passage}</div></div>
            <div style="margin-top:var(--space-md);"><div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(ex, ensure_ascii=False)}</script></div></div>
        </div>
    </section>"""


def listening_section(level_code):
    title, script = LISTENING[level_code]
    return f"""<section id="listening" class="section section--tight" aria-labelledby="listening-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code} &middot; Listening (script)</p>
                <h2 id="listening-heading">{esc(title)}</h2>
                <p>No audio recording yet &mdash; read this exchange as a listening-style dialogue and imagine the pacing of real speech.</p>
            </div>
            <div class="card"><div class="prose">{script}</div></div>
        </div>
    </section>"""


def writing_speaking_section(level_code):
    prompt = WRITING[level_code]
    speaking_items = "".join(f"<li>{esc(p)}</li>" for p in SPEAKING[level_code])
    return f"""<section id="writing" class="section section--surface" aria-labelledby="writing-heading">
        <div class="section__inner split">
            <div>
                <p class="eyebrow">{level_code} &middot; Writing</p>
                <h2 id="writing-heading">Guided Writing Task</h2>
                <p style="max-width:56ch;">{esc(prompt)}</p>
            </div>
            <div class="card card--feature" id="speaking">
                <p class="eyebrow">{level_code} &middot; Speaking</p>
                <h3 style="font-size:var(--step-0);">Conversation Prompts</h3>
                <ul class="summary-list">{speaking_items}</ul>
            </div>
        </div>
    </section>"""


def build(level_code, level_slug):
    name, blurb = LEVEL_META[level_code]
    nav_map = json.loads((REPO_ROOT / "scripts" / "lesson_nav_map.json").read_text(encoding="utf-8"))
    nav_list = nav_map.get(level_slug, [])
    index = json.loads((REPO_ROOT / "curriculum" / "index.json").read_text(encoding="utf-8"))
    overview = index["levels"][level_code]["overview"]

    title = f"{level_code} — {name} — Renan the Teacher Italian Course"
    description = f"{level_code} {name}: {blurb}"[:300]
    breadcrumb = (
        f'<li><a href="{REL}index.html">Home</a></li>'
        f'<li aria-current="page">Levels</li>'
        f'<li aria-current="page">{level_code} {name}</li>'
    )
    page_header = f"""<div class="page-header">
        {site_chrome.STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">Let's learn</p>
                <h1>{level_code} &mdash; {esc(name)}</h1>
                <p class="page-header__lede">{esc(blurb)}</p>
            </div>
        </div>
    </div>"""
    toc = ('<div class="level-toc" data-scrollspy><div class="level-toc__inner">'
           '<a href="#lessons">Lessons</a><a href="#test-yourself">Test Yourself</a>'
           '<a href="#vocabulary">Vocabulary</a><a href="#reading">Reading</a>'
           '<a href="#listening">Listening</a><a href="#writing">Writing</a>'
           '<a href="#speaking">Speaking</a></div></div>')

    overview_section = f"""<section class="section section--tight" aria-labelledby="overview-heading">
        <div class="section__inner">
            <h2 id="overview-heading" class="visually-hidden">Overview</h2>
            <p style="max-width:62ch;font-size:var(--step-0);color:var(--color-text-muted);">{esc(overview)}</p>
        </div>
    </section>"""

    lessons_section = f"""<section id="lessons" class="section section--surface" aria-labelledby="grammar-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code}</p>
                <h2 id="grammar-heading">Lessons</h2>
                <p>{len(nav_list)} lessons, in order &mdash; each one builds on the one before it.</p>
            </div>
            <div class="grid">{lesson_cards(level_slug, nav_list)}</div>
        </div>
    </section>"""

    ty_section = f"""<section id="test-yourself" class="section section--tight" aria-labelledby="ty-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code}</p>
                <h2 id="ty-heading">Test Yourself</h2>
                <p>A single, comprehensive review covering every {level_code} grammar topic &mdash; every exercise from every lesson, mixed together.</p>
            </div>
            <a class="btn btn--accent" href="{level_slug}/test-yourself.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="15" r="6"/><path d="m9 10-3-7"/><path d="m15 10 3-7"/><path d="M9.5 15.5 12 17l2.5-1.5"/></svg>Start the test</a>
        </div>
    </section>"""

    out = []
    out.append(site_chrome.head(REL, title, description, extra_css=["exercises", "lessons"]))
    out.append(site_chrome.header(REL, level_code, breadcrumb, active_top="levels"))
    out.append(page_header)
    out.append(toc)
    out.append(overview_section)
    out.append(lessons_section)
    out.append(ty_section)
    out.append(vocab_section(level_code))
    out.append(reading_section(level_code))
    out.append(listening_section(level_code))
    out.append(writing_speaking_section(level_code))
    out.append(site_chrome.footer(REL, extra_scripts=["exercises.js", "mastery.js"]))

    out_path = REPO_ROOT / "levels" / f"{level_slug}.html"
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"Built {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    for code, slug in [("A1", "a1"), ("A2", "a2"), ("B1", "b1"), ("B2", "b2"), ("C1", "c1"), ("C2", "c2")]:
        build(code, slug)
