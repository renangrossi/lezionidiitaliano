# -*- coding: utf-8 -*-
"""C2 — Proficient curriculum data."""

OVERVIEW = ("C2 moves past the mechanics of grammar into control of style: complex syntax and "
            "inversion, literary and archaic register, precise collocations, cohesive devices for "
            "long texts, hedging and nuanced modality, and awareness of Italy's real linguistic "
            "variety. This is fluency as judgment, not just correctness.")

LESSONS = [
    {
        "id": "c2-sintassi-complessa",
        "level": "C2", "unit": "1", "order": 1, "skill": "grammar", "strand": "syntax",
        "title": "Sintassi Complessa e Inversione",
        "subtitle": "Reordering a sentence for emphasis, without breaking it.",
        "objectives": [
            "Use subject-verb inversion for stylistic emphasis in written Italian",
            "Front a subordinate clause or object for emphasis",
            "Recognize inversion after certain adverbs and in formal narrative style",
        ],
        "content": {
            "intro": "Standard Italian word order (subject-verb-object) is flexible enough that shifting an element to the front or inverting subject and verb reshapes emphasis — a tool fluent writers use deliberately.",
            "explanation": "<p>Fronting an object or subordinate clause pulls focus onto it: <em>Quello che mi preoccupa è il costo.</em> (What worries me is the cost — instead of <em>Il costo mi preoccupa.</em>) Certain adverbs and adverbial phrases at the start of a sentence trigger or favor inversion in more formal/literary registers: <em>Solo così si può capire davvero.</em> (Only in this way can one truly understand.)</p>",
            "rules": [
                {"heading": "a) Subject postponed for emphasis", "body": "<p><em>È arrivato il momento della verità.</em> (The moment of truth has arrived — subject after the verb, more dramatic than Il momento della verità è arrivato.)</p>"},
                {"heading": "b) Fronting for focus", "body": "<p><em>Di questo non voglio parlare.</em> (About this, I don't want to talk — object/prepositional phrase fronted for emphasis.)</p>"},
                {"heading": "c) Cleft sentences", "body": "<p><em>È proprio questo il punto.</em> (This is exactly the point.) <em>Fu allora che capii tutto.</em> (It was then that I understood everything.)</p>"},
            ],
            "examples": [
                {"it": "Solo allora capii la gravità della situazione.", "en": "Only then did I understand the seriousness of the situation."},
                {"it": "È il coraggio che ammiro di più in lei.", "en": "It's her courage that I admire most."},
                {"it": "Di soldi non ne aveva mai avuti molti.", "en": "Money, he had never had much of."},
                {"it": "Non appena arrivò la notizia, tutti tacquero.", "en": "As soon as the news arrived, everyone fell silent."},
            ],
            "commonMistakes": [
                {"wrong": "Overusing inversion in casual conversation", "right": "Reserve heavy inversion for formal writing/narrative", "why": "Constant inversion sounds stilted or overly literary in everyday spoken Italian — it's a stylistic register choice, not a default."},
                {"wrong": "È il coraggio che io ammiro di più in lei. (redundant pronoun)", "right": "È il coraggio che ammiro di più in lei.", "why": "In a cleft sentence like this, the subject pronoun io is typically dropped as usual — adding it back doesn't add emphasis, since the cleft structure itself already provides it."},
            ],
        },
        "exercises": [
            {"id": "c2sc-mc", "type": "multiple-choice", "title": "Identify the Emphasis Structure",
             "items": [
                {"id": "c2sc1", "prompt": "\"È proprio questo il problema.\" — What does this structure emphasize?", "options": ["The subject, questo/il problema", "Nothing in particular", "The verb only"], "answerIndex": 0, "explanation": "This is a cleft sentence, structurally designed to spotlight questo/il problema."},
                {"id": "c2sc2", "prompt": "Which register favors frequent subject-verb inversion?", "options": ["Casual texting", "Formal/literary narrative", "Everyday small talk"], "answerIndex": 1, "explanation": "Inversion for emphasis is a formal/literary stylistic device."},
             ]},
            {"id": "c2sc-correction", "type": "correction", "title": "Improve for Emphasis",
             "items": [
                {"id": "c2sc3", "incorrect": "Il coraggio è la qualità che ammiro di più in lei. (flat, no emphasis structure)", "answer": ["È il coraggio la qualità che ammiro di più in lei."], "explanation": "Fronting/clefting il coraggio sharpens the emphasis compared to the flat statement."},
             ]},
        ],
        "summary": [
            "Fronting an object, subordinate clause, or adverbial phrase shifts emphasis onto it.",
            "Cleft sentences (è... che) spotlight one element of the sentence explicitly.",
            "Heavy inversion is a formal/literary register choice, not the everyday default.",
        ],
    },
    {
        "id": "c2-registro-letterario",
        "level": "C2", "unit": "1", "order": 2, "skill": "reading", "strand": "register",
        "title": "Registro Letterario e Forme Arcaiche",
        "subtitle": "Recognizing (not necessarily using) the Italian of literature and formal narration.",
        "objectives": [
            "Recognize the passato remoto and its role in literary narration",
            "Identify archaic/literary pronouns and vocabulary",
            "Read a short literary-register passage with comprehension",
        ],
        "content": {
            "intro": "Literary Italian preserves forms that have largely disappeared from speech — most importantly the passato remoto, still standard for narrating completed historical or fictional events at a narrative distance.",
            "explanation": "<p>The <strong>passato remoto</strong> is a simple (one-word) past tense, used in place of the passato prossimo for events felt as historically or narratively distant — literature, history books, some regional speech (especially southern Italy, where it remains common even in conversation). At C2, the goal is <em>recognition</em> for reading, not necessarily active production.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Passato remoto — parlare, credere, partire (recognition forms)</caption><thead><tr><th>Subject</th><th>parlare</th><th>credere</th><th>partire</th></tr></thead><tbody><tr><td>io</td><td>parlai</td><td>credei/credetti</td><td>partii</td></tr><tr><td>tu</td><td>parlasti</td><td>credesti</td><td>partisti</td></tr><tr><td>lui/lei</td><td>parlò</td><td>credé/credette</td><td>partì</td></tr><tr><td>noi</td><td>parlammo</td><td>credemmo</td><td>partimmo</td></tr><tr><td>voi</td><td>parlaste</td><td>credeste</td><td>partiste</td></tr><tr><td>loro</td><td>parlarono</td><td>crederono/credettero</td><td>partirono</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Where you'll meet it", "body": "<p>Novels, fairy tales (<em>C'era una volta... il principe partì...</em>), history books, formal biographical writing, and everyday conversation in much of southern Italy.</p>"},
                {"heading": "b) Archaic/literary vocabulary and forms", "body": "<p><em>ove</em> (dove, poetic), <em>giacché</em> (poiché), <em>dianzi</em> (poco fa), <em>egli/ella</em> (lui/lei, now purely literary), <em>testé</em> (proprio ora).</p>"},
            ],
            "examples": [
                {"it": "Nacque a Firenze nel 1265 e morì nel 1321.", "en": "He was born in Florence in 1265 and died in 1321. (biographical passato remoto)"},
                {"it": "Il re, udita la notizia, convocò subito il consiglio.", "en": "The king, having heard the news, immediately summoned the council."},
                {"it": "Ella non disse nulla e se ne andò in silenzio.", "en": "She said nothing and left in silence. (literary ella, not lei)"},
                {"it": "Giacché era tardi, decisero di rimandare la partenza.", "en": "Since it was late, they decided to postpone the departure."},
            ],
            "commonMistakes": [
                {"wrong": "Using the passato remoto for yesterday's events in everyday central/northern Italian conversation", "right": "Use the passato prossimo for recent events in everyday speech (outside southern regional use)", "why": "The passato remoto reads as narratively distant/literary in most of Italy — using it for something that happened yesterday sounds jarring outside its normal contexts."},
            ],
        },
        "exercises": [
            {"id": "c2rl-mc", "type": "multiple-choice", "title": "Reading Comprehension",
             "items": [
                {"id": "c2rl1", "prompt": "In \"Il re, udita la notizia, convocò subito il consiglio,\" what is convocò?", "options": ["Present tense of convocare", "Passato remoto of convocare", "Imperfetto of convocare"], "answerIndex": 1, "explanation": "Convocò is the third-person singular passato remoto of convocare."},
                {"id": "c2rl2", "prompt": "Where would you most expect to encounter the passato remoto?", "options": ["A casual text message", "A historical novel", "A shopping list"], "answerIndex": 1, "explanation": "The passato remoto is the standard narrative past of literature and history writing."},
             ]},
            {"id": "c2rl-match", "type": "matching", "title": "Match the Literary Form to Its Modern Equivalent",
             "items": [
                {"id": "c2rl3", "pairs": [
                    {"left": "ove", "right": "dove"},
                    {"left": "giacché", "right": "poiché"},
                    {"left": "egli/ella", "right": "lui/lei"},
                    {"left": "testé", "right": "proprio ora"},
                ], "explanation": "These literary forms are recognizable but no longer used in everyday spoken Italian."},
             ]},
        ],
        "summary": [
            "The passato remoto is the standard narrative past of literature, history, and (regionally) southern Italian speech.",
            "C2 reading fluency requires recognizing it and a handful of archaic pronouns/connectors, even without actively using them.",
            "Using literary forms in ordinary conversation outside their natural context sounds stilted or affected.",
        ],
    },
    {
        "id": "c2-sfumature-lessicali",
        "level": "C2", "unit": "1", "order": 3, "skill": "vocabulary", "strand": "lexis",
        "title": "Sfumature Lessicali e Collocazioni",
        "subtitle": "Near-synonyms that aren't interchangeable, and the fixed word pairings native speakers expect.",
        "objectives": [
            "Distinguish near-synonym pairs by register, connotation, or precise meaning",
            "Use common fixed collocations correctly",
            "Avoid literal word-for-word translation from English collocations",
        ],
        "content": {
            "intro": "At C2, correctness alone isn't enough — native-like Italian depends on choosing the word a native speaker would actually reach for, in the exact combination they expect.",
            "explanation": "<p>Many Italian near-synonyms differ by connotation, formality, or precise shade of meaning — not by strict correctness. Collocations (fixed word pairings, like English \"heavy rain\" rather than \"strong rain\") are equally important and rarely translate literally from English.</p>",
            "rules": [
                {"heading": "a) Near-synonym pairs", "body": "<ul><li><em>lavoro</em> (neutral) vs. <em>occupazione</em> (more formal/administrative) vs. <em>impiego</em> (a specific job/position)</li><li><em>felice</em> (deep, meaningful happiness) vs. <em>contento</em> (satisfied, more everyday)</li><li><em>guardare</em> (to look at, active) vs. <em>vedere</em> (to see, perceive)</li></ul>"},
                {"heading": "b) Fixed collocations", "body": "<p><em>fare una domanda</em> (to ask a question, not \"chiedere una domanda\"); <em>prendere una decisione</em> (to make a decision, not \"fare una decisione\"); <em>commettere un errore</em> (to make a mistake, not \"fare un errore\", though this is now widely tolerated); <em>pioggia battente</em> (pouring rain, not \"pioggia forte\").</p>"},
            ],
            "examples": [
                {"it": "Ho preso una decisione difficile.", "en": "I made a difficult decision."},
                {"it": "Mi ha fatto una domanda imbarazzante.", "en": "He asked me an embarrassing question."},
                {"it": "Ha commesso un grave errore di valutazione.", "en": "He made a serious error of judgment."},
                {"it": "Sono felice di essere qui con voi stasera.", "en": "I am [deeply] happy to be here with you tonight."},
            ],
            "commonMistakes": [
                {"wrong": "Ho fatto una decisione.", "right": "Ho preso una decisione.", "why": "Decisions are \"taken\" (prendere), not \"made\" (fare), in standard Italian — a direct calque from English fails here."},
                {"wrong": "Mi ha chiesto una domanda.", "right": "Mi ha fatto una domanda.", "why": "Questions are \"made/asked\" with fare, not chiedere — chiedere una domanda is a common learner error, redundant in meaning too."},
            ],
        },
        "exercises": [
            {"id": "c2sl-fill", "type": "fill-blank", "title": "Fill in the Correct Collocation",
             "items": [
                {"id": "c2sl1", "prompt": "Devo ___ una decisione importante.", "answers": [["prendere"]], "explanation": "Prendere una decisione is the fixed collocation.", "options": ["prendere", "fare", "dare"]},
                {"id": "c2sl2", "prompt": "Posso ___ ti una domanda?", "answers": [["fare"]], "explanation": "Fare una domanda is the fixed collocation.", "options": ["fare", "chiedere", "dire"]},
             ]},
            {"id": "c2sl-mc", "type": "multiple-choice", "title": "Choose the Better Word",
             "items": [
                {"id": "c2sl3", "prompt": "Describing torrential rain: \"pioggia ___\"", "options": ["forte", "battente", "grande"], "answerIndex": 1, "explanation": "Pioggia battente is the natural collocation for heavy, driving rain."},
             ]},
        ],
        "summary": [
            "Near-synonyms often differ by register or connotation rather than strict correctness — precise use is a C2 marker.",
            "Collocations are fixed word pairings (prendere una decisione, fare una domanda) that rarely translate literally.",
            "Direct calques from English collocations are one of the most persistent tells of a non-native speaker.",
        ],
    },
    {
        "id": "c2-sintesi-argomentazione",
        "level": "C2", "unit": "1", "order": 4, "skill": "writing", "strand": "argumentation",
        "title": "L'Arte della Sintesi: Riassumere e Argomentare",
        "subtitle": "Structuring a persuasive argument and summarizing precisely.",
        "objectives": [
            "Structure a short argumentative text with thesis, evidence, and counterargument",
            "Use hedging and concession to acknowledge an opposing view before rebutting it",
            "Summarize a longer text concisely without losing its key claims",
        ],
        "content": {
            "intro": "Real argumentative writing in Italian doesn't just state opinions — it anticipates and addresses the other side, using concession as a rhetorical tool rather than a weakness.",
            "explanation": "<p>A strong argumentative paragraph typically states a thesis, concedes a point to the opposing view (<em>È vero che..., Non si può negare che...</em>), and then pivots to the counter-argument (<em>Tuttavia..., Ciononostante...</em>). Summarizing well means compressing a text to its core claims without adding opinion or losing the original logical structure.</p>",
            "rules": [
                {"heading": "a) Concession + rebuttal structure", "body": "<p><em>È vero che [concession], tuttavia [counter-argument].</em> <em>Sebbene si possa obiettare che..., resta il fatto che...</em></p>"},
                {"heading": "b) Summarizing formulas", "body": "<p><em>L'autore sostiene che... / Il testo affronta il tema di... / In sintesi, l'argomento centrale è...</em></p>"},
            ],
            "examples": [
                {"it": "È vero che il progetto comporta dei rischi; tuttavia, i benefici a lungo termine superano di gran lunga i costi iniziali.", "en": "It's true the project carries risks; however, the long-term benefits far outweigh the initial costs."},
                {"it": "L'autore sostiene che la tecnologia, se usata con moderazione, possa migliorare la qualità della vita.", "en": "The author argues that technology, if used in moderation, can improve quality of life."},
                {"it": "Sebbene si possa obiettare che la misura sia costosa, resta il fatto che salverebbe molte vite.", "en": "Although one might object that the measure is expensive, the fact remains it would save many lives."},
            ],
            "commonMistakes": [
                {"wrong": "Ignoring the counterargument entirely in a persuasive text", "right": "Acknowledge it explicitly (è vero che...) before rebutting", "why": "A persuasive argument that never addresses the obvious objection reads as one-sided and less convincing at this level of writing."},
                {"wrong": "Summarizing by copying full sentences from the original", "right": "Restate the core claim in your own, more compressed words", "why": "A genuine summary requires reformulation, not verbatim extraction — copying isn't synthesis."},
            ],
        },
        "exercises": [
            {"id": "c2sa-mc", "type": "multiple-choice", "title": "Identify the Rhetorical Move",
             "items": [
                {"id": "c2sa1", "prompt": "\"È vero che... tuttavia...\" is an example of:", "options": ["A simple statement of fact", "Concession followed by rebuttal", "A summary formula"], "answerIndex": 1, "explanation": "This is the classic concession + counter-argument structure."},
             ]},
            {"id": "c2sa-fill", "type": "fill-blank", "title": "Complete the Argumentative Structure",
             "items": [
                {"id": "c2sa2", "prompt": "___ si possa obiettare che il piano sia rischioso, i vantaggi sono evidenti. (although)", "answers": [["Sebbene", "Benché"]], "explanation": "Concessive conjunction, subjunctive follows.", "options": ["Sebbene", "Perché", "Quindi"]},
            ]},
        ],
        "summary": [
            "Strong argumentative writing concedes a point to the opposing view before rebutting it with tuttavia/ciononostante.",
            "Summarizing means restating core claims in compressed, original wording — not copying sentences.",
            "Set formulas (l'autore sostiene che, in sintesi) structure both argument and summary clearly.",
        ],
    },
    {
        "id": "c2-modalita-attenuazione",
        "level": "C2", "unit": "1", "order": 5, "skill": "grammar", "strand": "modality",
        "title": "Modalità e Attenuazione",
        "subtitle": "Hedging a claim, softening a criticism, and expressing calibrated certainty.",
        "objectives": [
            "Use hedging expressions to soften a claim or opinion",
            "Calibrate certainty with modal expressions (sembra che, pare che, a quanto pare)",
            "Soften criticism or disagreement diplomatically",
        ],
        "content": {
            "intro": "Native fluency includes knowing how to avoid sounding too blunt or too certain — Italian has a rich set of hedging tools for exactly this.",
            "explanation": "<p>Hedging expressions distance the speaker slightly from a claim, making room for doubt or diplomacy. Many pair naturally with the subjunctive (since they present something as less than certain fact).</p>",
            "rules": [
                {"heading": "a) Softening certainty", "body": "<p><em>Sembra che, pare che</em> + congiuntivo (it seems that); <em>a quanto pare, a quanto sembra</em> (apparently, + indicative); <em>Direi che...</em> (I'd say that..., conditional softening).</p>"},
                {"heading": "b) Softening disagreement/criticism", "body": "<p><em>Non sono del tutto d'accordo...</em> (I don't entirely agree...); <em>Forse potremmo considerare anche...</em> (Perhaps we could also consider...); <em>Non vorrei sembrare scortese, ma...</em> (I don't want to seem rude, but...)</p>"},
                {"heading": "c) Impersonal hedges", "body": "<p><em>Si direbbe che...</em> (One might say that...); <em>Non è escluso che...</em> (It's not out of the question that...)</p>"},
            ],
            "examples": [
                {"it": "Sembra che il progetto sia stato rimandato.", "en": "It seems the project has been postponed."},
                {"it": "A quanto pare, la riunione è stata spostata a venerdì.", "en": "Apparently, the meeting has been moved to Friday."},
                {"it": "Non vorrei sembrare polemico, ma non sono del tutto d'accordo.", "en": "I don't want to seem argumentative, but I don't entirely agree."},
                {"it": "Direi che è la soluzione migliore, anche se non l'unica possibile.", "en": "I'd say it's the best solution, though not the only possible one."},
            ],
            "commonMistakes": [
                {"wrong": "Sembra che il progetto è stato rimandato.", "right": "Sembra che il progetto sia stato rimandato.", "why": "Sembra che presents something as less than certain, triggering the subjunctive, unlike a quanto pare, which takes the indicative."},
                {"wrong": "Sei sbagliato. (blunt, unhedged disagreement)", "right": "Non sono del tutto d'accordo, credo che...", "why": "Bluntly telling someone they're wrong reads as impolite in most registers — hedged disagreement is the diplomatic, native-like default."},
            ],
        },
        "exercises": [
            {"id": "c2ma-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "c2ma1", "prompt": "Pare che la situazione ___ (migliorare) negli ultimi giorni.", "answers": [["sia migliorata"]], "explanation": "Pare che triggers the subjunctive.", "options": ["sia migliorata", "è migliorata", "migliora"]},
                {"id": "c2ma2", "prompt": "A quanto ___, il volo è stato cancellato. (apparently)", "answers": [["pare", "sembra"]], "explanation": "A quanto pare/sembra takes the indicative that follows normally (here already given as a fact statement).", "options": ["pare", "sia", "sembri"]},
             ]},
            {"id": "c2ma-mc", "type": "multiple-choice", "title": "Choose the More Diplomatic Option",
             "items": [
                {"id": "c2ma3", "prompt": "Disagreeing politely in a meeting:", "options": ["Non è vero.", "Non sono del tutto d'accordo, se posso dire.", "Ti sbagli."], "answerIndex": 1, "explanation": "Hedged disagreement is the diplomatically appropriate register."},
             ]},
        ],
        "summary": [
            "Sembra che/pare che soften certainty and trigger the subjunctive; a quanto pare is a fixed indicative alternative.",
            "Hedged disagreement (non sono del tutto d'accordo) is the diplomatic default, not blunt contradiction.",
            "Calibrating certainty and softening criticism are markers of genuinely native-like social fluency.",
        ],
    },
    {
        "id": "c2-coesione-testuale",
        "level": "C2", "unit": "1", "order": 6, "skill": "writing", "strand": "cohesion",
        "title": "Coesione Testuale Avanzata: Anafora ed Ellissi",
        "subtitle": "Keeping a long text connected without repeating yourself.",
        "objectives": [
            "Use anaphoric reference (pronouns, demonstratives) to avoid repetition across sentences",
            "Recognize and use ellipsis to omit a repeated element cleanly",
            "Maintain clarity of reference across a multi-sentence paragraph",
        ],
        "content": {
            "intro": "A cohesive text avoids repeating the same noun sentence after sentence, but also avoids ambiguity about what each pronoun refers back to — a balance advanced writing has to manage deliberately.",
            "explanation": "<p><strong>Anaphora</strong> here means referring back to something already mentioned, using a pronoun, demonstrative (<em>questo/quello</em>), or a summarizing noun (<em>tale scelta, questo fatto</em>) instead of repeating it. <strong>Ellipsis</strong> is the clean omission of a repeated element when the grammar makes it recoverable: <em>Marco studia legge, Anna [studia] medicina.</em></p>",
            "rules": [
                {"heading": "a) Anaphoric devices", "body": "<ul><li>Pronouns: <em>lo, la, li, le, ne, ci</em></li><li>Demonstratives: <em>questo, quello, ciò</em> (ciò is a fixed, invariable \"this/that [abstract idea]\")</li><li>Summarizing nouns: <em>tale decisione, questo approccio, il tutto</em></li></ul>"},
                {"heading": "b) Ellipsis", "body": "<p>Omitting a repeated verb (or verb phrase) when context makes it recoverable: <em>Lui ama la musica classica, lei [ama] il jazz.</em></p>"},
                {"heading": "c) Avoiding ambiguous reference", "body": "<p>When two possible antecedents exist, prefer a demonstrative or a repeated noun over an ambiguous pronoun: <em>Marco ha parlato con Luca; quest'ultimo sembrava preoccupato.</em> (quest'ultimo = \"the latter\", unambiguous.)</p>"},
            ],
            "examples": [
                {"it": "Il progetto è ambizioso. Ciò non significa che sia irrealizzabile.", "en": "The project is ambitious. That doesn't mean it's unachievable."},
                {"it": "Marco preferisce il tè, Anna il caffè.", "en": "Marco prefers tea, Anna [prefers] coffee. (ellipsis)"},
                {"it": "Ho parlato con il direttore e con il suo assistente; quest'ultimo si è mostrato molto disponibile.", "en": "I spoke with the director and his assistant; the latter was very helpful. (unambiguous anaphora)"},
                {"it": "Tale scelta ha sorpreso molti osservatori.", "en": "This choice surprised many observers. (summarizing anaphora)"},
            ],
            "commonMistakes": [
                {"wrong": "Repeating the full noun phrase in every sentence of a paragraph", "right": "Vary with pronouns, demonstratives, and summarizing nouns", "why": "Constant repetition of the same full noun phrase reads as mechanical and unpolished in fluent written Italian."},
                {"wrong": "Using lui/lei ambiguously when two people of the same gender were just mentioned", "right": "Use quest'ultimo/quel primo or repeat the name for clarity", "why": "An ambiguous pronoun with two possible antecedents forces the reader to guess — advanced writing resolves this explicitly."},
            ],
        },
        "exercises": [
            {"id": "c2ct-mc", "type": "multiple-choice", "title": "Choose the Best Cohesive Device",
             "items": [
                {"id": "c2ct1", "prompt": "Two people were just mentioned; you need to refer unambiguously to the second one:", "options": ["lui", "quest'ultimo", "quello"], "answerIndex": 1, "explanation": "Quest'ultimo (\"the latter\") unambiguously points to the most recently mentioned of the two."},
             ]},
            {"id": "c2ct-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "c2ct2", "prompt": "Il piano è complesso. ___ non lo rende impossibile. (this [abstract])", "answers": [["Ciò"]], "explanation": "Ciò is the fixed, invariable pronoun for an abstract \"this/that idea\".", "options": ["Ciò", "Questo oggetto", "Lui"]},
             ]},
        ],
        "summary": [
            "Anaphoric devices (pronouns, ciò, quest'ultimo, summarizing nouns) avoid repeating a noun phrase across sentences.",
            "Ellipsis cleanly omits a repeated verb/phrase when grammar makes it recoverable.",
            "Ambiguous pronoun reference is resolved with demonstratives like quest'ultimo, not left to guesswork.",
        ],
    },
    {
        "id": "c2-varieta-regionale",
        "level": "C2", "unit": "1", "order": 7, "skill": "reading", "strand": "sociolinguistics",
        "title": "Italiano Regionale e Varietà",
        "subtitle": "Standard Italian isn't the only Italian — a proficient speaker recognizes the variation.",
        "objectives": [
            "Recognize that regional variation affects vocabulary, not just accent",
            "Identify a handful of well-known regionalisms and their standard equivalents",
            "Understand the sociolinguistic relationship between standard Italian and regional dialects",
        ],
        "content": {
            "intro": "Standard Italian, taught throughout this course, coexists with genuine regional varieties and dialects across Italy — true proficiency includes knowing this landscape exists, even without mastering every variety.",
            "explanation": "<p>Italy's regional dialects (Sicilian, Neapolitan, Venetian, Milanese/Lombard, Sardinian, and many more) are, linguistically, distinct languages descended independently from Latin — not simply \"accented Italian\". What most Italians actually speak day-to-day is <strong>regional Italian</strong>: standard Italian with regional vocabulary, some grammar habits, and intonation carried over from the local dialect.</p>",
            "rules": [
                {"heading": "a) Well-known regional vocabulary", "body": "<ul><li>\"What are you doing?\" — standard <em>Che fai?</em>; Roman <em>Che stai a fa'?</em></li><li>Bread roll: standard <em>panino</em>; in parts of the south, <em>panuozzo/rosetta</em> (regional bread specialties, with their own names)</li><li>Small bar snack before lunch (a well-known Northern custom): <em>aperitivo</em>, standard nationwide by now, originally strongly Milanese</li></ul>"},
                {"heading": "b) A well-known grammar habit: passato remoto in the south", "body": "<p>In much of southern Italy, the passato remoto (Lesson 2 of this level) remains common in everyday speech for recent events, where standard/northern Italian would use the passato prossimo.</p>"},
                {"heading": "c) Standard Italian's role", "body": "<p>Standard Italian (based historically on literary Florentine) is the shared language of education, media, and formal communication nationwide — the variety this entire course teaches, and the safest, most broadly understood register anywhere in Italy.</p>"},
            ],
            "examples": [
                {"it": "A Napoli si dice spesso \"jamm\" per \"andiamo\".", "en": "In Naples, \"jamm\" is often said for \"let's go\" (dialectal, not standard)."},
                {"it": "Al sud è comune sentire \"Andai al mercato stamattina\" invece di \"Sono andato\".", "en": "In the south it's common to hear the passato remoto (\"andai\") instead of the passato prossimo, even for this morning."},
                {"it": "L'italiano standard è capito e usato in tutto il Paese, anche dove si parla ancora il dialetto in famiglia.", "en": "Standard Italian is understood and used throughout the country, even where dialect is still spoken at home."},
            ],
            "commonMistakes": [
                {"wrong": "Treating regional Italian/dialect as simply \"bad\" or \"incorrect\" Italian", "right": "Recognize dialects as distinct language varieties with their own history and grammar", "why": "Italy's dialects are linguistically independent developments from Latin, not corruptions of standard Italian — a common misconception worth correcting at this level."},
            ],
        },
        "exercises": [
            {"id": "c2vr-mc", "type": "multiple-choice", "title": "Test Your Sociolinguistic Awareness",
             "items": [
                {"id": "c2vr1", "prompt": "Italy's regional dialects are best described as...", "options": ["Corrupted forms of standard Italian", "Independent language varieties descended from Latin", "Just different accents"], "answerIndex": 1, "explanation": "Dialects developed independently from Latin, parallel to standard Italian itself, not as deviations from it."},
                {"id": "c2vr2", "prompt": "In everyday southern Italian speech, which tense often replaces the passato prossimo for recent events?", "options": ["Il futuro", "Il passato remoto", "L'imperfetto"], "answerIndex": 1, "explanation": "The passato remoto remains common in everyday southern speech, unlike in the standard/northern norm."},
             ]},
        ],
        "summary": [
            "Italy's dialects are distinct language varieties, not \"incorrect\" Italian — a key sociolinguistic distinction.",
            "Most Italians actually speak regional Italian day-to-day: standard Italian with regional vocabulary and habits.",
            "Standard Italian, taught throughout this course, remains the shared, universally understood register nationwide.",
        ],
    },
]
