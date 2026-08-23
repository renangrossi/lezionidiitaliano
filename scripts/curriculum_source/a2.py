# -*- coding: utf-8 -*-
"""A2 — Elementary curriculum data."""

OVERVIEW = ("A2 puts the present tense to work with more irregular verbs and modal verbs, "
            "adds the two building blocks of the past — passato prossimo with avere and with "
            "essere — and introduces reflexive verbs, possessives, direct object pronouns and "
            "comparatives. By the end you can talk about your day, your past, and your plans.")

LESSONS = [
    {
        "id": "a2-verbi-irregolari-presente",
        "level": "A2", "unit": "1", "order": 1, "skill": "grammar", "strand": "verbs",
        "title": "Altri Verbi Irregolari al Presente",
        "subtitle": "Dire, venire, uscire, dare, stare, sapere — the rest of Italian's everyday irregulars.",
        "objectives": [
            "Conjugate dire, venire, uscire, dare, stare and sapere in the present",
            "Distinguish sapere (to know facts/how to) from conoscere (to know people/places)",
            "Recognize stare in fixed expressions and the progressive form",
        ],
        "content": {
            "intro": "Alongside andare, fare and volere, a second wave of irregular verbs — dire, venire, uscire, dare, stare, sapere — appears constantly in everyday Italian.",
            "explanation": "<p>These verbs don't share one single pattern, so it's most efficient to learn them as a set through repeated use. Two are worth a special note: <strong>stare</strong> is the base of the progressive form (<em>sto mangiando</em>, I am eating) and of asking how someone is (<em>Come stai?</em>); and Italian splits English's single verb \"to know\" into two: <strong>sapere</strong> (facts, information, skills — often + infinitive) and <strong>conoscere</strong> (people, places — a regular -ere verb, covered alongside sapere here for contrast).</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Dire, venire, uscire, dare, stare, sapere — present tense</caption><thead><tr><th>Subject</th><th>dire</th><th>venire</th><th>uscire</th><th>dare</th><th>stare</th><th>sapere</th></tr></thead><tbody><tr><td>io</td><td>dico</td><td>vengo</td><td>esco</td><td>do</td><td>sto</td><td>so</td></tr><tr><td>tu</td><td>dici</td><td>vieni</td><td>esci</td><td>dai</td><td>stai</td><td>sai</td></tr><tr><td>lui/lei</td><td>dice</td><td>viene</td><td>esce</td><td>dà</td><td>sta</td><td>sa</td></tr><tr><td>noi</td><td>diciamo</td><td>veniamo</td><td>usciamo</td><td>diamo</td><td>stiamo</td><td>sappiamo</td></tr><tr><td>voi</td><td>dite</td><td>venite</td><td>uscite</td><td>date</td><td>state</td><td>sapete</td></tr><tr><td>loro</td><td>dicono</td><td>vengono</td><td>escono</td><td>danno</td><td>stanno</td><td>sanno</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Sapere vs. conoscere", "body": "<ul><li><strong>sapere</strong> + fact/information: <em>So che parli italiano.</em> (I know that you speak Italian.)</li><li><strong>sapere</strong> + infinitive = to know how to: <em>So nuotare.</em> (I know how to swim.)</li><li><strong>conoscere</strong> + person/place: <em>Conosco Marco. Conosco Roma bene.</em></li></ul>"},
                {"heading": "b) Stare — health, staying, and the progressive", "body": "<ul><li>Health: <em>Come stai? Sto bene.</em></li><li>To stay/remain: <em>Stiamo a casa stasera.</em></li><li>Progressive (stare + gerund, full detail at C1): <em>Sto studiando.</em> (I am studying [right now].)</li></ul>"},
            ],
            "examples": [
                {"it": "Cosa dici? Non ho capito.", "en": "What are you saying? I didn't understand."},
                {"it": "Vengo alla festa con Marco.", "en": "I'm coming to the party with Marco."},
                {"it": "Esco con gli amici stasera.", "en": "I'm going out with friends tonight."},
                {"it": "Non so dove sia l'ufficio.", "en": "I don't know where the office is."},
                {"it": "Conosco un buon ristorante qui vicino.", "en": "I know a good restaurant near here."},
                {"it": "Sto bene, grazie, e tu?", "en": "I'm well, thanks, and you?"},
            ],
            "commonMistakes": [
                {"wrong": "Conosco che tu parli italiano.", "right": "So che tu parli italiano.", "why": "A fact/piece of information needs sapere, not conoscere."},
                {"wrong": "So Marco molto bene.", "right": "Conosco Marco molto bene.", "why": "Knowing a person needs conoscere, not sapere."},
                {"wrong": "Io sao nuotare.", "right": "Io so nuotare.", "why": "The io form of sapere is so, an irregular one-syllable form, not sao."},
            ],
        },
        "exercises": [
            {"id": "a2vi-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a2vi1", "prompt": "Tu ___ (venire) alla festa?", "answers": [["vieni"]], "explanation": "Tu form of venire is vieni.", "options": ["vieni", "viene", "vengo"]},
                {"id": "a2vi2", "prompt": "Noi non ___ (sapere) la risposta.", "answers": [["sappiamo"]], "explanation": "Noi form of sapere is sappiamo.", "options": ["sappiamo", "sapiamo", "saviamo"]},
                {"id": "a2vi3", "prompt": "Loro ___ (uscire) ogni sabato sera.", "answers": [["escono"]], "explanation": "Loro form of uscire is escono.", "options": ["escono", "usciono", "esce"]},
             ]},
            {"id": "a2vi-mc", "type": "multiple-choice", "title": "Sapere or Conoscere?",
             "items": [
                {"id": "a2vi4", "prompt": "\"I know how to cook\"", "options": ["So cucinare.", "Conosco cucinare.", "So a cucinare."], "answerIndex": 0, "explanation": "Sapere + infinitive = to know how to."},
                {"id": "a2vi5", "prompt": "\"I know this city well\"", "options": ["So questa città bene.", "Conosco questa città bene.", "Conosco a questa città bene."], "answerIndex": 1, "explanation": "Places need conoscere."},
             ]},
        ],
        "summary": [
            "Dire, venire, uscire, dare, stare and sapere are irregular and must be memorized individually.",
            "Sapere = facts/skills (often + infinitive); conoscere = people/places.",
            "Stare covers health (Come stai?), staying/remaining, and is the base of the progressive form.",
        ],
    },
    {
        "id": "a2-verbi-modali",
        "level": "A2", "unit": "1", "order": 2, "skill": "grammar", "strand": "modals",
        "title": "I Verbi Modali: Dovere, Potere, Volere",
        "subtitle": "Must, can, and want — the three modal verbs that pair with an infinitive.",
        "objectives": [
            "Conjugate dovere, potere and volere in the present tense",
            "Distinguish obligation (dovere), ability/permission (potere), and desire (volere)",
            "Use modal verbs correctly with a following infinitive",
        ],
        "content": {
            "intro": "Dovere, potere and volere are Italian's three core modal verbs — each pairs directly with an infinitive to add a layer of meaning: obligation, ability/permission, or desire.",
            "explanation": "<p>All three are irregular, and all three are followed directly by a bare infinitive with no preposition in between — a simpler pattern than English's mix of \"must\", \"have to\", \"can\", \"is able to\". With reflexive verbs and object pronouns (covered later), the pronoun can attach either before the modal or to the end of the infinitive: <em>Mi devo alzare</em> / <em>Devo alzarmi</em> — both correct.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Dovere, potere, volere — present tense</caption><thead><tr><th>Subject</th><th>dovere</th><th>potere</th><th>volere</th></tr></thead><tbody><tr><td>io</td><td>devo</td><td>posso</td><td>voglio</td></tr><tr><td>tu</td><td>devi</td><td>puoi</td><td>vuoi</td></tr><tr><td>lui/lei</td><td>deve</td><td>può</td><td>vuole</td></tr><tr><td>noi</td><td>dobbiamo</td><td>possiamo</td><td>vogliamo</td></tr><tr><td>voi</td><td>dovete</td><td>potete</td><td>volete</td></tr><tr><td>loro</td><td>devono</td><td>possono</td><td>vogliono</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Dovere — obligation/necessity", "body": "<p><em>Devo studiare stasera.</em> (I have to study tonight.) Also used for probability: <em>Deve essere tardi.</em> (It must be late.)</p>"},
                {"heading": "b) Potere — ability/permission", "body": "<p><em>Posso aprire la finestra?</em> (Can/May I open the window? — both ability and permission use potere, unlike English's can/may distinction.)</p>"},
                {"heading": "c) Volere — desire", "body": "<p><em>Voglio andare in vacanza.</em> (I want to go on vacation.) A softer, more polite form is the conditional <em>vorrei</em> (I would like), introduced at B1.</p>"},
            ],
            "examples": [
                {"it": "Devo lavorare fino a tardi oggi.", "en": "I have to work late today."},
                {"it": "Puoi aiutarmi, per favore?", "en": "Can you help me, please?"},
                {"it": "Non possiamo uscire, piove troppo.", "en": "We can't go out, it's raining too much."},
                {"it": "Vogliono comprare una casa nuova.", "en": "They want to buy a new house."},
                {"it": "Dovete finire il compito entro venerdì.", "en": "You [pl.] have to finish the assignment by Friday."},
            ],
            "commonMistakes": [
                {"wrong": "Devo di studiare.", "right": "Devo studiare.", "why": "Dovere is followed directly by the infinitive, with no preposition."},
                {"wrong": "Io posso a nuotare bene.", "right": "Io posso nuotare bene.", "why": "Potere never takes a preposition before the infinitive."},
                {"wrong": "Lei deve essere tarda.", "right": "Deve essere tardi.", "why": "Tardi is an invariable adverb (late) here, not the adjective tarda — no agreement applies."},
            ],
        },
        "exercises": [
            {"id": "a2vm-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a2vm1", "prompt": "Io ___ (dovere) partire alle sette.", "answers": [["devo"]], "explanation": "Io form of dovere is devo.", "options": ["devo", "devi", "deve"]},
                {"id": "a2vm2", "prompt": "___ (Potere - tu) chiudere la porta?", "answers": [["Puoi"]], "explanation": "Tu form of potere is puoi.", "options": ["Puoi", "Posso", "Può"]},
                {"id": "a2vm3", "prompt": "Loro ___ (volere) partire subito.", "answers": [["vogliono"]], "explanation": "Loro form of volere is vogliono.", "options": ["vogliono", "vuole", "volete"]},
             ]},
            {"id": "a2vm-mc", "type": "multiple-choice", "title": "Choose the Right Modal",
             "items": [
                {"id": "a2vm4", "prompt": "You're asking permission to leave early: \"___ andare via prima?\"", "options": ["Devo", "Posso", "Voglio"], "answerIndex": 1, "explanation": "Asking permission uses potere."},
                {"id": "a2vm5", "prompt": "\"I must finish this today\" (obligation)", "options": ["Posso finire questo oggi.", "Voglio finire questo oggi.", "Devo finire questo oggi."], "answerIndex": 2, "explanation": "Obligation uses dovere."},
             ]},
            {"id": "a2vm-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a2vm6", "incorrect": "Devo di andare a casa.", "answer": ["Devo andare a casa."], "explanation": "No preposition between dovere and the infinitive."},
             ]},
        ],
        "summary": [
            "Dovere = obligation/probability; potere = ability/permission; volere = desire.",
            "All three are irregular and pair directly with a bare infinitive, no preposition.",
            "Potere covers both English \"can\" and \"may\" — Italian doesn't distinguish them.",
        ],
    },
    {
        "id": "a2-preposizioni-articolate",
        "level": "A2", "unit": "1", "order": 3, "skill": "grammar", "strand": "prepositions",
        "title": "Preposizioni Articolate",
        "subtitle": "When a, di, da, in and su fuse with the definite article.",
        "objectives": [
            "Combine a, di, da, in and su with the definite article",
            "Recall the fused forms al, del, dal, nel, sul and their variants",
            "Choose the correct fused form based on the noun's article",
        ],
        "content": {
            "intro": "Five of Italian's simple prepositions fuse with a following definite article into a single word — a pattern you'll use constantly once you start referring to specific, known things.",
            "explanation": "<p>Con and per also historically fuse (col, pel) but this is rare and old-fashioned in modern Italian — stick to con il/con i etc. The five that matter are <strong>a, di, da, in, su</strong>. Each combines with il/lo/la/l'/i/gli/le the same way, replacing the article's initial vowel or consonant pattern.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Preposizioni articolate</caption><thead><tr><th></th><th>il</th><th>lo</th><th>la</th><th>l'</th><th>i</th><th>gli</th><th>le</th></tr></thead><tbody><tr><td>a</td><td>al</td><td>allo</td><td>alla</td><td>all'</td><td>ai</td><td>agli</td><td>alle</td></tr><tr><td>di</td><td>del</td><td>dello</td><td>della</td><td>dell'</td><td>dei</td><td>degli</td><td>delle</td></tr><tr><td>da</td><td>dal</td><td>dallo</td><td>dalla</td><td>dall'</td><td>dai</td><td>dagli</td><td>dalle</td></tr><tr><td>in</td><td>nel</td><td>nello</td><td>nella</td><td>nell'</td><td>nei</td><td>negli</td><td>nelle</td></tr><tr><td>su</td><td>sul</td><td>sullo</td><td>sulla</td><td>sull'</td><td>sui</td><td>sugli</td><td>sulle</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) When to fuse", "body": "<p>Fuse the preposition whenever the noun that follows would itself take a definite article: <em>Vado al cinema.</em> (al = a + il, because \"il cinema\" needs il). No article, no fusion: <em>Vado a scuola.</em> (school with no article, a fixed expression).</p>"},
                {"heading": "b) Di as possession vs. dei/delle as \"some\"", "body": "<p>Del/dello/della/dei/degli/delle can also mean \"some\" (the partitive article, full detail at B1): <em>Vorrei del pane.</em> (I'd like some bread.)</p>"},
            ],
            "examples": [
                {"it": "Il libro è sul tavolo.", "en": "The book is on the table."},
                {"it": "Andiamo al mare questo weekend.", "en": "We're going to the seaside this weekend."},
                {"it": "La chiave è nella borsa.", "en": "The key is in the bag."},
                {"it": "Parlo spesso degli amici che vivono all'estero.", "en": "I often talk about the friends who live abroad."},
                {"it": "Il treno arriva dalla stazione centrale.", "en": "The train arrives from the central station."},
            ],
            "commonMistakes": [
                {"wrong": "Vado a il cinema.", "right": "Vado al cinema.", "why": "A + il must fuse into al — they're never written as two separate words."},
                {"wrong": "Il libro è su il tavolo.", "right": "Il libro è sul tavolo.", "why": "Su + il fuses into sul."},
                {"wrong": "Parlo delle amico.", "right": "Parlo dell'amico.", "why": "Amico is masculine singular, so the fused form must be dell' (di + l'), not the feminine plural delle."},
            ],
        },
        "exercises": [
            {"id": "a2pa-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a2pa1", "prompt": "Vado ___ (a + il) supermercato.", "answers": [["al"]], "explanation": "A + il = al.", "options": ["al", "allo", "alla"]},
                {"id": "a2pa2", "prompt": "Il gatto dorme ___ (su + la) sedia.", "answers": [["sulla"]], "explanation": "Su + la = sulla.", "options": ["sulla", "sul", "sullo"]},
                {"id": "a2pa3", "prompt": "Torniamo ___ (da + lo) stadio.", "answers": [["dallo"]], "explanation": "Da + lo = dallo.", "options": ["dallo", "dal", "dai"]},
             ]},
            {"id": "a2pa-match", "type": "matching", "title": "Match the Fusion",
             "items": [
                {"id": "a2pa4", "pairs": [
                    {"left": "in + gli", "right": "negli"},
                    {"left": "di + le", "right": "delle"},
                    {"left": "a + l'", "right": "all'"},
                    {"left": "su + i", "right": "sui"},
                ], "explanation": "Each preposition follows the same pattern across il/lo/la/l'/i/gli/le."},
             ]},
        ],
        "summary": [
            "A, di, da, in and su fuse with the definite article whenever the noun needs one.",
            "The pattern is regular across all five prepositions: al/allo/alla/all'/ai/agli/alle, and so on.",
            "No article needed, no fusion — fixed expressions like a scuola, a casa stay unfused.",
        ],
    },
    {
        "id": "a2-aggettivi-pronomi-possessivi",
        "level": "A2", "unit": "1", "order": 4, "skill": "grammar", "strand": "possessives",
        "title": "Aggettivi e Pronomi Possessivi",
        "subtitle": "My, your, his/her — possessives that agree with the thing owned, not the owner.",
        "objectives": [
            "Use possessive adjectives that agree with the noun possessed",
            "Use the article with most possessives, except for singular family members",
            "Use possessive pronouns to avoid repeating the noun",
        ],
        "content": {
            "intro": "Italian possessives are one of the biggest grammatical differences from English: they agree with the thing owned, not with the owner — so suo can mean \"his\" or \"her\", depending only on what's possessed and by whom in context.",
            "explanation": "<p>Possessives are almost always preceded by the definite article, agreeing with both the article and the noun: <em>il mio libro, la mia casa, i miei libri, le mie case</em>. The one major exception is <strong>singular, unmodified family members</strong>, which drop the article: <em>mio padre, tua sorella</em> — but the article returns with a plural family noun or a modified one: <em>i miei genitori, la mia sorella maggiore</em>.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Possessive adjectives (masc. singular shown; all four forms exist for each)</caption><thead><tr><th>Owner</th><th>Possessive</th></tr></thead><tbody><tr><td>io</td><td>il mio</td></tr><tr><td>tu</td><td>il tuo</td></tr><tr><td>lui/lei/Lei</td><td>il suo</td></tr><tr><td>noi</td><td>il nostro</td></tr><tr><td>voi</td><td>il vostro</td></tr><tr><td>loro</td><td>il loro (invariable)</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Agreement", "body": "<p>Mio/tuo/suo/nostro/vostro each have four forms (-o/-a/-i/-e) agreeing with the noun possessed. Loro never changes: <em>il loro libro, la loro casa, i loro libri</em>.</p>"},
                {"heading": "b) Singular family members drop the article", "body": "<ul><li><em>mio fratello, tua madre, suo zio</em> (no article)</li><li>but: <em>i miei fratelli</em> (plural — article returns)</li><li>and: <em>la mia sorella maggiore</em> (modified by an adjective — article returns)</li></ul>"},
                {"heading": "c) Possessive pronouns", "body": "<p>Same forms, used alone to avoid repeating the noun: <em>Questo è il mio libro. Dov'è il tuo?</em> (This is my book. Where's yours?)</p>"},
            ],
            "examples": [
                {"it": "Questa è la mia macchina.", "en": "This is my car."},
                {"it": "Mio fratello vive a Torino.", "en": "My brother lives in Turin."},
                {"it": "I loro figli studiano all'estero.", "en": "Their children study abroad."},
                {"it": "Il tuo è più grande del mio.", "en": "Yours is bigger than mine."},
                {"it": "Suo padre è medico.", "en": "His/her father is a doctor."},
            ],
            "commonMistakes": [
                {"wrong": "il mio fratello", "right": "mio fratello", "why": "Singular, unmodified family members drop the article — the article only returns for plurals or modified nouns."},
                {"wrong": "la sua libro", "right": "il suo libro", "why": "The possessive and article must agree with libro (masculine), not with the owner's gender."},
                {"wrong": "i loro figlio", "right": "il loro figlio / i loro figli", "why": "The article must match the number of the noun; loro itself never changes but the article and noun must agree with each other."},
            ],
        },
        "exercises": [
            {"id": "a2ap-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a2ap1", "prompt": "___ (my) sorella lavora in banca. (family, singular, unmodified)", "answers": [["Mia"]], "explanation": "Singular, unmodified family member drops the article: mia sorella.", "options": ["Mia", "La mia", "Le mie"]},
                {"id": "a2ap2", "prompt": "Ecco ___ (our) casa nuova.", "answers": [["la nostra"]], "explanation": "Casa is not a family member, so it keeps its article: la nostra.", "options": ["la nostra", "nostra", "il nostro"]},
                {"id": "a2ap3", "prompt": "___ (their) amici arrivano domani.", "answers": [["I loro"]], "explanation": "Loro is invariable but the article agrees with amici (masc. plural): i loro.", "options": ["I loro", "Il loro", "Le loro"]},
             ]},
            {"id": "a2ap-mc", "type": "multiple-choice", "title": "Choose the Correct Form",
             "items": [
                {"id": "a2ap4", "prompt": "\"His car\" (macchina is feminine)", "options": ["il suo macchina", "la sua macchina", "la suo macchina"], "answerIndex": 1, "explanation": "Suo agrees with macchina, a feminine noun: la sua macchina."},
             ]},
        ],
        "summary": [
            "Possessive adjectives agree with the thing possessed, not the owner — suo can mean his or her.",
            "Almost always used with the article, except before a singular, unmodified family member.",
            "Loro never changes form, but the article before it still agrees with the noun.",
        ],
    },
    {
        "id": "a2-passato-prossimo-avere",
        "level": "A2", "unit": "1", "order": 5, "skill": "grammar", "strand": "past-tenses",
        "title": "Passato Prossimo con Avere",
        "subtitle": "Your first past tense: avere + past participle.",
        "objectives": [
            "Form the past participle of regular -are, -ere, -ire verbs",
            "Conjugate the passato prossimo with avere",
            "Recognize the most common irregular past participles",
        ],
        "content": {
            "intro": "The passato prossimo is Italian's everyday past tense — used constantly in conversation for anything that happened and is now finished, from five minutes ago to years ago.",
            "explanation": "<p>Most verbs form the passato prossimo with the present tense of <strong>avere</strong> plus the past participle of the main verb. The regular participle endings are predictable from the infinitive, but a long list of very common verbs have irregular participles that simply need memorizing.</p>",
            "rules": [
                {"heading": "a) Regular past participles", "body": "<ul><li>-are → -ato: <em>parlare → parlato</em></li><li>-ere → -uto: <em>credere → creduto</em></li><li>-ire → -ito: <em>dormire → dormito</em></li></ul>"},
                {"heading": "b) Common irregular participles", "body": "<ul><li><em>fare → fatto, dire → detto, leggere → letto, scrivere → scritto</em></li><li><em>fare → fatto, prendere → preso, mettere → messo, chiedere → chiesto</em></li><li><em>aprire → aperto, vedere → visto, bere → bevuto</em></li></ul>"},
                {"heading": "c) Conjugating with avere", "body": "<p>Present tense of avere + past participle, which stays invariable in gender/number when the auxiliary is avere: <em>Ho mangiato. Hai mangiato. Ha mangiato. Abbiamo mangiato. Avete mangiato. Hanno mangiato.</em></p>"},
            ],
            "examples": [
                {"it": "Ieri ho lavorato tutto il giorno.", "en": "Yesterday I worked all day."},
                {"it": "Hai letto quel libro?", "en": "Have you read that book?"},
                {"it": "Abbiamo mangiato al ristorante.", "en": "We ate at the restaurant."},
                {"it": "Cosa hai detto?", "en": "What did you say?"},
                {"it": "Ho preso il treno delle otto.", "en": "I took the eight o'clock train."},
                {"it": "Non hanno finito il progetto.", "en": "They haven't finished the project."},
            ],
            "commonMistakes": [
                {"wrong": "Ho parlata con lei.", "right": "Ho parlato con lei.", "why": "With avere, the past participle doesn't agree with the subject — it stays in its base -o form."},
                {"wrong": "Ho leggeto il libro.", "right": "Ho letto il libro.", "why": "Leggere has an irregular participle, letto, not the regular -uto pattern."},
                {"wrong": "Io sono mangiato la pizza.", "right": "Io ho mangiato la pizza.", "why": "Mangiare (like most verbs) takes avere as its auxiliary, not essere."},
            ],
        },
        "exercises": [
            {"id": "a2pp-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "instructions": "Use the passato prossimo of the verb in parentheses.",
             "items": [
                {"id": "a2pp1", "prompt": "Ieri ___ (io - lavorare) fino a tardi.", "answers": [["ho lavorato"]], "explanation": "Ho + lavorato (regular -ato participle).", "options": ["ho lavorato", "sono lavorato", "ha lavorato"]},
                {"id": "a2pp2", "prompt": "___ (tu - scrivere) la lettera?", "answers": [["Hai scritto"]], "explanation": "Scrivere has the irregular participle scritto.", "options": ["Hai scritto", "Hai scriveto", "Hai scrivuto"]},
                {"id": "a2pp3", "prompt": "Noi ___ (vedere) un bel film.", "answers": [["abbiamo visto"]], "explanation": "Vedere has the irregular participle visto.", "options": ["abbiamo visto", "abbiamo veduto", "siamo visto"]},
             ]},
            {"id": "a2pp-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a2pp4", "incorrect": "Ho mangiata la pasta.", "answer": ["Ho mangiato la pasta."], "explanation": "With avere, the participle stays invariable — no agreement with the object."},
                {"id": "a2pp5", "incorrect": "Ho facere i compiti.", "answer": ["Ho fatto i compiti."], "explanation": "Fare has the irregular participle fatto, and it can't stay as an infinitive after avere."},
             ]},
            {"id": "a2pp-mc", "type": "multiple-choice", "title": "Choose the Correct Participle",
             "items": [
                {"id": "a2pp6", "prompt": "The past participle of \"prendere\" is...", "options": ["prendato", "preso", "prenduto"], "answerIndex": 1, "explanation": "Prendere has the irregular participle preso."},
             ]},
        ],
        "summary": [
            "Passato prossimo = present tense of avere/essere + past participle; most verbs use avere.",
            "Regular participles: -are→-ato, -ere→-uto, -ire→-ito; many common verbs are irregular.",
            "With avere, the participle never agrees with the subject.",
        ],
    },
    {
        "id": "a2-passato-prossimo-essere",
        "level": "A2", "unit": "1", "order": 6, "skill": "grammar", "strand": "past-tenses",
        "title": "Passato Prossimo con Essere",
        "subtitle": "Motion and change-of-state verbs, and why the participle must agree.",
        "objectives": [
            "Identify the common verbs that take essere as their auxiliary",
            "Make the past participle agree with the subject when using essere",
            "Recognize the essere pattern for reflexive verbs",
        ],
        "content": {
            "intro": "A smaller, learnable group of verbs — mostly about motion, staying, or a change of state — use essere instead of avere as their passato prossimo auxiliary, and this changes one important rule.",
            "explanation": "<p>With essere, the past participle behaves like an adjective: it <strong>agrees in gender and number with the subject</strong>. The classic mnemonic for which verbs take essere is a short list learned by heart (often taught as \"the house of essere\"): andare, venire, partire, arrivare, entrare, uscire, salire, scendere, nascere, morire, diventare, stare, essere itself, rimanere, tornare, cadere, crescere.</p>",
            "rules": [
                {"heading": "a) Common essere verbs", "body": "<ul><li>Motion: <em>andare, venire, partire, arrivare, entrare, uscire, salire, scendere, tornare, cadere</em></li><li>Change of state: <em>nascere (to be born), morire (to die), diventare (to become), crescere (to grow)</em></li><li>Staying: <em>stare, rimanere</em></li></ul>"},
                {"heading": "b) Participle agreement", "body": "<p>The participle takes -o (m. sing.), -a (f. sing.), -i (m. pl.), -e (f. pl.): <em>Marco è andato. Maria è andata. I ragazzi sono andati. Le ragazze sono andate.</em></p>"},
            ],
            "examples": [
                {"it": "Maria è arrivata alle nove.", "en": "Maria arrived at nine."},
                {"it": "I miei genitori sono partiti ieri.", "en": "My parents left yesterday."},
                {"it": "Siamo tornati tardi ieri sera.", "en": "We got back late last night."},
                {"it": "Sei mai stato in Italia?", "en": "Have you ever been to Italy?"},
                {"it": "Sono nata nel 1995.", "en": "I was born in 1995. (female speaker)"},
                {"it": "Le ragazze sono uscite presto.", "en": "The girls went out early."},
            ],
            "commonMistakes": [
                {"wrong": "Maria ha andata al lavoro.", "right": "Maria è andata al lavoro.", "why": "Andare takes essere, not avere, as its auxiliary."},
                {"wrong": "Maria è andato al lavoro.", "right": "Maria è andata al lavoro.", "why": "With essere, the participle must agree with the feminine subject Maria: andata, not andato."},
                {"wrong": "Le ragazze sono arrivato.", "right": "Le ragazze sono arrivate.", "why": "Feminine plural subject needs the -e ending on the participle: arrivate."},
            ],
        },
        "exercises": [
            {"id": "a2pe-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "instructions": "Use the passato prossimo, making the participle agree with the subject.",
             "items": [
                {"id": "a2pe1", "prompt": "Anna ___ (arrivare) tardi.", "answers": [["è arrivata"]], "explanation": "Feminine singular subject: è arrivata.", "options": ["è arrivata", "è arrivato", "ha arrivato"]},
                {"id": "a2pe2", "prompt": "I ragazzi ___ (partire) alle sette.", "answers": [["sono partiti"]], "explanation": "Masculine plural subject: sono partiti.", "options": ["sono partiti", "sono partite", "hanno partito"]},
                {"id": "a2pe3", "prompt": "Noi (femminile) ___ (tornare) a casa presto.", "answers": [["siamo tornate"]], "explanation": "Feminine plural noi: siamo tornate.", "options": ["siamo tornate", "siamo tornati", "abbiamo tornato"]},
             ]},
            {"id": "a2pe-mc", "type": "multiple-choice", "title": "Avere or Essere?",
             "items": [
                {"id": "a2pe4", "prompt": "\"She was born in Rome\"", "options": ["Ha nato a Roma.", "È nata a Roma.", "È nato a Roma."], "answerIndex": 1, "explanation": "Nascere takes essere, and the participle agrees with the feminine subject: nata."},
             ]},
            {"id": "a2pe-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a2pe5", "incorrect": "Le mie amiche sono arrivato.", "answer": ["Le mie amiche sono arrivate."], "explanation": "Feminine plural subject needs the -e participle ending."},
             ]},
        ],
        "summary": [
            "A learnable list of motion, change-of-state, and staying verbs take essere as their auxiliary.",
            "With essere, the past participle agrees in gender and number with the subject.",
            "With avere, the participle never agrees — this is the key contrast to remember.",
        ],
    },
    {
        "id": "a2-verbi-riflessivi",
        "level": "A2", "unit": "1", "order": 7, "skill": "grammar", "strand": "reflexive",
        "title": "Verbi Riflessivi",
        "subtitle": "Actions you do to yourself — and why their passato prossimo always uses essere.",
        "objectives": [
            "Use reflexive pronouns (mi, ti, si, ci, vi, si) with reflexive verbs",
            "Conjugate common reflexive verbs in the present tense",
            "Form the passato prossimo of reflexive verbs, always with essere",
        ],
        "content": {
            "intro": "Italian uses reflexive verbs far more than English does — routines like waking up, getting dressed, or getting bored are all built with a reflexive pronoun plus the verb.",
            "explanation": "<p>A reflexive verb's infinitive ends in <strong>-si</strong> (e.g. <em>alzarsi</em>, to get [oneself] up), and the reflexive pronoun changes to match the subject, placed right before the conjugated verb. Every reflexive verb takes <strong>essere</strong> in the passato prossimo, with the usual subject agreement on the participle.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Alzarsi (to get up) — present and passato prossimo</caption><thead><tr><th>Subject</th><th>Present</th><th>Passato prossimo</th></tr></thead><tbody><tr><td>io</td><td>mi alzo</td><td>mi sono alzato/a</td></tr><tr><td>tu</td><td>ti alzi</td><td>ti sei alzato/a</td></tr><tr><td>lui/lei</td><td>si alza</td><td>si è alzato/a</td></tr><tr><td>noi</td><td>ci alziamo</td><td>ci siamo alzati/e</td></tr><tr><td>voi</td><td>vi alzate</td><td>vi siete alzati/e</td></tr><tr><td>loro</td><td>si alzano</td><td>si sono alzati/e</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Common reflexive verbs", "body": "<p><em>svegliarsi</em> (to wake up), <em>alzarsi</em> (to get up), <em>lavarsi</em> (to wash oneself), <em>vestirsi</em> (to get dressed), <em>chiamarsi</em> (to be named), <em>sentirsi</em> (to feel), <em>annoiarsi</em> (to get bored), <em>divertirsi</em> (to have fun), <em>arrabbiarsi</em> (to get angry).</p>"},
                {"heading": "b) Position of the pronoun", "body": "<p>Before a conjugated verb: <em>Mi sveglio alle sette.</em> Attached to an infinitive (dropping the infinitive's final -e): <em>Devo alzarmi presto.</em> (equally correct: <em>Mi devo alzare presto.</em>)</p>"},
            ],
            "examples": [
                {"it": "Mi sveglio sempre alle sei e mezza.", "en": "I always wake up at half past six."},
                {"it": "Ti sei divertito alla festa?", "en": "Did you have fun at the party? (to a male)"},
                {"it": "Ci vediamo domani!", "en": "See you tomorrow! (literally: we see each other)"},
                {"it": "Si è arrabbiata con me.", "en": "She got angry with me."},
                {"it": "I bambini si sono lavati le mani.", "en": "The children washed their hands."},
            ],
            "commonMistakes": [
                {"wrong": "Ho alzato alle sette.", "right": "Mi sono alzato/a alle sette.", "why": "Reflexive verbs need both the reflexive pronoun and essere as the auxiliary in the passato prossimo — avere alone is never used."},
                {"wrong": "Si è arrabbiato con me. (about a woman)", "right": "Si è arrabbiata con me.", "why": "The participle must agree with the subject's gender, exactly as with any other essere verb."},
                {"wrong": "Io mi sveglia alle sette.", "right": "Io mi sveglio alle sette.", "why": "The pronoun mi must pair with the io verb form, sveglio, not the lui/lei form sveglia."},
            ],
        },
        "exercises": [
            {"id": "a2vr-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a2vr1", "prompt": "Io ___ (svegliarsi) alle sette.", "answers": [["mi sveglio"]], "explanation": "Reflexive pronoun mi + present tense sveglio.", "options": ["mi sveglio", "ti svegli", "si sveglia"]},
                {"id": "a2vr2", "prompt": "Loro ___ (divertirsi) sempre alle feste.", "answers": [["si divertono"]], "explanation": "Reflexive pronoun si + loro form divertono.", "options": ["si divertono", "ci divertiamo", "si diverte"]},
                {"id": "a2vr3", "prompt": "Maria ___ (vestirsi - passato prossimo) in fretta.", "answers": [["si è vestita"]], "explanation": "Reflexive + essere, agreeing with feminine Maria.", "options": ["si è vestita", "si è vestito", "ha vestito"]},
             ]},
            {"id": "a2vr-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a2vr4", "incorrect": "Ho svegliato alle otto.", "answer": ["Mi sono svegliato alle otto.", "Mi sono svegliata alle otto."], "explanation": "Reflexive verbs need the pronoun and essere, never avere alone."},
                {"id": "a2vr5", "incorrect": "Le ragazze si sono divertito.", "answer": ["Le ragazze si sono divertite."], "explanation": "Feminine plural subject needs the -e participle ending."},
             ]},
        ],
        "summary": [
            "Reflexive verbs (infinitive -si) use mi/ti/si/ci/vi/si before the conjugated verb.",
            "Every reflexive verb takes essere in the passato prossimo, with participle agreement.",
            "The pronoun can attach to an infinitive instead: devo alzarmi = mi devo alzare.",
        ],
    },
    {
        "id": "a2-comparativi",
        "level": "A2", "unit": "1", "order": 8, "skill": "grammar", "strand": "comparatives",
        "title": "I Comparativi",
        "subtitle": "More than, less than, as ... as — comparing two things.",
        "objectives": [
            "Form comparatives of majority and minority with più/meno ... di/che",
            "Choose between di and che correctly",
            "Form the comparative of equality with (così) ... come / (tanto) ... quanto",
        ],
        "content": {
            "intro": "Comparing two things is built from simple, reusable pieces: più (more), meno (less), and a choice between di and che that trips up almost every learner at first.",
            "explanation": "<p>Use <strong>di</strong> when comparing two different nouns or pronouns (people, places, things): <em>Marco è più alto di Luca.</em> Use <strong>che</strong> when comparing two elements of the same type within the same clause — two adjectives, two verbs, two nouns with the same preposition: <em>È più simpatico che intelligente.</em> (He's more nice than [he is] smart.)</p>",
            "rules": [
                {"heading": "a) Majority/minority with di", "body": "<p>più/meno + adjective + <strong>di</strong> + noun/pronoun: <em>Roma è più grande di Milano. Sono meno alto di te.</em></p>"},
                {"heading": "b) Majority/minority with che", "body": "<p>più/meno + adjective + <strong>che</strong> + adjective/verb/same-preposition noun: <em>È più simpatico che bello. Preferisco leggere che guardare la TV.</em></p>"},
                {"heading": "c) Equality", "body": "<p><em>(così) ... come</em> or <em>(tanto) ... quanto</em> — the first word is often dropped in speech: <em>Marco è (così) alto come suo padre. / Marco è (tanto) alto quanto suo padre.</em></p>"},
            ],
            "examples": [
                {"it": "Il treno è più veloce dell'autobus.", "en": "The train is faster than the bus."},
                {"it": "Sono meno stanca di ieri.", "en": "I'm less tired than yesterday."},
                {"it": "È più facile parlare che scrivere.", "en": "It's easier to speak than to write."},
                {"it": "Mia sorella è alta come me.", "en": "My sister is as tall as me."},
                {"it": "Questo film è interessante quanto il libro.", "en": "This film is as interesting as the book."},
            ],
            "commonMistakes": [
                {"wrong": "Marco è più alto che Luca.", "right": "Marco è più alto di Luca.", "why": "Comparing two different people/nouns needs di, not che."},
                {"wrong": "È più intelligente di bello.", "right": "È più intelligente che bello.", "why": "Comparing two adjectives about the same subject needs che, not di."},
                {"wrong": "più alto di te di quanto pensavo (extra di)", "right": "più alto di quanto pensassi", "why": "This advanced comparative construction takes di quanto + subjunctive, covered later — for now, keep to simple di/che comparisons."},
            ],
        },
        "exercises": [
            {"id": "a2co-fill", "type": "fill-blank", "title": "Di or Che?",
             "items": [
                {"id": "a2co1", "prompt": "Milano è più grande ___ Firenze.", "answers": [["di"]], "explanation": "Comparing two cities (nouns): di.", "options": ["di", "che"]},
                {"id": "a2co2", "prompt": "È più bravo a cantare ___ a ballare.", "answers": [["che"]], "explanation": "Comparing two activities/verbs: che.", "options": ["che", "di"]},
                {"id": "a2co3", "prompt": "Sono più giovane ___ te.", "answers": [["di"]], "explanation": "Comparing with a pronoun (te): di.", "options": ["di", "che"]},
             ]},
            {"id": "a2co-mc", "type": "multiple-choice", "title": "Choose the Correct Comparative",
             "items": [
                {"id": "a2co4", "prompt": "\"This book is as interesting as that film\"", "options": ["Questo libro è interessante come quel film.", "Questo libro è più interessante di quel film.", "Questo libro è interessante che quel film."], "answerIndex": 0, "explanation": "Equality uses come (or quanto), not più/che."},
             ]},
        ],
        "summary": [
            "Di compares two different nouns/pronouns; che compares two elements of the same type in one clause.",
            "Majority/minority: più/meno ... di/che.",
            "Equality: (così) ... come or (tanto) ... quanto.",
        ],
    },
    {
        "id": "a2-pronomi-diretti",
        "level": "A2", "unit": "1", "order": 9, "skill": "grammar", "strand": "pronouns",
        "title": "Pronomi Diretti",
        "subtitle": "Mi, ti, lo, la, ci, vi, li, le — replacing a direct object to avoid repeating it.",
        "objectives": [
            "Identify a direct object and choose the matching pronoun",
            "Place direct object pronouns correctly before a conjugated verb",
            "Make the past participle agree with lo/la/li/le in the passato prossimo",
        ],
        "content": {
            "intro": "Once you've mentioned something, Italian — like English — lets you replace it with a pronoun instead of repeating the noun. Direct object pronouns go before the verb, which takes some getting used to for English speakers.",
            "explanation": "<p>A direct object answers \"what?\" or \"whom?\" with no preposition: in <em>Leggo il libro</em>, il libro is the direct object, replaceable by <strong>lo</strong>: <em>Lo leggo.</em> Unlike English (\"I read it\"), the pronoun goes <strong>before</strong> the conjugated verb, not after.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Direct object pronouns</caption><thead><tr><th>Person</th><th>Pronoun</th></tr></thead><tbody><tr><td>me</td><td>mi</td></tr><tr><td>you (informal)</td><td>ti</td></tr><tr><td>him / it (m.)</td><td>lo</td></tr><tr><td>her / it (f.)</td><td>la</td></tr><tr><td>us</td><td>ci</td></tr><tr><td>you (pl.)</td><td>vi</td></tr><tr><td>them (m.)</td><td>li</td></tr><tr><td>them (f.)</td><td>le</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Position", "body": "<p>Before a conjugated verb: <em>La conosco bene.</em> Attached to an infinitive (dropping its final -e): <em>Voglio conoscerla.</em> (also correct: <em>La voglio conoscere.</em>)</p>"},
                {"heading": "b) Agreement in the passato prossimo", "body": "<p>With avere, lo/la/li/le force the past participle to agree, even though avere verbs otherwise never agree: <em>Ho comprato la macchina. → L'ho comprata.</em> (Lo/la elide to l' before a vowel.)</p>"},
            ],
            "examples": [
                {"it": "Compro il pane. Lo compro ogni giorno.", "en": "I buy bread. I buy it every day."},
                {"it": "Vedi Maria stasera? Sì, la vedo alle otto.", "en": "Are you seeing Maria tonight? Yes, I'm seeing her at eight."},
                {"it": "Hai visto i miei occhiali? Non li trovo.", "en": "Have you seen my glasses? I can't find them."},
                {"it": "Ho comprato le mele e le ho lavate.", "en": "I bought the apples and washed them."},
                {"it": "Ti chiamo dopo, va bene?", "en": "I'll call you later, okay?"},
            ],
            "commonMistakes": [
                {"wrong": "Leggo lo.", "right": "Lo leggo.", "why": "The direct object pronoun goes before the conjugated verb, not after, unlike English."},
                {"wrong": "Ho comprato la e ho mangiato la. (for la mela)", "right": "L'ho comprata e l'ho mangiata.", "why": "Lo/la elide to l' before a vowel (ho), and the participle must agree: comprata, not comprato."},
                {"wrong": "Ho visto li ieri.", "right": "Li ho visti ieri.", "why": "The pronoun must precede the verb, and the participle agrees with li: visti."},
            ],
        },
        "exercises": [
            {"id": "a2pd-fill", "type": "fill-blank", "title": "Replace with the Correct Pronoun",
             "items": [
                {"id": "a2pd1", "prompt": "Mangio la pizza. → ___ mangio.", "answers": [["La"]], "explanation": "La pizza is feminine singular → la.", "options": ["La", "Lo", "Li"]},
                {"id": "a2pd2", "prompt": "Compro i biglietti. → ___ compro.", "answers": [["Li"]], "explanation": "I biglietti is masculine plural → li.", "options": ["Li", "Le", "Lo"]},
                {"id": "a2pd3", "prompt": "Conosco Marco. → ___ conosco bene.", "answers": [["Lo"]], "explanation": "Marco is masculine singular → lo.", "options": ["Lo", "La", "Li"]},
             ]},
            {"id": "a2pd-mc", "type": "multiple-choice", "title": "Choose the Correct Sentence",
             "items": [
                {"id": "a2pd4", "prompt": "How do you say \"I bought them\" (le chiavi, feminine plural, passato prossimo)?", "options": ["Le ho comprato.", "Le ho comprate.", "Ho comprato le."], "answerIndex": 1, "explanation": "Le goes before ho, and the participle agrees: comprate."},
             ]},
        ],
        "summary": [
            "Direct object pronouns (mi, ti, lo, la, ci, vi, li, le) replace a direct object and go before the conjugated verb.",
            "They can attach to an infinitive instead, dropping its final -e.",
            "With avere in the passato prossimo, lo/la/li/le force participle agreement — the one exception to \"avere never agrees\".",
        ],
    },
    {
        "id": "a2-avverbi-di-frequenza",
        "level": "A2", "unit": "1", "order": 10, "skill": "grammar", "strand": "adverbs",
        "title": "Espressioni di Tempo e Avverbi di Frequenza",
        "subtitle": "Sempre, spesso, a volte, raramente, mai — and where they go in the sentence.",
        "objectives": [
            "Use the core frequency adverbs from most to least frequent",
            "Place frequency adverbs correctly in simple and compound tenses",
            "Use non ... mai correctly for \"never\"",
        ],
        "content": {
            "intro": "Frequency adverbs let you describe routines and habits with precision — and they follow a placement rule that differs from the present tense to the passato prossimo.",
            "explanation": "<p>In the present tense, frequency adverbs usually follow the verb directly: <em>Vado sempre in palestra.</em> In the passato prossimo, short, common adverbs (sempre, già, mai, ancora, ma also ben-known più) slot in <strong>between</strong> the auxiliary and the past participle: <em>Non sono mai stato a Venezia.</em></p>",
            "rules": [
                {"heading": "a) Frequency scale, most to least", "body": "<p><em>sempre</em> (always) &gt; <em>di solito</em> (usually) &gt; <em>spesso</em> (often) &gt; <em>a volte / qualche volta</em> (sometimes) &gt; <em>raramente</em> (rarely) &gt; <em>non ... mai</em> (never)</p>"},
                {"heading": "b) Mai — \"never\" needs non", "body": "<p>Non before the verb + mai after (or between auxiliary and participle): <em>Non mangio mai carne.</em> (I never eat meat.) <em>Non ho mai visto quel film.</em> (I've never seen that film.)</p>"},
                {"heading": "c) Placement in the passato prossimo", "body": "<p>Sempre, mai, già, ancora, più typically go between the auxiliary and the participle: <em>Ho già mangiato. Non ho ancora finito.</em> (I've already eaten. I haven't finished yet.)</p>"},
            ],
            "examples": [
                {"it": "Faccio sempre colazione alle otto.", "en": "I always have breakfast at eight."},
                {"it": "Vado spesso in palestra dopo il lavoro.", "en": "I often go to the gym after work."},
                {"it": "Non sono mai stata in Giappone.", "en": "I've never been to Japan."},
                {"it": "A volte lavoro anche il weekend.", "en": "Sometimes I even work on the weekend."},
                {"it": "Ho già finito i compiti.", "en": "I've already finished my homework."},
            ],
            "commonMistakes": [
                {"wrong": "Mangio mai carne.", "right": "Non mangio mai carne.", "why": "Mai needs non before the verb — Italian, unlike English \"never\", still requires the negative particle."},
                {"wrong": "Ho mai visitato Venezia.", "right": "Non ho mai visitato Venezia.", "why": "Same rule in the passato prossimo — non is required alongside mai."},
                {"wrong": "Ho finito già i compiti.", "right": "Ho già finito i compiti.", "why": "Già typically sits between the auxiliary and the participle, not after the whole verb phrase."},
            ],
        },
        "exercises": [
            {"id": "a2af-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a2af1", "prompt": "___ mangio carne. (never)", "answers": [["Non mangio mai"]], "explanation": "Mai needs non before the verb.", "options": ["Non mangio mai", "Mangio mai", "Mai mangio"]},
                {"id": "a2af2", "prompt": "Ho ___ (already) finito il lavoro.", "answers": [["già"]], "explanation": "Già slots between auxiliary and participle.", "options": ["già", "sempre", "mai"]},
             ]},
            {"id": "a2af-mc", "type": "multiple-choice", "title": "Order Them by Frequency",
             "items": [
                {"id": "a2af3", "prompt": "Which word means the LEAST frequent (besides never)?", "options": ["spesso", "raramente", "di solito"], "answerIndex": 1, "explanation": "Raramente (rarely) is the least frequent option here, short of mai (never)."},
             ]},
            {"id": "a2af-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a2af4", "incorrect": "Sono mai stato a Roma.", "answer": ["Non sono mai stato a Roma."], "explanation": "Mai requires non before the verb."},
             ]},
        ],
        "summary": [
            "Frequency scale: sempre > di solito > spesso > a volte > raramente > non ... mai.",
            "Mai (never) always needs non before the verb — Italian double-marks the negation.",
            "In the passato prossimo, sempre/mai/già/ancora typically go between the auxiliary and the participle.",
        ],
    },
]
