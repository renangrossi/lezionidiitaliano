# -*- coding: utf-8 -*-
"""B1 — Intermediate curriculum data."""

OVERVIEW = ("B1 rounds out the past with the imperfetto and its crucial contrast with the "
            "passato prossimo, adds indirect and combined pronouns, and introduces the future, "
            "the conditional, the imperative, and the particles ci and ne. By the end you can "
            "narrate the past fluently, make requests and suggestions, and give instructions.")

LESSONS = [
    {
        "id": "b1-imperfetto",
        "level": "B1", "unit": "1", "order": 1, "skill": "grammar", "strand": "past-tenses",
        "title": "L'Imperfetto",
        "subtitle": "Italian's other past tense — for background, habits, and descriptions.",
        "objectives": [
            "Conjugate regular verbs in the imperfetto",
            "Conjugate the three key irregular imperfetto verbs: essere, fare, bere",
            "Use the imperfetto for habitual past actions and descriptions",
        ],
        "content": {
            "intro": "While the passato prossimo reports a completed event, the imperfetto paints the background: what things were like, what used to happen, what was already going on.",
            "explanation": "<p>The imperfetto is one of the most regular tenses in Italian — nearly every verb (even most that are irregular elsewhere) follows the same pattern, built by dropping -re from the infinitive and adding the imperfetto endings. Only essere is truly irregular; fare and bere use their old Latin stems (facere, bevere) rather than the modern infinitive.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Imperfetto — parlare, avere, essere</caption><thead><tr><th>Subject</th><th>parlare</th><th>avere</th><th>essere</th></tr></thead><tbody><tr><td>io</td><td>parlavo</td><td>avevo</td><td>ero</td></tr><tr><td>tu</td><td>parlavi</td><td>avevi</td><td>eri</td></tr><tr><td>lui/lei</td><td>parlava</td><td>aveva</td><td>era</td></tr><tr><td>noi</td><td>parlavamo</td><td>avevamo</td><td>eravamo</td></tr><tr><td>voi</td><td>parlavate</td><td>avevate</td><td>eravate</td></tr><tr><td>loro</td><td>parlavano</td><td>avevano</td><td>erano</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Regular pattern", "body": "<p>Drop -are/-ere/-ire, add: -vo, -vi, -va, -vamo, -vate, -vano (with the conjugation's vowel kept: parla-vo, cred-e-vo, dorm-i-vo).</p>"},
                {"heading": "b) When to use the imperfetto", "body": "<ul><li>Habitual/repeated past actions: <em>Da bambino giocavo sempre fuori.</em> (As a child I always used to play outside.)</li><li>Descriptions (people, places, weather, time, age) in the past: <em>Era una bella giornata. Faceva caldo.</em></li><li>Background action interrupted by another (paired with passato prossimo, next lesson): <em>Dormivo quando hai chiamato.</em></li></ul>"},
            ],
            "examples": [
                {"it": "Da piccolo abitavo in campagna.", "en": "As a child I lived in the countryside."},
                {"it": "Ogni estate andavamo al mare.", "en": "Every summer we would go to the seaside."},
                {"it": "Erano le nove di sera.", "en": "It was nine in the evening."},
                {"it": "Faceva molto freddo quel giorno.", "en": "It was very cold that day."},
                {"it": "Mia nonna raccontava sempre storie bellissime.", "en": "My grandmother always used to tell wonderful stories."},
            ],
            "commonMistakes": [
                {"wrong": "Ieri sono andato al mare ogni giorno.", "right": "Ogni giorno andavo al mare.", "why": "A repeated/habitual action needs the imperfetto, not the passato prossimo, which reports a single completed event."},
                {"wrong": "Io ero avevo dieci anni.", "right": "Avevo dieci anni.", "why": "Age uses avere alone (avevo), not combined with essere."},
                {"wrong": "Fecevo i compiti ogni sera. (for fare)", "right": "Facevo i compiti ogni sera.", "why": "Fare's imperfetto stem is fac- (from facere), giving facevo, not a form based on the modern infinitive fare."},
            ],
        },
        "exercises": [
            {"id": "b1im-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b1im1", "prompt": "Da bambina, io ___ (giocare) sempre in giardino.", "answers": [["giocavo"]], "explanation": "Regular -are imperfetto: giocavo.", "options": ["giocavo", "giocai", "ho giocato"]},
                {"id": "b1im2", "prompt": "Quando ___ (essere) giovane, viaggiavo molto.", "answers": [["ero"]], "explanation": "Essere's irregular imperfetto io form is ero.", "options": ["ero", "sono stato", "fui"]},
                {"id": "b1im3", "prompt": "Noi ___ (avere) un cane quando ero piccolo.", "answers": [["avevamo"]], "explanation": "Regular imperfetto of avere: avevamo.", "options": ["avevamo", "abbiamo avuto", "avevano"]},
             ]},
            {"id": "b1im-mc", "type": "multiple-choice", "title": "Choose the Correct Use",
             "items": [
                {"id": "b1im4", "prompt": "Describing what the weather was like yesterday afternoon:", "options": ["Ha fatto caldo.", "Faceva caldo.", "Fece caldo per un minuto."], "answerIndex": 1, "explanation": "Weather description in the past uses the imperfetto."},
             ]},
        ],
        "summary": [
            "The imperfetto is built regularly: stem + -vo/-vi/-va/-vamo/-vate/-vano; only essere is truly irregular.",
            "Use it for habitual past actions, descriptions, and background states.",
            "Contrast with the passato prossimo, which reports single, completed events — next lesson.",
        ],
    },
    {
        "id": "b1-imperfetto-vs-passato-prossimo",
        "level": "B1", "unit": "1", "order": 2, "skill": "grammar", "strand": "past-tenses",
        "title": "Imperfetto vs. Passato Prossimo",
        "subtitle": "The single most important contrast in Italian storytelling.",
        "objectives": [
            "Choose between imperfetto and passato prossimo based on the type of past action",
            "Combine both tenses correctly in one narrative",
            "Recognize verbs whose meaning shifts between the two tenses",
        ],
        "content": {
            "intro": "Almost every Italian story mixes both past tenses: the imperfetto sets the scene, the passato prossimo moves the plot forward. Getting this contrast right is what makes your Italian sound like real narration instead of a list of facts.",
            "explanation": "<p>Think of the imperfetto as a video camera left running in the background (ongoing, no clear end point) and the passato prossimo as a snapshot (a single, completed, often sudden event). The classic pattern is a background action (imperfetto) interrupted by a completed one (passato prossimo): <em>Dormivo quando è suonato il telefono.</em> (I was sleeping when the phone rang.)</p>",
            "rules": [
                {"heading": "a) Imperfetto — background, ongoing, habitual", "body": "<ul><li>Descriptions: <em>Il cielo era grigio.</em></li><li>Habits/repetition: <em>Andavo in palestra ogni martedì.</em></li><li>Ongoing action in progress: <em>Leggevo un libro.</em></li></ul>"},
                {"heading": "b) Passato prossimo — completed, sudden, sequential events", "body": "<ul><li>A single completed event: <em>Ieri sono andato in palestra.</em></li><li>A sudden interruption: <em>...quando è suonato il telefono.</em></li><li>A sequence of events: <em>Mi sono alzato, ho fatto colazione, sono uscito.</em></li></ul>"},
                {"heading": "c) Verbs that change meaning", "body": "<ul><li><em>sapere</em>: imperfetto = knew (state) &mdash; <em>Non sapevo</em> (I didn't know); passato prossimo = found out (event) &mdash; <em>Ho saputo</em> (I found out)</li><li><em>conoscere</em>: imperfetto = knew (already acquainted); passato prossimo = met (for the first time) &mdash; <em>Ho conosciuto mia moglie a Roma.</em></li></ul>"},
            ],
            "examples": [
                {"it": "Mentre cucinavo, è arrivato Marco.", "en": "While I was cooking, Marco arrived."},
                {"it": "Da giovane, giocavo a calcio ogni weekend.", "en": "As a young man, I used to play soccer every weekend."},
                {"it": "Ieri ho giocato a calcio con i miei amici.", "en": "Yesterday I played soccer with my friends."},
                {"it": "Non sapevo che eri qui!", "en": "I didn't know you were here!"},
                {"it": "Ho conosciuto mia moglie in Italia.", "en": "I met my wife in Italy."},
            ],
            "commonMistakes": [
                {"wrong": "Mentre cucinavo, Marco è arrivava.", "right": "Mentre cucinavo, Marco è arrivato.", "why": "The interrupting, completed event (arriving) needs the passato prossimo; only the background action stays in the imperfetto."},
                {"wrong": "Ieri giocavo a calcio.", "right": "Ieri ho giocato a calcio.", "why": "A single, completed event on a specific occasion (\"yesterday\") needs the passato prossimo, not the imperfetto."},
                {"wrong": "Ho conosciuto la geografia dell'Italia da anni.", "right": "Conoscevo la geografia dell'Italia da anni.", "why": "An ongoing state of already knowing something needs the imperfetto; passato prossimo here would wrongly suggest a single \"meeting\" event."},
            ],
        },
        "exercises": [
            {"id": "b1ip-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "instructions": "Choose imperfetto or passato prossimo.",
             "items": [
                {"id": "b1ip1", "prompt": "___ (Piovere) quando siamo usciti di casa.", "answers": [["Pioveva"]], "explanation": "Background, ongoing weather → imperfetto.", "options": ["Pioveva", "È piovuto", "Piove"]},
                {"id": "b1ip2", "prompt": "Ieri sera ___ (io - guardare) un film e poi ___ (andare) a letto.", "answers": [["ho guardato"], ["sono andato"]], "explanation": "A sequence of completed events → passato prossimo for both.", "options": ["ho guardato", "guardavo", "sono andato"]},
                {"id": "b1ip3", "prompt": "Quando ___ (essere) piccolo, ___ (avere) paura del buio.", "answers": [["ero"], ["avevo"]], "explanation": "A description/state in the past → imperfetto for both.", "options": ["ero", "sono stato", "avevo"]},
             ]},
            {"id": "b1ip-mc", "type": "multiple-choice", "title": "Choose the Correct Tense",
             "items": [
                {"id": "b1ip4", "prompt": "\"I found out yesterday that she moved.\"", "options": ["Sapevo ieri che si è trasferita.", "Ho saputo ieri che si è trasferita.", "Ho sapere ieri che si trasferiva."], "answerIndex": 1, "explanation": "\"Found out\" is a single event → passato prossimo of sapere."},
             ]},
            {"id": "b1ip-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "b1ip5", "incorrect": "Ieri giocavo a tennis con Marco.", "answer": ["Ieri ho giocato a tennis con Marco."], "explanation": "A single completed occasion needs the passato prossimo."},
             ]},
        ],
        "summary": [
            "Imperfetto = background, ongoing, habitual, description; passato prossimo = completed, sudden, sequential.",
            "The classic pattern: imperfetto sets the scene, passato prossimo interrupts or advances the plot.",
            "Sapere and conoscere shift meaning between the two tenses — state vs. event.",
        ],
    },
    {
        "id": "b1-pronomi-indiretti",
        "level": "B1", "unit": "1", "order": 3, "skill": "grammar", "strand": "pronouns",
        "title": "Pronomi Indiretti",
        "subtitle": "Mi, ti, gli, le, ci, vi, gli — replacing \"to/for someone\".",
        "objectives": [
            "Identify an indirect object and choose the matching pronoun",
            "Distinguish gli (to him) from le (to her)",
            "Use common verbs that take an indirect object: dare, dire, scrivere, telefonare, piacere",
        ],
        "content": {
            "intro": "An indirect object answers \"to whom?\" or \"for whom?\" — in English it's often marked by \"to\", but in Italian, once replaced by a pronoun, that \"to\" disappears entirely.",
            "explanation": "<p>Many indirect object pronouns look identical to the direct ones you already know (mi, ti, ci, vi) — only the third person differs: <strong>gli</strong> (to him), <strong>le</strong> (to her, also the formal \"to you\"), and <strong>gli</strong> again for the plural \"to them\" (loro is the old, formal alternative, placed after the verb, but gli before the verb is now standard in speech).</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Indirect object pronouns</caption><thead><tr><th>To/for...</th><th>Pronoun</th></tr></thead><tbody><tr><td>me</td><td>mi</td></tr><tr><td>you (informal)</td><td>ti</td></tr><tr><td>him</td><td>gli</td></tr><tr><td>her / you (formal)</td><td>le</td></tr><tr><td>us</td><td>ci</td></tr><tr><td>you (pl.)</td><td>vi</td></tr><tr><td>them</td><td>gli</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Verbs that take an indirect object", "body": "<p><em>dare</em> (to give), <em>dire</em> (to say/tell), <em>scrivere</em> (to write), <em>telefonare</em> (to phone), <em>chiedere</em> (to ask), <em>rispondere</em> (to answer) — all describe an action directed \"to/for\" someone.</p>"},
                {"heading": "b) Piacere — a special case", "body": "<p><em>Piacere</em> (to like/please) works backwards from English: the thing liked is the subject, and the person is an indirect object. <em>Mi piace il caffè.</em> (Coffee is pleasing to me = I like coffee.) <em>Mi piacciono i film.</em> (plural subject → plural verb piacciono)</p>"},
            ],
            "examples": [
                {"it": "Gli scrivo un'email ogni settimana.", "en": "I write him an email every week."},
                {"it": "Le ho telefonato ieri.", "en": "I called her yesterday."},
                {"it": "Ci hanno detto la verità.", "en": "They told us the truth."},
                {"it": "Mi piace molto questa città.", "en": "I really like this city."},
                {"it": "Non gli piacciono i dolci.", "en": "He doesn't like sweets."},
            ],
            "commonMistakes": [
                {"wrong": "Gli scrivo a Maria. (using gli for a woman)", "right": "Le scrivo.", "why": "Gli is masculine (\"to him\"); a female indirect object needs le."},
                {"wrong": "Mi piaccio il gelato.", "right": "Mi piace il gelato.", "why": "Piacere agrees with the thing liked (il gelato, singular), not with the speaker — mi piaccio would mean \"I like myself\"."},
                {"wrong": "Telefono a lei ogni giorno. (natural but the pronoun form is preferred in fluent speech)", "right": "Le telefono ogni giorno.", "why": "While a lei is grammatical, fluent Italian strongly prefers the unstressed pronoun le before the verb in everyday speech."},
            ],
        },
        "exercises": [
            {"id": "b1pi-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b1pi1", "prompt": "___ scrivo un messaggio a Marco. (to him)", "answers": [["Gli"]], "explanation": "Gli = to him.", "options": ["Gli", "Le", "Lo"]},
                {"id": "b1pi2", "prompt": "___ piace il cinema italiano. (I like)", "answers": [["Mi"]], "explanation": "Mi piace = it is pleasing to me.", "options": ["Mi", "Io", "Mia"]},
                {"id": "b1pi3", "prompt": "___ telefono domani. (to her)", "answers": [["Le"]], "explanation": "Le = to her.", "options": ["Le", "Gli", "La"]},
             ]},
            {"id": "b1pi-mc", "type": "multiple-choice", "title": "Choose the Correct Pronoun",
             "items": [
                {"id": "b1pi4", "prompt": "\"I like Italian songs\" (canzoni is plural)", "options": ["Mi piace le canzoni italiane.", "Mi piacciono le canzoni italiane.", "Mi piaccio le canzoni italiane."], "answerIndex": 1, "explanation": "Piacere agrees with the plural subject canzoni: piacciono."},
             ]},
        ],
        "summary": [
            "Indirect object pronouns: mi, ti, gli (to him), le (to her/formal you), ci, vi, gli (to them).",
            "Verbs like dare, dire, scrivere, telefonare, chiedere naturally take an indirect object.",
            "Piacere works backwards from English: the thing liked is the subject, agreeing with the verb.",
        ],
    },
    {
        "id": "b1-pronomi-combinati",
        "level": "B1", "unit": "1", "order": 4, "skill": "grammar", "strand": "pronouns",
        "title": "Pronomi Combinati",
        "subtitle": "Me lo, te lo, glielo — direct and indirect pronouns fused into one word.",
        "objectives": [
            "Combine indirect and direct object pronouns in the correct order",
            "Recognize the mi/ti/ci/vi → me/te/ce/ve vowel change",
            "Recognize glielo/gliela/glieli/gliele as one fused word",
        ],
        "content": {
            "intro": "When both a direct and an indirect object pronoun appear in the same sentence — \"I'll give it to you\" — Italian fuses them into a single combined form, always indirect before direct.",
            "explanation": "<p>Mi, ti, ci, vi change their final -i to -e before a direct object pronoun (mi + lo &rarr; <strong>me lo</strong>). Gli and le both become <strong>glie-</strong> and physically fuse with the direct pronoun into one word: gli/le + lo &rarr; <strong>glielo</strong>, gli/le + la &rarr; <strong>gliela</strong>, and so on — this single form covers \"to him/her/them\" plus the direct object, disambiguated only by context.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Combined pronouns (indirect + lo/la/li/le)</caption><thead><tr><th>Indirect</th><th>+ lo</th><th>+ la</th><th>+ li</th><th>+ le</th></tr></thead><tbody><tr><td>mi</td><td>me lo</td><td>me la</td><td>me li</td><td>me le</td></tr><tr><td>ti</td><td>te lo</td><td>te la</td><td>te li</td><td>te le</td></tr><tr><td>gli/le</td><td>glielo</td><td>gliela</td><td>glieli</td><td>gliele</td></tr><tr><td>ci</td><td>ce lo</td><td>ce la</td><td>ce li</td><td>ce le</td></tr><tr><td>vi</td><td>ve lo</td><td>ve la</td><td>ve li</td><td>ve le</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Order and position", "body": "<p>Indirect always comes first, direct second, and both go before the conjugated verb (or attach to an infinitive): <em>Te lo do.</em> (I give it to you.) <em>Posso dartelo.</em> / <em>Te lo posso dare.</em></p>"},
                {"heading": "b) Participle agreement", "body": "<p>The past participle agrees with the direct object exactly as with lo/la/li/le alone: <em>Te l'ho dato.</em> (m. sing.) <em>Te l'ho data.</em> (f. sing., elided the same way)</p>"},
            ],
            "examples": [
                {"it": "Il libro? Te lo do domani.", "en": "The book? I'll give it to you tomorrow."},
                {"it": "Le chiavi? Gliele ho lasciate sul tavolo.", "en": "The keys? I left them for him/her on the table."},
                {"it": "Ce lo ha spiegato bene.", "en": "He/she explained it to us well."},
                {"it": "Non ve lo posso dire.", "en": "I can't tell it to you [pl.]."},
                {"it": "Se vuoi il mio numero, te lo scrivo.", "en": "If you want my number, I'll write it down for you."},
            ],
            "commonMistakes": [
                {"wrong": "Lo mi do.", "right": "Me lo do.", "why": "The indirect pronoun always comes before the direct one, and both come before the verb — never after in this order."},
                {"wrong": "Gli lo do.", "right": "Glielo do.", "why": "Gli/le physically fuse with lo/la/li/le into one written word — they never stay separate."},
                {"wrong": "Te l'ho dato. (for una lettera, feminine)", "right": "Te l'ho data.", "why": "The participle must agree with the feminine direct object (la lettera), even though it's now hidden inside the elided l'."},
            ],
        },
        "exercises": [
            {"id": "b1pc-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b1pc1", "prompt": "Il regalo? ___ do subito. (to you, tu)", "answers": [["Te lo"]], "explanation": "Ti + lo = te lo.", "options": ["Te lo", "Ti lo", "Lo te"]},
                {"id": "b1pc2", "prompt": "La ricetta? ___ ho spiegata ieri. (to him)", "answers": [["Gliela"]], "explanation": "Gli + la = gliela, fused into one word.", "options": ["Gliela", "Gli la", "Le la"]},
                {"id": "b1pc3", "prompt": "I documenti? ___ mando subito. (to us)", "answers": [["Ce li"]], "explanation": "Ci + li = ce li.", "options": ["Ce li", "Ci li", "Ce le"]},
             ]},
            {"id": "b1pc-mc", "type": "multiple-choice", "title": "Choose the Correct Combined Pronoun",
             "items": [
                {"id": "b1pc4", "prompt": "\"I explained it to her\" (la spiegazione, feminine)", "options": ["Gliel'ho spiegato.", "Gliel'ho spiegata.", "Le l'ho spiegata."], "answerIndex": 1, "explanation": "Glielo/gliela fuses gli+le into one word, and the participle agrees with the feminine object."},
             ]},
        ],
        "summary": [
            "Mi/ti/ci/vi change to me/te/ce/ve before a direct object pronoun.",
            "Gli and le both become glie-, fusing into one word: glielo, gliela, glieli, gliele.",
            "The past participle still agrees with the direct object hidden inside the combined pronoun.",
        ],
    },
    {
        "id": "b1-futuro-semplice",
        "level": "B1", "unit": "1", "order": 5, "skill": "grammar", "strand": "future",
        "title": "Il Futuro Semplice",
        "subtitle": "One tense for predictions, plans, and probability.",
        "objectives": [
            "Conjugate regular verbs in the futuro semplice",
            "Recognize the main irregular future stems",
            "Use the future of probability to express a guess about the present",
        ],
        "content": {
            "intro": "The futuro semplice covers what English splits between \"will\" and \"going to\" — and it has one more job English's future doesn't: expressing a guess about right now.",
            "explanation": "<p>Built from the infinitive (with -are verbs changing their a to e) plus one shared set of endings across all three conjugations. A number of very common verbs have a shortened, irregular stem that the endings then attach to.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Futuro semplice — parlare, avere, essere</caption><thead><tr><th>Subject</th><th>parlare</th><th>avere</th><th>essere</th></tr></thead><tbody><tr><td>io</td><td>parlerò</td><td>avrò</td><td>sarò</td></tr><tr><td>tu</td><td>parlerai</td><td>avrai</td><td>sarai</td></tr><tr><td>lui/lei</td><td>parlerà</td><td>avrà</td><td>sarà</td></tr><tr><td>noi</td><td>parleremo</td><td>avremo</td><td>saremo</td></tr><tr><td>voi</td><td>parlerete</td><td>avrete</td><td>sarete</td></tr><tr><td>loro</td><td>parleranno</td><td>avranno</td><td>saranno</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Regular endings", "body": "<p>-erò, -erai, -erà, -eremo, -erete, -eranno (for -are verbs, the a of the infinitive becomes e first: parlare → parler-).</p>"},
                {"heading": "b) Common irregular stems", "body": "<p><em>essere &rarr; sar-, avere &rarr; avr-, andare &rarr; andr-, fare &rarr; far-, potere &rarr; potr-, dovere &rarr; dovr-, volere &rarr; vorr-, venire &rarr; verr-, vedere &rarr; vedr-, sapere &rarr; sapr-</em> — the regular endings still attach to these stems.</p>"},
                {"heading": "c) Future of probability", "body": "<p>A guess about the present, not a real future event: <em>Che ore sono? Saranno le tre.</em> (What time is it? It's probably around three.) <em>Non risponde: sarà occupato.</em> (He's not answering: he's probably busy.)</p>"},
            ],
            "examples": [
                {"it": "Domani lavorerò da casa.", "en": "Tomorrow I'll work from home."},
                {"it": "L'anno prossimo andremo in Giappone.", "en": "Next year we'll go to Japan."},
                {"it": "Farà bel tempo questo weekend.", "en": "It will be good weather this weekend."},
                {"it": "Chi sarà a quella festa?", "en": "I wonder who'll be at that party."},
                {"it": "Avranno vent'anni, più o meno.", "en": "They're probably about twenty."},
            ],
            "commonMistakes": [
                {"wrong": "Io vado studiare domani. (for a distant plan)", "right": "Studierò domani. / Andrò a studiare domani.", "why": "While present tense works for near, casual plans, a clearer future statement uses the futuro semplice."},
                {"wrong": "Io avrò vent'anni oggi. (stating a fact)", "right": "Ho vent'anni.", "why": "The future is for prediction or probability, not a present fact — use the present tense to simply state your age."},
                {"wrong": "Farò meaning \"I will make/do\" spelled faro", "right": "farò (with the accent)", "why": "The accent on the final ò marks stress and is required — dropping it changes both spelling and, in writing, meaning."},
            ],
        },
        "exercises": [
            {"id": "b1fs-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b1fs1", "prompt": "Domani ___ (io - lavorare) tutto il giorno.", "answers": [["lavorerò"]], "explanation": "Regular future of lavorare: lavorerò.", "options": ["lavorerò", "lavoro", "lavoravo"]},
                {"id": "b1fs2", "prompt": "L'anno prossimo ___ (loro - andare) in Australia.", "answers": [["andranno"]], "explanation": "Andare has the irregular stem andr-.", "options": ["andranno", "anderanno", "vanno"]},
                {"id": "b1fs3", "prompt": "___ (Essere - tu) libero sabato?", "answers": [["Sarai"]], "explanation": "Essere's irregular future stem is sar-.", "options": ["Sarai", "Sei", "Serai"]},
             ]},
            {"id": "b1fs-mc", "type": "multiple-choice", "title": "Prediction or Probability?",
             "items": [
                {"id": "b1fs4", "prompt": "\"Someone's knocking — it's probably the postman.\"", "options": ["È il postino.", "Sarà il postino.", "Era il postino."], "answerIndex": 1, "explanation": "A guess about the present uses the future of probability."},
             ]},
        ],
        "summary": [
            "Regular future: infinitive stem (-are → -er-) + -ò, -ai, -à, -emo, -ete, -anno.",
            "Common irregular stems: sar-, avr-, andr-, far-, potr-, dovr-, vorr-, verr-, vedr-, sapr-.",
            "The future also expresses probability about the present, not just genuine future events.",
        ],
    },
    {
        "id": "b1-condizionale-presente",
        "level": "B1", "unit": "1", "order": 6, "skill": "grammar", "strand": "conditional",
        "title": "Il Condizionale Presente",
        "subtitle": "Would — for politeness, wishes, and advice.",
        "objectives": [
            "Conjugate regular verbs in the condizionale presente",
            "Use vorrei for polite requests",
            "Use the conditional of dovere for advice",
        ],
        "content": {
            "intro": "The conditional is what makes Italian sound polite: vorrei instead of voglio, potrebbe instead of può — the single grammatical feature that softens a request into a courtesy.",
            "explanation": "<p>The conditional shares the same irregular stems as the future (sar-, avr-, andr-, and so on) but takes its own distinct set of endings. It's used constantly in everyday speech for politeness, wishes, and giving advice.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Condizionale presente — parlare, avere, essere</caption><thead><tr><th>Subject</th><th>parlare</th><th>avere</th><th>essere</th></tr></thead><tbody><tr><td>io</td><td>parlerei</td><td>avrei</td><td>sarei</td></tr><tr><td>tu</td><td>parleresti</td><td>avresti</td><td>saresti</td></tr><tr><td>lui/lei</td><td>parlerebbe</td><td>avrebbe</td><td>sarebbe</td></tr><tr><td>noi</td><td>parleremmo</td><td>avremmo</td><td>saremmo</td></tr><tr><td>voi</td><td>parlereste</td><td>avreste</td><td>sareste</td></tr><tr><td>loro</td><td>parlerebbero</td><td>avrebbero</td><td>sarebbero</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Endings", "body": "<p>-ei, -esti, -ebbe, -emmo, -este, -ebbero, added to the same stem as the future (parler-, avr-, sar-...).</p>"},
                {"heading": "b) Politeness", "body": "<p><em>Vorrei</em> (I would like) is the standard polite way to order or request, replacing the blunter <em>voglio</em>: <em>Vorrei un caffè, per favore.</em> <em>Potrebbe aiutarmi?</em> (Could you help me? — formal)</p>"},
                {"heading": "c) Advice with dovrei/dovresti", "body": "<p><em>Dovresti riposare di più.</em> (You should rest more.) Softer and more natural than the blunt obligation of devi.</p>"},
            ],
            "examples": [
                {"it": "Vorrei un tavolo per due, per favore.", "en": "I would like a table for two, please."},
                {"it": "Mi piacerebbe visitare la Sicilia.", "en": "I would love to visit Sicily."},
                {"it": "Dovresti parlare con lui.", "en": "You should talk to him."},
                {"it": "Potresti chiudere la finestra?", "en": "Could you close the window?"},
                {"it": "Sarebbe fantastico viaggiare insieme.", "en": "It would be fantastic to travel together."},
            ],
            "commonMistakes": [
                {"wrong": "Voglio un caffè. (as a polite order in a café)", "right": "Vorrei un caffè, per favore.", "why": "Voglio is grammatically fine but blunt — vorrei is the standard polite register for ordering or requesting."},
                {"wrong": "Dovrei che tu studi di più.", "right": "Dovresti studiare di più.", "why": "Dovere + infinitive needs no conjunction che — it pairs directly with the infinitive, just like in the present tense."},
                {"wrong": "Io vorrei andare al mare. spelled voglierei", "right": "vorrei (irregular stem vorr-, not a regular volere stem)", "why": "Volere has an irregular conditional stem, vorr-, shared with the future — not a regular form built from the infinitive."},
            ],
        },
        "exercises": [
            {"id": "b1cp-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b1cp1", "prompt": "___ (Volere - io) un bicchiere d'acqua, per favore.", "answers": [["Vorrei"]], "explanation": "Vorrei is the polite conditional of volere.", "options": ["Vorrei", "Voglio", "Volevo"]},
                {"id": "b1cp2", "prompt": "___ (Potere - tu) aiutarmi con le valigie?", "answers": [["Potresti"]], "explanation": "Conditional of potere, tu form: potresti.", "options": ["Potresti", "Puoi", "Potevi"]},
                {"id": "b1cp3", "prompt": "Voi ___ (dovere) riposare di più.", "answers": [["dovreste"]], "explanation": "Conditional of dovere, voi form: dovreste.", "options": ["dovreste", "dovete", "dovevate"]},
             ]},
            {"id": "b1cp-mc", "type": "multiple-choice", "title": "Choose the Politest Option",
             "items": [
                {"id": "b1cp4", "prompt": "Ordering coffee politely at a café bar:", "options": ["Voglio un caffè.", "Vorrei un caffè, per favore.", "Devo un caffè."], "answerIndex": 1, "explanation": "Vorrei is the standard polite conditional for ordering."},
             ]},
        ],
        "summary": [
            "The conditional shares the future's irregular stems, with its own endings: -ei, -esti, -ebbe, -emmo, -este, -ebbero.",
            "Vorrei/potrebbe soften requests into polite register — used constantly in daily life.",
            "Dovrei/dovresti give gentle advice, softer than the direct obligation of devo/devi.",
        ],
    },
    {
        "id": "b1-imperativo-informale",
        "level": "B1", "unit": "1", "order": 7, "skill": "grammar", "strand": "imperative",
        "title": "L'Imperativo Informale",
        "subtitle": "Giving commands and instructions with tu, noi, voi.",
        "objectives": [
            "Form the informal imperative for tu, noi, voi",
            "Form the negative tu imperative correctly",
            "Attach object and reflexive pronouns to the informal imperative",
        ],
        "content": {
            "intro": "The informal imperative is how you give instructions, make suggestions, or issue commands to someone you'd address with tu — a friend, a child, someone your own age.",
            "explanation": "<p>The tu and voi imperative forms match the present tense exactly for -ere and -ire verbs, but -are verbs change their tu ending from -i to -a. The noi form (\"let's...\") is identical to the noi present tense in every conjugation. The negative tu form is special: <strong>non + infinitive</strong>, not the expected non + imperative.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Imperativo informale — parlare, prendere, aprire</caption><thead><tr><th>Subject</th><th>parlare</th><th>prendere</th><th>aprire</th></tr></thead><tbody><tr><td>(tu)</td><td>parla!</td><td>prendi!</td><td>apri!</td></tr><tr><td>(noi)</td><td>parliamo!</td><td>prendiamo!</td><td>apriamo!</td></tr><tr><td>(voi)</td><td>parlate!</td><td>prendete!</td><td>aprite!</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Negative tu — non + infinitive", "body": "<p><em>Non parlare!</em> (Don't speak!) — not \"non parla\". Noi and voi simply add non before the normal form: <em>Non parliamo. Non parlate.</em></p>"},
                {"heading": "b) Pronouns attach to the end", "body": "<p><em>Aiutami!</em> (Help me!) <em>Chiamalo!</em> (Call him!) <em>Alzati!</em> (Get up! — reflexive) In the negative, they can attach to the infinitive instead: <em>Non aiutarmi!</em> / <em>Non mi aiutare!</em></p>"},
                {"heading": "c) Irregular tu imperatives", "body": "<p><em>andare &rarr; va'/vai, dare &rarr; da'/dai, fare &rarr; fa'/fai, stare &rarr; sta'/stai, dire &rarr; di'</em> — short, apostrophized forms, both versions correct.</p>"},
            ],
            "examples": [
                {"it": "Ascolta bene!", "en": "Listen carefully!"},
                {"it": "Non toccare quello!", "en": "Don't touch that!"},
                {"it": "Andiamo al cinema stasera!", "en": "Let's go to the movies tonight!"},
                {"it": "Chiamami quando arrivi.", "en": "Call me when you arrive."},
                {"it": "Ragazzi, fate silenzio!", "en": "Guys, be quiet!"},
                {"it": "Non ti preoccupare, andrà tutto bene.", "en": "Don't worry, everything will be fine."},
            ],
            "commonMistakes": [
                {"wrong": "Non parla!", "right": "Non parlare!", "why": "The negative tu imperative uses non + infinitive, not the affirmative imperative form with non added."},
                {"wrong": "Mi aiuta!", "right": "Aiutami!", "why": "Pronouns attach to the end of the informal imperative form, not before it as with a conjugated verb."},
                {"wrong": "Parlate! (addressing one friend)", "right": "Parla!", "why": "Voi is plural — addressing a single friend needs the tu form, parla."},
            ],
        },
        "exercises": [
            {"id": "b1ii-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b1ii1", "prompt": "___ (Ascoltare - tu) con attenzione!", "answers": [["Ascolta"]], "explanation": "-are verbs change the tu ending to -a in the imperative.", "options": ["Ascolta", "Ascolti", "Ascoltare"]},
                {"id": "b1ii2", "prompt": "___ (Non parlare - tu) così forte!", "answers": [["Non parlare"]], "explanation": "Negative tu imperative = non + infinitive.", "options": ["Non parlare", "Non parla", "Non parli"]},
                {"id": "b1ii3", "prompt": "Ragazzi, ___ (fare) silenzio!", "answers": [["fate"]], "explanation": "Voi imperative of fare matches its present tense: fate.", "options": ["fate", "fai", "facciamo"]},
             ]},
            {"id": "b1ii-mc", "type": "multiple-choice", "title": "Choose the Correct Command",
             "items": [
                {"id": "b1ii4", "prompt": "\"Call me!\" (informal)", "options": ["Mi chiama!", "Chiamami!", "Chiama mi!"], "answerIndex": 1, "explanation": "Pronouns attach directly to the end of the imperative verb."},
             ]},
            {"id": "b1ii-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "b1ii5", "incorrect": "Non tocca quello!", "answer": ["Non toccare quello!"], "explanation": "Negative tu imperative needs the infinitive, not the present tense form."},
             ]},
        ],
        "summary": [
            "Tu imperative: -are verbs use -a; -ere/-ire verbs match the present tense tu form.",
            "Negative tu imperative is always non + infinitive — a genuine exception, not the affirmative + non.",
            "Object and reflexive pronouns attach to the end of the imperative verb (Aiutami!, Alzati!).",
        ],
    },
    {
        "id": "b1-imperativo-formale",
        "level": "B1", "unit": "1", "order": 8, "skill": "grammar", "strand": "imperative",
        "title": "L'Imperativo Formale",
        "subtitle": "Commands and instructions with Lei — and where pronouns go this time.",
        "objectives": [
            "Form the formal (Lei) imperative",
            "Place pronouns correctly before the formal imperative",
            "Contrast formal and informal imperative in the same situation",
        ],
        "content": {
            "intro": "The formal imperative uses the Lei form — borrowed, interestingly, from the present subjunctive rather than the present indicative — and its pronoun placement rule is the opposite of the informal imperative's.",
            "explanation": "<p>Where the informal imperative attaches pronouns to the end of the verb, the <strong>formal imperative places pronouns before the verb</strong>, exactly like any other conjugated verb form. The Lei imperative form itself looks like an -are verb's tu present tense and vice versa — a genuinely irregular-feeling swap worth memorizing as a pattern.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Imperativo formale (Lei) — parlare, prendere, aprire</caption><thead><tr><th>Verb</th><th>Lei imperative</th></tr></thead><tbody><tr><td>parlare</td><td>parli!</td></tr><tr><td>prendere</td><td>prenda!</td></tr><tr><td>aprire</td><td>apra!</td></tr><tr><td>fare (irregular)</td><td>faccia!</td></tr><tr><td>andare (irregular)</td><td>vada!</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Formation", "body": "<p>-are verbs take -i (the opposite of their tu present -i); -ere/-ire verbs take -a. Negation is simple: just add non before the form — no infinitive switch, unlike the informal tu.</p>"},
                {"heading": "b) Pronoun placement — before the verb", "body": "<p><em>Mi dica!</em> (Tell me! — formal) <em>Si accomodi.</em> (Please have a seat/come in.) <em>Lo prenda pure.</em> (Please take it.)</p>"},
            ],
            "examples": [
                {"it": "Mi scusi, dov'è la stazione?", "en": "Excuse me, where's the station? (Lei form of scusare)"},
                {"it": "Si accomodi, prego.", "en": "Please, have a seat / come in."},
                {"it": "Aspetti un momento, per favore.", "en": "Please wait a moment."},
                {"it": "Non si preoccupi.", "en": "Don't worry. (formal)"},
                {"it": "Mi dica pure, come posso aiutarla?", "en": "Go ahead and tell me, how can I help you?"},
            ],
            "commonMistakes": [
                {"wrong": "Scusami! (to a stranger you'd address as Lei)", "right": "Mi scusi!", "why": "Scusami is the informal tu imperative; a stranger or formal context needs the Lei form, mi scusi."},
                {"wrong": "Dicami!", "right": "Mi dica!", "why": "Unlike the informal imperative, pronouns go before the formal (Lei) imperative verb, not attached after it."},
                {"wrong": "Non aspettare! (as a formal negative command)", "right": "Non aspetti!", "why": "Only the informal tu negative imperative switches to the infinitive — the formal negative simply adds non before the normal Lei form."},
            ],
        },
        "exercises": [
            {"id": "b1if-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b1if1", "prompt": "___, dov'è il bagno? (Excuse me, formal)", "answers": [["Mi scusi"]], "explanation": "Formal imperative of scusare, with the pronoun before the verb.", "options": ["Mi scusi", "Scusami", "Mi scusa"]},
                {"id": "b1if2", "prompt": "Signora, ___ (accomodarsi), prego.", "answers": [["si accomodi"]], "explanation": "Formal reflexive imperative, pronoun before the verb.", "options": ["si accomodi", "si accomoda", "accomodisi"]},
             ]},
            {"id": "b1if-mc", "type": "multiple-choice", "title": "Formal or Informal?",
             "items": [
                {"id": "b1if3", "prompt": "Talking to your doctor: \"Please don't worry\"", "options": ["Non ti preoccupare.", "Non si preoccupi.", "Non preoccupati."], "answerIndex": 1, "explanation": "A doctor is addressed formally: non si preoccupi."},
             ]},
        ],
        "summary": [
            "Formal (Lei) imperative: -are verbs take -i, -ere/-ire verbs take -a — the reverse of their present tense pattern.",
            "Pronouns go before the formal imperative verb, unlike the informal, which attaches them after.",
            "The formal negative is just non + the normal Lei form — no infinitive switch as with informal tu.",
        ],
    },
    {
        "id": "b1-superlativi",
        "level": "B1", "unit": "1", "order": 9, "skill": "grammar", "strand": "comparatives",
        "title": "I Superlativi",
        "subtitle": "The most/least..., and the intensifier -issimo.",
        "objectives": [
            "Form the relative superlative (the most/least ... of/in)",
            "Form the absolute superlative with -issimo",
            "Recognize irregular comparative/superlative forms: migliore, peggiore, meglio, peggio",
        ],
        "content": {
            "intro": "Italian has two different kinds of superlative: the relative (\"the most... of the group\") and the absolute (\"extremely...\", with no comparison at all) — and the second is one of the most distinctive features of everyday Italian.",
            "explanation": "<p>The <strong>relative superlative</strong> reuses the comparative più/meno, adding the definite article: <em>il più alto della classe</em> (the tallest in the class). The <strong>absolute superlative</strong> replaces the adjective's final vowel with <strong>-issimo/a/i/e</strong>, meaning \"extremely/very\" with no comparison implied at all: <em>bellissimo</em> (extremely beautiful) is stronger and more common in speech than <em>molto bello</em>.</p>",
            "rules": [
                {"heading": "a) Relative superlative", "body": "<p>Article + (noun +) più/meno + adjective + di: <em>È la ragazza più intelligente della classe.</em> (She's the smartest girl in the class.)</p>"},
                {"heading": "b) Absolute superlative — -issimo", "body": "<p>Drop the final vowel, add -issimo/a/i/e: <em>alto &rarr; altissimo, facile &rarr; facilissimo, buona &rarr; buonissima</em>. Words ending in -co/-go often add an h to keep the hard sound: <em>stanco &rarr; stanchissimo</em>.</p>"},
                {"heading": "c) Irregular comparatives/superlatives", "body": "<ul><li><em>buono &rarr; migliore</em> (better) <em>&rarr; il migliore/ottimo</em> (the best/excellent)</li><li><em>cattivo &rarr; peggiore</em> (worse) <em>&rarr; il peggiore/pessimo</em> (the worst/terrible)</li><li>As adverbs: <em>bene &rarr; meglio</em> (better), <em>male &rarr; peggio</em> (worse)</li></ul>"},
            ],
            "examples": [
                {"it": "Questo è il ristorante migliore della città.", "en": "This is the best restaurant in the city."},
                {"it": "Sono stanchissima oggi.", "en": "I'm extremely tired today."},
                {"it": "Il Colosseo è il monumento più famoso di Roma.", "en": "The Colosseum is the most famous monument in Rome."},
                {"it": "Questa torta è buonissima!", "en": "This cake is delicious!"},
                {"it": "Oggi mi sento meglio di ieri.", "en": "Today I feel better than yesterday."},
            ],
            "commonMistakes": [
                {"wrong": "molto bellissimo", "right": "bellissimo (already means \"very beautiful\")", "why": "-issimo already means \"extremely\" — adding molto in front is redundant, doubling the intensifier."},
                {"wrong": "più buono for the irregular comparative", "right": "migliore", "why": "Buono has an irregular comparative, migliore — più buono is understood but non-standard where migliore is expected."},
                {"wrong": "Sto bene meglio.", "right": "Sto meglio.", "why": "Meglio already is the comparative of bene (\"better\") — bene meglio combines two forms of the same idea."},
            ],
        },
        "exercises": [
            {"id": "b1su-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b1su1", "prompt": "Questo esame è difficil___. (extremely difficult)", "answers": [["issimo"]], "explanation": "Absolute superlative: difficile → difficilissimo.", "options": ["issimo", "molto", "più"]},
                {"id": "b1su2", "prompt": "È il film ___ interessante dell'anno. (the most)", "answers": [["più"]], "explanation": "Relative superlative uses più + article (already given).", "options": ["più", "tanto", "issimo"]},
                {"id": "b1su3", "prompt": "Questo ristorante è ___ (better) di quello di ieri.", "answers": [["migliore"]], "explanation": "Buono's irregular comparative is migliore.", "options": ["migliore", "più buono", "buonissimo"]},
             ]},
            {"id": "b1su-mc", "type": "multiple-choice", "title": "Choose the Correct Form",
             "items": [
                {"id": "b1su4", "prompt": "\"Extremely tired\" (feminine)", "options": ["molto stanchissima", "stanchissima", "più stanca"], "answerIndex": 1, "explanation": "-issima alone already conveys \"extremely\"."},
             ]},
        ],
        "summary": [
            "Relative superlative: article + più/meno + adjective + di (the most/least ... in/of).",
            "Absolute superlative: -issimo/a/i/e, meaning \"extremely\", with no molto needed.",
            "Buono/cattivo/bene/male have irregular comparatives and superlatives: migliore, peggiore, meglio, peggio.",
        ],
    },
    {
        "id": "b1-ci-e-ne",
        "level": "B1", "unit": "1", "order": 10, "skill": "grammar", "strand": "particles",
        "title": "Ci e Ne",
        "subtitle": "Two small particles that replace a place, a topic, or a quantity.",
        "objectives": [
            "Use ci to replace a place or a topic introduced by a, in, su",
            "Use ne to replace a quantity or a topic introduced by di",
            "Place ci and ne correctly relative to the verb",
        ],
        "content": {
            "intro": "You already met ci inside c'è/ci sono — now meet its full range, alongside its partner particle ne, both of which let you avoid repeating a place, topic, or quantity you've already mentioned.",
            "explanation": "<p><strong>Ci</strong> replaces a place (\"there\") or a phrase introduced by a/in/su: <em>Vai a Roma? Sì, ci vado domani.</em> (Are you going to Rome? Yes, I'm going [there] tomorrow.) <strong>Ne</strong> replaces a quantity, or a phrase introduced by di: <em>Quanti libri hai? Ne ho tre.</em> (How many books do you have? I have three [of them].)</p>",
            "rules": [
                {"heading": "a) Ci — place and topic (a/in/su)", "body": "<ul><li>Place: <em>Sei mai stato in Sicilia? Sì, ci sono stato l'anno scorso.</em></li><li>Topic (pensare a): <em>Pensi al tuo futuro? Sì, ci penso spesso.</em></li></ul>"},
                {"heading": "b) Ne — quantity and topic (di)", "body": "<ul><li>Quantity: <em>Vuoi del vino? Sì, ne vorrei un po'.</em></li><li>Topic (parlare di): <em>Parli di politica? Non ne parlo mai.</em></li></ul>"},
                {"heading": "c) Position", "body": "<p>Both go before a conjugated verb, or attach to an infinitive: <em>Ci vado. / Voglio andarci.</em> With a number/quantity + passato prossimo, the participle agrees with ne's quantity: <em>Quante mele hai comprato? Ne ho comprate cinque.</em></p>"},
            ],
            "examples": [
                {"it": "Vai spesso in palestra? Sì, ci vado tre volte a settimana.", "en": "Do you go to the gym often? Yes, I go [there] three times a week."},
                {"it": "Quanti fratelli hai? Ne ho due.", "en": "How many siblings do you have? I have two [of them]."},
                {"it": "Credi in questo progetto? Sì, ci credo davvero.", "en": "Do you believe in this project? Yes, I really believe in it."},
                {"it": "Vuoi ancora del caffè? No grazie, non ne voglio più.", "en": "Do you want more coffee? No thanks, I don't want any more [of it]."},
                {"it": "Ne ho parlato con il mio capo.", "en": "I talked about it with my boss."},
            ],
            "commonMistakes": [
                {"wrong": "Vado ci domani.", "right": "Ci vado domani.", "why": "Ci goes before the conjugated verb, exactly like other object pronouns — not after it."},
                {"wrong": "Ho comprato cinque.", "right": "Ne ho comprate cinque.", "why": "A bare number needs ne to stand in for \"of them\" — Italian can't drop the quantity's referent the way casual English sometimes does."},
                {"wrong": "Ne ho comprato cinque mele. (both ne and the noun)", "right": "Ho comprato cinque mele. / Ne ho comprate cinque.", "why": "Ne replaces the noun — using both ne and the noun together in the same clause is redundant."},
            ],
        },
        "exercises": [
            {"id": "b1cn-fill", "type": "fill-blank", "title": "Ci or Ne?",
             "items": [
                {"id": "b1cn1", "prompt": "Vai in Italia quest'estate? Sì, ___ vado ad agosto.", "answers": [["ci"]], "explanation": "Replacing a place (in Italia) → ci.", "options": ["ci", "ne", "lo"]},
                {"id": "b1cn2", "prompt": "Quanti anni hai? ___ ho ventotto.", "answers": [["Ne"]], "explanation": "Replacing a quantity (anni) → ne.", "options": ["Ne", "Ci", "Li"]},
                {"id": "b1cn3", "prompt": "Pensi spesso al futuro? Sì, ___ penso ogni giorno.", "answers": [["ci"]], "explanation": "Pensare a → ci.", "options": ["ci", "ne", "gli"]},
             ]},
            {"id": "b1cn-mc", "type": "multiple-choice", "title": "Choose the Correct Particle",
             "items": [
                {"id": "b1cn4", "prompt": "\"Do you want some water?\" — \"Yes, I want a little [of it].\"", "options": ["Sì, ci voglio un po'.", "Sì, ne voglio un po'.", "Sì, lo voglio un po'."], "answerIndex": 1, "explanation": "A quantity of water → ne."},
             ]},
        ],
        "summary": [
            "Ci replaces a place or a topic introduced by a/in/su.",
            "Ne replaces a quantity or a topic introduced by di.",
            "Both go before the conjugated verb; ne with a number forces participle agreement in the passato prossimo.",
        ],
    },
]
