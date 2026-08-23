# -*- coding: utf-8 -*-
"""C1 — Advanced curriculum data."""

OVERVIEW = ("C1 completes the subjunctive system with the trapassato and full sequence of "
            "tenses, adds the impossible-past conditional, the gerund and progressive form, "
            "pronominal verbs, and the discourse connectors and register choices that separate "
            "fluent Italian from merely correct Italian.")

LESSONS = [
    {
        "id": "c1-congiuntivo-trapassato",
        "level": "C1", "unit": "1", "order": 1, "skill": "grammar", "strand": "subjunctive",
        "title": "Il Congiuntivo Trapassato e la Concordanza dei Tempi",
        "subtitle": "The subjunctive's past-before-past tense, and the complete sequence-of-tenses picture.",
        "objectives": [
            "Form the congiuntivo trapassato",
            "Apply the full sequence-of-tenses table across all four subjunctive forms",
            "Use the congiuntivo trapassato for a completed action before a past main clause",
        ],
        "content": {
            "intro": "With the congiuntivo trapassato, Italian's subjunctive system is complete — four tenses (presente, passato, imperfetto, trapassato) that map cleanly onto the four indicative time frames.",
            "explanation": "<p>Formed with the congiuntivo imperfetto of avere/essere + past participle: <em>avessi parlato, fossi partito/a</em>. It expresses an action that had already happened before the time of a past main clause — the subjunctive counterpart of the trapassato prossimo.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Sequence of tenses (simplified, standard cases)</caption><thead><tr><th>Main clause</th><th>Same time / later</th><th>Earlier (already happened)</th></tr></thead><tbody><tr><td>Present/future</td><td>congiuntivo presente</td><td>congiuntivo passato</td></tr><tr><td>Past/conditional</td><td>congiuntivo imperfetto</td><td>congiuntivo trapassato</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Formation", "body": "<p>avessi/avessi/avesse/avessimo/aveste/avessero, or fossi/fossi/fosse/fossimo/foste/fossero, + past participle (agreeing with the subject when the auxiliary is essere).</p>"},
                {"heading": "b) Use", "body": "<p><em>Pensavo che avesse già finito.</em> (I thought he had already finished.) <em>Non credevo che fossero già partiti.</em> (I didn't think they had already left.)</p>"},
            ],
            "examples": [
                {"it": "Pensavo che aveste già mangiato.", "en": "I thought you had already eaten."},
                {"it": "Speravo che non fosse successo niente di grave.", "en": "I hoped nothing serious had happened."},
                {"it": "Non sapevo che si fossero già conosciuti.", "en": "I didn't know they had already met each other."},
                {"it": "Era il film più bello che avessi mai visto.", "en": "It was the best film I had ever seen."},
            ],
            "commonMistakes": [
                {"wrong": "Pensavo che avesse finito ieri. (needs already-completed nuance but uses the wrong tense)", "right": "Pensavo che avesse già finito.", "why": "An action completed before the past main clause needs the trapassato, matching the earlier-than-earlier timeline."},
                {"wrong": "Era il film più bello che ho mai visto.", "right": "Era il film più bello che avessi mai visto.", "why": "A superlative relative clause (\"the most... that...\") conventionally triggers the subjunctive in Italian, and past context calls for the trapassato here."},
            ],
        },
        "exercises": [
            {"id": "c1ct-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "c1ct1", "prompt": "Pensavo che tu ___ (già - partire).", "answers": [["fossi già partito", "fossi già partita"]], "explanation": "Congiuntivo trapassato of partire (essere).", "options": ["fossi già partito", "sia già partito", "eri già partito"]},
                {"id": "c1ct2", "prompt": "Non credevo che loro ___ (finire) il progetto così presto.", "answers": [["avessero finito"]], "explanation": "Congiuntivo trapassato of finire (avere).", "options": ["avessero finito", "abbiano finito", "avevano finito"]},
             ]},
            {"id": "c1ct-mc", "type": "multiple-choice", "title": "Choose the Correct Tense",
             "items": [
                {"id": "c1ct3", "prompt": "\"It was the hardest exam I had ever taken.\"", "options": ["che avevo mai fatto", "che avessi mai fatto", "che ho mai fatto"], "answerIndex": 1, "explanation": "Superlative relative clause in a past context → congiuntivo trapassato."},
             ]},
        ],
        "summary": [
            "Congiuntivo trapassato = congiuntivo imperfetto of avere/essere + past participle.",
            "Completes the four-tense subjunctive system, mirroring the indicative's time frames.",
            "Used for an action already completed before a past-tense (or conditional) main clause.",
        ],
    },
    {
        "id": "c1-periodo-ipotetico-terzo-tipo",
        "level": "C1", "unit": "1", "order": 2, "skill": "grammar", "strand": "conditionals",
        "title": "Il Periodo Ipotetico di Terzo Tipo",
        "subtitle": "\"If I had known...\" — the impossible past.",
        "objectives": [
            "Form the third type hypothetical sentence for the unreal past",
            "Use the condizionale passato in the main clause",
            "Recognize mixed hypotheticals (past condition, present consequence)",
        ],
        "content": {
            "intro": "The third type of hypothetical sentence talks about something that didn't happen in the past — and, by logical necessity, whose consequence also never happened.",
            "explanation": "<p>Se + congiuntivo trapassato, condizionale passato (avrei/sarei + past participle): <em>Se avessi saputo, sarei venuto.</em> (If I had known, I would have come — but I didn't know, and I didn't come.) Both halves describe a counterfactual past.</p>",
            "rules": [
                {"heading": "a) Formation", "body": "<p>se + avessi/fossi + participle, avrei/sarei + participle: <em>Se avessi studiato di più, avrei passato l'esame.</em></p>"},
                {"heading": "b) Mixed hypothetical", "body": "<p>A past condition can have a present consequence: <em>Se avessi accettato quel lavoro, ora vivrei a Milano.</em> (If I had accepted that job, I'd be living in Milan now.) — condizionale presente in the main clause, since the consequence is felt now, not back then.</p>"},
            ],
            "examples": [
                {"it": "Se avessi saputo, ti avrei chiamato subito.", "en": "If I had known, I would have called you right away."},
                {"it": "Se non avessimo perso il treno, saremmo già arrivati.", "en": "If we hadn't missed the train, we would already have arrived."},
                {"it": "Avrei accettato l'offerta se me l'avessero fatta prima.", "en": "I would have accepted the offer if they had made it to me sooner."},
                {"it": "Se mi fossi laureato in ingegneria, ora lavorerei in un'altra azienda.", "en": "If I had graduated in engineering, I'd be working at a different company now. (mixed)"},
            ],
            "commonMistakes": [
                {"wrong": "Se avrei saputo, sarei venuto.", "right": "Se avessi saputo, sarei venuto.", "why": "The se-clause needs the congiuntivo trapassato, never the conditional — same rule as the second type, one tense further back."},
                {"wrong": "Se avessi studiato di più, avessi passato l'esame.", "right": "Se avessi studiato di più, avrei passato l'esame.", "why": "The main clause needs the condizionale passato, not a repeated subjunctive."},
            ],
        },
        "exercises": [
            {"id": "c1pt-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "c1pt1", "prompt": "Se ___ (io - sapere), ti ___ (avvisare) subito.", "answers": [["avessi saputo"], ["avrei avvisato"]], "explanation": "Third type: congiuntivo trapassato + condizionale passato.", "options": ["avessi saputo", "sapevo", "avrei avvisato", "avvisavo"]},
                {"id": "c1pt2", "prompt": "Se non ___ (perdere) il volo, ___ (arrivare) in tempo.", "answers": [["avessimo perso"], ["saremmo arrivati", "saremmo arrivate"]], "explanation": "Third type, essere auxiliary in the main clause.", "options": ["avessimo perso", "abbiamo perso", "saremmo arrivati", "arriveremmo"]},
             ]},
            {"id": "c1pt-mc", "type": "multiple-choice", "title": "Choose the Correct Sentence",
             "items": [
                {"id": "c1pt3", "prompt": "\"If you had told me, I would have helped you.\"", "options": ["Se mi avresti detto, ti avrei aiutato.", "Se mi avessi detto, ti avrei aiutato.", "Se mi dicevi, ti aiutavo."], "answerIndex": 1, "explanation": "Se + congiuntivo trapassato, condizionale passato in the main clause."},
             ]},
        ],
        "summary": [
            "Third type (unreal past): se + congiuntivo trapassato, condizionale passato.",
            "Both halves are counterfactual: neither the condition nor its consequence actually happened.",
            "A mixed hypothetical pairs a past condition with a condizionale presente for a present consequence.",
        ],
    },
    {
        "id": "c1-gerundio-progressivo",
        "level": "C1", "unit": "1", "order": 3, "skill": "grammar", "strand": "gerund",
        "title": "Il Gerundio e la Forma Progressiva",
        "subtitle": "Stare + gerundio for actions in progress, and the gerund's other uses.",
        "objectives": [
            "Form the gerund of regular and common irregular verbs",
            "Use stare + gerundio for an action happening right now",
            "Use the gerund alone to express cause, means, or a simultaneous action",
        ],
        "content": {
            "intro": "The Italian gerund (-ando/-endo) is the base of the progressive form and, used on its own, a compact way to express cause, method, or a simultaneous action without a connector word.",
            "explanation": "<p>Regular gerunds: -are &rarr; -ando, -ere/-ire &rarr; -endo. A few verbs use their old Latin stem, matching the imperfetto: <em>fare &rarr; facendo, dire &rarr; dicendo, bere &rarr; bevendo</em>. Object and reflexive pronouns attach to the end of a standalone gerund, but go before <em>stare</em> in the progressive.</p>",
            "rules": [
                {"heading": "a) Stare + gerundio — progressive", "body": "<p>Marks an action genuinely in progress right now, more emphatic than the simple present: <em>Sto leggendo un libro.</em> (I am [right now] reading a book.) Pronouns go before stare or attach to the gerund: <em>Lo sto leggendo. / Sto leggendolo.</em></p>"},
                {"heading": "b) Gerund alone — cause, means, simultaneous action", "body": "<ul><li>Cause: <em>Studiando ogni giorno, ho imparato molto.</em> (By studying every day, I learned a lot.)</li><li>Simultaneous action: <em>Ho letto il giornale bevendo il caffè.</em> (I read the paper while drinking coffee.)</li></ul>"},
            ],
            "examples": [
                {"it": "Sto scrivendo un'email importante.", "en": "I'm [right now] writing an important email."},
                {"it": "Stavamo dormendo quando è arrivata la chiamata.", "en": "We were sleeping when the call came in."},
                {"it": "Camminando per la città, ho scoperto un bel caffè.", "en": "Walking through the city, I discovered a nice café."},
                {"it": "Ha imparato l'italiano guardando film senza sottotitoli.", "en": "He learned Italian by watching films without subtitles."},
            ],
            "commonMistakes": [
                {"wrong": "Sto leggere un libro.", "right": "Sto leggendo un libro.", "why": "Stare requires the gerund, not the infinitive, in the progressive form."},
                {"wrong": "Facendo attenzione. (spelled as if regular)", "right": "facendo (irregular stem fac-)", "why": "Fare's gerund uses the old stem fac-, matching its imperfetto (facevo), not a regular -are gerund."},
            ],
        },
        "exercises": [
            {"id": "c1gp-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "c1gp1", "prompt": "Cosa ___ (tu - fare)? Sto ___.", "answers": [["stai facendo"], ["studiando"]], "explanation": "Progressive: stare + gerundio.", "options": ["stai facendo", "fai", "studiando", "studiare"]},
                {"id": "c1gp2", "prompt": "___ (Bere) il caffè, ho letto le notizie.", "answers": [["Bevendo"]], "explanation": "Bere's irregular gerund stem: bevendo.", "options": ["Bevendo", "Berendo", "Bevuto"]},
             ]},
            {"id": "c1gp-mc", "type": "multiple-choice", "title": "Choose the Correct Form",
             "items": [
                {"id": "c1gp3", "prompt": "\"I learned a lot by traveling.\"", "options": ["Ho imparato molto viaggiare.", "Ho imparato molto viaggiando.", "Ho imparato molto viaggiato."], "answerIndex": 1, "explanation": "The gerund expresses means/method here."},
             ]},
        ],
        "summary": [
            "Regular gerund: -are→-ando, -ere/-ire→-endo; some verbs use an irregular Latin-derived stem.",
            "Stare + gerundio marks an action genuinely in progress right now.",
            "A standalone gerund can express cause, method, or a simultaneous action, with pronouns attached to its end.",
        ],
    },
    {
        "id": "c1-connettivi-testuali",
        "level": "C1", "unit": "1", "order": 4, "skill": "writing", "strand": "discourse",
        "title": "Connettivi Testuali Avanzati",
        "subtitle": "Linking ideas like a fluent writer: contrast, cause, consequence, addition.",
        "objectives": [
            "Use a range of connectors beyond the basic e, ma, perché",
            "Choose connectors appropriate to formal written Italian",
            "Structure a short argumentative paragraph with clear logical connectors",
        ],
        "content": {
            "intro": "Fluent written Italian relies on a richer set of connectors than everyday speech — signalling contrast, consequence, and addition precisely instead of stringing ideas together with e and ma.",
            "explanation": "<p>These connectors are especially common in essays, articles, and formal writing/speech. Many pair naturally: <em>da un lato... dall'altro</em> (on one hand... on the other).</p>",
            "rules": [
                {"heading": "a) Contrast", "body": "<p><em>tuttavia, però, nonostante ciò, d'altra parte, al contrario, mentre</em> — all stronger/more formal alternatives to ma.</p>"},
                {"heading": "b) Cause and consequence", "body": "<p><em>poiché, dato che, dal momento che</em> (cause, more formal than perché); <em>quindi, perciò, di conseguenza, pertanto</em> (consequence, more formal than allora).</p>"},
                {"heading": "c) Addition and sequence", "body": "<p><em>inoltre, per di più, in aggiunta</em> (addition); <em>innanzitutto, in primo luogo, infine</em> (sequencing an argument).</p>"},
            ],
            "examples": [
                {"it": "Il progetto è ambizioso; tuttavia, i tempi sono realistici.", "en": "The project is ambitious; however, the timeline is realistic."},
                {"it": "Dato che il traffico era intenso, siamo arrivati in ritardo.", "en": "Since traffic was heavy, we arrived late."},
                {"it": "Il costo è aumentato; di conseguenza, abbiamo dovuto rivedere il budget.", "en": "The cost increased; as a result, we had to revise the budget."},
                {"it": "Da un lato capisco le tue ragioni; dall'altro, non sono d'accordo.", "en": "On one hand I understand your reasons; on the other, I don't agree."},
            ],
            "commonMistakes": [
                {"wrong": "Perciò using it to introduce a cause (instead of a consequence)", "right": "poiché/dato che for cause; perciò/quindi for consequence", "why": "Cause and consequence connectors aren't interchangeable — mixing them reverses the logical relationship of the sentence."},
                {"wrong": "Overusing tuttavia/quindi in casual conversation", "right": "però/allora in casual speech; tuttavia/quindi in writing", "why": "These heavier connectors read as formal/written register — using them constantly in casual speech can sound stilted."},
            ],
        },
        "exercises": [
            {"id": "c1ct2-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "c1ct2a", "prompt": "___ pioveva, siamo usciti lo stesso. (since/given that)", "answers": [["Dato che", "Poiché"]], "explanation": "Cause connector.", "options": ["Dato che", "Quindi", "Tuttavia"]},
                {"id": "c1ct2b", "prompt": "Ha lavorato molto; ___, ha ottenuto una promozione. (as a result)", "answers": [["di conseguenza", "quindi", "perciò"]], "explanation": "Consequence connector.", "options": ["di conseguenza", "poiché", "mentre"]},
             ]},
            {"id": "c1ct2-mc", "type": "multiple-choice", "title": "Choose the Right Connector",
             "items": [
                {"id": "c1ct2c", "prompt": "Which connector expresses contrast?", "options": ["inoltre", "tuttavia", "perciò"], "answerIndex": 1, "explanation": "Tuttavia (however) expresses contrast."},
             ]},
        ],
        "summary": [
            "Formal connectors express cause (poiché, dato che), consequence (quindi, perciò), and contrast (tuttavia, d'altra parte) more precisely than e/ma/perché.",
            "Cause and consequence connectors are not interchangeable — they mark opposite logical directions.",
            "Heavier connectors belong mainly to written/formal register, not everyday conversation.",
        ],
    },
    {
        "id": "c1-registro-formale-informale",
        "level": "C1", "unit": "1", "order": 5, "skill": "writing", "strand": "register",
        "title": "Registro Formale e Informale nella Scrittura",
        "subtitle": "Choosing vocabulary and structure to match the situation.",
        "objectives": [
            "Identify markers of formal vs. informal written register",
            "Rewrite an informal sentence in a formal register and vice versa",
            "Use standard formal opening/closing formulas for emails and letters",
        ],
        "content": {
            "intro": "Beyond tu vs. Lei, Italian marks formality through vocabulary choice, sentence structure, and set phrases — especially visible in written communication.",
            "explanation": "<p>Formal writing favors longer, more explicit sentences, the connectors from the previous lesson, and a vocabulary that avoids colloquialisms. Informal writing (texts, casual emails to friends) allows contractions, colloquial vocabulary, and much shorter sentences.</p>",
            "rules": [
                {"heading": "a) Vocabulary pairs (informal → formal)", "body": "<p><em>un sacco di &rarr; molti/numerosi; un po' &rarr; un po' (fine) / leggermente; fare un giro &rarr; effettuare una visita; iniziare &rarr; dare inizio a; dire &rarr; comunicare, dichiarare</em></p>"},
                {"heading": "b) Email/letter formulas", "body": "<ul><li>Formal opening: <em>Gentile Sig.ra/Sig. [Cognome], La contatto per...</em></li><li>Formal closing: <em>Cordiali saluti / Distinti saluti</em></li><li>Informal opening: <em>Ciao [Nome],</em></li><li>Informal closing: <em>A presto! / Un abbraccio</em></li></ul>"},
            ],
            "examples": [
                {"it": "Gentile Dott.ssa Rossi, Le scrivo per chiederLe informazioni riguardo al Suo prossimo seminario.", "en": "Dear Dr. Rossi, I am writing to ask you for information about your upcoming seminar."},
                {"it": "Ciao Marco, ti scrivo per chiederti se sei libero sabato!", "en": "Hi Marco, I'm writing to ask if you're free Saturday!"},
                {"it": "La informiamo che la Sua richiesta è stata accolta.", "en": "We inform you that your request has been accepted."},
                {"it": "Ti volevo dire che ho accettato il lavoro!", "en": "I wanted to tell you I accepted the job!"},
            ],
            "commonMistakes": [
                {"wrong": "Ciao Direttore, volevo sapere... (mixing informal greeting with a formal context)", "right": "Gentile Direttore, vorrei sapere...", "why": "Mixing an informal opening with formal content and pronouns is inconsistent — pick one register and keep it throughout."},
                {"wrong": "Ending a formal email with Ciao!", "right": "Ending with Cordiali saluti / Distinti saluti", "why": "Ciao is strictly informal — a formal closing formula is expected to match a Lei-register email."},
            ],
        },
        "exercises": [
            {"id": "c1rf-mc", "type": "multiple-choice", "title": "Formal or Informal?",
             "items": [
                {"id": "c1rf1", "prompt": "Which closing fits a formal email to a company?", "options": ["A presto!", "Cordiali saluti", "Ciao ciao!"], "answerIndex": 1, "explanation": "Cordiali saluti is the standard formal closing."},
                {"id": "c1rf2", "prompt": "Which is the more formal way to say \"a lot of people\"?", "options": ["un sacco di gente", "numerose persone", "tanta gente"], "answerIndex": 1, "explanation": "Numerose persone is the formal-register equivalent."},
             ]},
            {"id": "c1rf-correction", "type": "correction", "title": "Fix the Register",
             "items": [
                {"id": "c1rf3", "incorrect": "Gentile Direttore, ciao! Volevo un po' di info.", "answer": ["Gentile Direttore, Le scrivo per richiedere alcune informazioni."], "explanation": "A formal opening (Gentile Direttore) should be followed by consistently formal vocabulary and structure, not casual expressions."},
             ]},
        ],
        "summary": [
            "Formal register favors explicit, longer sentences and formal vocabulary; informal favors contractions and colloquialisms.",
            "Set formulas exist for opening/closing formal and informal correspondence — don't mix them.",
            "Consistency matters more than any single word choice: pick a register and hold it throughout.",
        ],
    },
    {
        "id": "c1-verbi-pronominali",
        "level": "C1", "unit": "1", "order": 6, "skill": "grammar", "strand": "pronominal-verbs",
        "title": "Verbi Pronominali",
        "subtitle": "Farsi, andarsene, cavarsela — idiomatic verbs built from pronoun combinations.",
        "objectives": [
            "Recognize pronominal verbs as fixed idiomatic units",
            "Conjugate andarsene and cavarsela correctly across their pronoun set",
            "Use common pronominal verbs naturally in context",
        ],
        "content": {
            "intro": "Pronominal verbs fuse a base verb with one or more pronouns into an idiomatic unit whose meaning often can't be guessed from the parts — a hallmark of fluent, native-sounding Italian.",
            "explanation": "<p><strong>Andarsene</strong> (to leave, to go away) combines the reflexive andarsi with ne, both of which move together through the conjugation. <strong>Cavarsela</strong> (to get by, to manage) combines cavarsi with la. These aren't literal reflexive/partitive meanings anymore — they're memorized as whole idiomatic verbs.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Andarsene — present tense</caption><thead><tr><th>Subject</th><th>Form</th></tr></thead><tbody><tr><td>io</td><td>me ne vado</td></tr><tr><td>tu</td><td>te ne vai</td></tr><tr><td>lui/lei</td><td>se ne va</td></tr><tr><td>noi</td><td>ce ne andiamo</td></tr><tr><td>voi</td><td>ve ne andate</td></tr><tr><td>loro</td><td>se ne vanno</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Common pronominal verbs", "body": "<ul><li><em>farcela</em> — to manage, to make it: <em>Ce l'ho fatta!</em> (I made it!)</li><li><em>cavarsela</em> — to get by: <em>Me la cavo bene in inglese.</em> (I get by well in English.)</li><li><em>prendersela</em> — to take offense/get upset: <em>Non prendertela!</em> (Don't take it personally!)</li><li><em>sentirsela</em> — to feel up to something: <em>Non me la sento di uscire stasera.</em></li></ul>"},
                {"heading": "b) Passato prossimo of andarsene", "body": "<p>Takes essere, with the participle agreeing: <em>Se n'è andato.</em> (He left.) <em>Se ne sono andate.</em> (They [f.] left.)</p>"},
            ],
            "examples": [
                {"it": "Me ne vado, ci vediamo domani.", "en": "I'm leaving, see you tomorrow."},
                {"it": "Non ce la faccio più.", "en": "I can't take it anymore."},
                {"it": "Se l'è cavata benissimo all'esame.", "en": "He/she got through the exam really well."},
                {"it": "Non prendertela, non era colpa tua.", "en": "Don't take it personally, it wasn't your fault."},
            ],
            "commonMistakes": [
                {"wrong": "Io vado ne.", "right": "Me ne vado.", "why": "Andarsene's pronouns (me/te/se/ce/ve/se + ne) precede the verb as a fixed unit — they can't be reordered or split."},
                {"wrong": "Ho fatta cela. (word order)", "right": "Ce l'ho fatta.", "why": "The combined pronoun ce l' comes before the auxiliary, as one fixed sequence."},
            ],
        },
        "exercises": [
            {"id": "c1vp-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "c1vp1", "prompt": "Sono stanco, ___ vado a dormire. (andarsene, io)", "answers": [["me ne"]], "explanation": "Io form of andarsene: me ne vado.", "options": ["me ne", "mi ne", "ne mi"]},
                {"id": "c1vp2", "prompt": "Finalmente ___ fatta! (farcela, io, passato prossimo)", "answers": [["ce l'ho"]], "explanation": "Ce l'ho fatta — I made it.", "options": ["ce l'ho", "l'ho ce", "ce ho la"]},
             ]},
            {"id": "c1vp-mc", "type": "multiple-choice", "title": "Choose the Correct Meaning",
             "items": [
                {"id": "c1vp3", "prompt": "\"Non prendertela\" means...", "options": ["Don't take it (an object) with you.", "Don't take offense / don't be upset about it.", "Don't take it away from him."], "answerIndex": 1, "explanation": "Prendersela is an idiomatic pronominal verb meaning to take offense/get upset."},
             ]},
        ],
        "summary": [
            "Pronominal verbs (andarsene, cavarsela, farcela, prendersela) are idiomatic fixed units, not literal reflexive+pronoun combinations.",
            "Their pronoun sequence moves together as a block through the conjugation.",
            "Andarsene takes essere in the passato prossimo, with normal participle agreement.",
        ],
    },
    {
        "id": "c1-sfumature-congiuntivo",
        "level": "C1", "unit": "1", "order": 7, "skill": "grammar", "strand": "subjunctive",
        "title": "Sfumature del Congiuntivo",
        "subtitle": "The independent subjunctive: wishes, doubts, and concession without che.",
        "objectives": [
            "Use the subjunctive independently to express a wish (magari, che)",
            "Use the subjunctive in concessive clauses (benché, sebbene, nonostante)",
            "Recognize the doubt-expressing subjunctive in a standalone question",
        ],
        "content": {
            "intro": "Beyond che-clauses, the subjunctive appears on its own to express wishes, doubts, and concession — small, idiomatic patterns that make speech sound genuinely fluent rather than textbook-correct.",
            "explanation": "<p>An independent subjunctive can open a sentence with an implied \"I wish\" (<em>Magari piovesse!</em>, If only it would rain!) or ask a rhetorical, doubtful question (<em>Che sia già partito?</em>, Could he have already left?). Concessive conjunctions (although/even though) also trigger the subjunctive, unlike their English equivalents.</p>",
            "rules": [
                {"heading": "a) Wishes", "body": "<p><em>Magari</em> + congiuntivo (imperfetto for something unlikely/impossible, trapassato for the past): <em>Magari avessi più tempo!</em> (If only I had more time!) <em>Che Dio ce la mandi buona.</em> (a set expression, \"let's hope for the best\")</p>"},
                {"heading": "b) Concession", "body": "<p><em>benché, sebbene, nonostante, malgrado</em> + congiuntivo: <em>Benché piova, usciamo lo stesso.</em> (Although it's raining, we're going out anyway.)</p>"},
                {"heading": "c) Doubtful questions", "body": "<p><em>Che + congiuntivo</em> as a standalone rhetorical question: <em>Che si sia dimenticato?</em> (Could he have forgotten?)</p>"},
            ],
            "examples": [
                {"it": "Magari fosse così semplice!", "en": "If only it were that simple!"},
                {"it": "Sebbene sia stanco, continuo a lavorare.", "en": "Although I'm tired, I keep working."},
                {"it": "Nonostante avessero poco tempo, hanno finito il progetto.", "en": "Despite having little time, they finished the project."},
                {"it": "Che abbia frainteso?", "en": "Could he/she have misunderstood?"},
            ],
            "commonMistakes": [
                {"wrong": "Benché piove, usciamo lo stesso.", "right": "Benché piova, usciamo lo stesso.", "why": "Concessive conjunctions like benché always trigger the subjunctive in Italian, unlike English \"although\", which takes a normal indicative."},
                {"wrong": "Magari ho più tempo!", "right": "Magari avessi più tempo!", "why": "An unreal/unlikely wish with magari needs the congiuntivo imperfetto, not the indicative."},
            ],
        },
        "exercises": [
            {"id": "c1sc-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "c1sc1", "prompt": "Sebbene ___ (essere) difficile, ce l'ho fatta.", "answers": [["fosse"]], "explanation": "Sebbene always triggers the subjunctive.", "options": ["fosse", "era", "è stato"]},
                {"id": "c1sc2", "prompt": "Magari ___ (io - potere) venire con te!", "answers": [["potessi"]], "explanation": "Unreal wish with magari → congiuntivo imperfetto.", "options": ["potessi", "posso", "potrei"]},
             ]},
            {"id": "c1sc-mc", "type": "multiple-choice", "title": "Choose the Correct Form",
             "items": [
                {"id": "c1sc3", "prompt": "\"Despite the rain, we went out.\"", "options": ["Nonostante piovesse, siamo usciti.", "Nonostante pioveva, siamo usciti.", "Nonostante piove, siamo usciti."], "answerIndex": 0, "explanation": "Nonostante triggers the subjunctive."},
             ]},
        ],
        "summary": [
            "Magari + congiuntivo expresses an unreal wish; che + congiuntivo can open a doubtful, rhetorical question.",
            "Concessive conjunctions (benché, sebbene, nonostante, malgrado) always trigger the subjunctive, unlike English \"although\".",
            "These independent uses go beyond che-clause triggers and mark genuinely fluent speech.",
        ],
    },
    {
        "id": "c1-ci-ne-avanzato",
        "level": "C1", "unit": "1", "order": 8, "skill": "grammar", "strand": "pronouns",
        "title": "Ci e Ne Avanzati con l'Imperativo e l'Infinito",
        "subtitle": "Combining pronouns, ci and ne with commands and infinitives, including irregular tu forms.",
        "objectives": [
            "Attach ci, ne, and combined pronouns correctly to the informal imperative",
            "Apply consonant doubling with the irregular tu imperatives (va', da', fa', sta', di')",
            "Combine multiple pronouns with an infinitive after another verb",
        ],
        "content": {
            "intro": "At this level, pronoun attachment needs to work smoothly even in the trickiest combinations: an irregular tu imperative plus a pronoun, or a chain of pronouns onto an infinitive after a modal verb.",
            "explanation": "<p>The apostrophized irregular tu imperatives (va', da', fa', sta', di') <strong>double the first consonant</strong> of any pronoun that attaches to them (except gli): <em>va' + ci &rarr; vacci; da' + mi &rarr; dammi; fa' + lo &rarr; fallo; di' + gli &rarr; digli</em> (gli never doubles). With a modal + infinitive, pronouns (including combined ones, ci, ne) can attach to the infinitive or precede the modal — both correct, but the attached form is more common in formal writing.</p>",
            "rules": [
                {"heading": "a) Consonant doubling after va'/da'/fa'/sta'/di'", "body": "<ul><li><em>Vacci subito!</em> (Go there right away!)</li><li><em>Dammi una mano.</em> (Give me a hand.)</li><li><em>Fallo per me.</em> (Do it for me.)</li><li><em>Digli la verità.</em> (Tell him the truth — gli never doubles.)</li></ul>"},
                {"heading": "b) Pronouns with modal + infinitive", "body": "<p><em>Voglio andarci.</em> / <em>Ci voglio andare.</em> <em>Devo dirglielo.</em> / <em>Glielo devo dire.</em> (combined pronoun, both positions correct)</p>"},
            ],
            "examples": [
                {"it": "Vacci tu, io sono troppo stanco.", "en": "You go there, I'm too tired."},
                {"it": "Dammi il tuo numero, ti chiamo dopo.", "en": "Give me your number, I'll call you later."},
                {"it": "Fallo subito, non aspettare.", "en": "Do it right away, don't wait."},
                {"it": "Devo dirglielo prima che sia troppo tardi.", "en": "I have to tell him/her before it's too late."},
                {"it": "Non voglio più parlarne.", "en": "I don't want to talk about it anymore."},
            ],
            "commonMistakes": [
                {"wrong": "Vaci subito!", "right": "Vacci subito!", "why": "The pronoun's first consonant doubles after va'/da'/fa'/sta' — a single c would be a spelling error here."},
                {"wrong": "Digli la verità → Dilli la verità", "right": "Digli la verità (no doubling)", "why": "Gli is the one pronoun that never doubles after these irregular imperatives — a genuine, memorized exception."},
            ],
        },
        "exercises": [
            {"id": "c1cn-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "c1cn1", "prompt": "___ subito! (Vai lì — irregular tu imperative + ci)", "answers": [["Vacci"]], "explanation": "Va' + ci, with consonant doubling: vacci.", "options": ["Vacci", "Vaci", "Va'ci"]},
                {"id": "c1cn2", "prompt": "___ una mano, per favore! (Dai a me — irregular tu imperative + mi)", "answers": [["Dammi"]], "explanation": "Da' + mi, with doubling: dammi.", "options": ["Dammi", "Dami", "Da'mi"]},
             ]},
            {"id": "c1cn-mc", "type": "multiple-choice", "title": "Choose the Correct Form",
             "items": [
                {"id": "c1cn3", "prompt": "\"Tell him!\" (Digli, or the wrong doubled version?)", "options": ["Dilli!", "Digli!", "Diglli!"], "answerIndex": 1, "explanation": "Gli never doubles after these irregular imperatives."},
             ]},
        ],
        "summary": [
            "Va', da', fa', sta', di' double the first consonant of an attached pronoun — except gli, which never doubles.",
            "With modal + infinitive, pronouns (including combined ones) can attach to the infinitive or precede the modal.",
            "These fine points of pronoun placement are a genuine marker of fluent, C1-level control.",
        ],
    },
]
