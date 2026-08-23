# -*- coding: utf-8 -*-
"""B2 — Upper Intermediate curriculum data."""

OVERVIEW = ("B2 opens the subjunctive mood — present and imperfect — alongside the "
            "trapassato prossimo, hypothetical sentences, reported speech, the passive voice, "
            "and relative pronouns. This is the level where Italian grammar stops being purely "
            "mechanical and starts requiring judgment about certainty, opinion and register.")

LESSONS = [
    {
        "id": "b2-trapassato-prossimo",
        "level": "B2", "unit": "1", "order": 1, "skill": "grammar", "strand": "past-tenses",
        "title": "Il Trapassato Prossimo",
        "subtitle": "The past before the past — what had already happened.",
        "objectives": [
            "Form the trapassato prossimo with the imperfetto of avere/essere + past participle",
            "Use it to mark an action that happened before another past action",
            "Apply the same auxiliary and agreement rules as the passato prossimo",
        ],
        "content": {
            "intro": "When you need to describe an event that had already finished before another past event, Italian reaches one step further back than the passato prossimo: the trapassato prossimo.",
            "explanation": "<p>Formed exactly like the passato prossimo, but with the auxiliary in the <strong>imperfetto</strong> instead of the present: <em>avevo parlato</em> (I had spoken), <em>ero partito</em> (I had left). Every rule you already know — which verbs take essere, when the participle agrees — carries over unchanged.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Trapassato prossimo — mangiare, partire</caption><thead><tr><th>Subject</th><th>mangiare</th><th>partire</th></tr></thead><tbody><tr><td>io</td><td>avevo mangiato</td><td>ero partito/a</td></tr><tr><td>tu</td><td>avevi mangiato</td><td>eri partito/a</td></tr><tr><td>lui/lei</td><td>aveva mangiato</td><td>era partito/a</td></tr><tr><td>noi</td><td>avevamo mangiato</td><td>eravamo partiti/e</td></tr><tr><td>voi</td><td>avevate mangiato</td><td>eravate partiti/e</td></tr><tr><td>loro</td><td>avevano mangiato</td><td>erano partiti/e</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Two past events, one earlier than the other", "body": "<p>The earlier event goes in the trapassato prossimo; the later one in the passato prossimo or imperfetto: <em>Quando sono arrivato, il treno era già partito.</em> (When I arrived, the train had already left.)</p>"},
                {"heading": "b) Common with già, non ancora, appena", "body": "<p><em>Non avevo mai visto un tramonto così.</em> (I had never seen a sunset like that.) <em>Aveva appena finito quando ho chiamato.</em> (He had just finished when I called.)</p>"},
            ],
            "examples": [
                {"it": "Quando sono arrivata, la lezione era già iniziata.", "en": "When I arrived, the lesson had already started."},
                {"it": "Non avevo mai mangiato il sushi prima di quel viaggio.", "en": "I had never eaten sushi before that trip."},
                {"it": "Avevamo già prenotato l'albergo quando hanno cancellato il volo.", "en": "We had already booked the hotel when they cancelled the flight."},
                {"it": "Era già partito quando ho chiamato a casa sua.", "en": "He had already left when I called his house."},
            ],
            "commonMistakes": [
                {"wrong": "Quando sono arrivata, la lezione è già iniziata.", "right": "Quando sono arrivata, la lezione era già iniziata.", "why": "The starting of the lesson happened before the arrival, so it needs the trapassato prossimo, not the passato prossimo."},
                {"wrong": "Avevo andato al mercato prima.", "right": "Ero andato al mercato prima.", "why": "Andare takes essere, and this doesn't change in the trapassato prossimo — only the auxiliary's tense changes, not which auxiliary is used."},
            ],
        },
        "exercises": [
            {"id": "b2tp-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b2tp1", "prompt": "Quando sono tornato a casa, mia madre ___ (già - cucinare) la cena.", "answers": [["aveva già cucinato"]], "explanation": "Trapassato prossimo for the earlier event.", "options": ["aveva già cucinato", "ha già cucinato", "cucinava già"]},
                {"id": "b2tp2", "prompt": "Non ___ (io - mai vedere) un film così bello prima.", "answers": [["avevo mai visto"]], "explanation": "Trapassato prossimo of vedere: avevo visto.", "options": ["avevo mai visto", "ho mai visto", "avevo mai vedeto"]},
             ]},
            {"id": "b2tp-mc", "type": "multiple-choice", "title": "Choose the Correct Tense",
             "items": [
                {"id": "b2tp3", "prompt": "\"When I woke up, everyone had already left.\"", "options": ["Tutti sono già partiti.", "Tutti erano già partiti.", "Tutti partivano già."], "answerIndex": 1, "explanation": "The leaving happened before the waking up — trapassato prossimo."},
             ]},
        ],
        "summary": [
            "Trapassato prossimo = imperfetto of avere/essere + past participle.",
            "Marks an action completed before another past action or reference point.",
            "Same auxiliary-choice and agreement rules as the passato prossimo — only the auxiliary's own tense changes.",
        ],
    },
    {
        "id": "b2-congiuntivo-presente",
        "level": "B2", "unit": "1", "order": 2, "skill": "grammar", "strand": "subjunctive",
        "title": "Il Congiuntivo Presente: Formazione",
        "subtitle": "The mood of opinion, doubt and wish — how to build it.",
        "objectives": [
            "Conjugate regular verbs in the congiuntivo presente",
            "Recognize that the tu/lui/lei forms are identical, requiring the subject pronoun for clarity",
            "Recognize common irregular subjunctive stems: essere, avere, andare, fare",
        ],
        "content": {
            "intro": "The subjunctive isn't a tense but a mood — it signals that what follows is an opinion, a wish, a doubt, or something not presented as objective fact, rather than a straightforward statement.",
            "explanation": "<p>Formed from the io form of the present indicative (drop the -o, add the subjunctive endings). Almost every verb that's irregular in the present indicative keeps that same irregular stem in the subjunctive. One quirk worth knowing early: <strong>io, tu, and lui/lei all share the identical ending</strong>, so the subject pronoun is often needed to avoid ambiguity, breaking Italian's usual pro-drop habit.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Congiuntivo presente — parlare, prendere, dormire</caption><thead><tr><th>Subject</th><th>parlare</th><th>prendere</th><th>dormire</th></tr></thead><tbody><tr><td>io</td><td>parli</td><td>prenda</td><td>dorma</td></tr><tr><td>tu</td><td>parli</td><td>prenda</td><td>dorma</td></tr><tr><td>lui/lei</td><td>parli</td><td>prenda</td><td>dorma</td></tr><tr><td>noi</td><td>parliamo</td><td>prendiamo</td><td>dormiamo</td></tr><tr><td>voi</td><td>parliate</td><td>prendiate</td><td>dormiate</td></tr><tr><td>loro</td><td>parlino</td><td>prendano</td><td>dormano</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Regular endings", "body": "<p>-are verbs: -i, -i, -i, -iamo, -iate, -ino. -ere/-ire verbs: -a, -a, -a, -iamo, -iate, -ano.</p>"},
                {"heading": "b) Common irregular stems", "body": "<p><em>essere → sia, sia, sia, siamo, siate, siano; avere → abbia...; andare → vada...; fare → faccia...; potere → possa...; dovere → debba...; volere → voglia...; venire → venga...</em></p>"},
                {"heading": "c) When it's triggered", "body": "<p>Almost always inside a subordinate clause introduced by <em>che</em>, after a main clause expressing opinion, doubt, emotion, or will — covered in detail in the next lesson.</p>"},
            ],
            "examples": [
                {"it": "Penso che lui abbia ragione.", "en": "I think he's right."},
                {"it": "Spero che tu stia bene.", "en": "I hope you're well."},
                {"it": "Credo che sia una buona idea.", "en": "I believe it's a good idea."},
                {"it": "È importante che voi arriviate in orario.", "en": "It's important that you arrive on time."},
                {"it": "Non credo che loro vengano stasera.", "en": "I don't think they're coming tonight."},
            ],
            "commonMistakes": [
                {"wrong": "Penso che lui ha ragione.", "right": "Penso che lui abbia ragione.", "why": "Penso che triggers the subjunctive, not the indicative ha."},
                {"wrong": "Spero che io sia felice. (ambiguous without context)", "right": "Spero di essere felice. (same subject, use di + infinitive instead)", "why": "When the subject of both verbs is the same, Italian prefers di + infinitive over che + subjunctive."},
                {"wrong": "Voglio che tu vai.", "right": "Voglio che tu vada.", "why": "Volere che triggers the subjunctive: vada, not the indicative vai."},
            ],
        },
        "exercises": [
            {"id": "b2cp-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b2cp1", "prompt": "Penso che lei ___ (avere) ragione.", "answers": [["abbia"]], "explanation": "Irregular subjunctive stem of avere: abbia.", "options": ["abbia", "ha", "avesse"]},
                {"id": "b2cp2", "prompt": "Spero che voi ___ (stare) bene.", "answers": [["stiate"]], "explanation": "Voi subjunctive of stare: stiate.", "options": ["stiate", "state", "stavate"]},
                {"id": "b2cp3", "prompt": "È necessario che tu ___ (venire) subito.", "answers": [["venga"]], "explanation": "Irregular subjunctive stem of venire: venga.", "options": ["venga", "vieni", "venisse"]},
             ]},
            {"id": "b2cp-mc", "type": "multiple-choice", "title": "Indicative or Subjunctive?",
             "items": [
                {"id": "b2cp4", "prompt": "\"I think it's raining.\"", "options": ["Penso che piove.", "Penso che piova.", "Penso piova."], "answerIndex": 1, "explanation": "Penso che always triggers the subjunctive."},
             ]},
        ],
        "summary": [
            "Congiuntivo presente: -are verbs → -i/-i/-i/-iamo/-iate/-ino; -ere/-ire verbs → -a/-a/-a/-iamo/-iate/-ano.",
            "Io, tu and lui/lei share an identical form — keep the subject pronoun for clarity.",
            "Most present-indicative irregular verbs keep the same irregular stem in the subjunctive.",
        ],
    },
    {
        "id": "b2-congiuntivo-uso",
        "level": "B2", "unit": "1", "order": 3, "skill": "grammar", "strand": "subjunctive",
        "title": "Il Congiuntivo dopo Opinione, Dubbio ed Emozione",
        "subtitle": "When exactly the subjunctive is required — and when it isn't.",
        "objectives": [
            "Identify the categories of main clause that trigger the subjunctive",
            "Distinguish opinion verbs (require subjunctive) from certainty verbs (require indicative)",
            "Use di + infinitive instead of che + subjunctive when the subject doesn't change",
        ],
        "content": {
            "intro": "The subjunctive isn't triggered by particular words alone, but by a whole category of meaning: whatever isn't presented as a plain, certain fact.",
            "explanation": "<p>Four broad triggers: <strong>opinion</strong> (penso che, credo che), <strong>doubt/uncertainty</strong> (dubito che, non sono sicuro che), <strong>emotion</strong> (sono felice che, mi dispiace che), and <strong>will/necessity</strong> (voglio che, è necessario che, bisogna che). By contrast, verbs of <strong>certainty</strong> — sapere che, essere sicuro che (in the affirmative), è vero che — take the indicative, because they present the information as an established fact, not an opinion.</p>",
            "rules": [
                {"heading": "a) Subjunctive triggers", "body": "<ul><li>Opinion: <em>penso, credo, immagino</em> + che</li><li>Doubt: <em>dubito, non sono sicuro/a</em> + che</li><li>Emotion: <em>sono contento/a, mi dispiace, ho paura</em> + che</li><li>Will/necessity: <em>voglio, spero, è importante, bisogna</em> + che</li></ul>"},
                {"heading": "b) Indicative instead", "body": "<p><em>So che hai ragione.</em> (I know you're right — a fact.) <em>È vero che piove.</em> (It's true that it's raining.) Negating a certainty verb (non sono sicuro che) flips it back to subjunctive, since it now expresses doubt.</p>"},
                {"heading": "c) Same subject → di + infinitive", "body": "<p>When both verbs share the same subject, Italian avoids che + subjunctive: <em>Spero di partire presto.</em> (I hope to leave early — not <em>Spero che io parta</em>.)</p>"},
            ],
            "examples": [
                {"it": "Dubito che lui arrivi in tempo.", "en": "I doubt he'll arrive on time."},
                {"it": "So che hai ragione.", "en": "I know you're right."},
                {"it": "Mi dispiace che tu non possa venire.", "en": "I'm sorry you can't come."},
                {"it": "È vero che i prezzi sono aumentati.", "en": "It's true that prices have gone up."},
                {"it": "Spero di finire in tempo.", "en": "I hope to finish in time. (same subject, di + infinitive)"},
            ],
            "commonMistakes": [
                {"wrong": "So che tu abbia ragione.", "right": "So che tu hai ragione.", "why": "Sapere che presents a known fact, so it takes the indicative, not the subjunctive."},
                {"wrong": "Sono sicuro che sia vero. (in the affirmative, presenting genuine certainty)", "right": "Sono sicuro che è vero.", "why": "Affirmative certainty verbs take the indicative; only their negation (non sono sicuro che) triggers the subjunctive."},
                {"wrong": "Spero che io possa venire.", "right": "Spero di poter venire.", "why": "With the same subject in both clauses, Italian prefers di + infinitive over che + subjunctive."},
            ],
        },
        "exercises": [
            {"id": "b2cu-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b2cu1", "prompt": "Dubito che loro ___ (potere) aiutarci.", "answers": [["possano"]], "explanation": "Dubito che triggers the subjunctive.", "options": ["possano", "possono", "potevano"]},
                {"id": "b2cu2", "prompt": "So che tu ___ (essere) molto occupato.", "answers": [["sei"]], "explanation": "Sapere che presents a fact — indicative.", "options": ["sei", "sia", "eri"]},
             ]},
            {"id": "b2cu-mc", "type": "multiple-choice", "title": "Which Trigger Requires the Subjunctive?",
             "items": [
                {"id": "b2cu3", "prompt": "Which verb requires the indicative, not the subjunctive?", "options": ["Dubito che...", "So che...", "Ho paura che..."], "answerIndex": 1, "explanation": "So che presents a fact, so it takes the indicative."},
             ]},
        ],
        "summary": [
            "Opinion, doubt, emotion and will/necessity trigger the subjunctive; certainty (sapere che, è vero che) takes the indicative.",
            "Negating a certainty verb flips it to the subjunctive, since it now expresses doubt.",
            "Same subject in both clauses → prefer di + infinitive over che + subjunctive.",
        ],
    },
    {
        "id": "b2-congiuntivo-imperfetto",
        "level": "B2", "unit": "1", "order": 4, "skill": "grammar", "strand": "subjunctive",
        "title": "Il Congiuntivo Imperfetto",
        "subtitle": "The subjunctive's past tense, used after a past-tense main clause.",
        "objectives": [
            "Conjugate regular verbs in the congiuntivo imperfetto",
            "Apply the sequence-of-tenses rule with a past-tense main verb",
            "Recognize essere's fully irregular imperfect subjunctive",
        ],
        "content": {
            "intro": "When the main clause is in a past tense, the subjunctive in the subordinate clause shifts back too — into the congiuntivo imperfetto.",
            "explanation": "<p>Formed regularly for almost every verb, including most that are irregular elsewhere: drop -re from the infinitive, add the endings. Only <strong>essere</strong> has a genuinely irregular stem (fossi, fossi, fosse...).</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Congiuntivo imperfetto — parlare, avere, essere</caption><thead><tr><th>Subject</th><th>parlare</th><th>avere</th><th>essere</th></tr></thead><tbody><tr><td>io</td><td>parlassi</td><td>avessi</td><td>fossi</td></tr><tr><td>tu</td><td>parlassi</td><td>avessi</td><td>fossi</td></tr><tr><td>lui/lei</td><td>parlasse</td><td>avesse</td><td>fosse</td></tr><tr><td>noi</td><td>parlassimo</td><td>avessimo</td><td>fossimo</td></tr><tr><td>voi</td><td>parlaste</td><td>aveste</td><td>foste</td></tr><tr><td>loro</td><td>parlassero</td><td>avessero</td><td>fossero</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Regular endings", "body": "<p>-assi, -assi, -asse, -assimo, -aste, -assero (-are verbs); -essi, -essi, -esse, -essimo, -este, -essero (-ere/-ire verbs).</p>"},
                {"heading": "b) Sequence of tenses (simplified)", "body": "<p>Main clause in the present/future → subordinate in the congiuntivo presente. Main clause in a past tense or the conditional → subordinate in the congiuntivo imperfetto: <em>Pensavo che avesse ragione.</em> (I thought he was right.)</p>"},
            ],
            "examples": [
                {"it": "Pensavo che fossi già partito.", "en": "I thought you had already left."},
                {"it": "Speravo che venissi alla festa.", "en": "I was hoping you'd come to the party."},
                {"it": "Non credevo che fosse così difficile.", "en": "I didn't think it would be so difficult."},
                {"it": "Volevo che tu sapessi la verità.", "en": "I wanted you to know the truth."},
                {"it": "Era importante che tutti capissero.", "en": "It was important that everyone understood."},
            ],
            "commonMistakes": [
                {"wrong": "Pensavo che lui abbia ragione.", "right": "Pensavo che lui avesse ragione.", "why": "A past-tense main verb (pensavo) requires the congiuntivo imperfetto, not the congiuntivo presente."},
                {"wrong": "Volevo che tu sapevi.", "right": "Volevo che tu sapessi.", "why": "Volere che always requires the subjunctive, regardless of tense — here, the imperfect subjunctive."},
            ],
        },
        "exercises": [
            {"id": "b2ci-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b2ci1", "prompt": "Speravo che tu ___ (venire) alla cena.", "answers": [["venissi"]], "explanation": "Regular congiuntivo imperfetto of venire.", "options": ["venissi", "venga", "venivi"]},
                {"id": "b2ci2", "prompt": "Non pensavo che ___ (essere) così tardi.", "answers": [["fosse"]], "explanation": "Essere's irregular imperfect subjunctive: fosse.", "options": ["fosse", "sia", "era"]},
             ]},
            {"id": "b2ci-mc", "type": "multiple-choice", "title": "Choose the Correct Tense",
             "items": [
                {"id": "b2ci3", "prompt": "\"I wanted you to understand\" — Volevo che tu ___", "options": ["capisca", "capissi", "capivi"], "answerIndex": 1, "explanation": "Past main clause → imperfect subjunctive."},
             ]},
        ],
        "summary": [
            "Congiuntivo imperfetto: -assi/-assi/-asse/-assimo/-aste/-assero, or -essi/-essi/-esse/-essimo/-este/-essero.",
            "Only essere is irregular: fossi, fossi, fosse, fossimo, foste, fossero.",
            "A past-tense (or conditional) main clause requires the imperfect subjunctive in the subordinate clause.",
        ],
    },
    {
        "id": "b2-periodo-ipotetico",
        "level": "B2", "unit": "1", "order": 5, "skill": "grammar", "strand": "conditionals",
        "title": "Il Periodo Ipotetico (I e II tipo)",
        "subtitle": "Real and possible/unreal \"if\" sentences.",
        "objectives": [
            "Form the first type (real, likely) hypothetical sentence",
            "Form the second type (possible but unlikely, or contrary-to-fact present) hypothetical sentence",
            "Match the correct tense/mood in the se-clause and the main clause",
        ],
        "content": {
            "intro": "Italian hypothetical sentences are built from a matched pair of tenses/moods in the se-clause and the main clause — get the pairing right, and the whole sentence falls into place.",
            "explanation": "<p>The <strong>first type</strong> describes a real or likely condition: se + present indicative, main clause in the present or future. The <strong>second type</strong> describes something possible but unlikely, or contrary to fact right now: se + congiuntivo imperfetto, main clause in the present conditional. (The third type, for the impossible past, comes at C1.)</p>",
            "rules": [
                {"heading": "a) First type — real/likely", "body": "<p>Se + presente indicativo, presente/futuro: <em>Se piove, resto a casa. / Se piove, resterò a casa.</em> (If it rains, I'll stay home.)</p>"},
                {"heading": "b) Second type — possible/unreal", "body": "<p>Se + congiuntivo imperfetto, condizionale presente: <em>Se avessi più tempo, viaggerei di più.</em> (If I had more time, I'd travel more — implying I don't, right now.)</p>"},
                {"heading": "c) Order can flip", "body": "<p>The main clause can come first: <em>Viaggerei di più se avessi più tempo.</em> — same meaning, just reordered.</p>"},
            ],
            "examples": [
                {"it": "Se ho tempo stasera, ti chiamo.", "en": "If I have time tonight, I'll call you."},
                {"it": "Se studi di più, passerai l'esame.", "en": "If you study more, you'll pass the exam."},
                {"it": "Se fossi in te, non lo farei.", "en": "If I were you, I wouldn't do it."},
                {"it": "Se avessimo una macchina, andremmo al mare più spesso.", "en": "If we had a car, we'd go to the seaside more often."},
                {"it": "Comprerei quella casa se costasse meno.", "en": "I'd buy that house if it cost less."},
            ],
            "commonMistakes": [
                {"wrong": "Se avrei più tempo, viaggerei di più.", "right": "Se avessi più tempo, viaggerei di più.", "why": "The se-clause of the second type needs the congiuntivo imperfetto (avessi), never the conditional — the conditional only goes in the main clause."},
                {"wrong": "Se piovesse, resto a casa. (mixing types)", "right": "Se piove, resto a casa. / Se piovesse, resterei a casa.", "why": "The se-clause tense/mood must match the main clause type — congiuntivo imperfetto pairs with the conditional, not the present indicative."},
            ],
        },
        "exercises": [
            {"id": "b2pi-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b2pi1", "prompt": "Se ___ (io - avere) più soldi, comprerei una macchina nuova.", "answers": [["avessi"]], "explanation": "Second type: se + congiuntivo imperfetto.", "options": ["avessi", "ho", "avrei"]},
                {"id": "b2pi2", "prompt": "Se ___ (tu - studiare) di più, prenderai un voto migliore.", "answers": [["studi"]], "explanation": "First type: se + presente indicativo.", "options": ["studi", "studiassi", "studieresti"]},
             ]},
            {"id": "b2pi-mc", "type": "multiple-choice", "title": "Choose the Correct Sentence",
             "items": [
                {"id": "b2pi3", "prompt": "\"If I were rich, I would travel the world.\"", "options": ["Se sono ricco, viaggerei per il mondo.", "Se fossi ricco, viaggerei per il mondo.", "Se sarei ricco, viaggerei per il mondo."], "answerIndex": 1, "explanation": "Unreal present condition needs se + congiuntivo imperfetto, conditional in the main clause."},
             ]},
            {"id": "b2pi-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "b2pi4", "incorrect": "Se avrei tempo, verrei con te.", "answer": ["Se avessi tempo, verrei con te."], "explanation": "The se-clause of the second type needs the imperfect subjunctive, not the conditional."},
             ]},
        ],
        "summary": [
            "First type (real/likely): se + presente indicativo, presente/futuro.",
            "Second type (unreal/unlikely, present): se + congiuntivo imperfetto, condizionale presente.",
            "The conditional never appears in the se-clause itself, only in the main clause.",
        ],
    },
    {
        "id": "b2-discorso-indiretto",
        "level": "B2", "unit": "1", "order": 6, "skill": "grammar", "strand": "reported-speech",
        "title": "Il Discorso Indiretto",
        "subtitle": "Reporting what someone said, and how the tenses shift back.",
        "objectives": [
            "Convert direct speech into reported speech with dire che",
            "Shift tenses back correctly when the reporting verb is in the past",
            "Adjust pronouns, possessives and time expressions appropriately",
        ],
        "content": {
            "intro": "Reporting what someone said requires more than just adding \"that\" — pronouns, tenses and time expressions often all need to shift to fit the new perspective.",
            "explanation": "<p>When the reporting verb (<em>dire, chiedere, rispondere</em>) is in the present, little changes besides pronouns. When it's in the <strong>past</strong> — by far the more common case in real narration — every tense in the reported clause shifts one step back: present → imperfetto, passato prossimo → trapassato prossimo, futuro → condizionale passato (a form met at C1; condizionale presente is an acceptable simplification at this level).</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Tense shift after a past reporting verb (ha detto che...)</caption><thead><tr><th>Direct speech</th><th>Reported speech</th></tr></thead><tbody><tr><td>presente</td><td>imperfetto</td></tr><tr><td>passato prossimo</td><td>trapassato prossimo</td></tr><tr><td>futuro semplice</td><td>condizionale (presente/passato)</td></tr><tr><td>imperativo</td><td>di + infinito</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Also shift: pronouns, possessives, time words", "body": "<ul><li><em>domani → il giorno dopo; oggi → quel giorno; ieri → il giorno prima</em></li><li><em>qui → lì; questo → quello</em></li><li>Subject/possessive pronouns adjust to the new speaker's perspective</li></ul>"},
                {"heading": "b) Imperative becomes di + infinitive", "body": "<p>Direct: <em>\"Chiudi la porta!\"</em> Reported: <em>Mi ha detto di chiudere la porta.</em></p>"},
            ],
            "examples": [
                {"it": "Marco ha detto: \"Sono stanco.\" → Marco ha detto che era stanco.", "en": "Marco said: \"I'm tired.\" → Marco said he was tired."},
                {"it": "Ha detto: \"Verrò domani.\" → Ha detto che sarebbe venuto il giorno dopo.", "en": "He said: \"I'll come tomorrow.\" → He said he would come the next day."},
                {"it": "Mi ha chiesto: \"Hai finito?\" → Mi ha chiesto se avevo finito.", "en": "She asked me: \"Have you finished?\" → She asked me if I had finished."},
                {"it": "\"Aspetta qui!\" → Mi ha detto di aspettare lì.", "en": "\"Wait here!\" → She told me to wait there."},
            ],
            "commonMistakes": [
                {"wrong": "Ha detto che è stanco. (reporting from a past viewpoint)", "right": "Ha detto che era stanco.", "why": "A past reporting verb (ha detto) shifts the present tense of direct speech back to the imperfetto."},
                {"wrong": "Mi ha detto \"chiudi la porta\" as reported speech kept verbatim", "right": "Mi ha detto di chiudere la porta.", "why": "The imperative in direct speech becomes di + infinitive when reported, never kept as a literal imperative."},
            ],
        },
        "exercises": [
            {"id": "b2di-fill", "type": "fill-blank", "title": "Convert to Reported Speech",
             "items": [
                {"id": "b2di1", "prompt": "Ha detto: \"Sto lavorando.\" → Ha detto che ___.", "answers": [["stava lavorando"]], "explanation": "Present → imperfetto after a past reporting verb.", "options": ["stava lavorando", "sta lavorando", "stia lavorando"]},
                {"id": "b2di2", "prompt": "Ha detto: \"Ho finito il lavoro.\" → Ha detto che ___.", "answers": [["aveva finito il lavoro"]], "explanation": "Passato prossimo → trapassato prossimo.", "options": ["aveva finito il lavoro", "ha finito il lavoro", "finiva il lavoro"]},
             ]},
            {"id": "b2di-mc", "type": "multiple-choice", "title": "Choose the Correct Reported Form",
             "items": [
                {"id": "b2di3", "prompt": "Direct: \"Vengo domani.\" Reported (ha detto che...):", "options": ["sarebbe venuto il giorno dopo", "viene domani", "veniva domani"], "answerIndex": 0, "explanation": "Futuro shifts to the conditional, and domani shifts to il giorno dopo."},
             ]},
        ],
        "summary": [
            "A past reporting verb shifts tenses back: presente→imperfetto, passato prossimo→trapassato prossimo, futuro→condizionale.",
            "Pronouns, possessives and time expressions (domani→il giorno dopo) shift to the new perspective too.",
            "A reported imperative becomes di + infinitive.",
        ],
    },
    {
        "id": "b2-forma-passiva",
        "level": "B2", "unit": "1", "order": 7, "skill": "grammar", "strand": "passive",
        "title": "La Forma Passiva",
        "subtitle": "When the object of the action becomes the subject of the sentence.",
        "objectives": [
            "Form the passive voice with essere + past participle",
            "Introduce the agent with da",
            "Recognize venire as an alternative passive auxiliary in simple tenses",
        ],
        "content": {
            "intro": "The passive voice shifts the focus from who does an action to what happens to something or someone — common in news, formal writing, and whenever the agent is unknown or unimportant.",
            "explanation": "<p>Built with <strong>essere</strong> (conjugated in whatever tense the sentence needs) + the past participle, which agrees with the subject exactly like any essere + participle structure. The agent, when mentioned, is introduced by <strong>da</strong>. In simple tenses (present, imperfetto, futuro), <strong>venire</strong> can replace essere as a slightly more literary/formal alternative — never in compound tenses.</p>",
            "rules": [
                {"heading": "a) Formation", "body": "<p>essere (in the needed tense) + past participle (agreeing with the subject) [+ da + agent]: <em>La lettera è scritta da Marco.</em> (The letter is written by Marco.)</p>"},
                {"heading": "b) Across tenses", "body": "<ul><li>Present: <em>Il pane è fatto ogni mattina.</em></li><li>Passato prossimo: <em>La casa è stata costruita nel 1990.</em> (note: essere itself needs a participle here too, stata)</li><li>Futuro: <em>Il progetto sarà completato entro giugno.</em></li></ul>"},
                {"heading": "c) Venire as an alternative (simple tenses only)", "body": "<p><em>Il museo viene visitato da migliaia di turisti.</em> = <em>Il museo è visitato da migliaia di turisti.</em> — same meaning, venire is common in more formal/written registers.</p>"},
            ],
            "examples": [
                {"it": "Il libro è stato scritto da un autore famoso.", "en": "The book was written by a famous author."},
                {"it": "Le decisioni vengono prese dal direttore.", "en": "The decisions are made by the director."},
                {"it": "Questo edificio fu costruito nel Seicento.", "en": "This building was built in the 1600s."},
                {"it": "I risultati saranno annunciati domani.", "en": "The results will be announced tomorrow."},
            ],
            "commonMistakes": [
                {"wrong": "La lettera è scrivere da Marco.", "right": "La lettera è scritta da Marco.", "why": "The passive needs the past participle, not the infinitive, after essere."},
                {"wrong": "La casa è stato costruita nel 1990.", "right": "La casa è stata costruita nel 1990.", "why": "Both participles must agree with the feminine subject la casa: stata and costruita."},
                {"wrong": "Il libro è scritto per Marco. (agent)", "right": "Il libro è scritto da Marco.", "why": "The agent in a passive sentence is introduced by da, not per."},
            ],
        },
        "exercises": [
            {"id": "b2fp-fill", "type": "fill-blank", "title": "Turn into the Passive",
             "items": [
                {"id": "b2fp1", "prompt": "Il pane ___ (fare) ogni mattina dal fornaio.", "answers": [["è fatto"]], "explanation": "Present passive: essere + participle.", "options": ["è fatto", "fa", "ha fatto"]},
                {"id": "b2fp2", "prompt": "Il quadro ___ (dipingere) da un artista famoso nel 1800.", "answers": [["fu dipinto"]], "explanation": "Passive in a past narrative tense: essere (here, the passato remoto fu, common in this context) + participle.", "options": ["fu dipinto", "ha dipinto", "dipinge"]},
             ]},
            {"id": "b2fp-mc", "type": "multiple-choice", "title": "Choose the Correct Passive Form",
             "items": [
                {"id": "b2fp3", "prompt": "\"The results will be published tomorrow.\"", "options": ["I risultati pubblicheranno domani.", "I risultati saranno pubblicati domani.", "I risultati sono pubblicare domani."], "answerIndex": 1, "explanation": "Future passive: sarà/saranno + past participle."},
             ]},
        ],
        "summary": [
            "Passive voice: essere (in any tense) + past participle, agreeing with the subject.",
            "The agent, if stated, is introduced with da.",
            "Venire can replace essere in simple tenses for a more formal register, but never in compound tenses.",
        ],
    },
    {
        "id": "b2-pronomi-relativi",
        "level": "B2", "unit": "1", "order": 8, "skill": "grammar", "strand": "relative-clauses",
        "title": "I Pronomi Relativi",
        "subtitle": "Che, cui, il quale — linking two ideas about the same noun.",
        "objectives": [
            "Use che as the all-purpose relative pronoun for subject and direct object",
            "Use cui after a preposition",
            "Use il quale/la quale as a more formal, gender-marked alternative to cui",
        ],
        "content": {
            "intro": "Relative pronouns let you fold a second sentence about the same noun directly into the first, instead of starting a new one — the backbone of fluent, connected Italian.",
            "explanation": "<p><strong>Che</strong> is invariable and covers both subject and direct object relative clauses — by far the most common case. As soon as a preposition is involved, che is replaced by <strong>cui</strong> (also invariable), with the preposition placed directly before it. <strong>Il quale/la quale/i quali/le quali</strong> is a more formal alternative to cui, useful mainly when cui's lack of gender/number would otherwise be ambiguous.</p>",
            "rules": [
                {"heading": "a) Che — subject or direct object", "body": "<p><em>La ragazza che parla è mia sorella.</em> (subject) <em>Il libro che ho letto è bellissimo.</em> (direct object)</p>"},
                {"heading": "b) Cui — after a preposition", "body": "<p><em>La persona a cui ho scritto</em> (the person I wrote to) <em>Il paese in cui sono nato</em> (the country I was born in) <em>di cui</em> parlava = what he was talking about</p>"},
                {"heading": "c) Cui with an article = whose", "body": "<p><em>il cui, la cui, i cui, le cui</em> (agreeing with the noun that follows, not with the owner): <em>Lo scrittore il cui libro ho letto.</em> (The writer whose book I read.)</p>"},
            ],
            "examples": [
                {"it": "Il film che abbiamo visto ieri era fantastico.", "en": "The film we watched yesterday was fantastic."},
                {"it": "La città in cui sono cresciuto è piccola.", "en": "The city I grew up in is small."},
                {"it": "Ecco la persona di cui ti parlavo.", "en": "Here's the person I was telling you about."},
                {"it": "L'uomo con cui lavoro è molto simpatico.", "en": "The man I work with is very nice."},
                {"it": "Lo scrittore il cui romanzo ha vinto il premio è italiano.", "en": "The writer whose novel won the prize is Italian."},
            ],
            "commonMistakes": [
                {"wrong": "La persona a che ho scritto.", "right": "La persona a cui ho scritto.", "why": "After a preposition, che is replaced by cui — che alone never follows a preposition."},
                {"wrong": "Il cui il libro (word order)", "right": "il cui libro", "why": "Cui + article goes directly before the noun it modifies, with no extra article repeated."},
            ],
        },
        "exercises": [
            {"id": "b2pr-fill", "type": "fill-blank", "title": "Che or Cui?",
             "items": [
                {"id": "b2pr1", "prompt": "Il libro ___ ho comprato è molto interessante.", "answers": [["che"]], "explanation": "Direct object, no preposition → che.", "options": ["che", "cui", "il quale"]},
                {"id": "b2pr2", "prompt": "La ragazza a ___ ho scritto è mia amica.", "answers": [["cui"]], "explanation": "After the preposition a → cui.", "options": ["cui", "che", "quale"]},
             ]},
            {"id": "b2pr-mc", "type": "multiple-choice", "title": "Choose the Correct Pronoun",
             "items": [
                {"id": "b2pr3", "prompt": "\"The house I was born in\"", "options": ["La casa che sono nato.", "La casa in cui sono nato.", "La casa cui sono nato."], "answerIndex": 1, "explanation": "The preposition in must be kept, followed by cui."},
             ]},
        ],
        "summary": [
            "Che covers subject and direct object relative clauses — the default, most common choice.",
            "Cui is used directly after any preposition, and is invariable.",
            "Il/la/i/le cui = whose, agreeing with the noun possessed, not the owner.",
        ],
    },
    {
        "id": "b2-verbi-preposizione-infinito",
        "level": "B2", "unit": "1", "order": 9, "skill": "grammar", "strand": "verb-patterns",
        "title": "Verbi Seguiti da Preposizione + Infinito",
        "subtitle": "Which verbs need a, which need di, and which need nothing at all before an infinitive.",
        "objectives": [
            "Group common verbs by whether they take a, di, or no preposition before an infinitive",
            "Apply the pattern correctly in context",
            "Recognize a handful of high-frequency exceptions worth memorizing individually",
        ],
        "content": {
            "intro": "There's no single rule for predicting which preposition (if any) connects a verb to a following infinitive — but the most common verbs sort into learnable groups.",
            "explanation": "<p>Modal verbs (dovere, potere, volere) and a handful of others take the bare infinitive with no preposition, as you already know. Many verbs of movement and beginning take <strong>a</strong>; many verbs of stopping, deciding, and trying take <strong>di</strong>. There's real overlap and no fully reliable shortcut — building intuition through exposure is the realistic goal at this stage.</p>",
            "rules": [
                {"heading": "a) No preposition", "body": "<p><em>dovere, potere, volere, sapere, piacere, preferire, amare, desiderare</em>: <em>Preferisco restare a casa.</em></p>"},
                {"heading": "b) + a", "body": "<p><em>andare a, venire a, cominciare a, iniziare a, imparare a, continuare a, riuscire a, aiutare a</em>: <em>Ho imparato a nuotare da bambino.</em></p>"},
                {"heading": "c) + di", "body": "<p><em>finire di, smettere di, decidere di, cercare di, dimenticare di, avere bisogno di, avere voglia di, chiedere di, promettere di</em>: <em>Ho deciso di cambiare lavoro.</em></p>"},
            ],
            "examples": [
                {"it": "Ho smesso di fumare due anni fa.", "en": "I quit smoking two years ago."},
                {"it": "Sto imparando a suonare la chitarra.", "en": "I'm learning to play the guitar."},
                {"it": "Cerco di mangiare più sano.", "en": "I'm trying to eat healthier."},
                {"it": "Continua a piovere da stamattina.", "en": "It's kept raining since this morning."},
                {"it": "Ho bisogno di riposare un po'.", "en": "I need to rest a bit."},
            ],
            "commonMistakes": [
                {"wrong": "Ho smesso fumare.", "right": "Ho smesso di fumare.", "why": "Smettere requires di before an infinitive — it's never dropped."},
                {"wrong": "Ho imparato di nuotare.", "right": "Ho imparato a nuotare.", "why": "Imparare takes a, not di, before an infinitive."},
                {"wrong": "Voglio di partire.", "right": "Voglio partire.", "why": "Volere, a modal verb, takes no preposition at all before an infinitive."},
            ],
        },
        "exercises": [
            {"id": "b2vp-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "b2vp1", "prompt": "Ho deciso ___ trasferirmi a Milano.", "answers": [["di"]], "explanation": "Decidere takes di.", "options": ["di", "a", "(nothing)"]},
                {"id": "b2vp2", "prompt": "Ho iniziato ___ studiare il francese.", "answers": [["a"]], "explanation": "Iniziare takes a.", "options": ["a", "di", "(nothing)"]},
                {"id": "b2vp3", "prompt": "Non riesco ___ dormire stanotte.", "answers": [["a"]], "explanation": "Riuscire takes a.", "options": ["a", "di", "(nothing)"]},
             ]},
            {"id": "b2vp-mc", "type": "multiple-choice", "title": "Choose the Correct Preposition",
             "items": [
                {"id": "b2vp4", "prompt": "\"I need to talk to you.\"", "options": ["Ho bisogno a parlarti.", "Ho bisogno di parlarti.", "Ho bisogno parlarti."], "answerIndex": 1, "explanation": "Avere bisogno takes di before an infinitive."},
             ]},
        ],
        "summary": [
            "Modal-type verbs take no preposition; many motion/beginning verbs take a; many stopping/deciding verbs take di.",
            "There's real overlap — treat each verb's pattern as a fact to learn alongside its meaning.",
            "The preposition, once required, is never optional or interchangeable.",
        ],
    },
]
