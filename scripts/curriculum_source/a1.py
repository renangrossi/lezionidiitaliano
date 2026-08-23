# -*- coding: utf-8 -*-
"""A1 — Beginner curriculum data. See curriculum/SCHEMA.md for the JSON
shape this compiles to (scripts/generate_curriculum.py does the compiling).
Written as Python rather than hand-escaped JSON so prose containing
apostrophes (c'è, dell'acqua, l'amico...) reads naturally."""

OVERVIEW = ("A1 starts from zero: the alphabet and sounds, greetings, the essential verbs "
            "essere and avere, gender and articles, and the present tense of regular verbs. "
            "By the end you can introduce yourself, describe your family and daily routine, "
            "and ask simple questions — the base everything else in this course builds on.")

LESSONS = [
    {
        "id": "a1-saluti-e-presentazioni",
        "level": "A1", "unit": "1", "order": 1, "skill": "functional", "strand": "greetings",
        "title": "Saluti e Presentazioni",
        "subtitle": "Greet people and introduce yourself — and know when to use tu or Lei.",
        "objectives": [
            "Greet someone and say goodbye at any time of day",
            "Introduce yourself and ask someone's name",
            "Choose between the informal tu and the formal Lei",
        ],
        "content": {
            "intro": "Every conversation in Italian starts with a greeting — and the greeting you choose already signals how formal the conversation will be.",
            "explanation": "<p>Italian has time-of-day greetings (<em>buongiorno</em>, <em>buonasera</em>) that work in both formal and informal situations, and an all-purpose informal <em>ciao</em> used only with people you're on first-name terms with — friends, family, children, and often colleagues your own age. <em>Salve</em> sits in between: a polite, neutral greeting safe for someone you don't know well.</p><p>Italian also has two ways to say &ldquo;you&rdquo;: <strong>tu</strong> (informal, singular) and <strong>Lei</strong> (formal, singular — note the capital L, and that it takes third-person verb forms, the same as <em>lui/lei</em>). Use <em>Lei</em> with strangers, older people, doctors, officials, and anyone in a professional context until they invite you to use <em>tu</em> (<em>diamoci del tu</em>, &ldquo;let's use tu with each other&rdquo;).</p>",
            "rules": [
                {"heading": "a) Greetings by time and formality", "body": "<ul><li><strong>Buongiorno</strong> — good morning / good day (formal or informal, until mid-afternoon)</li><li><strong>Buonasera</strong> — good evening (formal or informal, from mid-afternoon)</li><li><strong>Buonanotte</strong> — good night (only when leaving/going to bed, never as a greeting on arrival)</li><li><strong>Ciao</strong> — hi / bye (informal only, any time)</li><li><strong>Salve</strong> — hello (neutral, safe with strangers)</li><li><strong>Arrivederci</strong> — goodbye (formal-safe); <strong>ArrivederLa</strong> is the fully formal version</li></ul>"},
                {"heading": "b) Asking and giving names", "body": "<ul><li>Informal: <em>Come ti chiami?</em> (What's your name?) &rarr; <em>Mi chiamo Marco.</em></li><li>Formal: <em>Come si chiama?</em> &rarr; <em>Mi chiamo Marco.</em> (the answer doesn't change)</li><li><em>Piacere</em> — &ldquo;pleasure [to meet you]&rdquo;, said by both people when introduced</li></ul>"},
                {"heading": "c) Tu vs. Lei", "body": "<ul><li><strong>Tu</strong>: friends, family, children, peers &mdash; <em>Tu come stai?</em></li><li><strong>Lei</strong>: strangers, elders, professional settings &mdash; <em>Lei come sta?</em></li><li>Lei uses third-person singular verb forms, the same ones used for <em>lui/lei</em> (he/she)</li></ul>"},
            ],
            "examples": [
                {"it": "Buongiorno, come sta?", "en": "Good morning, how are you? (formal)"},
                {"it": "Ciao! Come stai?", "en": "Hi! How are you? (informal)"},
                {"it": "Mi chiamo Giulia. E tu, come ti chiami?", "en": "My name is Giulia. And you, what's your name?"},
                {"it": "Piacere di conoscerla.", "en": "Pleasure to meet you. (formal)"},
                {"it": "Sto bene, grazie. E Lei?", "en": "I'm well, thank you. And you? (formal)"},
                {"it": "Arrivederci, a presto!", "en": "Goodbye, see you soon!"},
            ],
            "commonMistakes": [
                {"wrong": "Ciao, come sta?", "right": "Ciao, come stai? / Buongiorno, come sta?", "why": "Ciao is informal, so it pairs with the informal stai — mixing ciao with the formal sta is inconsistent."},
                {"wrong": "Buonanotte! (as a hello when arriving)", "right": "Buonasera! (as a hello when arriving)", "why": "Buonanotte is only for leaving or going to bed, never for greeting someone on arrival."},
                {"wrong": "Come ti chiama?", "right": "Come ti chiami? / Come si chiama?", "why": "Ti chiami is the tu-form (2nd person: you call yourself); ti chiama mixes tu with a 3rd-person verb ending."},
            ],
        },
        "exercises": [
            {"id": "a1sp-mc", "type": "multiple-choice", "title": "Choose the Right Greeting",
             "items": [
                {"id": "a1sp1", "prompt": "You meet your boss for the first time this morning. What do you say?", "options": ["Ciao!", "Buongiorno!", "Buonanotte!"], "answerIndex": 1, "explanation": "Buongiorno is the safe, formal-appropriate morning greeting for someone you don't know well."},
                {"id": "a1sp2", "prompt": "You're leaving your friend's house late at night.", "options": ["Buongiorno", "Ciao, buonanotte!", "Buonasera"], "answerIndex": 1, "explanation": "Buonanotte is used when leaving or going to bed, paired here with the informal ciao since it's a friend."},
                {"id": "a1sp3", "prompt": "Which pronoun goes with a stranger you're asking for directions?", "options": ["tu", "Lei", "voi"], "answerIndex": 1, "explanation": "Lei is the formal singular \"you\", the safe default with strangers."},
             ]},
            {"id": "a1sp-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "instructions": "Complete each exchange.",
             "items": [
                {"id": "a1sp4", "prompt": "— Come ti ___? — Mi chiamo Anna.", "answers": [["chiami"]], "explanation": "Chiami is the informal tu-form of chiamarsi.", "options": ["chiami", "chiama", "chiamo"]},
                {"id": "a1sp5", "prompt": "— Buonasera, come ___? — Sto bene, grazie.", "answers": [["sta"]], "explanation": "Sta is the formal Lei-form of stare, matching buonasera used formally here.", "options": ["sta", "stai", "sto"]},
             ]},
            {"id": "a1sp-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a1sp6", "incorrect": "Ciao, come sta?", "answer": ["Ciao, come stai?"], "explanation": "Ciao is informal, so it should pair with the informal stai, not the formal sta."},
                {"id": "a1sp7", "incorrect": "Buonanotte! (greeting a colleague who just arrived)", "answer": ["Buongiorno!", "Buonasera!"], "explanation": "Buonanotte is never used to greet someone arriving — only when leaving or going to sleep."},
             ]},
        ],
        "summary": [
            "Buongiorno/buonasera work formally or informally; ciao is informal-only; buonanotte is for leaving, not arriving.",
            "Come ti chiami? (informal) vs. Come si chiama? (formal) — the answer, mi chiamo..., stays the same.",
            "Use tu with people you're close to; use Lei with strangers, elders and professional contacts.",
        ],
    },
    {
        "id": "a1-alfabeto-e-pronuncia",
        "level": "A1", "unit": "1", "order": 2, "skill": "pronunciation", "strand": "phonetics",
        "title": "L'Alfabeto e la Pronuncia",
        "subtitle": "Italian spelling is famously regular — learn the handful of rules that make it so.",
        "objectives": [
            "Say the 21 letters of the Italian alphabet",
            "Pronounce c/g before different vowels correctly",
            "Recognize gn, gl and sc as single sounds",
        ],
        "content": {
            "intro": "Italian is written almost exactly as it sounds. Once you know a small set of spelling rules, you can read any Italian word aloud correctly — even one you've never seen.",
            "explanation": "<p>The Italian alphabet has 21 native letters (no j, k, w, x, y — these appear only in loanwords like <em>jeans</em> or <em>whisky</em>). Every vowel (a, e, i, o, u) is always pronounced clearly and the same way — Italian has no silent vowels and no vowel reduction like English &ldquo;the&rdquo; becoming &ldquo;thuh&rdquo;.</p><p>The trickiest part for English speakers is that <strong>c</strong> and <strong>g</strong> change sound depending on the letter that follows them, and a few two/three-letter combinations represent a single sound.</p>",
            "rules": [
                {"heading": "a) C and G before vowels", "body": "<ul><li><strong>ca, co, cu</strong> = hard \"k\" sound &mdash; <em>casa, cosa, cubo</em></li><li><strong>ce, ci</strong> = soft \"ch\" sound (like English \"cheese\") &mdash; <em>cena, cinema</em></li><li><strong>ga, go, gu</strong> = hard \"g\" sound &mdash; <em>gatto, gonna, guanto</em></li><li><strong>ge, gi</strong> = soft \"j\" sound (like English \"jet\") &mdash; <em>gelato, giorno</em></li></ul>"},
                {"heading": "b) Keeping the hard/soft sound before e or i", "body": "<ul><li>Add an <strong>h</strong> to keep the hard sound before e/i: <strong>che, chi</strong> = \"k\" (<em>chi</em>, \"who\"); <strong>ghe, ghi</strong> = hard \"g\" (<em>spaghetti</em>)</li><li>Add an <strong>i</strong> to keep the soft sound before a/o/u: <strong>cia, cio, ciu</strong> = \"ch\" (<em>ciao</em>); <strong>gia, gio, giu</strong> = \"j\" (<em>giorno</em>) — the i is silent here, just a spelling signal</li></ul>"},
                {"heading": "c) Special combinations", "body": "<ul><li><strong>gn</strong> = \"ny\" as in canyon &mdash; <em>gnocchi, bagno</em></li><li><strong>gli</strong> = \"ly\" as in million &mdash; <em>famiglia, figlio</em></li><li><strong>sc</strong> before e/i = \"sh\" &mdash; <em>pesce, sciare</em>; before a/o/u = \"sk\" &mdash; <em>scuola, pesca</em></li><li>Double consonants are held longer than single ones &mdash; <em>sono</em> (I am) vs. <em>sonno</em> (sleep) are genuinely different words</li></ul>"},
            ],
            "examples": [
                {"it": "Ciao, come ti chiami?", "en": "Hi, what's your name? — ciao starts with the soft \"ch\" sound"},
                {"it": "Ho fame, voglio la pasta.", "en": "I'm hungry, I want pasta — voglio has a soft \"ly\"-like gli is not here, but voglio's gli combo shows the pattern in famiglia"},
                {"it": "Il gatto dorme sul letto.", "en": "The cat sleeps on the bed — gatto has the hard \"g\" sound"},
                {"it": "Mia figlia studia all'università.", "en": "My daughter studies at university — figlia uses the gli \"ly\" sound"},
                {"it": "Gli spaghetti sono buonissimi.", "en": "The spaghetti is delicious — spaghetti keeps the hard \"g\" thanks to the h"},
            ],
            "commonMistakes": [
                {"wrong": "Pronouncing \"ciao\" with a hard \"k\" sound", "right": "\"ciao\" with a soft \"ch\" sound (chow)", "why": "ci before a vowel is always the soft \"ch\" sound in Italian, unlike the hard c English speakers expect."},
                {"wrong": "Treating \"sono\" and \"sonno\" as the same word", "right": "sono (I am / they are) vs. sonno (sleep, drowsiness) — genuinely different", "why": "Double consonants change the meaning of the word, not just the spelling — they must be held longer in speech."},
            ],
        },
        "exercises": [
            {"id": "a1ap-mc", "type": "multiple-choice", "title": "Which Sound?",
             "items": [
                {"id": "a1ap1", "prompt": "How is the \"c\" in \"cena\" (dinner) pronounced?", "options": ["Hard, like \"k\"", "Soft, like \"ch\" in cheese", "Silent"], "answerIndex": 1, "explanation": "Ce/ci is always the soft \"ch\" sound in Italian."},
                {"id": "a1ap2", "prompt": "How is the \"gn\" in \"bagno\" (bathroom) pronounced?", "options": ["\"g\" + \"n\" separately", "\"ny\" as in canyon", "silent g"], "answerIndex": 1, "explanation": "gn is always a single \"ny\" sound, never two separate letters."},
                {"id": "a1ap3", "prompt": "Which word has the hard \"g\" sound?", "options": ["gente", "gatto", "giorno"], "answerIndex": 1, "explanation": "Ga/go/gu is hard; ge/gi is soft — gatto has ga, the hard sound."},
             ]},
            {"id": "a1ap-match", "type": "matching", "title": "Match the Spelling to Its Sound",
             "items": [
                {"id": "a1ap4", "pairs": [
                    {"left": "che, chi", "right": "hard \"k\" before e/i"},
                    {"left": "ce, ci", "right": "soft \"ch\""},
                    {"left": "gli", "right": "\"ly\" as in million"},
                    {"left": "sc + e/i", "right": "\"sh\" sound"},
                ], "explanation": "The h and i in these combinations are silent spelling signals, not pronounced letters of their own."},
             ]},
        ],
        "summary": [
            "Every Italian vowel is pronounced clearly — there is no vowel reduction.",
            "C/g are hard before a, o, u and soft before e, i; h keeps them hard, i keeps them soft.",
            "gn = \"ny\", gli = \"ly\", sc(e/i) = \"sh\" — and double consonants are genuinely held longer.",
        ],
    },
    {
        "id": "a1-genere-e-articoli",
        "level": "A1", "unit": "1", "order": 3, "skill": "grammar", "strand": "nouns-articles",
        "title": "Genere degli Articoli e dei Sostantivi",
        "subtitle": "Every Italian noun is masculine or feminine — and the article always agrees.",
        "objectives": [
            "Identify whether a noun is masculine or feminine from its ending",
            "Choose the correct definite article (il, lo, la, l', i, gli, le)",
            "Choose the correct indefinite article (un, uno, una, un')",
        ],
        "content": {
            "intro": "In Italian, every noun — even for objects with no natural gender, like a table or a book — is grammatically masculine or feminine, and every article that points to it must agree.",
            "explanation": "<p>Most nouns ending in <strong>-o</strong> are masculine (<em>il libro</em>, the book) and most ending in <strong>-a</strong> are feminine (<em>la casa</em>, the house). Nouns ending in <strong>-e</strong> can be either gender and simply have to be learned (<em>il pane</em> is masculine, <em>la notte</em> is feminine). The article you use depends on both the noun's gender and the sound it starts with.</p>",
            "rules": [
                {"heading": "a) Definite article (\"the\") — singular", "body": "<ul><li><strong>il</strong> — masculine + consonant: <em>il libro</em></li><li><strong>lo</strong> — masculine + s+consonant, z, gn, ps, y: <em>lo studente, lo zaino</em></li><li><strong>l'</strong> — masculine or feminine + vowel: <em>l'amico, l'amica</em></li><li><strong>la</strong> — feminine + consonant: <em>la casa</em></li></ul>"},
                {"heading": "b) Definite article — plural", "body": "<ul><li><strong>i</strong> — plural of il: <em>i libri</em></li><li><strong>gli</strong> — plural of lo and of l' (masculine): <em>gli studenti, gli amici</em></li><li><strong>le</strong> — plural of la and l' (feminine): <em>le case, le amiche</em></li></ul>"},
                {"heading": "c) Indefinite article (\"a/an\")", "body": "<ul><li><strong>un</strong> — masculine + consonant or vowel: <em>un libro, un amico</em></li><li><strong>uno</strong> — masculine + s+consonant, z, gn: <em>uno studente, uno zaino</em></li><li><strong>una</strong> — feminine + consonant: <em>una casa</em></li><li><strong>un'</strong> — feminine + vowel (with apostrophe): <em>un'amica</em></li></ul>"},
                {"heading": "d) Forming the plural", "body": "<ul><li>-o &rarr; -i: <em>libro &rarr; libri</em></li><li>-a &rarr; -e: <em>casa &rarr; case</em></li><li>-e &rarr; -i (both genders): <em>notte &rarr; notti, pane &rarr; pani</em></li></ul>"},
            ],
            "examples": [
                {"it": "Il libro è sul tavolo.", "en": "The book is on the table."},
                {"it": "Ho un'amica a Roma.", "en": "I have a [female] friend in Rome."},
                {"it": "Lo studente studia in biblioteca.", "en": "The student studies in the library."},
                {"it": "Gli studenti sono bravi.", "en": "The students are good [at what they do]."},
                {"it": "Le case in questa via sono antiche.", "en": "The houses on this street are old."},
                {"it": "Uno zaino nuovo costa molto.", "en": "A new backpack costs a lot."},
            ],
            "commonMistakes": [
                {"wrong": "il amico", "right": "l'amico", "why": "Before a vowel, il/lo shorten to l' — il amico is never used."},
                {"wrong": "il zaino", "right": "lo zaino", "why": "Masculine nouns starting with z take lo, not il."},
                {"wrong": "un'amico", "right": "un amico", "why": "The apostrophe form un' is only for feminine nouns before a vowel; masculine amico takes plain un."},
                {"wrong": "la libri", "right": "i libri", "why": "Plural masculine nouns need the plural article i (or gli), never the feminine la."},
            ],
        },
        "exercises": [
            {"id": "a1ga-fill", "type": "fill-blank", "title": "Fill in the Correct Article",
             "instructions": "Complete each phrase with il, lo, la, or l'.",
             "items": [
                {"id": "a1ga1", "prompt": "___ studente (the student, m.)", "answers": [["Lo"]], "explanation": "Masculine nouns starting with s+consonant take lo.", "options": ["Il", "Lo", "La"]},
                {"id": "a1ga2", "prompt": "___ amica (the friend, f.)", "answers": [["L'"]], "explanation": "Before a vowel, the feminine article shortens to l'.", "options": ["La", "L'", "Lo"]},
                {"id": "a1ga3", "prompt": "___ pane (the bread, m.)", "answers": [["Il"]], "explanation": "Pane is masculine and starts with a consonant, so it takes il.", "options": ["Il", "La", "Lo"]},
                {"id": "a1ga4", "prompt": "___ notte (the night, f.)", "answers": [["La"]], "explanation": "Notte is feminine (despite the -e ending) and starts with a consonant.", "options": ["Il", "La", "Lo"]},
             ]},
            {"id": "a1ga-mc", "type": "multiple-choice", "title": "Plural Forms",
             "items": [
                {"id": "a1ga5", "prompt": "What is the plural of \"lo zaino\"?", "options": ["i zaini", "gli zaini", "le zaini"], "answerIndex": 1, "explanation": "Gli is the plural of lo."},
                {"id": "a1ga6", "prompt": "What is the plural of \"la casa\"?", "options": ["le case", "i case", "le casi"], "answerIndex": 0, "explanation": "Feminine -a nouns become -e in the plural, with the article le."},
             ]},
            {"id": "a1ga-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a1ga7", "incorrect": "il amico", "answer": ["l'amico"], "explanation": "Before a vowel, il shortens to l'."},
                {"id": "a1ga8", "incorrect": "una amica", "answer": ["un'amica"], "explanation": "Before a vowel, feminine una becomes un', with an apostrophe."},
             ]},
        ],
        "summary": [
            "Nouns ending in -o are usually masculine; -a usually feminine; -e can be either and must be learned.",
            "Definite articles: il/lo/l' (m. sing.), la/l' (f. sing.), i/gli (m. pl.), le (f. pl.) — chosen by gender and starting sound.",
            "Indefinite articles: un/uno (m.), una/un' (f.) — un' only before a feminine vowel.",
        ],
    },
    {
        "id": "a1-essere-e-avere",
        "level": "A1", "unit": "1", "order": 4, "skill": "grammar", "strand": "verbs",
        "title": "Essere e Avere",
        "subtitle": "The two most essential verbs in Italian — irregular, and used everywhere.",
        "objectives": [
            "Conjugate essere (to be) in the present tense",
            "Conjugate avere (to have) in the present tense",
            "Use avere in fixed expressions like avere fame and avere ... anni",
        ],
        "content": {
            "intro": "Essere and avere are the two pillars of Italian: you'll use them in almost every sentence, and later they're also the building blocks of the passato prossimo (compound past tense).",
            "explanation": "<p>Both verbs are irregular and must be memorized — but they're used so constantly that this happens naturally with practice. <strong>Essere</strong> expresses identity, origin, characteristics and location (with certain expressions); <strong>avere</strong> expresses possession, but also age, and a large family of physical/emotional-state expressions where English uses &ldquo;to be&rdquo;.</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Essere and avere — present tense</caption><thead><tr><th>Subject</th><th>essere</th><th>avere</th></tr></thead><tbody><tr><td>io</td><td>sono</td><td>ho</td></tr><tr><td>tu</td><td>sei</td><td>hai</td></tr><tr><td>lui/lei/Lei</td><td>è</td><td>ha</td></tr><tr><td>noi</td><td>siamo</td><td>abbiamo</td></tr><tr><td>voi</td><td>siete</td><td>avete</td></tr><tr><td>loro</td><td>sono</td><td>hanno</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Essere", "body": "<ul><li>Identity/profession: <em>Sono Marco. Sei insegnante.</em></li><li>Origin: <em>Siamo di Milano.</em></li><li>Characteristics: <em>È simpatica.</em></li></ul>"},
                {"heading": "b) Avere — possession and age", "body": "<ul><li>Possession: <em>Ho una macchina.</em></li><li>Age (never essere here): <em>Ho trent'anni.</em> (I am thirty — literally \"I have thirty years\")</li></ul>"},
                {"heading": "c) Avere in fixed expressions", "body": "<ul><li><em>avere fame/sete</em> — to be hungry/thirsty</li><li><em>avere caldo/freddo</em> — to be hot/cold</li><li><em>avere sonno</em> — to be sleepy</li><li><em>avere paura (di)</em> — to be afraid (of)</li><li><em>avere ragione/torto</em> — to be right/wrong</li><li><em>avere fretta</em> — to be in a hurry</li><li><em>avere bisogno di</em> — to need</li></ul>"},
            ],
            "examples": [
                {"it": "Io sono italiano, ma abito in Spagna.", "en": "I am Italian, but I live in Spain."},
                {"it": "Hai fratelli o sorelle?", "en": "Do you have brothers or sisters?"},
                {"it": "Ho vent'anni.", "en": "I am twenty years old."},
                {"it": "Abbiamo fame, mangiamo qualcosa?", "en": "We're hungry, shall we eat something?"},
                {"it": "Loro sono sempre in ritardo.", "en": "They are always late."},
                {"it": "Hai ragione, hai proprio ragione.", "en": "You're right, you're really right."},
            ],
            "commonMistakes": [
                {"wrong": "Sono venti anni.", "right": "Ho vent'anni.", "why": "Age uses avere in Italian, not essere — a direct English-to-Italian translation of \"I am\" is wrong here."},
                {"wrong": "Sono fame.", "right": "Ho fame.", "why": "Physical/emotional states like hunger use avere, not essere, even though English says \"I am hungry.\""},
                {"wrong": "Io ha vent'anni.", "right": "Io ho vent'anni.", "why": "Ha is the lui/lei form; io always pairs with ho."},
            ],
        },
        "exercises": [
            {"id": "a1ea-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "instructions": "Complete each sentence with the correct form of essere or avere.",
             "items": [
                {"id": "a1ea1", "prompt": "Io ___ studentessa.", "answers": [["sono"]], "explanation": "Io + essere (identity/profession) = sono.", "options": ["sono", "sei", "ho"]},
                {"id": "a1ea2", "prompt": "Loro ___ due gatti.", "answers": [["hanno"]], "explanation": "Loro + avere (possession) = hanno.", "options": ["hanno", "sono", "ha"]},
                {"id": "a1ea3", "prompt": "Noi ___ fame, andiamo a mangiare!", "answers": [["abbiamo"]], "explanation": "Avere fame — to be hungry — needs avere: abbiamo.", "options": ["abbiamo", "siamo", "avete"]},
                {"id": "a1ea4", "prompt": "Tu ___ di Napoli?", "answers": [["sei"]], "explanation": "Origin uses essere: tu + essere = sei.", "options": ["sei", "hai", "è"]},
             ]},
            {"id": "a1ea-mc", "type": "multiple-choice", "title": "Essere or Avere?",
             "items": [
                {"id": "a1ea5", "prompt": "How do you say \"I am thirty years old\"?", "options": ["Sono trent'anni.", "Ho trent'anni.", "Ho essere trent'anni."], "answerIndex": 1, "explanation": "Age always uses avere in Italian."},
                {"id": "a1ea6", "prompt": "\"Ha sonno\" means...", "options": ["He/she has a dream.", "He/she is sleepy.", "He/she is asleep."], "answerIndex": 1, "explanation": "Avere sonno is a fixed expression meaning \"to be sleepy\"."},
             ]},
            {"id": "a1ea-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a1ea7", "incorrect": "Sono diciotto anni.", "answer": ["Ho diciotto anni."], "explanation": "Age needs avere, not essere."},
                {"id": "a1ea8", "incorrect": "Io ha una sorella.", "answer": ["Io ho una sorella."], "explanation": "Io always takes ho, never ha (which is the lui/lei form)."},
             ]},
        ],
        "summary": [
            "Essere = identity, origin, characteristics; avere = possession and age.",
            "Age, hunger, thirst, heat/cold, fear, being right/wrong all use avere in Italian, unlike English \"to be\".",
            "Both verbs are irregular — memorize the six forms: sono/sei/è/siamo/siete/sono and ho/hai/ha/abbiamo/avete/hanno.",
        ],
    },
    {
        "id": "a1-pronomi-soggetto",
        "level": "A1", "unit": "1", "order": 5, "skill": "grammar", "strand": "pronouns",
        "title": "Pronomi Personali Soggetto",
        "subtitle": "Subject pronouns — and why Italian sentences usually leave them out.",
        "objectives": [
            "List the Italian subject pronouns",
            "Explain why subject pronouns are usually omitted",
            "Use subject pronouns for emphasis or contrast when needed",
        ],
        "content": {
            "intro": "Italian verb endings already tell you who's doing the action, so subject pronouns are optional and often dropped entirely — the opposite of English, where a sentence needs its subject.",
            "explanation": "<p>Because each verb ending is unique to a subject (parl<strong>o</strong> can only mean \"I speak\"), Italian is a &ldquo;pro-drop&rdquo; language: <em>Parlo italiano</em> is a complete, natural sentence — adding <em>io</em> is grammatically fine but usually unnecessary. Subject pronouns reappear mainly for emphasis, contrast, or clarity (e.g. when a lui/lei form could refer to more than one person in context).</p>",
            "rules": [
                {"heading": "a) The subject pronouns", "body": "<ul><li><strong>io</strong> — I</li><li><strong>tu</strong> — you (informal)</li><li><strong>lui / lei</strong> — he / she; <strong>Lei</strong> (capitalized) — you (formal)</li><li><strong>noi</strong> — we</li><li><strong>voi</strong> — you (plural)</li><li><strong>loro</strong> — they</li></ul>"},
                {"heading": "b) When to keep the pronoun", "body": "<ul><li>Contrast: <em>Io studio, tu guardi la TV.</em> (I study, you watch TV.)</li><li>Emphasis: <em>Lo dico io!</em> (I'm the one saying it!)</li><li>Answering a question alone: <em>Chi vuole il caffè? Io!</em></li></ul>"},
            ],
            "examples": [
                {"it": "Parlo italiano e inglese.", "en": "I speak Italian and English. (io dropped)"},
                {"it": "Tu studi, io lavoro.", "en": "You study, I work. (kept, for contrast)"},
                {"it": "Vive a Roma.", "en": "He/she lives in Rome. (lui/lei dropped — context makes it clear)"},
                {"it": "Voi venite alla festa?", "en": "Are you [plural] coming to the party?"},
                {"it": "Loro non capiscono.", "en": "They don't understand."},
            ],
            "commonMistakes": [
                {"wrong": "Io sono io stanco.", "right": "Sono stanco.", "why": "Italian never needs an explicit subject pronoun to make a sentence grammatical — it's redundant here, not required."},
                {"wrong": "lei (lowercase) for the formal \"you\"", "right": "Lei (capitalized) for formal \"you\"", "why": "Capitalizing Lei distinguishes formal \"you\" from lei meaning \"she\" in writing."},
            ],
        },
        "exercises": [
            {"id": "a1ps-mc", "type": "multiple-choice", "title": "Which Pronoun?",
             "items": [
                {"id": "a1ps1", "prompt": "Which pronoun means \"they\"?", "options": ["voi", "loro", "noi"], "answerIndex": 1, "explanation": "Loro is the third-person plural, \"they\"."},
                {"id": "a1ps2", "prompt": "\"Parlo italiano\" needs which extra word to be correct?", "options": ["io, but it's optional", "io, it's required", "nothing else is needed and no pronoun would help"], "answerIndex": 0, "explanation": "The -o ending already means \"I\", so io is grammatically optional here."},
             ]},
            {"id": "a1ps-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "instructions": "Add the pronoun only where it's needed for contrast or clarity.",
             "items": [
                {"id": "a1ps3", "prompt": "___ studio, ___ guardi la TV. (contrast between \"I\" and \"you\")", "answers": [["Io"]], "explanation": "Kept for contrast between two different subjects in the same sentence.", "options": ["Io", "Tu", "(nothing)"]},
             ]},
        ],
        "summary": [
            "Subject pronouns are io, tu, lui/lei/Lei, noi, voi, loro.",
            "Italian verb endings identify the subject, so pronouns are usually dropped.",
            "Keep the pronoun for contrast, emphasis, or when the verb form alone would be ambiguous.",
        ],
    },
    {
        "id": "a1-aggettivi-e-accordo",
        "level": "A1", "unit": "1", "order": 6, "skill": "grammar", "strand": "adjectives",
        "title": "Aggettivi e Accordo",
        "subtitle": "Adjectives must match the noun they describe in gender and number.",
        "objectives": [
            "Make -o/-a adjectives agree in gender and number",
            "Use -e adjectives, which don't change for gender",
            "Place adjectives correctly before or after the noun",
        ],
        "content": {
            "intro": "An Italian adjective isn't fixed — it changes its ending to match the noun it describes, exactly like the article does.",
            "explanation": "<p>Most adjectives end in <strong>-o</strong> in the masculine singular and change to <strong>-a</strong>, <strong>-i</strong>, <strong>-e</strong> to agree with the noun. A second group ends in <strong>-e</strong> for both masculine and feminine singular, changing only for plural. Most descriptive adjectives follow the noun (<em>una casa grande</em>), while a small set of very common adjectives (bello, buono, grande, piccolo, giovane, vecchio...) can also come before it, sometimes with a slightly different nuance.</p>",
            "rules": [
                {"heading": "a) -o/-a adjectives (four forms)", "body": "<ul><li>m. sing. <strong>-o</strong>: <em>alto</em></li><li>f. sing. <strong>-a</strong>: <em>alta</em></li><li>m. pl. <strong>-i</strong>: <em>alti</em></li><li>f. pl. <strong>-e</strong>: <em>alte</em></li></ul>"},
                {"heading": "b) -e adjectives (two forms)", "body": "<ul><li>sing. (m. or f.) <strong>-e</strong>: <em>un ragazzo intelligente, una ragazza intelligente</em></li><li>pl. (m. or f.) <strong>-i</strong>: <em>ragazzi intelligenti, ragazze intelligenti</em></li></ul>"},
                {"heading": "c) Position", "body": "<ul><li>Most adjectives follow the noun: <em>un libro interessante</em></li><li>A short list (bello, brutto, buono, cattivo, grande, piccolo, giovane, vecchio, nuovo) often precede it: <em>una bella giornata</em></li></ul>"},
            ],
            "examples": [
                {"it": "Marco è alto e simpatico.", "en": "Marco is tall and nice."},
                {"it": "Le mie amiche sono intelligenti.", "en": "My [female] friends are intelligent."},
                {"it": "È una macchina veloce.", "en": "It's a fast car."},
                {"it": "Abbiamo una bella casa piccola.", "en": "We have a nice small house."},
                {"it": "I ragazzi sono stanchi.", "en": "The boys are tired."},
            ],
            "commonMistakes": [
                {"wrong": "una ragazza alto", "right": "una ragazza alta", "why": "The adjective must agree with the feminine noun ragazza, so it needs the -a ending."},
                {"wrong": "i libri interessanto", "right": "i libri interessanti", "why": "-e adjectives take -i for the plural, not -o — interessante is not an -o/-a adjective."},
                {"wrong": "le case bianco", "right": "le case bianche", "why": "Bianco needs a spelling adjustment (c→ch) to keep the hard \"k\" sound before the plural -e."},
            ],
        },
        "exercises": [
            {"id": "a1aa-fill", "type": "fill-blank", "title": "Fill in the Correct Ending",
             "items": [
                {"id": "a1aa1", "prompt": "Maria è molto simpatic___.", "answers": [["a"]], "explanation": "Simpatica agrees with the feminine subject Maria.", "options": ["a", "o", "e"]},
                {"id": "a1aa2", "prompt": "I ragazzi sono alt___.", "answers": [["i"]], "explanation": "Masculine plural takes -i.", "options": ["i", "e", "o"]},
                {"id": "a1aa3", "prompt": "Una casa grand___.", "answers": [["e"]], "explanation": "Grande is an -e adjective — same form for masculine and feminine singular.", "options": ["e", "a", "o"]},
             ]},
            {"id": "a1aa-mc", "type": "multiple-choice", "title": "Choose the Correct Form",
             "items": [
                {"id": "a1aa4", "prompt": "Le mie sorelle sono molto ___.", "options": ["intelligente", "intelligenti", "intelligento"], "answerIndex": 1, "explanation": "Feminine plural of an -e adjective is -i, same as masculine plural."},
             ]},
            {"id": "a1aa-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a1aa5", "incorrect": "una ragazza alto", "answer": ["una ragazza alta"], "explanation": "The adjective must agree with feminine ragazza."},
                {"id": "a1aa6", "incorrect": "gli studenti bravo", "answer": ["gli studenti bravi"], "explanation": "Masculine plural subject needs the -i ending on the adjective."},
             ]},
        ],
        "summary": [
            "-o/-a adjectives have four forms: -o, -a, -i, -e, matching the noun's gender and number.",
            "-e adjectives have only two forms: -e (singular, both genders) and -i (plural, both genders).",
            "Most adjectives follow the noun; a short, common set can also precede it.",
        ],
    },
    {
        "id": "a1-presente-verbi-regolari",
        "level": "A1", "unit": "1", "order": 7, "skill": "grammar", "strand": "verbs",
        "title": "Presente Indicativo dei Verbi Regolari",
        "subtitle": "The present tense of -are, -ere and -ire verbs — Italian's three regular conjugations.",
        "objectives": [
            "Conjugate regular -are, -ere and -ire verbs in the present tense",
            "Recognize -isc- verbs, a common pattern within -ire",
            "Use the present tense for habits, facts and (unlike English) near-future plans",
        ],
        "content": {
            "intro": "Every Italian verb belongs to one of three families, named for their infinitive ending: -are, -ere, -ire. Learn the pattern for one regular verb in each family, and you can conjugate hundreds of others the same way.",
            "explanation": "<p>To conjugate a regular verb, drop the infinitive ending (-are/-ere/-ire) and add the ending for each subject. A subgroup of -ire verbs (like <em>capire</em>, to understand) inserts <strong>-isc-</strong> before the ending in all forms except noi/voi — there's no way to predict which -ire verbs do this, so it's learned per verb.</p><p>The present tense also covers ground English splits into two tenses: <em>Parlo italiano</em> can mean both &ldquo;I speak Italian&rdquo; and, right now, &ldquo;I am speaking Italian&rdquo;. It's also commonly used for near-future plans: <em>Domani parto per Roma</em> (Tomorrow I'm leaving for Rome).</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Present tense — parlare, scrivere, dormire, capire (-isc-)</caption><thead><tr><th>Subject</th><th>parlare</th><th>scrivere</th><th>dormire</th><th>capire</th></tr></thead><tbody><tr><td>io</td><td>parlo</td><td>scrivo</td><td>dormo</td><td>capisco</td></tr><tr><td>tu</td><td>parli</td><td>scrivi</td><td>dormi</td><td>capisci</td></tr><tr><td>lui/lei</td><td>parla</td><td>scrive</td><td>dorme</td><td>capisce</td></tr><tr><td>noi</td><td>parliamo</td><td>scriviamo</td><td>dormiamo</td><td>capiamo</td></tr><tr><td>voi</td><td>parlate</td><td>scrivete</td><td>dormite</td><td>capite</td></tr><tr><td>loro</td><td>parlano</td><td>scrivono</td><td>dormono</td><td>capiscono</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) -are verbs (e.g. parlare, lavorare, abitare)", "body": "<p>Endings: -o, -i, -a, -iamo, -ate, -ano</p>"},
                {"heading": "b) -ere verbs (e.g. scrivere, leggere, prendere)", "body": "<p>Endings: -o, -i, -e, -iamo, -ete, -ono</p>"},
                {"heading": "c) -ire verbs (e.g. dormire, partire, aprire)", "body": "<p>Endings: -o, -i, -e, -iamo, -ite, -ono</p>"},
                {"heading": "d) -isc- verbs (e.g. capire, finire, preferire, pulire)", "body": "<p>Same -ire endings, but -isc- is inserted before the ending for io/tu/lui-lei/loro: <em>capisco, capisci, capisce, capiamo, capite, capiscono</em>.</p>"},
            ],
            "examples": [
                {"it": "Io lavoro in un ufficio.", "en": "I work in an office."},
                {"it": "Tu scrivi molte email.", "en": "You write a lot of emails."},
                {"it": "Lei dorme otto ore ogni notte.", "en": "She sleeps eight hours every night."},
                {"it": "Non capisco questa parola.", "en": "I don't understand this word."},
                {"it": "Domani partiamo per le vacanze.", "en": "Tomorrow we're leaving for vacation."},
                {"it": "Preferisco il tè al caffè.", "en": "I prefer tea to coffee."},
            ],
            "commonMistakes": [
                {"wrong": "Io parlo l'italiano fluentemente da domani.", "right": "Da domani parlerò... / Parlo italiano ora, ma da domani...", "why": "Present tense for future plans works for near, planned events (\"tomorrow I leave\"), not for describing a change that will only become true later — that needs the future tense (covered at B1)."},
                {"wrong": "Io capo la lezione.", "right": "Io capisco la lezione.", "why": "Capire is an -isc- verb: the io form is capisco, not a bare capo."},
                {"wrong": "Noi parla italiano.", "right": "Noi parliamo italiano.", "why": "Noi always takes the -iamo ending, never the lui/lei -a/-e ending."},
            ],
        },
        "exercises": [
            {"id": "a1pr-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "instructions": "Conjugate the verb in parentheses.",
             "items": [
                {"id": "a1pr1", "prompt": "Io ___ (lavorare) a Milano.", "answers": [["lavoro"]], "explanation": "Io + -are verb = -o ending.", "options": ["lavoro", "lavori", "lavora"]},
                {"id": "a1pr2", "prompt": "Tu ___ (scrivere) molto bene.", "answers": [["scrivi"]], "explanation": "Tu + -ere verb = -i ending.", "options": ["scrivi", "scrive", "scrivo"]},
                {"id": "a1pr3", "prompt": "Loro ___ (dormire) fino a tardi.", "answers": [["dormono"]], "explanation": "Loro + -ire verb = -ono ending.", "options": ["dormono", "dormano", "dormiamo"]},
                {"id": "a1pr4", "prompt": "Noi non ___ (capire) l'esercizio.", "answers": [["capiamo"]], "explanation": "Noi never takes -isc-, even in an -isc- verb: capiamo.", "options": ["capiamo", "capisciamo", "capisce"]},
             ]},
            {"id": "a1pr-mc", "type": "multiple-choice", "title": "Choose the Correct Conjugation",
             "items": [
                {"id": "a1pr5", "prompt": "Which is the correct io form of \"finire\"?", "options": ["finisco", "fino", "finiso"], "answerIndex": 0, "explanation": "Finire is an -isc- verb: io finisco."},
                {"id": "a1pr6", "prompt": "\"Lei ___ un libro\" (leggere)", "options": ["legge", "leggi", "leggo"], "answerIndex": 0, "explanation": "Lui/lei + -ere verb = -e ending: legge."},
             ]},
            {"id": "a1pr-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a1pr7", "incorrect": "Io capo l'italiano.", "answer": ["Io capisco l'italiano."], "explanation": "Capire needs -isc- in the io form: capisco."},
                {"id": "a1pr8", "incorrect": "Noi parla molto.", "answer": ["Noi parliamo molto."], "explanation": "Noi always uses -iamo, not a singular ending."},
             ]},
        ],
        "summary": [
            "Three regular conjugations: -are (-o,-i,-a,-iamo,-ate,-ano), -ere (-o,-i,-e,-iamo,-ete,-ono), -ire (-o,-i,-e,-iamo,-ite,-ono).",
            "Some -ire verbs insert -isc- before the ending, except for noi/voi.",
            "The present tense covers habits, facts, right-now actions, and near-future plans.",
        ],
    },
    {
        "id": "a1-numeri-ora-e-data",
        "level": "A1", "unit": "1", "order": 8, "skill": "vocabulary", "strand": "numbers-time",
        "title": "Numeri, Ora e Data",
        "subtitle": "Count, tell the time, and say today's date.",
        "objectives": [
            "Count from 0 to 100 and use large round numbers",
            "Ask for and tell the time",
            "Say the date, including day of the week and month",
        ],
        "content": {
            "intro": "Numbers, time and dates come up in almost every real conversation — booking a table, catching a train, making plans.",
            "explanation": "<p>Italian numbers 1–19 are irregular and must be memorized; from 20 on, tens combine regularly with units, dropping the final vowel of the ten before <em>uno</em> and <em>otto</em> (<em>ventuno</em>, <em>ventotto</em>, not <em>venti-uno</em>). Telling time uses <em>Che ora è?</em>/<em>Che ore sono?</em> and answers with <em>È l'una</em> (it's one o'clock, singular) or <em>Sono le due/tre...</em> (plural for everything else).</p>",
            "rules": [
                {"heading": "a) Numbers 0–20", "body": "<p>zero, uno, due, tre, quattro, cinque, sei, sette, otto, nove, dieci, undici, dodici, tredici, quattordici, quindici, sedici, diciassette, diciotto, diciannove, venti</p>"},
                {"heading": "b) Tens", "body": "<p>venti (20), trenta (30), quaranta (40), cinquanta (50), sessanta (60), settanta (70), ottanta (80), novanta (90), cento (100). Elide the final vowel before -uno/-otto: <em>ventuno, trentotto</em>.</p>"},
                {"heading": "c) Telling time", "body": "<ul><li><em>Che ora è? / Che ore sono?</em> — What time is it?</li><li><em>È l'una</em> — It's one o'clock (only l'una is singular)</li><li><em>Sono le tre e mezza</em> — It's half past three</li><li><em>Sono le quattro meno un quarto</em> — It's a quarter to four</li></ul>"},
                {"heading": "d) Dates", "body": "<p><em>Che giorno è oggi? &mdash; Oggi è il 5 marzo.</em> Days and months are lowercase in Italian. Only the first of the month uses an ordinal: <em>il primo maggio</em>, but <em>il due maggio, il tre maggio</em>...</p>"},
            ],
            "examples": [
                {"it": "Ho trentatré anni.", "en": "I am thirty-three years old."},
                {"it": "Che ore sono? Sono le nove e un quarto.", "en": "What time is it? It's a quarter past nine."},
                {"it": "Il treno parte all'una e mezza.", "en": "The train leaves at half past one."},
                {"it": "Oggi è lunedì, il primo settembre.", "en": "Today is Monday, the first of September."},
                {"it": "Il mio compleanno è il ventitré aprile.", "en": "My birthday is the twenty-third of April."},
            ],
            "commonMistakes": [
                {"wrong": "venti-uno", "right": "ventuno", "why": "Tens drop their final vowel before -uno and -otto, and the result is written as one word."},
                {"wrong": "È le tre.", "right": "Sono le tre.", "why": "Every hour except one o'clock uses the plural sono le..., not è."},
                {"wrong": "il uno maggio", "right": "il primo maggio", "why": "The first of the month uses the ordinal primo, not the cardinal number uno."},
            ],
        },
        "exercises": [
            {"id": "a1no-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a1no1", "prompt": "28 in Italian is ___.", "answers": [["ventotto"]], "explanation": "Venti loses its final vowel before otto: ventotto.", "options": ["ventotto", "venti-otto", "ventiotto"]},
                {"id": "a1no2", "prompt": "___ le due del pomeriggio.", "answers": [["Sono"]], "explanation": "All hours except one o'clock use the plural sono.", "options": ["Sono", "È", "Ho"]},
                {"id": "a1no3", "prompt": "Oggi è il ___ maggio. (the 1st)", "answers": [["primo"]], "explanation": "The first of the month uses the ordinal primo, not uno.", "options": ["primo", "uno", "prima"]},
             ]},
            {"id": "a1no-mc", "type": "multiple-choice", "title": "Choose the Correct Answer",
             "items": [
                {"id": "a1no4", "prompt": "How do you say \"it's one o'clock\"?", "options": ["Sono l'una.", "È l'una.", "È le una."], "answerIndex": 1, "explanation": "One o'clock is the only hour that uses the singular è."},
             ]},
        ],
        "summary": [
            "0–19 are irregular; from 20, tens + units combine regularly, eliding before -uno/-otto.",
            "Sono le... for every hour except È l'una.",
            "Only the first of the month uses an ordinal (il primo); every other day uses the cardinal number.",
        ],
    },
    {
        "id": "a1-preposizioni-semplici",
        "level": "A1", "unit": "1", "order": 9, "skill": "grammar", "strand": "prepositions",
        "title": "Preposizioni Semplici",
        "subtitle": "In, a, di, da, su, con, per, tra/fra — Italian's core simple prepositions.",
        "objectives": [
            "Use the eight simple prepositions correctly",
            "Distinguish in vs. a for location",
            "Recognize di for possession and origin",
        ],
        "content": {
            "intro": "Prepositions link the pieces of a sentence together — and their use in Italian often doesn't match English word-for-word, so it's worth learning them as fixed patterns rather than translating literally.",
            "explanation": "<p>The eight simple prepositions are <strong>di, a, da, in, con, su, per, tra/fra</strong> (tra and fra are interchangeable, chosen just to avoid repeating sounds). In the next lesson you'll see how several of them combine with the definite article (<em>a</em> + <em>il</em> = <em>al</em>) — for now, focus on their use before a noun with no article, and before city names.</p>",
            "rules": [
                {"heading": "a) di — of, from, possession", "body": "<ul><li>Possession: <em>il libro di Marco</em> (Marco's book)</li><li>Origin: <em>Sono di Torino.</em> (I'm from Turin.)</li><li>Material: <em>un tavolo di legno</em> (a wooden table)</li></ul>"},
                {"heading": "b) a — to, at, in (with cities)", "body": "<ul><li>Destination/location with cities: <em>Vado a Roma. Abito a Roma.</em></li><li>Time of day: <em>a mezzogiorno</em> (at noon)</li><li>Indirect object: <em>Scrivo a Maria.</em> (I write to Maria.)</li></ul>"},
                {"heading": "c) in — in, to (with countries/regions/enclosed spaces)", "body": "<ul><li>Countries, regions, enclosed spaces: <em>Vivo in Italia. Sono in ufficio.</em></li><li>Note the contrast with a: <strong>a</strong> Roma, but <strong>in</strong> Italia</li></ul>"},
                {"heading": "d) da, su, con, per, tra/fra", "body": "<ul><li><strong>da</strong> — from, since, at someone's place: <em>Vengo da Napoli. Vado da Marco.</em> (I'm going to Marco's place.)</li><li><strong>su</strong> — on: <em>Il libro è su tavolo.</em></li><li><strong>con</strong> — with: <em>Esco con gli amici.</em></li><li><strong>per</strong> — for, in order to: <em>Studio per l'esame.</em></li><li><strong>tra/fra</strong> — between, among, in [time]: <em>tra due ore</em> (in two hours)</li></ul>"},
            ],
            "examples": [
                {"it": "Sono di Firenze, ma vivo a Milano.", "en": "I'm from Florence, but I live in Milan."},
                {"it": "Il gatto dorme su una sedia.", "en": "The cat sleeps on a chair."},
                {"it": "Vado da Anna stasera.", "en": "I'm going to Anna's place tonight."},
                {"it": "Questo regalo è per te.", "en": "This gift is for you."},
                {"it": "Ci vediamo tra un'ora.", "en": "See you in an hour."},
                {"it": "Studio l'italiano con un insegnante.", "en": "I study Italian with a teacher."},
            ],
            "commonMistakes": [
                {"wrong": "Vivo in Roma.", "right": "Vivo a Roma.", "why": "Cities take a for location; in is for countries and regions (Vivo in Italia)."},
                {"wrong": "Vado a Marco.", "right": "Vado da Marco.", "why": "\"Going to someone's place\" uses da, not a — a is for destinations like cities or specific places, not people."},
                {"wrong": "Sono a Torino. (origin)", "right": "Sono di Torino.", "why": "Di expresses origin (\"I'm from...\"); a would describe current location, a different meaning."},
            ],
        },
        "exercises": [
            {"id": "a1pp-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a1pp1", "prompt": "Vivo ___ Roma, ma sono ___ Napoli.", "answers": [["a"], ["di"]], "explanation": "A for city location, di for origin.", "options": ["a", "di", "in"]},
                {"id": "a1pp2", "prompt": "Il libro è ___ tavolo.", "answers": [["su"]], "explanation": "Su expresses \"on\".", "options": ["su", "in", "a"]},
                {"id": "a1pp3", "prompt": "Vado ___ Giulia stasera.", "answers": [["da"]], "explanation": "\"Going to someone's place\" uses da.", "options": ["da", "a", "per"]},
             ]},
            {"id": "a1pp-mc", "type": "multiple-choice", "title": "In or A?",
             "items": [
                {"id": "a1pp4", "prompt": "Vivo ___ Spagna.", "options": ["a", "in", "di"], "answerIndex": 1, "explanation": "Countries take in, not a."},
                {"id": "a1pp5", "prompt": "Abito ___ Barcellona.", "options": ["in", "a", "su"], "answerIndex": 1, "explanation": "Cities take a, not in."},
             ]},
        ],
        "summary": [
            "Di = of/from/possession; a = to/at/in with cities; in = with countries, regions, enclosed spaces.",
            "Da = from/since/at someone's place; su = on; con = with; per = for; tra/fra = between/in [time].",
            "The contrast a Roma vs. in Italia is one of the most common early mistakes — learn it as a pair.",
        ],
    },
    {
        "id": "a1-ce-ci-sono",
        "level": "A1", "unit": "1", "order": 10, "skill": "grammar", "strand": "existence",
        "title": "C'è e Ci Sono",
        "subtitle": "\"There is\" and \"there are\" — your first taste of the particle ci.",
        "objectives": [
            "Use c'è for singular and ci sono for plural existence",
            "Form the negative and question forms",
            "Recognize ci as \"here/there\" in this fixed expression",
        ],
        "content": {
            "intro": "C'è and ci sono are how Italian says \"there is\" and \"there are\" — useful from your very first day, for describing a room, a menu, or a city.",
            "explanation": "<p>C'è is a contraction of <strong>ci</strong> (here/there) + <strong>è</strong> (is); ci sono is <strong>ci</strong> + <strong>sono</strong> (are). You'll meet <em>ci</em> again properly at B1 as a full pronoun/particle — for now, just learn c'è/ci sono as a fixed pair, matching singular vs. plural exactly like essere itself does.</p>",
            "rules": [
                {"heading": "a) Affirmative", "body": "<ul><li><strong>c'è</strong> + singular noun: <em>C'è un bar qui vicino.</em></li><li><strong>ci sono</strong> + plural noun: <em>Ci sono due bar qui vicino.</em></li></ul>"},
                {"heading": "b) Negative", "body": "<ul><li><em>Non c'è</em> tempo. (There isn't time.)</li><li><em>Non ci sono</em> problemi. (There aren't [any] problems.)</li></ul>"},
                {"heading": "c) Question", "body": "<ul><li><em>C'è latte in frigo?</em> (Is there milk in the fridge?)</li><li><em>Ci sono posti liberi?</em> (Are there free seats?)</li></ul>"},
            ],
            "examples": [
                {"it": "C'è un ristorante molto buono qui vicino.", "en": "There's a very good restaurant near here."},
                {"it": "Ci sono tre camere da letto.", "en": "There are three bedrooms."},
                {"it": "Non c'è nessuno in casa.", "en": "There's nobody home."},
                {"it": "Quante persone ci sono alla festa?", "en": "How many people are there at the party?"},
                {"it": "C'è un problema con il tuo biglietto.", "en": "There's a problem with your ticket."},
            ],
            "commonMistakes": [
                {"wrong": "C'è due gatti.", "right": "Ci sono due gatti.", "why": "A plural noun (due gatti) needs the plural ci sono, not the singular c'è."},
                {"wrong": "È un problema.", "right": "C'è un problema.", "why": "\"There is a problem\" needs c'è, not just è — plain è means \"[it] is\", not \"there is\"."},
            ],
        },
        "exercises": [
            {"id": "a1cs-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a1cs1", "prompt": "___ un bar qui vicino.", "answers": [["C'è"]], "explanation": "Singular noun (un bar) → c'è.", "options": ["C'è", "Ci sono", "È"]},
                {"id": "a1cs2", "prompt": "___ molte persone in piazza.", "answers": [["Ci sono"]], "explanation": "Plural noun (molte persone) → ci sono.", "options": ["Ci sono", "C'è", "Sono"]},
             ]},
            {"id": "a1cs-mc", "type": "multiple-choice", "title": "Choose the Correct Form",
             "items": [
                {"id": "a1cs3", "prompt": "\"Are there any free tables?\"", "options": ["C'è tavoli liberi?", "Ci sono tavoli liberi?", "Sono tavoli liberi?"], "answerIndex": 1, "explanation": "Plural tavoli needs ci sono."},
             ]},
            {"id": "a1cs-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a1cs4", "incorrect": "C'è tre camere.", "answer": ["Ci sono tre camere."], "explanation": "Plural camere needs ci sono, not c'è."},
             ]},
        ],
        "summary": [
            "C'è = there is (singular); ci sono = there are (plural).",
            "Negate with non c'è / non ci sono; question by intonation or word order, same as any yes/no question.",
            "You'll meet ci again as a full particle at B1 — for now, treat c'è/ci sono as one fixed pair.",
        ],
    },
    {
        "id": "a1-domande",
        "level": "A1", "unit": "1", "order": 11, "skill": "grammar", "strand": "questions",
        "title": "Domande e Parole Interrogative",
        "subtitle": "Ask yes/no questions and use the question words: chi, cosa, dove, quando, perché, come, quanto.",
        "objectives": [
            "Form a yes/no question with no word-order change",
            "Use the seven core question words",
            "Answer perché questions with perché",
        ],
        "content": {
            "intro": "Forming a question in Italian is refreshingly simple: for yes/no questions, the word order usually doesn't change at all.",
            "explanation": "<p>A statement becomes a yes/no question just by using rising intonation in speech, or a question mark in writing — <em>Parli italiano.</em> becomes <em>Parli italiano?</em> with no other change. For questions asking for information, place the question word at the start of the sentence.</p>",
            "rules": [
                {"heading": "a) Yes/no questions", "body": "<p>Same word order as the statement, just rising intonation / a question mark: <em>Sei italiano? Hai fame? Vuoi un caffè?</em></p>"},
                {"heading": "b) The seven question words", "body": "<ul><li><strong>chi</strong> — who: <em>Chi è?</em></li><li><strong>cosa / che cosa</strong> — what: <em>Cosa fai?</em></li><li><strong>dove</strong> — where: <em>Dove abiti?</em></li><li><strong>quando</strong> — when: <em>Quando parti?</em></li><li><strong>perché</strong> — why: <em>Perché studi l'italiano?</em></li><li><strong>come</strong> — how: <em>Come stai?</em></li><li><strong>quanto/a/i/e</strong> — how much/many (agrees like an adjective): <em>Quanti anni hai?</em></li></ul>"},
                {"heading": "c) Answering perché", "body": "<p><em>Perché</em> means both \"why\" and \"because\" — context (and a comma, in writing) tells them apart: <em>Perché studi l'italiano? Perché mi piace.</em> (Why do you study Italian? Because I like it.)</p>"},
            ],
            "examples": [
                {"it": "Dove abiti?", "en": "Where do you live?"},
                {"it": "Quando arriva il treno?", "en": "When does the train arrive?"},
                {"it": "Perché sei triste? Perché ho perso il lavoro.", "en": "Why are you sad? Because I lost my job."},
                {"it": "Quanti fratelli hai?", "en": "How many siblings do you have?"},
                {"it": "Parli spagnolo?", "en": "Do you speak Spanish?"},
                {"it": "Come si dice \"grazie\" in inglese?", "en": "How do you say \"thank you\" in English?"},
            ],
            "commonMistakes": [
                {"wrong": "Fai cosa?", "right": "Cosa fai? / Che cosa fai?", "why": "Question words go at the start of the sentence, not at the end as in some casual English word order."},
                {"wrong": "Quanto sorelle hai?", "right": "Quante sorelle hai?", "why": "Quanto agrees like an adjective — sorelle is feminine plural, so it must be quante."},
                {"wrong": "Do you speak Spanish? — Fai tu parlare spagnolo?", "right": "Parli spagnolo?", "why": "Italian doesn't use a \"do/does\" auxiliary for questions — just use the plain conjugated verb."},
            ],
        },
        "exercises": [
            {"id": "a1dq-mc", "type": "multiple-choice", "title": "Choose the Right Question Word",
             "items": [
                {"id": "a1dq1", "prompt": "___ ti chiami?", "options": ["Come", "Dove", "Quando"], "answerIndex": 0, "explanation": "\"Come ti chiami\" — how are you called — is the standard way to ask a name."},
                {"id": "a1dq2", "prompt": "___ anni hai?", "options": ["Quanti", "Quanto", "Quanta"], "answerIndex": 0, "explanation": "Anni is masculine plural, so quanto agrees as quanti."},
                {"id": "a1dq3", "prompt": "___ è il tuo insegnante?", "options": ["Chi", "Cosa", "Come"], "answerIndex": 0, "explanation": "Chi asks \"who\", the right word for asking about a person."},
             ]},
            {"id": "a1dq-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a1dq4", "prompt": "___ abiti? — Abito a Torino.", "answers": [["Dove"]], "explanation": "Dove asks about location.", "options": ["Dove", "Quando", "Come"]},
                {"id": "a1dq5", "prompt": "___ parti? — Parto domani.", "answers": [["Quando"]], "explanation": "Quando asks about time.", "options": ["Quando", "Dove", "Perché"]},
             ]},
        ],
        "summary": [
            "Yes/no questions in Italian use the same word order as the statement — only intonation/punctuation changes.",
            "The seven core question words: chi, cosa, dove, quando, perché, come, quanto (which agrees like an adjective).",
            "Perché means both \"why\" and \"because\" — the same word covers both sides of the exchange.",
        ],
    },
    {
        "id": "a1-verbi-irregolari-comuni",
        "level": "A1", "unit": "1", "order": 12, "skill": "grammar", "strand": "verbs",
        "title": "I Primi Verbi Irregolari: Andare, Fare, Volere",
        "subtitle": "Three high-frequency irregular verbs to get you talking about going, doing, and wanting.",
        "objectives": [
            "Conjugate andare, fare and volere in the present tense",
            "Use andare + a + infinitive for near-future plans",
            "Use volere + infinitive to express wants",
        ],
        "content": {
            "intro": "Not every irregular verb waits until A2 — andare (to go), fare (to do/make) and volere (to want) are so common in everyday speech that you need them from the start.",
            "explanation": "<p>These three don't follow the regular -are/-ire patterns you just learned, so their forms simply need memorizing. The reward is immediate: andare + a + infinitive lets you talk about near-future plans (<em>Vado a mangiare</em>, I'm going to eat), and volere + infinitive is the simplest way to express a wish (<em>Voglio partire</em>, I want to leave).</p>",
            "table": "<div class=\"table-scroll\"><table class=\"ref-table\"><caption>Andare, fare, volere — present tense</caption><thead><tr><th>Subject</th><th>andare</th><th>fare</th><th>volere</th></tr></thead><tbody><tr><td>io</td><td>vado</td><td>faccio</td><td>voglio</td></tr><tr><td>tu</td><td>vai</td><td>fai</td><td>vuoi</td></tr><tr><td>lui/lei</td><td>va</td><td>fa</td><td>vuole</td></tr><tr><td>noi</td><td>andiamo</td><td>facciamo</td><td>vogliamo</td></tr><tr><td>voi</td><td>andate</td><td>fate</td><td>volete</td></tr><tr><td>loro</td><td>vanno</td><td>fanno</td><td>vogliono</td></tr></tbody></table></div>",
            "rules": [
                {"heading": "a) Andare + a + infinitive", "body": "<p>Expresses \"going to [do something]\": <em>Vado a studiare.</em> (I'm going to study.) The a is required even though English doesn't need an equivalent word here.</p>"},
                {"heading": "b) Fare in fixed expressions", "body": "<p>Fare is used for weather (<em>Fa caldo</em>, It's hot) and many activities that don't literally involve \"making\" anything: <em>fare la spesa</em> (to go grocery shopping), <em>fare colazione</em> (to have breakfast), <em>fare una domanda</em> (to ask a question).</p>"},
                {"heading": "c) Volere + infinitive", "body": "<p>Directly followed by an infinitive, no preposition needed: <em>Voglio imparare l'italiano.</em> (I want to learn Italian.)</p>"},
            ],
            "examples": [
                {"it": "Vado a lavorare.", "en": "I'm going to work."},
                {"it": "Cosa fai stasera?", "en": "What are you doing tonight?"},
                {"it": "Voglio un caffè, grazie.", "en": "I want a coffee, thanks."},
                {"it": "Faccio colazione alle otto.", "en": "I have breakfast at eight."},
                {"it": "Vogliamo andare al mare.", "en": "We want to go to the sea."},
                {"it": "Loro vanno in vacanza domani.", "en": "They're going on vacation tomorrow."},
            ],
            "commonMistakes": [
                {"wrong": "Vado studiare.", "right": "Vado a studiare.", "why": "Andare requires the preposition a before an infinitive — it can never be dropped."},
                {"wrong": "Io voglio a mangiare.", "right": "Io voglio mangiare.", "why": "Volere is followed directly by the infinitive, with no preposition — unlike andare."},
                {"wrong": "Noi vado al cinema.", "right": "Noi andiamo al cinema.", "why": "Noi always needs its own form, andiamo, not the io form vado."},
            ],
        },
        "exercises": [
            {"id": "a1vi-fill", "type": "fill-blank", "title": "Fill in the Blanks",
             "items": [
                {"id": "a1vi1", "prompt": "Io ___ (andare) a scuola ogni giorno.", "answers": [["vado"]], "explanation": "Io form of andare is vado.", "options": ["vado", "vai", "va"]},
                {"id": "a1vi2", "prompt": "Cosa ___ (fare) tu di bello?", "answers": [["fai"]], "explanation": "Tu form of fare is fai.", "options": ["fai", "fa", "faccio"]},
                {"id": "a1vi3", "prompt": "Loro ___ (volere) partire domani.", "answers": [["vogliono"]], "explanation": "Loro form of volere is vogliono.", "options": ["vogliono", "vuole", "volete"]},
             ]},
            {"id": "a1vi-mc", "type": "multiple-choice", "title": "Choose the Correct Form",
             "items": [
                {"id": "a1vi4", "prompt": "\"I'm going to eat\" translates as...", "options": ["Vado mangiare.", "Vado a mangiare.", "Vado di mangiare."], "answerIndex": 1, "explanation": "Andare requires a before the infinitive."},
                {"id": "a1vi5", "prompt": "\"We want to travel\" translates as...", "options": ["Vogliamo a viaggiare.", "Vogliamo viaggiare.", "Voliamo viaggiare."], "answerIndex": 1, "explanation": "Volere is followed directly by the infinitive, no preposition."},
             ]},
            {"id": "a1vi-correction", "type": "correction", "title": "Correct the Mistakes",
             "items": [
                {"id": "a1vi6", "incorrect": "Vado studiare stasera.", "answer": ["Vado a studiare stasera."], "explanation": "Andare + infinitive always needs a in between."},
                {"id": "a1vi7", "incorrect": "Lei vuole a dormire.", "answer": ["Lei vuole dormire."], "explanation": "Volere never takes a before the infinitive."},
             ]},
        ],
        "summary": [
            "Andare, fare and volere are irregular and must be memorized: vado/vai/va/andiamo/andate/vanno, etc.",
            "Andare + a + infinitive expresses near-future plans; the a is mandatory.",
            "Volere + infinitive expresses a want, with no preposition needed.",
        ],
    },
]
